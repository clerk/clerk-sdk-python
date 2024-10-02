import jwt
import pytest
from clerk_backend_api.jwks_helpers import (
    verify_token,
    TokenVerificationErrorReason,
    TokenVerificationError,
)


def test_verify_token_invalid_token(vt_options):

    vt_options.jwt_key = None

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token('invalid.session.token', vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID


def test_verify_token_public_key_invalid_kid(vt_options):

    vt_options.jwt_key = None
    dummy_token = jwt.encode({}, "dummy_secret")

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(dummy_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH


def test_verify_token_missing_secret_key(session_token, vt_options):

    vt_options.jwt_key = None
    vt_options.secret_key = None

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.SECRET_KEY_MISSING


def test_verify_token_invalid_secret_key(session_token, vt_options):

    vt_options.jwt_key = None
    vt_options.secret_key='sk_test_invalid'

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_LOAD


def test_verify_token_invalid_jwt_key(session_token, vt_options):

    vt_options.jwt_key = 'invalid_pem_key'

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)

    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_RESOLVE


def test_verify_token_remote_ok(session_token, vt_options):

    vt_options.jwt_key = None
    payload = verify_token(session_token, vt_options)
    assert payload is not None
    assert payload.get('azp') in vt_options.authorized_parties


def test_verify_token_local_ok(session_token, vt_options):

    assert vt_options.jwt_key is not None

    payload = verify_token(session_token, vt_options)
    assert payload is not None
    assert payload.get('azp') in vt_options.authorized_parties
