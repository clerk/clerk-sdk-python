import importlib.metadata
import json
import sys
from abc import ABC, abstractmethod

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


class DebugTelemetryCollector(TelemetryCollector):
    # we intentionally do not use `logging` here to avoid
    # interfering with the application's logging configuration
    def _collect(self, event: TelemetryEvent):
        print(json.dumps({
            'event': event.event,
            'it': event.it,
            'sdk': self.sdk,
            'sdkv': self.sdkv,
            'sk': event.sk,
            'payload': event.payload
        }, default=str), file=sys.stderr)


class LiveTelemetryCollector(TelemetryCollector):

    def _collect(self, event: TelemetryEvent):
        # raise NotImplementedError("LiveTelemetryReporter is not implemented yet")
        pass
