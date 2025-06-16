import os

from .clerk_before_request_hook import ClerkBeforeRequestHook
from .telemetry_hooks import TelemetryBeforeRequestHook, TelemetryAfterSuccessHook, TelemetryAfterErrorHook
from .telemetry.collector import LiveTelemetryCollector, DebugTelemetryCollector
from .telemetry.samplers import RandomSampler, DeduplicatingSampler
from .types import Hooks


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


def init_hooks(hooks: Hooks):
    # pylint: disable=unused-argument
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook 
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_before_request_hook(ClerkBeforeRequestHook())
    configure_telemetry(hooks)

def configure_telemetry(hooks: Hooks):
    # one of two filters for telemetry
    # the other is when we can detect that it's a development environment
    # which we can only see when we see the secret key starting with sk_test
    if os.environ.get('CLERK_TELEMETRY_DISABLED') == '1':
        return

    collectors = [LiveTelemetryCollector([RandomSampler(), DeduplicatingSampler()])]
    if os.environ.get('CLERK_TELEMETRY_DEBUG') == '1':
        collectors.append(DebugTelemetryCollector())

    hooks.register_before_request_hook(TelemetryBeforeRequestHook(collectors))
    hooks.register_after_success_hook(TelemetryAfterSuccessHook(collectors))
    hooks.register_after_error_hook(TelemetryAfterErrorHook(collectors))
