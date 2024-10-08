"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateSignUpRequestBodyTypedDict(TypedDict):
    custom_action: NotRequired[bool]
    r"""Specifies whether a custom action has run for this sign-up attempt.
    This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user.
    After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting `custom_action` to `true`.
    """
    external_id: NotRequired[Nullable[str]]
    r"""The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution.
    This will be copied to the resulting user when the sign-up is completed.
    """
    

class UpdateSignUpRequestBody(BaseModel):
    custom_action: Optional[bool] = None
    r"""Specifies whether a custom action has run for this sign-up attempt.
    This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user.
    After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting `custom_action` to `true`.
    """
    external_id: OptionalNullable[str] = UNSET
    r"""The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution.
    This will be copied to the resulting user when the sign-up is completed.
    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["custom_action", "external_id"]
        nullable_fields = ["external_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class UpdateSignUpRequestTypedDict(TypedDict):
    id: str
    r"""The ID of the sign-up to update"""
    request_body: NotRequired[UpdateSignUpRequestBodyTypedDict]
    

class UpdateSignUpRequest(BaseModel):
    id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the sign-up to update"""
    request_body: Annotated[Optional[UpdateSignUpRequestBody], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
