"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class DeleteBackupCodeRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user whose backup codes are to be deleted."""
    

class DeleteBackupCodeRequest(BaseModel):
    user_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the user whose backup codes are to be deleted."""
    

class DeleteBackupCodeResponseBodyTypedDict(TypedDict):
    r"""Successful operation."""
    
    user_id: NotRequired[str]
    

class DeleteBackupCodeResponseBody(BaseModel):
    r"""Successful operation."""
    
    user_id: Optional[str] = None
    
