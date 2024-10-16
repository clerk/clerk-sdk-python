"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from enum import Enum
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UsersGetOrganizationInvitationsQueryParamStatus(str, Enum):
    r"""Filter organization invitations based on their status"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    REVOKED = "revoked"

class UsersGetOrganizationInvitationsRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user whose organization invitations we want to retrieve"""
    limit: NotRequired[int]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[int]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    status: NotRequired[UsersGetOrganizationInvitationsQueryParamStatus]
    r"""Filter organization invitations based on their status"""
    

class UsersGetOrganizationInvitationsRequest(BaseModel):
    user_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the user whose organization invitations we want to retrieve"""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    status: Annotated[Optional[UsersGetOrganizationInvitationsQueryParamStatus], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Filter organization invitations based on their status"""
    