"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import TypedDict
from typing_extensions import NotRequired


class UpdateInstanceRestrictionsRequestBodyTypedDict(TypedDict):
    allowlist: NotRequired[Nullable[bool]]
    blocklist: NotRequired[Nullable[bool]]
    block_email_subaddresses: NotRequired[Nullable[bool]]
    block_disposable_email_domains: NotRequired[Nullable[bool]]
    ignore_dots_for_gmail_addresses: NotRequired[Nullable[bool]]
    

class UpdateInstanceRestrictionsRequestBody(BaseModel):
    allowlist: OptionalNullable[bool] = UNSET
    blocklist: OptionalNullable[bool] = UNSET
    block_email_subaddresses: OptionalNullable[bool] = UNSET
    block_disposable_email_domains: OptionalNullable[bool] = UNSET
    ignore_dots_for_gmail_addresses: OptionalNullable[bool] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["allowlist", "blocklist", "block_email_subaddresses", "block_disposable_email_domains", "ignore_dots_for_gmail_addresses"]
        nullable_fields = ["allowlist", "blocklist", "block_email_subaddresses", "block_disposable_email_domains", "ignore_dots_for_gmail_addresses"]
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
        
