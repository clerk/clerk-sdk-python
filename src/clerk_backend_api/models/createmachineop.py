"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class CreateMachineRequestBodyTypedDict(TypedDict):
    name: str
    r"""The name of the machine"""
    scoped_machines: NotRequired[List[str]]
    r"""Array of machine IDs that this machine will have access to. Maximum of 25 scopes per machine."""
    default_token_ttl: NotRequired[int]
    r"""The default time-to-live (TTL) in seconds for tokens created by this machine. Must be at least 1 second."""


class CreateMachineRequestBody(BaseModel):
    name: str
    r"""The name of the machine"""

    scoped_machines: Optional[List[str]] = None
    r"""Array of machine IDs that this machine will have access to. Maximum of 25 scopes per machine."""

    default_token_ttl: Optional[int] = 3600
    r"""The default time-to-live (TTL) in seconds for tokens created by this machine. Must be at least 1 second."""
