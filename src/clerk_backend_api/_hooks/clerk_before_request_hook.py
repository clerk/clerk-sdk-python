from typing import Union

import httpx

from .types import (
    BeforeRequestContext,
    BeforeRequestHook,
)

class ClerkBeforeRequestHook(BeforeRequestHook):
    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> Union[httpx.Request, Exception]:
        request.headers["Clerk-API-Version"] = "2024-10-01"

        return request
