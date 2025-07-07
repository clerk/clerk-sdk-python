import concurrent.futures
import json
from unittest.mock import Mock, patch

import httpx
import pytest

from clerk_backend_api._hooks.telemetry.collector import (
    DebugTelemetryCollector,
    LiveTelemetryCollector
)
from clerk_backend_api._hooks.telemetry.events import TelemetryEvent
from clerk_backend_api._hooks.telemetry.samplers import TelemetrySampler


@pytest.fixture
def test_event():
    """Create a test TelemetryEvent"""
    return TelemetryEvent(
        sk="sk_test_123",
        event="TEST_EVENT",
        payload={"method": "test_method"},
        sampling_rate=1.0
    )


@pytest.fixture
def prod_event():
    """Create a production TelemetryEvent"""
    return TelemetryEvent(
        sk="sk_live_123",
        event="TEST_EVENT",
        payload={"method": "test_method"},
        sampling_rate=1.0
    )


class TestTelemetryCollector:
    def test_prepare_event(self, test_event):
        collector = DebugTelemetryCollector()  # Using Debug collector as concrete implementation
        prepared = collector._prepare_event(test_event)

        assert prepared["event"] == "TEST_EVENT"
        assert prepared["it"] == "development"
        assert prepared["sdk"].startswith("python/clerk-backend-api")
        assert "sdkv" in prepared
        assert prepared["sk"] == "sk_test_123"
        assert prepared["payload"] == {"method": "test_method"}

    def test_collect_development_only(self, test_event, prod_event):
        collector = DebugTelemetryCollector()

        # Mock the _collect method to track calls
        collector._collect = Mock()

        # Development event should be collected
        collector.collect(test_event)
        assert collector._collect.call_count == 1

        # Production event should not be collected
        collector.collect(prod_event)
        assert collector._collect.call_count == 1


class TestDebugTelemetryCollector:
    def test_debug_collector_prints_to_stderr(self, test_event):
        collector = DebugTelemetryCollector()

        with patch('builtins.print') as mock_print:
            collector.collect(test_event)

            # Verify that the event was printed as expected
            assert mock_print.called
            assert mock_print.call_args[0][
                       0] == '{"event": "TEST_EVENT", "it": "development", "sdk": "python/clerk-backend-api", "sdkv": "1.8.0", "sk": "sk_test_123", "payload": {"method": "test_method"}}'

    def test_debug_collector_does_not_crash_on_payload_with_non_serializable_types(self, test_event):
        collector = DebugTelemetryCollector()
        test_event.payload["non_serializable"] = lambda x: x
        with patch('builtins.print') as mock_print:
            collector.collect(test_event)

            # verify that the event was printed and things didn't blow up
            assert mock_print.called
            assert 'lambda' in mock_print.call_args[0][0]
            assert mock_print.call_args[0][0].startswith(
                '{"event": "TEST_EVENT", "it": "development", "sdk": "python/clerk-backend-api", "sdkv": "1.8.0", "sk": "sk_test_123", "payload": {"method": "test_method", "non_serializable":')


class TestLiveTelemetryCollector:
    @pytest.fixture
    def mock_sampler(self):
        sampler = Mock(spec=TelemetrySampler)
        sampler.should_sample.return_value = True
        return sampler

    @pytest.fixture
    def live_collector(self, mock_sampler):
        return LiveTelemetryCollector(
            samplers=[mock_sampler],
            endpoint="http://test.endpoint"
        )

    def test_collect_with_sampling(self, live_collector, mock_sampler, test_event):
        with patch.object(live_collector.executor, 'submit') as mock_submit:
            # Test when sampler returns True
            live_collector.collect(test_event)
            assert mock_submit.called

            # Test when sampler returns False
            mock_sampler.should_sample.return_value = False
            live_collector.collect(test_event)
            # submit should not be called again
            assert mock_submit.call_count == 1

    def test_send_events_success(self, live_collector, test_event, caplog):
        mock_response = Mock(spec=httpx.Response)
        mock_response.raise_for_status.return_value = None

        with patch('httpx.Client') as mock_client:
            mock_client.return_value.__enter__.return_value.post.return_value = mock_response

            # Call _send_events directly since it's called in a separate thread
            prepared_event = live_collector._prepare_event(test_event)
            live_collector._send_events([prepared_event])

            # Verify the POST request was made correctly
            mock_client.return_value.__enter__.return_value.post.assert_called_once_with(
                "http://test.endpoint",
                json=[prepared_event]
            )

            # Verify that no errors were logged
            assert caplog.text == ""

    def test_send_events_failure(self, live_collector, test_event, caplog):
        with patch('httpx.Client') as mock_client:
            # Create a mock response that will raise an error when raise_for_status is called
            mock_response = Mock(spec=httpx.Response)
            mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
                "Server error", request=Mock(), response=mock_response
            )
            mock_client.return_value.__enter__.return_value.post.return_value = mock_response

            # Call _send_events directly
            prepared_event = live_collector._prepare_event(test_event)
            live_collector._send_events([prepared_event])

            # Verify that the error was logged
            assert "Failed to send telemetry events" in caplog.text
            assert "Server error" in caplog.text
