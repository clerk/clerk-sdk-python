import datetime
import json
import random
from abc import abstractmethod, ABC
from typing import Optional, Union
from .events import TelemetryEvent


class TelemetrySampler(ABC):
    @abstractmethod
    def should_sample(
        self,
        event: TelemetryEvent,
        prepared_event: dict[str, Union[str, dict[str, str]]],
    ) -> bool:
        pass


class DeduplicatingSampler(TelemetrySampler):
    """
    An in-memory sampler that deduplicates telemetry events based on their content.
    """

    def __init__(self, window: Optional[datetime.timedelta] = None):
        self._seen: dict[str, datetime.datetime] = dict()
        self.window = datetime.timedelta(hours=24) if window is None else window

    def should_sample(
        self,
        event: TelemetryEvent,
        prepared_event: dict[str, Union[str, dict[str, str]]],
    ) -> bool:
        now = datetime.datetime.now()
        key = self._generate_key(prepared_event)
        last_sampled = self._seen.get(key, None)

        if last_sampled is None or now - last_sampled > self.window:
            self._seen[key] = now
            return True
        else:
            return False

    @staticmethod
    def _generate_key(prepared_event):
        """Remove sensitive information and spread the payload into the top level so it can be hashed."""
        sanitized_event = prepared_event.copy()
        sanitized_event.pop("sk", None)
        sanitized_event.pop("pk", None)
        payload = sanitized_event.pop("payload", None)
        sanitized_event = {**sanitized_event, **payload} if payload else sanitized_event
        # in theory, sort_keys isn't required since dicts are ordered in Python 3.7+
        # and we're consistent about insertion order, but it doesn't hurt to be explicit
        return json.dumps(sanitized_event, sort_keys=True)


class RandomSampler(TelemetrySampler):
    """
    A sampler that samples events randomly at the rate they say they should be sampled.
    """

    def __init__(self, seed: Optional[int] = None):
        self.random = random.Random(seed or 1)

    def should_sample(
        self,
        event: TelemetryEvent,
        prepared_event: dict[str, Union[str, dict[str, str]]],
    ) -> bool:
        if event.sampling_rate is None:
            return True
        else:
            return self.random.uniform(0, 1) < event.sampling_rate
