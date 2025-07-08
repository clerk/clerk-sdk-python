from abc import ABC
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


class TokenType(Enum):
    SESSION_TOKEN = 'session_token'
    API_KEY = 'api_key'
    MACHINE_TOKEN = 'machine_token'
    OAUTH_TOKEN = 'oauth_token'

class TokenPrefix(Enum):
    API_KEY_PREFIX = 'ak_'
    OAUTH_TOKEN_PREFIX = 'oat_'
    MACHINE_TOKEN_PREFIX = 'm2m_'


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
    SIGNED_IN = 'signed-in'
    SIGNED_OUT = 'signed-out'

class AuthObject(ABC):
    pass

@dataclass
class SessionAuthObjectV2(AuthObject):
    exp: Optional[int] = None
    iat: Optional[int] = None
    iss: Optional[str] = None
    sid: Optional[str] = None
    sub: Optional[str] = None
    v: Optional[int] = None
    jti: Optional[str] = None
    role: Optional[str] = None
    fva: Optional[list[int]] = None
    nbf: Optional[int] = None
    email: Optional[str] = None
    azp: Optional[str] = None


@dataclass
class SessionAuthObjectV1(AuthObject):
    session_id: Optional[str] = None
    user_id: Optional[str] = None
    org_id: Optional[str] = None
    org_role: Optional[str] = None
    org_permissions: Optional[List[str]] = None
    factor_verification_age: Optional[List[int]] = None
    claims: Optional[Dict[str, Any]] = None

@dataclass
class OAuthMachineAuthObject(AuthObject):
    token_type: TokenType = TokenType.OAUTH_TOKEN
    id: Optional[str] = None
    user_id: Optional[str] = None
    client_id: Optional[str] = None
    name: Optional[str] = None
    scopes: Optional[List[str]] = None

@dataclass
class APIKeyMachineAuthObject(AuthObject):
    token_type: TokenType = TokenType.API_KEY
    id: Optional[str] = None
    user_id: Optional[str] = None
    org_id: Optional[str] = None
    name: Optional[str] = None
    scopes: Optional[List[str]] = None
    claims: Optional[Dict[str, Any]] = None

@dataclass
class M2MMachineAuthObject(AuthObject):
    token_type: TokenType = TokenType.MACHINE_TOKEN
    id: Optional[str] = None
    machine_id: Optional[str] = None
    client_id: Optional[str] = None
    name: Optional[str] = None
    scopes: Optional[List[str]] = None
    claims: Optional[Dict[str, Any]] = None


@dataclass
class RequestState:
    """Request Authentication State"""

    status: AuthStatus
    reason: Optional[Union[AuthErrorReason, TokenVerificationErrorReason]] = None
    token: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None


    @property
    def is_authenticated(self) -> bool:
        return self.status == AuthStatus.SIGNED_IN

    @property
    def is_signed_in(self) -> bool:
        return self.status == AuthStatus.SIGNED_IN

    @property
    def message(self) -> Optional[str]:
        if self.reason is None:
            return None
        return self.reason.value[1]

    def to_auth(self) -> AuthObject:
        from clerk_backend_api.security.machine import get_token_type #pylint: disable=C0415
        if self.status == AuthStatus.SIGNED_IN:
            if self.payload is None:
                raise ValueError("Payload must be provided for authenticated states.")
            if self.token is None:
                raise ValueError("Token must be provided for authenticated states.")
            token_type = get_token_type(self.token)
            if token_type == TokenType.SESSION_TOKEN:
                if self.payload.get('v') == 2:
                    return SessionAuthObjectV2(
                        azp=self.payload.get('azp'),
                        email=self.payload.get('email'),
                        exp=self.payload.get('exp'),
                        fva=self.payload.get('fva'),
                        iat=self.payload.get('iat'),
                        iss=self.payload.get('iss'),
                        jti=self.payload.get('jti'),
                        nbf=self.payload.get('nbf'),
                        role=self.payload.get('role'),
                        sid=self.payload.get('sid'),
                        sub=self.payload.get('sub'),
                        v=self.payload.get('v')
                    )

                return SessionAuthObjectV1(
                    session_id=self.payload.get('sid'),
                    user_id=self.payload.get('sub'),
                    org_id=self.payload.get('org_id'),
                    org_role=self.payload.get('org_role'),
                    org_permissions=self.payload.get('org_permissions'),
                    factor_verification_age=self.payload.get('fva'),
                    claims=self.payload,
                )

            if token_type == TokenType.OAUTH_TOKEN:
                return OAuthMachineAuthObject(id=self.payload.get('id'),
                                              user_id=self.payload.get('subject'),
                                              client_id=self.payload.get('client_id'),
                                              name=self.payload.get('name'),
                                              scopes=self.payload.get('scopes'))
            if token_type == TokenType.API_KEY:
                return APIKeyMachineAuthObject(id=self.payload.get('id'),
                                                user_id=self.payload.get('subject'),
                                                org_id=self.payload.get('org_id'),
                                                name=self.payload.get('name'),
                                                scopes=self.payload.get('scopes'),
                                                claims=self.payload.get('claims'))
            if token_type == TokenType.MACHINE_TOKEN:
                return M2MMachineAuthObject(id=self.payload.get('id'),
                                     machine_id=self.payload.get('subject'),
                                     client_id=self.payload.get('client_id'),
                                     name=self.payload.get('name'),
                                     scopes=self.payload.get('scopes'),
                                     claims=self.payload.get('claims'))

            raise ValueError(f"Unsupported token type: {token_type}")
        else:
            raise ValueError("Cannot convert to AuthObject in unauthenticated state.")



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

