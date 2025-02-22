"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InstanceRestrictionsObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    INSTANCE_RESTRICTIONS = "instance_restrictions"


class InstanceRestrictionsTypedDict(TypedDict):
    r"""Success"""

    object: NotRequired[InstanceRestrictionsObject]
    r"""String representing the object's type. Objects of the same type share the same value."""
    allowlist: NotRequired[bool]
    blocklist: NotRequired[bool]
    block_email_subaddresses: NotRequired[bool]
    ignore_dots_for_gmail_addresses: NotRequired[bool]


class InstanceRestrictions(BaseModel):
    r"""Success"""

    object: Optional[InstanceRestrictionsObject] = None
    r"""String representing the object's type. Objects of the same type share the same value."""

    allowlist: Optional[bool] = None

    blocklist: Optional[bool] = None

    block_email_subaddresses: Optional[bool] = None

    ignore_dots_for_gmail_addresses: Optional[bool] = None
