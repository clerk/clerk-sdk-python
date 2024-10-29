import jwt
import pytest
from warnings import warn
from .conftest import has_env_vars
from clerk_backend_api.jwks_helpers import (
    verify_token,
    TokenVerificationErrorReason,
    TokenVerificationError,
    VerifyTokenOptions,
)


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SECRET_KEY']),
    reason="CLERK_SECRET_KEY environment variable must be set"
)
def test_verify_token_invalid_token(vt_options):

    vt_options.jwt_key = None

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token('invalid.session.token', vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SECRET_KEY']),
    reason="CLERK_SECRET_KEY environment variable must be set"
)
def test_verify_token_public_key_invalid_kid(vt_options):

    vt_options.jwt_key = None
    dummy_token = jwt.encode({}, "dummy_secret")

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(dummy_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SESSION_TOKEN']),
    reason="CLERK_SESSION_TOKEN environment variable must be set"
)
def test_verify_token_missing_secret_key(session_token, vt_options):

    vt_options.jwt_key = None
    vt_options.secret_key = None

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.SECRET_KEY_MISSING


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SESSION_TOKEN']),
    reason="CLERK_SESSION_TOKEN environment variable must be set"
)
def test_verify_token_invalid_secret_key(session_token, vt_options):

    vt_options.jwt_key = None
    vt_options.secret_key='sk_test_invalid'

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)
    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_LOAD


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SESSION_TOKEN']),
    reason="CLERK_SESSION_TOKEN environment variable must be set"
)
def test_verify_token_invalid_jwt_key(session_token, vt_options):

    vt_options.jwt_key = 'invalid_pem_key'

    with pytest.raises(TokenVerificationError) as exc_info:
        verify_token(session_token, vt_options)

    assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_RESOLVE


def assert_payload(session_token: str, vt_options: VerifyTokenOptions):
    payload = {}
    expired = False

    try:
        payload = verify_token(session_token, vt_options)
    except TokenVerificationError as e:
        if e.reason != TokenVerificationErrorReason.TOKEN_EXPIRED:
            raise
        expired = True
        warn("the provided session token is expired.")

    if expired:
        assert payload == {}
    else:
        assert payload.get('azp') in vt_options.authorized_parties


@pytest.mark.skipif(
    not has_env_vars(['CLERK_SECRET_KEY', 'CLERK_SESSION_TOKEN']),
    reason="CLERK_SECRET_KEY and CLERK_SESSION_TOKEN environment variables must be set"
)
def test_verify_token_remote_ok(session_token, vt_options):

    vt_options.jwt_key = None

    assert_payload(session_token, vt_options)


@pytest.mark.skipif(
    not has_env_vars(['CLERK_JWT_KEY', 'CLERK_SESSION_TOKEN']),
    reason="CLERK_JWT_KEY and CLERK_SESSION_TOKEN environment variables must be set"
)
def test_verify_token_local_ok(session_token, vt_options):

    assert vt_options.jwt_key is not None

    assert_payload(session_token, vt_options)
