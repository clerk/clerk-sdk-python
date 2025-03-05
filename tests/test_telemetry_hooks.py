import pytest
import httpx
from unittest.mock import Mock

from clerk_backend_api._hooks.telemetry_hooks import (
    TelemetryBeforeRequestHook,
    TelemetryAfterSuccessHook,
    TelemetryAfterErrorHook
)
from clerk_backend_api._hooks.types import (
    HookContext,
    BeforeRequestContext,
    AfterSuccessContext,
    AfterErrorContext
)
from clerk_backend_api._hooks.telemetry.events import (
    EVENT_METHOD_CALLED,
    EVENT_METHOD_SUCCEEDED,
    EVENT_METHOD_FAILED
)
from clerk_backend_api._hooks.telemetry.collector import TelemetryCollector

@pytest.fixture
def mock_collector():
    """Mock TelemetryCollector instance"""
    collector = Mock(spec=TelemetryCollector)
    return collector

@pytest.fixture
def hook_context():
    """HookContext instance"""
    return HookContext(
        base_url="https://api.clerk.dev",
        operation_id="test_operation",
        oauth2_scopes=None,
        security_source=lambda: Mock(bearer_auth="sk_test_123")
    )

@pytest.fixture
def before_request_context(hook_context):
    """BeforeRequestContext instance"""
    return BeforeRequestContext(hook_context)

@pytest.fixture
def after_success_context(hook_context):
    """AfterSuccessContext instance"""
    return AfterSuccessContext(hook_context)

@pytest.fixture
def after_error_context(hook_context):
    """AfterErrorContext instance"""
    return AfterErrorContext(hook_context)

class TestTelemetryBeforeRequestHook:
    def test_before_request_collects_event(self, mock_collector, before_request_context):
        # Create the hook with mock collector
        hook = TelemetryBeforeRequestHook([mock_collector])
        request = httpx.Request("GET", "https://api.clerk.dev/v1/users")

        # Call the before_request method
        modified_request = hook.before_request(before_request_context, request)

        # Assert collector.collect was called with correct event
        mock_collector.collect.assert_called_once()
        event = mock_collector.collect.call_args[0][0]
        assert event.event == EVENT_METHOD_CALLED
        assert event.sk == "sk_test_123"
        assert event.payload["method"] == "test_operation"
        assert event.sampling_rate == 0.1

        # Assert request is unchanged
        assert modified_request is request

class TestTelemetryAfterSuccessHook:
    def test_after_success_collects_event(self, mock_collector, after_success_context):
        # Create the hook with mock collector
        hook = TelemetryAfterSuccessHook([mock_collector])
        response = httpx.Response(201)

        # Call the after_success method
        modified_response = hook.after_success(after_success_context, response)

        # Assert collector.collect was called with correct event
        mock_collector.collect.assert_called_once()
        event = mock_collector.collect.call_args[0][0]
        assert event.event == EVENT_METHOD_SUCCEEDED
        assert event.sk == "sk_test_123"
        assert event.payload["method"] == "test_operation"
        assert event.payload["status_code"] == 201
        assert event.sampling_rate == 0.1

        # Assert response is unchanged
        assert modified_response is response

class TestTelemetryAfterErrorHook:
    def test_after_error_collects_event_with_response(self, mock_collector, after_error_context):
        # Create the hook with mock collector
        hook = TelemetryAfterErrorHook([mock_collector])
        response = httpx.Response(400)
        error = ValueError("test error")

        # Call the after_error method
        modified_response, modified_error = hook.after_error(after_error_context, response, error)

        # Assert collector.collect was called with correct event
        mock_collector.collect.assert_called_once()
        event = mock_collector.collect.call_args[0][0]
        assert event.event == EVENT_METHOD_FAILED
        assert event.sk == "sk_test_123"
        assert event.payload["method"] == "test_operation"
        assert event.payload["status_code"] == 400
        assert event.payload["exception"] == "ValueError"
        assert event.sampling_rate == 0.1

        # Assert response and error are unchanged
        assert modified_response is response
        assert modified_error is error

    def test_after_error_collects_event_without_response(self, mock_collector, after_error_context):
        # Create the hook with mock collector
        hook = TelemetryAfterErrorHook([mock_collector])
        error = ValueError("test error")

        # Call the after_error method
        modified_response, modified_error = hook.after_error(after_error_context, None, error)

        # Assert collector.collect was called with correct event
        mock_collector.collect.assert_called_once()
        event = mock_collector.collect.call_args[0][0]
        assert event.event == EVENT_METHOD_FAILED
        assert event.sk == "sk_test_123"
        assert event.payload["method"] == "test_operation"
        assert "status_code" not in event.payload
        assert event.payload["exception"] == "ValueError"
        assert event.sampling_rate == 0.1

        # Assert response and error are unchanged
        assert modified_response is None
        assert modified_error is error

    def test_after_error_collects_event_without_exception(self, mock_collector, after_error_context):
        # Create the hook with mock collector
        hook = TelemetryAfterErrorHook([mock_collector])
        response = httpx.Response(500)

        # Call the after_error method
        modified_response, modified_error = hook.after_error(after_error_context, response, None)

        # Assert collector.collect was called with correct event
        mock_collector.collect.assert_called_once()
        event = mock_collector.collect.call_args[0][0]
        assert event.event == EVENT_METHOD_FAILED
        assert event.sk == "sk_test_123"
        assert event.payload["method"] == "test_operation"
        assert event.payload["status_code"] == 500
        assert "exception" not in event.payload
        assert event.sampling_rate == 0.1

        # Assert response and error are unchanged
        assert modified_response is response
        assert modified_error is None
