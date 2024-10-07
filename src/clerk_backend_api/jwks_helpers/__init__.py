from ..sdk import Clerk
from .authenticaterequest import (
    AuthErrorReason,
    AuthStatus,
    AuthenticateRequestOptions,
    RequestState,
    authenticate_request
)
from .verifytoken import (
    TokenVerificationError,
    TokenVerificationErrorReason,
    VerifyTokenOptions,
    verify_token
)

__all__ = [
    "AuthErrorReason",
    "AuthStatus",
    "AuthenticateRequestOptions",
    "RequestState",
    "authenticate_request",
    "TokenVerificationError",
    "TokenVerificationErrorReason",
    "VerifyTokenOptions",
    "verify_token"
]


# Attach authenticate_request method to the Clerk class
setattr(Clerk, 'authenticate_request', authenticate_request)
