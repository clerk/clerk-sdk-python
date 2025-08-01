"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationmembershippublicuserdata import (
    OrganizationMembershipPublicUserData,
    OrganizationMembershipPublicUserDataTypedDict,
)
from clerk_backend_api.types import BaseModel, Nullable, UNSET_SENTINEL
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class OrganizationMembershipObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    ORGANIZATION_MEMBERSHIP = "organization_membership"


class OrganizationMembershipOrganizationObject(str, Enum):
    ORGANIZATION = "organization"


class OrganizationMembershipOrganizationTypedDict(TypedDict):
    object: OrganizationMembershipOrganizationObject
    id: str
    name: str
    slug: str
    has_image: bool
    max_allowed_memberships: int
    admin_delete_enabled: bool
    public_metadata: Dict[str, Any]
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    image_url: NotRequired[str]
    members_count: NotRequired[int]
    missing_member_with_elevated_permissions: NotRequired[bool]
    pending_invitations_count: NotRequired[int]
    private_metadata: NotRequired[Dict[str, Any]]
    created_by: NotRequired[str]


class OrganizationMembershipOrganization(BaseModel):
    object: OrganizationMembershipOrganizationObject

    id: str

    name: str

    slug: str

    has_image: bool

    max_allowed_memberships: int

    admin_delete_enabled: bool

    public_metadata: Dict[str, Any]

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    image_url: Optional[str] = None

    members_count: Optional[int] = None

    missing_member_with_elevated_permissions: Optional[bool] = None

    pending_invitations_count: Optional[int] = None

    private_metadata: Optional[Dict[str, Any]] = None

    created_by: Optional[str] = None


class OrganizationMembershipTypedDict(TypedDict):
    r"""Hello world"""

    id: str
    object: OrganizationMembershipObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    role: str
    permissions: Nullable[List[str]]
    public_metadata: Dict[str, Any]
    r"""Metadata saved on the organization membership, accessible from both Frontend and Backend APIs"""
    organization: OrganizationMembershipOrganizationTypedDict
    created_at: int
    r"""Unix timestamp of creation."""
    updated_at: int
    r"""Unix timestamp of last update."""
    role_name: NotRequired[str]
    private_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata saved on the organization membership, accessible only from the Backend API"""
    public_user_data: NotRequired[OrganizationMembershipPublicUserDataTypedDict]
    r"""An organization membership with public user data populated"""


class OrganizationMembership(BaseModel):
    r"""Hello world"""

    id: str

    object: OrganizationMembershipObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    role: str

    permissions: Nullable[List[str]]

    public_metadata: Dict[str, Any]
    r"""Metadata saved on the organization membership, accessible from both Frontend and Backend APIs"""

    organization: OrganizationMembershipOrganization

    created_at: int
    r"""Unix timestamp of creation."""

    updated_at: int
    r"""Unix timestamp of last update."""

    role_name: Optional[str] = None

    private_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata saved on the organization membership, accessible only from the Backend API"""

    public_user_data: Optional[OrganizationMembershipPublicUserData] = None
    r"""An organization membership with public user data populated"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["role_name", "private_metadata", "public_user_data"]
        nullable_fields = ["permissions"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
