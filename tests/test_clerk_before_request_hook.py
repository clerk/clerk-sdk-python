import pytest
import httpx

from clerk_backend_api._hooks.clerk_before_request_hook import ClerkBeforeRequestHook
from clerk_backend_api._hooks.types import (
    BeforeRequestContext,
    HookContext
)

@pytest.fixture
def hook():
    """ClerkBeforeRequestHook instance"""
    return ClerkBeforeRequestHook()

@pytest.fixture
def hook_context():
    """HookContext instance"""
    return HookContext(
        config=None,
        base_url="https://api.clerk.dev",
        operation_id="test_operation",
        oauth2_scopes=None,
        security_source=None
    )

@pytest.fixture
def before_request_context(hook_context):
    """BeforeRequestContext instance"""
    return BeforeRequestContext(hook_context)

def test_before_request_adds_api_version_header(hook, before_request_context):
    """Test that before_request adds the Clerk-API-Version header"""
    # Create a request
    request = httpx.Request("GET", "https://api.clerk.dev/v1/users")
    
    # Call the before_request method
    modified_request = hook.before_request(before_request_context, request)
    
    # Assert that the request is returned (not an Exception)
    assert isinstance(modified_request, httpx.Request)
    
    # Assert that the Clerk-API-Version header is added with the correct value
    assert "Clerk-API-Version" in modified_request.headers
    assert modified_request.headers["Clerk-API-Version"] == "2025-04-10"
    
    # Assert that the original request is modified, not a new one created
    assert modified_request is request


def test_before_request_preserves_existing_headers(hook, before_request_context):
    """Test that before_request preserves existing headers"""
    # Create a request with existing headers
    request = httpx.Request(
        "GET", 
        "https://api.clerk.dev/v1/users",
        headers={"Authorization": "Bearer sdk_test_foo", "Content-Type": "application/json"}
    )
    
    # Call the before_request method
    modified_request = hook.before_request(before_request_context, request)
    
    # Assert that existing headers are preserved
    assert modified_request.headers["Authorization"] == "Bearer sdk_test_foo"
    assert modified_request.headers["Content-Type"] == "application/json"
    
    # Assert that the Clerk-API-Version header is added
    assert modified_request.headers["Clerk-API-Version"] == "2025-04-10"


def test_before_request_overwrites_existing_api_version_header(hook, before_request_context):
    """Test that before_request overwrites an existing Clerk-API-Version header"""
    # Create a request with an existing Clerk-API-Version header
    request = httpx.Request(
        "GET", 
        "https://api.clerk.dev/v1/users",
        headers={"Clerk-API-Version": "2021-02-05"}
    )
    
    # Call the before_request method
    modified_request = hook.before_request(before_request_context, request)
    
    # Assert that the Clerk-API-Version header is overwritten
    assert modified_request.headers["Clerk-API-Version"] == "2025-04-10"
