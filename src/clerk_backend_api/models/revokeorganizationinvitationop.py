"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import TypedDict
from typing_extensions import Annotated


class RevokeOrganizationInvitationRequestBodyTypedDict(TypedDict):
    requesting_user_id: str
    r"""The ID of the user that revokes the invitation.
    Must be an administrator in the organization.
    """
    

class RevokeOrganizationInvitationRequestBody(BaseModel):
    requesting_user_id: str
    r"""The ID of the user that revokes the invitation.
    Must be an administrator in the organization.
    """
    

class RevokeOrganizationInvitationRequestTypedDict(TypedDict):
    organization_id: str
    r"""The organization ID."""
    invitation_id: str
    r"""The organization invitation ID."""
    request_body: RevokeOrganizationInvitationRequestBodyTypedDict
    

class RevokeOrganizationInvitationRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The organization ID."""
    invitation_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The organization invitation ID."""
    request_body: Annotated[RevokeOrganizationInvitationRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
