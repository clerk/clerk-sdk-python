"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpsertTemplatePathParamTemplateType(str, Enum):
    r"""The type of template to update"""
    EMAIL = "email"
    SMS = "sms"

class UpsertTemplateRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The user-friendly name of the template"""
    subject: NotRequired[Nullable[str]]
    r"""The email subject.
    Applicable only to email templates.
    """
    markup: NotRequired[Nullable[str]]
    r"""The editor markup used to generate the body of the template"""
    body: NotRequired[str]
    r"""The template body before variable interpolation"""
    delivered_by_clerk: NotRequired[Nullable[bool]]
    r"""Whether Clerk should deliver emails or SMS messages based on the current template"""
    from_email_name: NotRequired[str]
    r"""The local part of the From email address that will be used for emails.
    For example, in the address 'hello@example.com', the local part is 'hello'.
    Applicable only to email templates.
    """
    reply_to_email_name: NotRequired[str]
    r"""The local part of the Reply To email address that will be used for emails.
    For example, in the address 'hello@example.com', the local part is 'hello'.
    Applicable only to email templates.
    """
    

class UpsertTemplateRequestBody(BaseModel):
    name: Optional[str] = None
    r"""The user-friendly name of the template"""
    subject: OptionalNullable[str] = UNSET
    r"""The email subject.
    Applicable only to email templates.
    """
    markup: OptionalNullable[str] = UNSET
    r"""The editor markup used to generate the body of the template"""
    body: Optional[str] = None
    r"""The template body before variable interpolation"""
    delivered_by_clerk: OptionalNullable[bool] = UNSET
    r"""Whether Clerk should deliver emails or SMS messages based on the current template"""
    from_email_name: Optional[str] = None
    r"""The local part of the From email address that will be used for emails.
    For example, in the address 'hello@example.com', the local part is 'hello'.
    Applicable only to email templates.
    """
    reply_to_email_name: Optional[str] = None
    r"""The local part of the Reply To email address that will be used for emails.
    For example, in the address 'hello@example.com', the local part is 'hello'.
    Applicable only to email templates.
    """
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "subject", "markup", "body", "delivered_by_clerk", "from_email_name", "reply_to_email_name"]
        nullable_fields = ["subject", "markup", "delivered_by_clerk"]
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
        

class UpsertTemplateRequestTypedDict(TypedDict):
    template_type: UpsertTemplatePathParamTemplateType
    r"""The type of template to update"""
    slug: str
    r"""The slug of the template to update"""
    request_body: NotRequired[UpsertTemplateRequestBodyTypedDict]
    

class UpsertTemplateRequest(BaseModel):
    template_type: Annotated[UpsertTemplatePathParamTemplateType, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The type of template to update"""
    slug: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The slug of the template to update"""
    request_body: Annotated[Optional[UpsertTemplateRequestBody], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    
