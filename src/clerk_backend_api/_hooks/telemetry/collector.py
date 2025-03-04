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


class TelemetryCollector(ABC):
    CLERK_SDK = 'clerk-backend-api'

    def __init__(self):
        self.sdk = f'python/{TelemetryCollector.CLERK_SDK}'
        self.sdkv = TelemetryCollector._get_sdk_version()

    def collect(self, event: TelemetryEvent):
        if event.it == 'development':
            self._collect(event)

    @abstractmethod
    def _collect(self, event: TelemetryEvent):
        pass

    @staticmethod
    def _get_sdk_version():
        try:
            return importlib.metadata.version(TelemetryCollector.CLERK_SDK)
        except (importlib.metadata.PackageNotFoundError, ImportError):
            return 'unknown'

    def _prepare_event(self, event) -> dict[str, Union[str, dict[str, str]]]:
        return {
            'event': event.event,
            'it': event.it,
            'sdk': self.sdk,
            'sdkv': self.sdkv,
            'sk': event.sk,
            'payload': event.payload
        }


class DebugTelemetryCollector(TelemetryCollector):
    # we intentionally do not use `logging` here to avoid
    # interfering with the application's logging configuration
    def _collect(self, event: TelemetryEvent):
        print(json.dumps(self._prepare_event(event), default=str), file=sys.stderr)


class LiveTelemetryCollector(TelemetryCollector):
    """
        Accumulate telemetry events and send them to the Clerk Telemetry API.
        Intends to do the following:
        - Buffer events and send them in batches
        - Send events asynchronously
    """

    def __init__(
        self,
        max_buffer_size: int = 10,
        max_batch_size: int = 5,
    ):
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.max_buffer_size = max_buffer_size
        self.max_batch_size = max_batch_size
        self.endpoint = 'https://staging.clerk-telemetry.com'
        self.endpoint = 'http://localhost:3000/' # override temporarily so that I can test locally
        self.queue = queue.Queue(maxsize=max_buffer_size)
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=1,
            thread_name_prefix='telemetry_worker'
        )
        self.flush_timer = None

    def _collect(self, event: TelemetryEvent):
        prepared_event = self._prepare_event(event)

        while True:
            try:
                self.queue.put(prepared_event, block=False)
                break
            except queue.Full:
                if self.flush_timer is not None:
                    self.flush_timer.cancel()
                self._flush(self.queue)

        if self.flush_timer is None or not self.flush_timer.is_alive():
            self.flush_timer = threading.Timer(5, self._flush, args=(self.queue,))
            self.flush_timer.start()


    def _flush(self, q: queue.Queue[Dict[str, Union[str, dict[str, str]]]]):
        while not q.empty():
            events_to_send = []
            while len(events_to_send) < self.max_batch_size:
                try:
                    events_to_send.append(q.get(block=False))
                except queue.Empty:
                    if events_to_send:
                        self.executor.submit(self._send_events, events_to_send)
                    return
            self.executor.submit(self._send_events, events_to_send)

    def _send_events(self, events: List[Dict[str, Any]]):
        try:
            with httpx.Client() as client:
                response = client.post(self.endpoint, json=events)
                response.raise_for_status()
        except Exception as e:
            self.logger.warning(f'Failed to send telemetry events: {e}')