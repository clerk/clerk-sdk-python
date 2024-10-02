import httpx
import pytest
from http.cookies import SimpleCookie
from clerk_backend_api import ClerkErrors
from clerk_backend_api.jwks_helpers import authenticate_request


def test_authenticate_request_no_session_token(request_url, ar_options):
    request = httpx.Request('GET', request_url)

    with pytest.raises(ClerkErrors) as exc_info:
        authenticate_request(request, ar_options)

    assert exc_info.value.data[0].message == 'Session Token not found. Please sign in.'
    assert exc_info.value.data[0].code == '401'


def test_authenticate_request_cookie(request_url, session_token, ar_options):

    with httpx.Client(cookies = {'__session': session_token}) as client:
        request = client.build_request('GET', request_url)

        cookies = SimpleCookie(request.headers.get('cookie', ''))
        assert '__session' in cookies.keys()
        assert cookies['__session'].value == session_token

        is_signed_in = authenticate_request(request, ar_options)
        assert is_signed_in


def test_authenticate_request_header(request_url, session_token, ar_options):
    request = httpx.Request('GET', request_url)
    request.headers['Authorization'] = f'Bearer {session_token}'

    is_signed_in = authenticate_request(request, ar_options)
    assert is_signed_in
