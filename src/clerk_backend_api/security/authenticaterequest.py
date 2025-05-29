from http.cookies import SimpleCookie
from typing import Any, Dict, List, Optional
from warnings import warn

from .machine import is_machine_token, get_token_type
from .types import Requestish, AuthenticateRequestOptions, RequestState, AuthStatus, AuthErrorReason
from .verifytoken import (
    TokenVerificationError,
    VerifyTokenOptions,
    verify_token,
)


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

    token_type = get_token_type(session_token)
    if not (token_type.value in options.accepts_token or 'any' in options.accepts_token):
        return RequestState(
            status=AuthStatus.SIGNED_OUT,
            reason=AuthErrorReason.TOKEN_TYPE_NOT_SUPPORTED,
        )

    if is_machine_token(session_token):
        verify_token_options = VerifyTokenOptions(secret_key=options.secret_key)
    else:
        if options.secret_key:
            verify_token_options = VerifyTokenOptions(
                audience=options.audience,
                authorized_parties=options.authorized_parties,
                secret_key=options.secret_key,
                clock_skew_in_ms=options.clock_skew_in_ms,
                jwt_key=None,
            )
        elif options.jwt_key:
            verify_token_options = VerifyTokenOptions(
                audience=options.audience,
                authorized_parties=options.authorized_parties,
                secret_key=None,
                clock_skew_in_ms=options.clock_skew_in_ms,
                jwt_key=options.jwt_key,
            )
        else:
            return RequestState(status=AuthStatus.SIGNED_OUT, reason=AuthErrorReason.SECRET_KEY_MISSING)

    try:
        payload = verify_token(session_token, verify_token_options)
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





