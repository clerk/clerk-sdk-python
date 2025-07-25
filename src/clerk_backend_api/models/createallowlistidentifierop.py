"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateAllowlistIdentifierRequestBodyTypedDict(TypedDict):
    identifier: str
    r"""The identifier to be added in the allow-list.
    This can be an email address, a phone number, or a web3 wallet.
    """
    notify: NotRequired[bool]
    r"""This flag denotes whether the given identifier will receive an invitation to join the application.
    Note that this only works for email address and phone number identifiers.
    """


class CreateAllowlistIdentifierRequestBody(BaseModel):
    identifier: str
    r"""The identifier to be added in the allow-list.
    This can be an email address, a phone number, or a web3 wallet.
    """

    notify: Optional[bool] = False
    r"""This flag denotes whether the given identifier will receive an invitation to join the application.
    Note that this only works for email address and phone number identifiers.
    """
