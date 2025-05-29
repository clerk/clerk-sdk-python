from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Union, Optional, Protocol, Mapping


class TokenVerificationErrorReason(Enum):

    JWK_FAILED_TO_LOAD = (
        'jwk-failed-to-load',
        'Failed to load JWKS from Clerk Backend API. Contact support@clerk.com.'
    )

    JWK_REMOTE_INVALID = (
        'jwk-remote-invalid',
        'The JWKS endpoint did not contain any signing keys. Contact support@clerk.com.'
    )

    JWK_FAILED_TO_RESOLVE = (
        'jwk-failed-to-resolve',
        'Failed to resolve JWK. Public Key is not in the proper format.'
    )

    JWK_KID_MISMATCH = (
        'jwk-kid-mismatch',
        'Unable to find a signing key in JWKS that matches the kid of the provided session token.'
    )

    TOKEN_EXPIRED = (
        'token-expired',
        'Token has expired and is no longer valid.'
    )

    TOKEN_INVALID = (
        'token-invalid',
        'Token is invalid and could not be verified.'
    )

    TOKEN_INVALID_AUTHORIZED_PARTIES = (
        'token-invalid-authorized-parties',
        'Authorized party claim (azp) does not match any of the authorized parties.',
    )

    TOKEN_INVALID_AUDIENCE = (
        'token-invalid-audience',
        'Token audience claim (aud) does not match one of the expected audience values.',
    )

    TOKEN_IAT_IN_THE_FUTURE = (
        'token-iat-in-the-future',
        'Token Issued At claim (iat) represents a time in the future.'
        )

    TOKEN_NOT_ACTIVE_YET = (
        'token-not-active-yet',
        'Token is not yet valid. Not Before claim (nbf) is in the future.'
    )

    TOKEN_INVALID_SIGNATURE = (
        'token-invalid-signature',
        'Token signature is invalid and could not be verified.'
    )

    SECRET_KEY_MISSING = (
        'secret-key-missing',
        'Missing Clerk Secret Key. Go to https://dashboard.clerk.com and get your key for your instance.'
    )

    SERVER_ERROR = (
        'server-error',
        'An unexpected error occurred while verifying the token. Please try again later'
    )

    INVALID_TOKEN_TYPE = (
        'invalid-token-type',
        'The provided token is not a valid Clerk token type. Expected one of: session, machine, oauth, or api key.'
    )


class TokenVerificationError(Exception):
    """Exception raised when token verification fails"""

    def __init__(self, reason: TokenVerificationErrorReason):
        self.reason = reason
        super().__init__(self.reason.value[1])


@dataclass
class VerifyTokenOptions:
    """
    Options to configure verify_token.

    Attributes:
        audience (Union[str, List[str], None]): An audience or list of audiences to verify against.
        authorized_parties (Optional[List[str]]): An allowlist of origins to verify against.
        clock_skew_in_ms (int): Allowed time difference (in milliseconds) between the Clerk server (which generates the token)
                                and the clock of the user's application server when validating a token. Defaults to 5000 ms.
        jwt_key (Optional[str]): PEM Public Key used to verify the session token in a networkless manner.
        secret_key (Optional[str]): The Clerk secret key from the API Keys page in the Clerk Dashboard.
        api_url (str): The Clerk Backend API endpoint. Defaults to 'https://api.clerk.com'
        api_version (str): The version passed to the Clerk API. Defaults to 'v1'.
    """

    audience: Optional[Union[str, List[str]]] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000
    jwt_key: Optional[str] = None
    secret_key: Optional[str] = None
    api_url: str = 'https://api.clerk.com'
    api_version: str = 'v1'




class Requestish(Protocol):
    @property
    def headers(self) -> Mapping[str, str]:
        ...


class AuthErrorReason(Enum):

    SESSION_TOKEN_MISSING = (
        'session-token-missing',
        'Could not retrieve session token. Please make sure that the __session cookie or the HTTP authorization header contain a Clerk-generated session JWT',
    )

    SECRET_KEY_MISSING = (
        'secret-key-missing',
        'Missing Clerk Secret Key. Go to https://dashboard.clerk.com and get your key for your instance.'
    )

    TOKEN_TYPE_NOT_SUPPORTED = (
        'token-type-not-supported',
        'The provided token type is not supported. Expected one of: session_token, machine_token, oauth_token, or api_key.'
    )


class AuthStatus(Enum):
    """Authentication Status"""

    SIGNED_IN = 'signed-in'
    SIGNED_OUT = 'signed-out'


@dataclass
class RequestState:
    """Request Authentication State"""

    status: AuthStatus
    reason: Optional[Union[AuthErrorReason, TokenVerificationErrorReason]] = None
    token: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None

    @property
    def is_signed_in(self) -> bool:
        return self.status == AuthStatus.SIGNED_IN

    @property
    def message(self) -> Optional[str]:
        if self.reason is None:
            return None
        return self.reason.value[1]


@dataclass
class AuthenticateRequestOptions:
    """
    Options to configure authenticate_request.

    Attributes:
        secret_key (Optional[str]): The Clerk secret key from the API Keys page in the Clerk Dashboard.
        jwt_key (Optional[str]): Used to verify the session token in a networkless manner.
        audience (Union[str, List[str], None]): An audience or list of audiences to verify against.
        authorized_parties (Optional[List[str]]): An allowlist of origins to verify against.
        clock_skew_in_ms (int): Allowed time difference (in milliseconds) between the Clerk server (which generates the token)
                                and the clock of the user's application server when validating a token. Defaults to 5000 ms.
    """

    secret_key: Optional[str] = None
    jwt_key: Optional[str] = None
    audience: Union[str, List[str], None] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000
    accepts_token: List[str] = field(default_factory=lambda: ['any'])

class TokenType(Enum):
    SESSION_TOKEN = 'session_token'
    API_KEY = 'api_key'
    MACHINE_TOKEN = 'machine_token'
    OAUTH_TOKEN = 'oauth_token'

class TokenPrefix(Enum):
    API_KEY_PREFIX = 'ak_'
    OAUTH_TOKEN_PREFIX = 'oat_'
    MACHINE_TOKEN_PREFIX = 'mt_'
