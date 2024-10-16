"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationdomain import OrganizationDomain, OrganizationDomainTypedDict
from clerk_backend_api.types import BaseModel
from typing import List, TypedDict


class OrganizationDomainsTypedDict(TypedDict):
    data: List[OrganizationDomainTypedDict]
    total_count: int
    r"""Total number of organization domains

    """
    

class OrganizationDomains(BaseModel):
    data: List[OrganizationDomain]
    total_count: int
    r"""Total number of organization domains

    """
    