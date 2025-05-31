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
        # pylint: disable=import-outside-toplevel
        from .. import VERSION

        request.headers["Clerk-API-Version"] = "2025-04-10"
        request.headers["X-Clerk-SDK"] = f"python/{VERSION}"

        return request
