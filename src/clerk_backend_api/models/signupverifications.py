"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .signupverification import SignUpVerification, SignUpVerificationTypedDict
from clerk_backend_api.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class ExternalAccountTypedDict(TypedDict):
    pass


class ExternalAccount(BaseModel):
    pass


class SignUpVerificationsTypedDict(TypedDict):
    email_address: Nullable[SignUpVerificationTypedDict]
    phone_number: Nullable[SignUpVerificationTypedDict]
    web3_wallet: Nullable[SignUpVerificationTypedDict]
    external_account: Nullable[ExternalAccountTypedDict]


class SignUpVerifications(BaseModel):
    email_address: Nullable[SignUpVerification]

    phone_number: Nullable[SignUpVerification]

    web3_wallet: Nullable[SignUpVerification]

    external_account: Nullable[ExternalAccount]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "email_address",
            "phone_number",
            "web3_wallet",
            "external_account",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
