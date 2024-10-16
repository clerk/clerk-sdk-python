"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteExternalAccountRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user's external account"""
    external_account_id: str
    r"""The ID of the external account to delete"""
    

class DeleteExternalAccountRequest(BaseModel):
    user_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the user's external account"""
    external_account_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the external account to delete"""
    