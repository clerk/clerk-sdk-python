from typing import Union

import httpx

from ..types import (
    AfterErrorHook,
    AfterSuccessHook,
    BeforeRequestContext,
    BeforeRequestHook,
    SDKInitHook,
)


class ClerkBeforeRequestHook(SDKInitHook, BeforeRequestHook, AfterSuccessHook, AfterErrorHook):
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        request.headers["Clerk-API-Version"] = "2024-10-01"

        return request
