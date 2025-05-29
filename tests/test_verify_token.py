from unittest.mock import patch, MagicMock

import jwt
import pytest
from warnings import warn

from clerk_backend_api.security.verifytoken import verify_token
from clerk_backend_api.security.types import TokenVerificationError, TokenVerificationErrorReason, VerifyTokenOptions, TokenType

from .conftest import has_env_vars


class TestJwtVerification:
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY']),
        reason="CLERK_SECRET_KEY environment variable must be set"
    )
    def test_verify_token_invalid_token(self, vt_options):

        vt_options.jwt_key = None

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token('invalid.session.token', vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID

    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY']),
        reason="CLERK_SECRET_KEY environment variable must be set"
    )
    def test_verify_token_public_key_invalid_kid(self, vt_options):

        vt_options.jwt_key = None
        dummy_token = jwt.encode({}, "dummy_secret")

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(dummy_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH

    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    def test_verify_token_missing_secret_key(self, session_token, vt_options):

        vt_options.jwt_key = None
        vt_options.secret_key = None

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(session_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.SECRET_KEY_MISSING

    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    def test_verify_token_invalid_secret_key(self, session_token, vt_options):

        vt_options.jwt_key = None
        vt_options.secret_key = 'sk_test_invalid'

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(session_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_LOAD

    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    def test_verify_token_invalid_jwt_key(self, session_token, vt_options):

        vt_options.jwt_key = 'invalid_pem_key'

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(session_token, vt_options)

        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_RESOLVE



    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY', 'CLERK_SESSION_TOKEN']),
        reason="CLERK_SECRET_KEY and CLERK_SESSION_TOKEN environment variables must be set"
    )
    def test_verify_token_remote_ok(self, session_token, vt_options):

        vt_options.jwt_key = None

        self._assert_payload(session_token, vt_options)

    @pytest.mark.skipif(
        not has_env_vars(['CLERK_JWT_KEY', 'CLERK_SESSION_TOKEN']),
        reason="CLERK_JWT_KEY and CLERK_SESSION_TOKEN environment variables must be set"
    )
    def test_verify_token_local_ok(self, session_token, vt_options):

        assert vt_options.jwt_key is not None

        self._assert_payload(session_token, vt_options)

    def _assert_payload(self, session_token: str, vt_options: VerifyTokenOptions):
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
            assert payload.get('azp') in vt_options.authorized_parties  # type:ignore


class TestVerifyToken:
    @pytest.fixture
    def options(self):
        return VerifyTokenOptions(
            secret_key="test_secret",
            audience="test_audience",
            jwt_key=None,
            api_url="https://api.clerk.dev",
            api_version="v1",
            clock_skew_in_ms=0,
            authorized_parties=None
        )

    @patch("clerk_backend_api.security.verifytoken.jwt.decode")
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key")
    def test_verify_session_token_success(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.return_value = "pem_public_key"
        mock_jwt_decode.return_value = {"subject": "user_123"}

        result = verify_token(token, options)

        assert result == {"subject": "user_123"}
        mock_get_remote_jwt_key.assert_called_once()
        mock_jwt_decode.assert_called_once()

    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.ExpiredSignatureError("expired"))
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key")
    def test_verify_session_token_expired(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.return_value = "pem_public_key"

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_EXPIRED

    @patch("httpx.Client.post")
    def test_verify_machine_token_success(self, mock_post, options):
        token = "mt_exampletoken"
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"subject": "machine_123"}
        mock_post.return_value = response

        result = verify_token(token, options)

        assert result == {"subject": "machine_123"}
        mock_post.assert_called_once()

    @patch("httpx.Client.post")
    def test_verify_oauth_token_success(self, mock_post, options):
        token = "oat_exampletoken"
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"subject": "oauth_456"}
        mock_post.return_value = response

        result = verify_token(token, options)

        assert result == {"subject": "oauth_456"}
        mock_post.assert_called_once()

    @patch("httpx.Client.post")
    def test_verify_api_key_success(self, mock_post, options):
        token = "ak_exampletoken"
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {"subject": "apikey_789"}
        mock_post.return_value = response

        result = verify_token(token, options)

        assert result == {"subject": "apikey_789"}
        mock_post.assert_called_once()

    @patch("httpx.Client.post")
    def test_verify_machine_token_http_error(self, mock_post, options):
        token = "mt_broken_token"
        response = MagicMock()
        response.status_code = 403
        response.json.return_value = {"error": "unauthorized"}
        mock_post.return_value = response

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID



