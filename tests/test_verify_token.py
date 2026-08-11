import json
from unittest.mock import patch, MagicMock, AsyncMock

import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from jwt.algorithms import RSAAlgorithm
from warnings import warn

from clerk_backend_api.security.verifytoken import (
    verify_token,
    verify_token_async,
    _get_remote_jwt_key,
    _get_remote_jwt_key_async,
)
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


class TestJwtVerificationAsync:
    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY']),
        reason="CLERK_SECRET_KEY environment variable must be set"
    )
    async def test_verify_token_invalid_token(self, vt_options):

        vt_options.jwt_key = None

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async('invalid.session.token', vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY']),
        reason="CLERK_SECRET_KEY environment variable must be set"
    )
    async def test_verify_token_public_key_invalid_kid(self, vt_options):

        vt_options.jwt_key = None
        dummy_token = jwt.encode({}, "dummy_secret")

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(dummy_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    async def test_verify_token_missing_secret_key(self, session_token, vt_options):

        vt_options.jwt_key = None
        vt_options.secret_key = None

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(session_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.SECRET_KEY_MISSING

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    async def test_verify_token_invalid_secret_key(self, session_token, vt_options):

        vt_options.jwt_key = None
        vt_options.secret_key = 'sk_test_invalid'

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(session_token, vt_options)
        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_LOAD

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SESSION_TOKEN']),
        reason="CLERK_SESSION_TOKEN environment variable must be set"
    )
    async def test_verify_token_invalid_jwt_key(self, session_token, vt_options):

        vt_options.jwt_key = 'invalid_pem_key'

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(session_token, vt_options)

        assert exc_info.value.reason == TokenVerificationErrorReason.JWK_FAILED_TO_RESOLVE

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_SECRET_KEY', 'CLERK_SESSION_TOKEN']),
        reason="CLERK_SECRET_KEY and CLERK_SESSION_TOKEN environment variables must be set"
    )
    async def test_verify_token_remote_ok(self, session_token, vt_options):

        vt_options.jwt_key = None

        await self._assert_payload(session_token, vt_options)

    @pytest.mark.asyncio
    @pytest.mark.skipif(
        not has_env_vars(['CLERK_JWT_KEY', 'CLERK_SESSION_TOKEN']),
        reason="CLERK_JWT_KEY and CLERK_SESSION_TOKEN environment variables must be set"
    )
    async def test_verify_token_local_ok(self, session_token, vt_options):

        assert vt_options.jwt_key is not None

        await self._assert_payload(session_token, vt_options)

    async def _assert_payload(self, session_token: str, vt_options: VerifyTokenOptions):
        payload = {}
        expired = False

        try:
            payload = await verify_token_async(session_token, vt_options)
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

    @pytest.fixture
    def options_mt(self):
        return VerifyTokenOptions(
            secret_key=None,
            machine_secret_key="some_machine_secret",
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

    def test_verify_machine_token_v2_success(self, options_mt):
        token = "mt_exampletoken"
        response_data = {"subject": "machine_v2_123"}

        with patch("httpx.Client.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = response_data
            mock_post.return_value = mock_response

            result = verify_token(token, options_mt)

            assert result == response_data
            mock_post.assert_called_once()
            # verify auth header has machine secret key
            headers = mock_post.call_args[1]['headers']
            assert headers['Authorization'] == f'Bearer {options_mt.machine_secret_key}'

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

    @patch("clerk_backend_api.security.verifytoken.jwt.decode")
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key")
    def test_verify_session_token_retries_on_key_rotation(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.side_effect = ["stale_key", "fresh_key"]
        mock_jwt_decode.side_effect = [jwt.InvalidSignatureError("bad sig"), {"subject": "user_123"}]

        with patch("clerk_backend_api.security.verifytoken.jwt.get_unverified_header", return_value={"kid": "key_123"}):
            result = verify_token(token, options)

        assert result == {"subject": "user_123"}
        assert mock_get_remote_jwt_key.call_count == 2
        assert mock_jwt_decode.call_count == 2

    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.InvalidSignatureError("bad sig"))
    def test_verify_session_token_no_retry_with_jwt_key(self, mock_jwt_decode, options):
        token = "some.jwt.token"
        options.jwt_key = "some_pem_key"

        with pytest.raises(TokenVerificationError) as exc_info:
            verify_token(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID_SIGNATURE
        mock_jwt_decode.assert_called_once()

    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.InvalidSignatureError("bad sig"))
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key")
    def test_verify_session_token_retry_still_fails(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.side_effect = ["stale_key", "still_wrong_key"]

        with patch("clerk_backend_api.security.verifytoken.jwt.get_unverified_header", return_value={"kid": "key_123"}):
            with pytest.raises(TokenVerificationError) as exc_info:
                verify_token(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID_SIGNATURE
        assert mock_get_remote_jwt_key.call_count == 2
        assert mock_jwt_decode.call_count == 2


class TestVerifyTokenAsync:
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

    @pytest.fixture
    def options_mt(self):
        return VerifyTokenOptions(
            secret_key=None,
            machine_secret_key="some_machine_secret",
            audience="test_audience",
            jwt_key=None,
            api_url="https://api.clerk.dev",
            api_version="v1",
            clock_skew_in_ms=0,
            authorized_parties=None
        )

    @pytest.mark.asyncio
    @patch("clerk_backend_api.security.verifytoken.jwt.decode")
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key_async", new_callable=AsyncMock)
    async def test_verify_session_token_success(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.return_value = "pem_public_key"
        mock_jwt_decode.return_value = {"subject": "user_123"}

        result = await verify_token_async(token, options)

        assert result == {"subject": "user_123"}
        mock_get_remote_jwt_key.assert_called_once()
        mock_jwt_decode.assert_called_once()

    @pytest.mark.asyncio
    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.ExpiredSignatureError("expired"))
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key_async", new_callable=AsyncMock)
    async def test_verify_session_token_expired(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.return_value = "pem_public_key"

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_EXPIRED

    @pytest.mark.asyncio
    async def test_verify_machine_token_success(self, options):
        token = "mt_exampletoken"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subject": "machine_123"}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("clerk_backend_api.security.verifytoken.httpx.AsyncClient", return_value=mock_client):
            result = await verify_token_async(token, options)

        assert result == {"subject": "machine_123"}
        mock_client.post.assert_called_once()

    @pytest.mark.asyncio
    async def test_verify_machine_token_v2_success(self, options_mt):
        token = "mt_exampletoken"
        response_data = {"subject": "machine_v2_123"}

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("clerk_backend_api.security.verifytoken.httpx.AsyncClient", return_value=mock_client):
            result = await verify_token_async(token, options_mt)

        assert result == response_data
        mock_client.post.assert_called_once()
        headers = mock_client.post.call_args[1]['headers']
        assert headers['Authorization'] == f'Bearer {options_mt.machine_secret_key}'

    @pytest.mark.asyncio
    async def test_verify_oauth_token_success(self, options):
        token = "oat_exampletoken"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subject": "oauth_456"}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("clerk_backend_api.security.verifytoken.httpx.AsyncClient", return_value=mock_client):
            result = await verify_token_async(token, options)

        assert result == {"subject": "oauth_456"}
        mock_client.post.assert_called_once()

    @pytest.mark.asyncio
    async def test_verify_api_key_success(self, options):
        token = "ak_exampletoken"
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subject": "apikey_789"}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("clerk_backend_api.security.verifytoken.httpx.AsyncClient", return_value=mock_client):
            result = await verify_token_async(token, options)

        assert result == {"subject": "apikey_789"}
        mock_client.post.assert_called_once()

    @pytest.mark.asyncio
    async def test_verify_machine_token_http_error(self, options):
        token = "mt_broken_token"
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.json.return_value = {"error": "unauthorized"}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch("clerk_backend_api.security.verifytoken.httpx.AsyncClient", return_value=mock_client):
            with pytest.raises(TokenVerificationError) as exc_info:
                await verify_token_async(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID

    @pytest.mark.asyncio
    @patch("clerk_backend_api.security.verifytoken.jwt.decode")
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key_async", new_callable=AsyncMock)
    async def test_verify_session_token_retries_on_key_rotation(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.side_effect = ["stale_key", "fresh_key"]
        mock_jwt_decode.side_effect = [jwt.InvalidSignatureError("bad sig"), {"subject": "user_123"}]

        with patch("clerk_backend_api.security.verifytoken.jwt.get_unverified_header", return_value={"kid": "key_123"}):
            result = await verify_token_async(token, options)

        assert result == {"subject": "user_123"}
        assert mock_get_remote_jwt_key.call_count == 2
        assert mock_jwt_decode.call_count == 2

    @pytest.mark.asyncio
    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.InvalidSignatureError("bad sig"))
    async def test_verify_session_token_no_retry_with_jwt_key(self, mock_jwt_decode, options):
        token = "some.jwt.token"
        options.jwt_key = "some_pem_key"

        with pytest.raises(TokenVerificationError) as exc_info:
            await verify_token_async(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID_SIGNATURE
        mock_jwt_decode.assert_called_once()

    @pytest.mark.asyncio
    @patch("clerk_backend_api.security.verifytoken.jwt.decode", side_effect=jwt.InvalidSignatureError("bad sig"))
    @patch("clerk_backend_api.security.verifytoken._get_remote_jwt_key_async", new_callable=AsyncMock)
    async def test_verify_session_token_retry_still_fails(self, mock_get_remote_jwt_key, mock_jwt_decode, options):
        token = "some.jwt.token"
        mock_get_remote_jwt_key.side_effect = ["stale_key", "still_wrong_key"]

        with patch("clerk_backend_api.security.verifytoken.jwt.get_unverified_header", return_value={"kid": "key_123"}):
            with pytest.raises(TokenVerificationError) as exc_info:
                await verify_token_async(token, options)

        assert exc_info.value.reason == TokenVerificationErrorReason.TOKEN_INVALID_SIGNATURE
        assert mock_get_remote_jwt_key.call_count == 2
        assert mock_jwt_decode.call_count == 2


class TestJwksCacheInstanceScoping:
    """Regression tests for AISEC-82.

    The JWKS cache was keyed on the bare `kid`. Since a Clerk `kid` is the
    instance id, a key cached for one instance was a direct hit for another
    instance's verification in the same process, so a token minted by
    instance B authenticated against instance A.
    """

    @staticmethod
    def _tenant(kid):
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        jwk = json.loads(RSAAlgorithm.to_jwk(key.public_key()))
        jwk.update({'kid': kid, 'alg': 'RS256', 'use': 'sig'})
        token = jwt.encode({'sub': f'user_{kid}'}, key, algorithm='RS256', headers={'kid': kid})
        return jwk, token

    def _fixtures(self, suffix):
        # The module-level cache outlives each test, so kids must be unique.
        jwk_a, _ = self._tenant(f'ins_a_{suffix}')
        jwk_b, token_b = self._tenant(f'ins_b_{suffix}')
        jwks = {'sk_test_a': {'keys': [jwk_a]}, 'sk_test_b': {'keys': [jwk_b]}}
        fetched = []

        def fetch(options):
            fetched.append(options.secret_key)
            return jwks[options.secret_key]

        return token_b, fetched, fetch

    def test_cached_key_is_not_served_to_another_instance(self):
        token_b, fetched, fetch = self._fixtures('sync')
        opts_a = VerifyTokenOptions(secret_key='sk_test_a')
        opts_b = VerifyTokenOptions(secret_key='sk_test_b')

        with patch('clerk_backend_api.security.verifytoken._fetch_jwks', side_effect=fetch):
            pem_b = _get_remote_jwt_key(token_b, opts_b)
            assert fetched == ['sk_test_b']

            # Instance A must miss the cache and fetch its own JWKS, which
            # has no such kid.
            with pytest.raises(TokenVerificationError) as exc_info:
                _get_remote_jwt_key(token_b, opts_a)
            assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH
            assert fetched == ['sk_test_b', 'sk_test_a']

            # Instance B's own entry is still cached.
            assert _get_remote_jwt_key(token_b, opts_b) == pem_b
            assert fetched == ['sk_test_b', 'sk_test_a']

    @pytest.mark.asyncio
    async def test_cached_key_is_not_served_to_another_instance_async(self):
        token_b, fetched, fetch = self._fixtures('async')
        opts_a = VerifyTokenOptions(secret_key='sk_test_a')
        opts_b = VerifyTokenOptions(secret_key='sk_test_b')

        async def fetch_async(options):
            return fetch(options)

        with patch('clerk_backend_api.security.verifytoken._fetch_jwks_async', side_effect=fetch_async):
            pem_b = await _get_remote_jwt_key_async(token_b, opts_b)
            assert fetched == ['sk_test_b']

            with pytest.raises(TokenVerificationError) as exc_info:
                await _get_remote_jwt_key_async(token_b, opts_a)
            assert exc_info.value.reason == TokenVerificationErrorReason.JWK_KID_MISMATCH
            assert fetched == ['sk_test_b', 'sk_test_a']

            assert await _get_remote_jwt_key_async(token_b, opts_b) == pem_b
            assert fetched == ['sk_test_b', 'sk_test_a']
