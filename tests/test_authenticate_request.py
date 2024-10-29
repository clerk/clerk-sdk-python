import httpx
import pytest
from http.cookies import SimpleCookie
from warnings import warn
from .conftest import has_env_vars
from clerk_backend_api.jwks_helpers import (
    AuthErrorReason,
    AuthenticateRequestOptions,
    RequestState,
    TokenVerificationErrorReason
)


@pytest.mark.skipif(
    not has_env_vars(['CLERK_JWT_KEY']),
    reason="CLERK_JWT_KEY environment variable must be set"
)
def test_authenticate_request_no_session_token(clerk, request_url, ar_options):
    request = httpx.Request('GET', request_url)

    state = clerk.authenticate_request(request, ar_options)
    assert not state.is_signed_in
    assert state.reason == AuthErrorReason.SESSION_TOKEN_MISSING
    assert 'Could not retrieve session token' in state.message
    assert state.token is None
    assert state.payload is None


def assert_request_state(state: RequestState, session_token: str, ar_options: AuthenticateRequestOptions):
    if state.is_signed_in:
        assert state.message is None
        assert state.token is not None
        assert state.token == session_token
        assert state.payload is not None
        assert state.payload.get('azp') in ar_options.authorized_parties
    else:
        assert state.reason == TokenVerificationErrorReason.TOKEN_EXPIRED
        assert state.token is None
        assert state.payload is None
        warn("the provided session token is expired.")


@pytest.mark.skipif(
    not has_env_vars(['CLERK_JWT_KEY', 'CLERK_SESSION_TOKEN']),
    reason="CLERK_JWT_KEY and CLERK_SESSION_TOKEN environment variables must be set"
)
def test_authenticate_request_cookie(clerk, request_url, session_token, ar_options):
    with httpx.Client(cookies = {'__session': session_token}) as client:
        request = client.build_request('GET', request_url)
        cookies = SimpleCookie(request.headers.get('cookie', ''))
        assert '__session' in cookies.keys()
        assert cookies['__session'].value == session_token

        state = clerk.authenticate_request(request, ar_options)
        assert_request_state(state, session_token, ar_options)


@pytest.mark.skipif(
    not has_env_vars(['CLERK_JWT_KEY', 'CLERK_SESSION_TOKEN']),
    reason="CLERK_JWT_KEY and CLERK_SESSION_TOKEN environment variables must be set"
)
def test_authenticate_request_header(clerk, request_url, session_token, ar_options):
    request = httpx.Request('GET', request_url)
    request.headers['Authorization'] = f'Bearer {session_token}'

    ar_options.secret_key = None
    state = clerk.authenticate_request(request, ar_options)
    assert_request_state(state, session_token, ar_options)
