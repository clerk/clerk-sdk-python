import httpx
from http.cookies import SimpleCookie
from clerk_backend_api.jwks_helpers import AuthErrorReason


def test_authenticate_request_no_session_token(clerk, request_url, ar_options):
    request = httpx.Request('GET', request_url)

    state = clerk.authenticate_request(request, ar_options)
    assert not state.is_signed_in
    assert state.reason == AuthErrorReason.SESSION_TOKEN_MISSING
    assert 'Could not retrieve session token' in state.message


def test_authenticate_request_cookie(clerk, request_url, session_token, ar_options):
    with httpx.Client(cookies = {'__session': session_token}) as client:
        request = client.build_request('GET', request_url)
        cookies = SimpleCookie(request.headers.get('cookie', ''))
        assert '__session' in cookies.keys()
        assert cookies['__session'].value == session_token

        state = clerk.authenticate_request(request, ar_options)
        assert state.is_signed_in
        assert state.message is None
        assert state.token == session_token


def test_authenticate_request_header(clerk, request_url, session_token, ar_options):
    request = httpx.Request('GET', request_url)
    request.headers['Authorization'] = f'Bearer {session_token}'

    ar_options.secret_key = None
    state = clerk.authenticate_request(request, ar_options)
    assert state.is_signed_in
    assert state.message is None
    assert state.token == session_token
