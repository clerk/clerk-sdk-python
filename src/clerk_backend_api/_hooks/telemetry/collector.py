import concurrent.futures
import importlib.metadata
import json
import logging
import queue
import sys
import threading
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from typing import Union

import httpx

from .events import TelemetryEvent
from .samplers import TelemetrySampler


class TelemetryCollector(ABC):
    CLERK_SDK = "clerk-backend-api"

    def __init__(self):
        self.sdk = f"python/{TelemetryCollector.CLERK_SDK}"
        self.sdkv = TelemetryCollector._get_sdk_version()

    def collect(self, event: TelemetryEvent):
        if event.it == "development":
            self._collect(event)

    @abstractmethod
    def _collect(self, event: TelemetryEvent):
        pass

    @staticmethod
    def _get_sdk_version():
        try:
            return importlib.metadata.version(TelemetryCollector.CLERK_SDK)
        except (importlib.metadata.PackageNotFoundError, ImportError):
            return "unknown"

    def _prepare_event(self, event) -> dict[str, Union[str, dict[str, str]]]:
        return {
            "event": event.event,
            "it": event.it,
            "sdk": self.sdk,
            "sdkv": self.sdkv,
            "sk": event.sk,
            "payload": event.payload,
        }


class DebugTelemetryCollector(TelemetryCollector):
    # we intentionally do not use `logging` here to avoid
    # interfering with the application's logging configuration
    def _collect(self, event: TelemetryEvent):
        print(json.dumps(self._prepare_event(event), default=str), file=sys.stderr)


class LiveTelemetryCollector(TelemetryCollector):
    """
    Sends telemetry events to the Clerk Telemetry service immediately.
    This SDK is intended for server use so process lifecycle is not guaranteed.
    Hence, we do not buffer telemetry events for later
    """

    def __init__(
        self,
        samplers: List[TelemetrySampler],
        endpoint: str = 'http://localhost:3000/'
    ):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.samplers = samplers
        self.endpoint = endpoint
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="telemetry_worker"
        )

    def _collect(self, event: TelemetryEvent):
        prepared_event = self._prepare_event(event)
        for sampler in self.samplers:
            if not sampler.should_sample(event, prepared_event):
                return
        self.executor.submit(self._send_events, [prepared_event])

    def _send_events(self, events: List[Dict[str, Any]]):
        try:
            with httpx.Client() as client:
                response = client.post(self.endpoint, json=events)
                response.raise_for_status()
        except Exception as e:
            self.logger.warning(f"Failed to send telemetry events: {e}")
