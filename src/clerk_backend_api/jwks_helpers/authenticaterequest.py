from dataclasses import dataclass
from enum import Enum
from http.cookies import SimpleCookie
from typing import Any, Dict, List, Union, Optional, Protocol, Mapping
from warnings import warn

from .verifytoken import (
    TokenVerificationErrorReason,
    TokenVerificationError,
    VerifyTokenOptions,
    verify_token,
)


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

def authenticate_request(request: Requestish, options: AuthenticateRequestOptions) -> RequestState:
    """ Authenticates the session token. Networkless if the options.jwt_key is provided.
       Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API."""


    def __compute_org_permissions(claims: Dict[str, Any]) -> List[str]:
        features_str = claims.get("fea")
        if features_str is None:
            return []

        org_claims = claims.get("o", {})
        permissions_str = org_claims.get("per")
        mappings_str = org_claims.get("fpm")

        if not all(isinstance(s, str) for s in [permissions_str, mappings_str]):
            return []

        features = features_str.split(",")
        permissions = permissions_str.split(",")
        mappings = mappings_str.split(",")

        org_permissions = []

        for idx, mapping in enumerate(mappings):
            if idx >= len(features):
                continue
            feature_parts = features[idx].split(":")
            if len(feature_parts) != 2:
                continue

            scope, feature = feature_parts
            if "o" not in scope:
                continue

            try:
                binary = bin(int(mapping))[2:].lstrip("0")
            except ValueError:
                continue

            reversed_binary = binary[::-1]

            for i, bit in enumerate(reversed_binary):
                if bit == "1" and i < len(permissions):
                    org_permissions.append(f"org:{feature}:{permissions[i]}")

        return org_permissions

    warn('authenticate_request method is applicable in the context of Backend APIs only.')

    def get_session_token(request: Requestish) -> Optional[str]:
        """Retrieve token from __session cookie or Authorization header."""

        bearer_token = request.headers.get('Authorization')
        if bearer_token is not None:
            return bearer_token.replace('Bearer ', '')

        cookie_header = request.headers.get('cookie')
        if cookie_header is not None:
            if cookie_header is not None:
                cookies = SimpleCookie(cookie_header)
                for key, value in cookies.items():
                    if key.startswith("__session"):
                        return value.value

        return None


    session_token = get_session_token(request)

    if session_token is None:
        return RequestState(status=AuthStatus.SIGNED_OUT, reason=AuthErrorReason.SESSION_TOKEN_MISSING)

    try:
        if options.secret_key:
            payload = verify_token(
                session_token,
                VerifyTokenOptions(
                    audience=options.audience,
                    authorized_parties=options.authorized_parties,
                    secret_key=options.secret_key,
                    clock_skew_in_ms=options.clock_skew_in_ms,
                    jwt_key=None,
                ),
            )
        elif options.jwt_key:
            payload = verify_token(
                session_token,
                VerifyTokenOptions(
                    audience=options.audience,
                    authorized_parties=options.authorized_parties,
                    secret_key=None,
                    clock_skew_in_ms=options.clock_skew_in_ms,
                    jwt_key=options.jwt_key,
                ),
            )
        else:
            return RequestState(status=AuthStatus.SIGNED_OUT, reason=AuthErrorReason.SECRET_KEY_MISSING)

        if payload is not None and payload.get("v") == 2:
            org_claims = payload.get("o", {})
            if org_claims:
                payload["org_id"] = org_claims.get("id")
                payload["org_slug"] = org_claims.get("slg")
                payload["org_role"] = org_claims.get("rol")

                org_permissions = __compute_org_permissions(payload)
                if org_permissions:
                    payload["org_permissions"] = org_permissions

        return RequestState(status=AuthStatus.SIGNED_IN, token=session_token, payload=payload)

    except TokenVerificationError as e:
        return RequestState(status=AuthStatus.SIGNED_OUT, reason=e.reason)





