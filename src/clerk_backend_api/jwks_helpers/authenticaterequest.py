import httpx
from dataclasses import dataclass
from typing import List, Union, Optional
from http.cookies import SimpleCookie

from ..models import ClerkErrors, ClerkError
from .verifytoken import InvalidKeyException, InvalidTokenException, VerifyTokenOptions, verify_token


@dataclass
class AuthenticateRequestOptions:
    """
    Options to configure authenticate_request.

    Attributes:
        secret_key (Optional[str]): The Clerk secret key from the API Keys page in the Clerk Dashboard.
        jwt_key (Optional[str]): Used to verify the session token in a networkless manner.
        domain (Optional[str]): The domain for the application.
        audience (Union[str, List[str], None]): An audience or list of audiences to verify against.
        authorized_parties (Optional[List[str]]): An allowlist of origins to verify against.
        clock_skew_in_ms (int): Allowed time difference (in milliseconds) between the Clerk server (which generates the token)
                                and the clock of the user's application server when validating a token. Defaults to 5000 ms.
    """

    secret_key: Optional[str] = None
    jwt_key: Optional[str] = None
    domain: str = 'api.clerk.com'
    audience: Union[str, List[str], None] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000


def authenticate_request(request: httpx.Request, options: AuthenticateRequestOptions) -> bool:
    """ Authenticates the session token. Networkless if the options.jwt_key is provided.
    Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API.
    """

    def get_session_token(request) -> str:
        """Retrieve token from __session cookie or Authorization header."""

        cookie_header = request.headers.get('cookie')
        if cookie_header is not None:
            session_cookie = SimpleCookie(cookie_header).get('__session')
            if session_cookie is not None:
                return session_cookie.value

        bearer_token = request.headers.get('Authorization')
        if bearer_token is not None:
            return bearer_token.replace('Bearer ', '')

        raise ClerkErrors(data=[
            ClerkError(
                message='Session Token not found. Please sign in.',
                long_message='Could not retrieve session token from neither the "__session" cookie nor the Authorization Header',
                code='401'
            )
        ])

    try:
        verify_token(
            get_session_token(request),
            VerifyTokenOptions(
                audience=options.audience,
                authorized_parties=options.authorized_parties,
                secret_key=options.secret_key,
                clock_skew_in_ms=options.clock_skew_in_ms,
                jwt_key=options.jwt_key,
                api_url=f'https://{options.domain}',
            ),
        )
        return True

    except InvalidKeyException:
        raise
    except InvalidTokenException:
        return False
