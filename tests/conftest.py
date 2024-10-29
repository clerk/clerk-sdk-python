import os
import pytest
from typing import Optional, Union, List
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import AuthenticateRequestOptions, VerifyTokenOptions


def has_env_vars(env_vars: List[str]) -> bool:
    return all(os.getenv(var, "").strip() for var in env_vars)


@pytest.fixture
def secret_key() -> Optional[str]:
    """Secret Key from Clerk Dashboard."""

    return os.getenv('CLERK_SECRET_KEY')


@pytest.fixture
def clerk(secret_key) -> Clerk:
    """Clerk SDK instance"""

    return Clerk(bearer_auth=secret_key)


@pytest.fixture
def jwt_key() -> Optional[str]:
    """PEM public key from Clerk Dashboard."""

    return os.getenv('CLERK_JWT_KEY')


@pytest.fixture
def authorized_parties() -> Optional[Union[str, List[str]]]:
    """Test Authorized Parties."""

    return ['http://localhost:3000']


@pytest.fixture
def audience() -> Optional[str]:
    """Test audience."""

    return None


@pytest.fixture
def request_url() -> str:
    """Test request URL."""

    return os.getenv('CLERK_API_URL', 'http://localhost:3000')


@pytest.fixture
def session_token() -> Optional[str]:
    """Test Session Token."""

    return os.getenv('CLERK_SESSION_TOKEN')


@pytest.fixture
def ar_options(jwt_key, audience, authorized_parties) -> AuthenticateRequestOptions:
    """Test options for authenticate_request"""

    return AuthenticateRequestOptions(
        secret_key=None,
        jwt_key=jwt_key,
        audience=audience,
        authorized_parties=authorized_parties,
    )


@pytest.fixture
def vt_options(secret_key, jwt_key, audience, authorized_parties) -> VerifyTokenOptions:
    """Test options for verify_token"""

    return VerifyTokenOptions(
        secret_key=secret_key,
        jwt_key=jwt_key,
        audience=audience,
        authorized_parties=authorized_parties,
    )
