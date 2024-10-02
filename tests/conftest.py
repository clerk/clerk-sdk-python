import os
import pytest
from typing import Optional
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions, VerifyTokenOptions


@pytest.fixture
def secret_key() -> Optional[str]:
    """The Clerk secret key from Clerk Dashboard."""

    return os.getenv('CLERK_SECRET_KEY')

@pytest.fixture
def jwt_key() -> Optional[str]:
    """The PEM public key from Clerk Dashboard."""

    return os.getenv('CLERK_JWT_KEY')


@pytest.fixture
def domain() -> str:
    """The domain for the application."""

    return os.getenv('CLERK_DOMAIN', 'api.clerk.com')


@pytest.fixture
def api_url(domain) -> str:
    """Test API URL."""

    return f'https://{domain}'


@pytest.fixture
def api_version() -> str:
    """Test API version."""

    return 'v1'


@pytest.fixture
def request_url(api_url, api_version) -> str:
    """Test Request URL."""

    return f'{api_url}/{api_version}'


@pytest.fixture
def session_token() -> Optional[str]:
    """Test Session Token."""

    return os.getenv('CLERK_SESSION_TOKEN')


@pytest.fixture
def ar_options(secret_key, jwt_key, domain) -> AuthenticateRequestOptions:
    """Test options for authenticate_request"""

    return AuthenticateRequestOptions(
        secret_key=secret_key,
        jwt_key=jwt_key,
        domain=domain,
        audience=None,
        authorized_parties=[domain, 'localhost:3001'],
    )


@pytest.fixture
def vt_options(secret_key, jwt_key, domain, api_url, api_version) -> VerifyTokenOptions:
    """Test options for verify_token"""

    return VerifyTokenOptions(
        audience=None,
        authorized_parties=[domain, 'localhost:3001'],
        jwt_key=jwt_key,
        secret_key=secret_key,
        api_url=api_url,
        api_version=api_version,
    )
