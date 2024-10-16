"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListOrganizationMembershipsRequestTypedDict(TypedDict):
    organization_id: str
    r"""The organization ID."""
    limit: NotRequired[int]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[int]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    order_by: NotRequired[str]
    r"""Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username.
    By prepending one of those values with + or -,
    we can choose to sort in ascending (ASC) or descending (DESC) order.\" 
    """
    

class ListOrganizationMembershipsRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The organization ID."""
    limit: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[int], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    order_by: Annotated[Optional[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username.
    By prepending one of those values with + or -,
    we can choose to sort in ascending (ASC) or descending (DESC) order.\" 
    """
    
