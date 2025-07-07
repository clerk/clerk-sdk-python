import datetime
import json
from unittest.mock import patch

import copy
import pytest

from clerk_backend_api._hooks.telemetry.events import TelemetryEvent
from clerk_backend_api._hooks.telemetry.samplers import DeduplicatingSampler, RandomSampler


class FakeEvent(TelemetryEvent):
    """Test TelemetryEvent implementation"""

    def __init__(self, sampling_rate=None):
        self.sampling_rate = sampling_rate
        super().__init__("test_sk", "test_event", {}, sampling_rate=sampling_rate)


@pytest.fixture
def deduplicating_sampler():
    """DeduplicatingSampler instance with a small window for testing"""
    return DeduplicatingSampler(window=datetime.timedelta(seconds=8))


@pytest.fixture
def random_sampler():
    """RandomSampler instance with fixed seed for deterministic tests"""
    return RandomSampler(seed=42)


class TestDeduplicatingSampler:
    def test_should_sample_new_event(self, deduplicating_sampler):
        """Test that a new event is sampled"""
        event = FakeEvent()
        prepared_event = {"event_type": "test", "payload": {"test_key": "test_value"}}

        assert deduplicating_sampler.should_sample(event, prepared_event) is True

    def test_should_not_sample_duplicate_within_window(self, deduplicating_sampler):
        """Test that a duplicate event within the window is not sampled"""
        event = FakeEvent()
        prepared_event = {"event_type": "test", "payload": {"test_key": "test_value"}}

        # First call should sample
        assert deduplicating_sampler.should_sample(event, prepared_event) is True

        event_2 = FakeEvent()
        prepared_event_2 = {"event_type": "test", "payload": {"test_key": "test_value"}}
        # Second call with same event should not sample
        assert deduplicating_sampler.should_sample(event_2, prepared_event_2) is False

    def test_should_sample_after_window(self, deduplicating_sampler):
        """Test that an event is sampled again after the window has passed"""
        event = FakeEvent()
        prepared_event = {"event_type": "test", "payload": {"test_key": "test_value"}}

        # Get the initial time
        initial_time = datetime.datetime.now()

        # First call should sample
        assert deduplicating_sampler.should_sample(event, prepared_event) is True
        # Second call with same event should not sample
        assert deduplicating_sampler.should_sample(copy.deepcopy(event), copy.deepcopy(prepared_event)) is False

        # Patch datetime to return future time when called later
        future_time = initial_time + datetime.timedelta(seconds=10)

        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = future_time
            # Should sample again after window has passed (window is 8 seconds)
            assert deduplicating_sampler.should_sample(event, prepared_event) is True

    def test_different_events_are_sampled_separately(self, deduplicating_sampler):
        """Test that different events are sampled separately"""
        event1 = FakeEvent()
        prepared_event1 = {"event_type": "test1", "payload": {"test_key": "test_value1"}}

        event2 = FakeEvent()
        prepared_event2 = {"event_type": "test2", "payload": {"test_key": "test_value2"}}

        # Both should be sampled the first time
        assert deduplicating_sampler.should_sample(event1, prepared_event1) is True
        assert deduplicating_sampler.should_sample(event2, prepared_event2) is True

    def test_ignores_sk_pk_fields(self, deduplicating_sampler):
        """Test that sk and pk fields are ignored when generating the key"""
        event = FakeEvent()
        prepared_event1 = {
            "event_type": "test",
            "payload": {"test_key": "test_value"},
            "sk": "some_secret_key",
            "pk": "some_publishable_key"
        }

        prepared_event2 = {
            "event_type": "test",
            "payload": {"test_key": "test_value"},
            "sk": "different_secret_key",
            "pk": "different_publishable_key"
        }

        # First event should be sampled
        assert deduplicating_sampler.should_sample(event, prepared_event1) is True

        # Second event with different sk/pk but same content should not be sampled
        assert deduplicating_sampler.should_sample(event, prepared_event2) is False

    def test_generate_key(self):
        """Test the key generation logic"""
        # Test with payload
        prepared_event = {
            "event_type": "test",
            "payload": {"test_key": "test_value"},
            "sk": "some_secret_key",
            "pk": "some_publishable_key"
        }

        expected = json.dumps({"event_type": "test", "test_key": "test_value"}, sort_keys=True)
        assert DeduplicatingSampler._generate_key(prepared_event) == expected

        # Test without payload
        prepared_event = {
            "event_type": "test",
            "other_field": "other_value",
            "sk": "some_secret_key",
            "pk": "some_publishable_key"
        }

        expected = json.dumps({"event_type": "test", "other_field": "other_value"}, sort_keys=True)
        assert DeduplicatingSampler._generate_key(prepared_event) == expected


class TestRandomSampler:
    def test_should_sample_when_rate_is_none(self, random_sampler):
        """Test that events with no sampling rate are always sampled"""
        event = FakeEvent(sampling_rate=None)
        prepared_event = {"event_type": "test"}

        assert random_sampler.should_sample(event, prepared_event) is True

    def test_should_sample_according_to_rate(self, random_sampler):
        """Test that events are sampled based on their sampling rate"""
        # This should be approximately 80% sampled
        event_high_rate = FakeEvent(sampling_rate=0.8)
        prepared_events = [{"event_type": f"test{i}"} for i in range(1000)]
        results = [random_sampler.should_sample(event_high_rate, prepared_event) for prepared_event in prepared_events]
        accepted = sum([1 for result in results if result])
        assert 0.75 < accepted / len(results) < 0.85

        # This should be approximately 10% sampled
        event_low_rate = FakeEvent(sampling_rate=0.1)
        results = [random_sampler.should_sample(event_low_rate, prepared_event) for prepared_event in prepared_events]
        accepted = sum([1 for result in results if result])
        assert 0.09 < accepted / len(results) < 0.11

    def test_deterministic_with_seed(self):
        """Test that sampling is deterministic with a fixed seed"""
        sampler1 = RandomSampler(seed=99)
        sampler2 = RandomSampler(seed=99)

        event = FakeEvent(sampling_rate=0.5)
        prepared_event = {"event_type": "test"}

        # Both samplers should make the same decision
        result1 = sampler1.should_sample(event, prepared_event)
        result2 = sampler2.should_sample(event, prepared_event)

        assert result1 == result2
