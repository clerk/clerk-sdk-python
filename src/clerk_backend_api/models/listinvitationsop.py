"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListInvitationsQueryParamStatus(str, Enum):
    r"""Filter invitations based on their status"""

    PENDING = "pending"
    ACCEPTED = "accepted"
    REVOKED = "revoked"
    EXPIRED = "expired"


class ListInvitationsRequestTypedDict(TypedDict):
    status: NotRequired[ListInvitationsQueryParamStatus]
    r"""Filter invitations based on their status"""
    query: NotRequired[str]
    r"""Filter invitations based on their `email_address` or `id`"""
    order_by: NotRequired[str]
    r"""Allows to return invitations in a particular order.
    At the moment, you can order the returned invitations either by their `created_at`, `email_address` or `expires_at`.
    In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.
    For example, if you want invitations to be returned in descending order according to their `created_at` property, you can use `-created_at`.
    If you don't use `+` or `-`, then `+` is implied.
    Defaults to `-created_at`.
    """
    paginated: NotRequired[bool]
    r"""Whether to paginate the results.
    If true, the results will be paginated.
    If false, the results will not be paginated.
    """
    limit: NotRequired[int]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[int]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """


class ListInvitationsRequest(BaseModel):
    status: Annotated[
        Optional[ListInvitationsQueryParamStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter invitations based on their status"""

    query: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter invitations based on their `email_address` or `id`"""

    order_by: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "-created_at"
    r"""Allows to return invitations in a particular order.
    At the moment, you can order the returned invitations either by their `created_at`, `email_address` or `expires_at`.
    In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.
    For example, if you want invitations to be returned in descending order according to their `created_at` property, you can use `-created_at`.
    If you don't use `+` or `-`, then `+` is implied.
    Defaults to `-created_at`.
    """

    paginated: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to paginate the results.
    If true, the results will be paginated.
    If false, the results will not be paginated.
    """

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
