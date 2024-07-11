"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .organizationmembership import OrganizationMembership, OrganizationMembershipTypedDict
from clerk.types import BaseModel
from typing import List, TypedDict


class OrganizationMembershipsTypedDict(TypedDict):
    data: List[OrganizationMembershipTypedDict]
    total_count: int
    r"""Total number of organization memberships

    """
    

class OrganizationMemberships(BaseModel):
    data: List[OrganizationMembership]
    total_count: int
    r"""Total number of organization memberships

    """
    