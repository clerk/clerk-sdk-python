from typing import List, Optional, Any, Union, Tuple

import httpx

from .types import HookContext, BeforeRequestHook, BeforeRequestContext, AfterSuccessHook, AfterSuccessContext, AfterErrorHook, AfterErrorContext
from .telemetry.events import TelemetryEvent, EVENT_METHOD_CALLED, EVENT_METHOD_SUCCEEDED, EVENT_METHOD_FAILED
from .telemetry.collector import TelemetryCollector


class ClerkTelemetryHook:
    def __init__(self, collectors: List[TelemetryCollector]):
        self.collectors = collectors

    @staticmethod
    def _get_sk(hook_ctx: HookContext):
        security_source = hook_ctx.security_source
        if security_source:
            if callable(security_source):
                security_source = security_source()
            if hasattr(security_source, 'bearer_auth'):
                return security_source.bearer_auth
        return None

    def _construct_event(
        self,
        hook_ctx: HookContext,
        event: str,
        additional_payload: Optional[dict[str, Any]] = None,
        sampling_rate: Optional[float] = 1.0
    ) -> TelemetryEvent:
        additional_payload = {} if additional_payload is None else additional_payload
        return TelemetryEvent(
            self._get_sk(hook_ctx),
            event,
            {'method': hook_ctx.operation_id, **additional_payload},
            sampling_rate=sampling_rate
        )


class TelemetryBeforeRequestHook(ClerkTelemetryHook, BeforeRequestHook):

    def __init__(self, collectors: List[TelemetryCollector]):
        super().__init__(collectors)

    def before_request(self, hook_ctx: BeforeRequestContext, request: httpx.Request) -> httpx.Request:
        for collector in self.collectors:
            collector.collect(self._construct_event(
                hook_ctx,
                EVENT_METHOD_CALLED,
                sampling_rate=0.1
            ))
        return request


class TelemetryAfterSuccessHook(ClerkTelemetryHook, AfterSuccessHook):

    def __init__(self, collectors: List[TelemetryCollector]):
        super().__init__(collectors)

    def after_success(self, hook_ctx: AfterSuccessContext, response: httpx.Response) -> httpx.Response:
        for collector in self.collectors:
            collector.collect(self._construct_event(
                hook_ctx,
                EVENT_METHOD_SUCCEEDED,
                {'status_code': response.status_code},
                sampling_rate=0.1
            ))
        return response


class TelemetryAfterErrorHook(ClerkTelemetryHook, AfterErrorHook):

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception]
    ) -> Union[Tuple[Optional[httpx.Response], Optional[Exception]], Exception]:

        additional_payload = {}
        if response:
            additional_payload['status_code'] = response.status_code
        if error:
            additional_payload['exception'] = error.__class__.__name__

        for collector in self.collectors:
            collector.collect(self._construct_event(
                hook_ctx,
                EVENT_METHOD_FAILED,
                additional_payload,
                sampling_rate=0.1
            ))
        return response, error

    def __init__(self, collectors: List[TelemetryCollector]):
        super().__init__(collectors)
