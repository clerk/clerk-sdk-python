import json
import pytest
from clerk_backend_api import SDKError
from clerk_backend_api.jwks_helpers import (
    verify_token,
    VerifyTokenOptions,
    InvalidTokenException,
    InvalidKeyException
)


def test_verify_token_public_key_not_found(session_token, vt_options):

    vt_options.jwt_key = None

    with pytest.raises(InvalidTokenException) as exc_info:
        verify_token(session_token, vt_options)
    assert str(exc_info.value) == 'Public key not found in JWKS.'


def test_verify_token_invalid_kid(vt_options):

    vt_options.jwt_key = None

    with pytest.raises(InvalidTokenException) as exc_info:
        verify_token('invalid.session.token', vt_options)
    assert str(exc_info.value) == 'Could not parse kid from token.'


def test_verify_token_invalid_secret_key(session_token):

    # Testing on 'api.clerk.com' as no Bearer Authentication is required on test domain
    vt_options = VerifyTokenOptions(
        audience=None,
        authorized_parties=['api.clerk.com'],
        jwt_key=None,
        secret_key='sk_test_invalid',
        api_url='http://api.clerk.com',
        api_version='v1',
    )

    with pytest.raises(SDKError) as exc_info:
        verify_token(session_token, vt_options)
    error = json.loads(exc_info.value.body).get('errors')[0]
    assert error.get('message') == 'The provided Clerk Secret Key is invalid. Make sure that your Clerk Secret Key is correct.'
    assert error.get('code') == 'clerk_key_invalid'


def test_verify_token_invalid_jwt_key(session_token, vt_options):

    vt_options.jwt_key = 'invalid_pem_key'

    with pytest.raises(InvalidKeyException) as exc_info:
        verify_token(session_token, vt_options)

    assert str(exc_info.value) == 'Invalid Public Key'
