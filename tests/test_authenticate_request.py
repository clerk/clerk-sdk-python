from unittest.mock import patch

import pytest
from clerk_backend_api.security.types import AuthenticateRequestOptions, AuthStatus, AuthErrorReason
from clerk_backend_api.security.verifytoken import TokenVerificationError, TokenVerificationErrorReason, \
    VerifyTokenOptions

from clerk_backend_api import authenticate_request


class MockRequest:
    def __init__(self, headers):
        self._headers = headers

    @property
    def headers(self):
        return self._headers

@pytest.fixture
def session_token():
    return "dummy.jwt.token"

@pytest.fixture
def default_options_with_secret_key():
    return AuthenticateRequestOptions(
        secret_key="test-secret",
        jwt_key=None,
        audience="test-audience",
        authorized_parties=["https://example.com"],
        clock_skew_in_ms=5000
    )

@pytest.fixture
def default_options_with_jwt_key():
    return AuthenticateRequestOptions(
        secret_key=None,
        jwt_key="test-jwt-key",
        audience="test-audience",
        authorized_parties=["https://example.com"],
        clock_skew_in_ms=5000
    )


def make_headers(auth_token=None, cookie=None):
    headers = {}
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    if cookie:
        headers["cookie"] = cookie
    return headers

def assert_verify_called_with(mock_verify, token, opts: AuthenticateRequestOptions):
    assert mock_verify.called
    actual_token, actual_options = mock_verify.call_args.args
    assert actual_token == token
    assert isinstance(actual_options, VerifyTokenOptions)
    assert actual_options.secret_key == opts.secret_key
    assert actual_options.jwt_key == opts.jwt_key
    assert actual_options.audience == opts.audience
    assert actual_options.authorized_parties == opts.authorized_parties
    assert actual_options.clock_skew_in_ms == opts.clock_skew_in_ms

def test_missing_token_returns_signed_out(default_options_with_secret_key):
    request = MockRequest(headers={})
    state = authenticate_request(request, default_options_with_secret_key)
    assert state.status == AuthStatus.SIGNED_OUT
    assert state.reason == AuthErrorReason.SESSION_TOKEN_MISSING

def test_missing_secret_key_returns_signed_out(session_token):
    request = MockRequest(headers=make_headers(auth_token=session_token))
    opts = AuthenticateRequestOptions(secret_key=None)
    state = authenticate_request(request, opts)
    assert state.status == AuthStatus.SIGNED_OUT
    assert state.reason == AuthErrorReason.SECRET_KEY_MISSING

def test_missing_jwt_key_returns_signed_out(session_token):
    request = MockRequest(headers=make_headers(auth_token=session_token))
    opts = AuthenticateRequestOptions(secret_key=None, jwt_key=None)
    state = authenticate_request(request, opts)
    assert state.status == AuthStatus.SIGNED_OUT
    assert state.reason == AuthErrorReason.SECRET_KEY_MISSING


@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v1_token(mock_verify_token, session_token, default_options_with_secret_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_secret_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert state.payload["sub"] == "user_123"
    assert "org_permissions" not in state.payload
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_secret_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v1_token_with_jwt_key(mock_verify_token, session_token, default_options_with_jwt_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_jwt_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert state.payload["sub"] == "user_123"
    assert "org_permissions" not in state.payload
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_jwt_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v2_token_without_org(mock_verify_token, session_token, default_options_with_secret_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "v": 2,
        "fea": "u:foo,u:bar",
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_secret_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert "org_permissions" not in state.payload
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_secret_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v2_token_without_org_with_jwt_key(mock_verify_token, session_token, default_options_with_jwt_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "v": 2,
        "fea": "u:foo,u:bar",
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_jwt_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert "org_permissions" not in state.payload
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_jwt_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v2_token_with_org_permissions(mock_verify_token, session_token, default_options_with_secret_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "v": 2,
        "fea": "o:admin,o:reports",
        "o": {
            "id": "org_abc",
            "slg": "org-slug",
            "rol": "owner",
            "per": "view,edit",
            "fpm": "1,2"
        },
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_secret_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert state.payload["org_id"] == "org_abc"
    assert state.payload["org_slug"] == "org-slug"
    assert state.payload["org_role"] == "owner"
    assert "org:admin:view" in state.payload["org_permissions"] or "org:reports:edit" in state.payload["org_permissions"]
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_secret_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_valid_v2_token_with_org_permissions_with_jwt_key(mock_verify_token, session_token, default_options_with_jwt_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "v": 2,
        "fea": "o:admin,o:reports",
        "o": {
            "id": "org_abc",
            "slg": "org-slug",
            "rol": "owner",
            "per": "view,edit",
            "fpm": "1,2"
        },
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_jwt_key)

    assert state.status == AuthStatus.SIGNED_IN
    assert state.payload["org_id"] == "org_abc"
    assert state.payload["org_slug"] == "org-slug"
    assert state.payload["org_role"] == "owner"
    assert "org:admin:view" in state.payload["org_permissions"] or "org:reports:edit" in state.payload["org_permissions"]
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_jwt_key)

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_token_verification_error_returns_signed_out(mock_verify_token, session_token, default_options_with_secret_key):
    mock_verify_token.side_effect = TokenVerificationError(reason=TokenVerificationErrorReason.TOKEN_INVALID)

    request = MockRequest(headers=make_headers(auth_token=session_token))
    state = authenticate_request(request, default_options_with_secret_key)

    assert state.status == AuthStatus.SIGNED_OUT
    assert state.reason == TokenVerificationErrorReason.TOKEN_INVALID
    assert_verify_called_with(mock_verify_token, session_token, default_options_with_secret_key)

def test_invalid_token_type_returns_signed_out(session_token):
    request = MockRequest(headers=make_headers(auth_token=session_token))
    opts = AuthenticateRequestOptions(
        secret_key="test-secret",
        jwt_key=None,
        audience="test-audience",
        authorized_parties=["https://example.com"],
        clock_skew_in_ms=5000,
        accepts_token=["machine_token"]  # Only accepts machine tokens
    )
    state = authenticate_request(request, opts)
    assert state.status == AuthStatus.SIGNED_OUT
    assert state.reason == AuthErrorReason.TOKEN_TYPE_NOT_SUPPORTED

@patch("clerk_backend_api.security.authenticaterequest.verify_token", autospec=True)
def test_if_no_token_type_is_passed_then_any_token_type_is_accepted(mock_verify_token, session_token, default_options_with_jwt_key):
    mock_verify_token.return_value = {
        "sub": "user_123",
        "v": 2,
        "fea": "o:admin,o:reports",
        "o": {
            "id": "org_abc",
            "slg": "org-slug",
            "rol": "owner",
            "per": "view,edit",
            "fpm": "1,2"
        },
        "aud": "test-audience",
        "iss": "https://api.clerk.com"
    }
    request = MockRequest(headers=make_headers(auth_token=session_token))
    opts = AuthenticateRequestOptions(
        secret_key="test-secret",
        jwt_key=None,
        audience="test-audience",
        authorized_parties=["https://example.com"],
        clock_skew_in_ms=5000,
    )
    state = authenticate_request(request, opts)
    assert state.status == AuthStatus.SIGNED_IN
    assert state.token == session_token