"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from clerk.types import BaseModel
from clerk.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteOAuthApplicationRequestTypedDict(TypedDict):
    oauth_application_id: str
    r"""The ID of the OAuth application to delete"""
    

class DeleteOAuthApplicationRequest(BaseModel):
    oauth_application_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the OAuth application to delete"""
    