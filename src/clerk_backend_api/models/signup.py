"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class SignUpObject(str, Enum):
    SIGN_UP_ATTEMPT = "sign_up_attempt"


class SignUpStatus(str, Enum):
    MISSING_REQUIREMENTS = "missing_requirements"
    COMPLETE = "complete"
    ABANDONED = "abandoned"


class VerificationsTypedDict(TypedDict):
    pass


class Verifications(BaseModel):
    pass


class ExternalAccountTypedDict(TypedDict):
    pass


class ExternalAccount(BaseModel):
    pass


class SignUpTypedDict(TypedDict):
    r"""Success"""

    object: SignUpObject
    id: str
    status: SignUpStatus
    password_enabled: bool
    custom_action: bool
    abandon_at: int
    required_fields: NotRequired[List[str]]
    optional_fields: NotRequired[List[str]]
    missing_fields: NotRequired[List[str]]
    unverified_fields: NotRequired[List[str]]
    verifications: NotRequired[VerificationsTypedDict]
    username: NotRequired[Nullable[str]]
    email_address: NotRequired[Nullable[str]]
    phone_number: NotRequired[Nullable[str]]
    web3_wallet: NotRequired[Nullable[str]]
    first_name: NotRequired[Nullable[str]]
    last_name: NotRequired[Nullable[str]]
    unsafe_metadata: NotRequired[Dict[str, Any]]
    public_metadata: NotRequired[Dict[str, Any]]
    external_id: NotRequired[Nullable[str]]
    created_session_id: NotRequired[Nullable[str]]
    created_user_id: NotRequired[Nullable[str]]
    legal_accepted_at: NotRequired[Nullable[int]]
    r"""Unix timestamp at which the user accepted the legal requirements.

    """
    external_account: NotRequired[ExternalAccountTypedDict]


class SignUp(BaseModel):
    r"""Success"""

    object: SignUpObject

    id: str

    status: SignUpStatus

    password_enabled: bool

    custom_action: bool

    abandon_at: int

    required_fields: Optional[List[str]] = None

    optional_fields: Optional[List[str]] = None

    missing_fields: Optional[List[str]] = None

    unverified_fields: Optional[List[str]] = None

    verifications: Optional[Verifications] = None

    username: OptionalNullable[str] = UNSET

    email_address: OptionalNullable[str] = UNSET

    phone_number: OptionalNullable[str] = UNSET

    web3_wallet: OptionalNullable[str] = UNSET

    first_name: OptionalNullable[str] = UNSET

    last_name: OptionalNullable[str] = UNSET

    unsafe_metadata: Optional[Dict[str, Any]] = None

    public_metadata: Optional[Dict[str, Any]] = None

    external_id: OptionalNullable[str] = UNSET

    created_session_id: OptionalNullable[str] = UNSET

    created_user_id: OptionalNullable[str] = UNSET

    legal_accepted_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp at which the user accepted the legal requirements.

    """

    external_account: Optional[ExternalAccount] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "required_fields",
            "optional_fields",
            "missing_fields",
            "unverified_fields",
            "verifications",
            "username",
            "email_address",
            "phone_number",
            "web3_wallet",
            "first_name",
            "last_name",
            "unsafe_metadata",
            "public_metadata",
            "external_id",
            "created_session_id",
            "created_user_id",
            "legal_accepted_at",
            "external_account",
        ]
        nullable_fields = [
            "username",
            "email_address",
            "phone_number",
            "web3_wallet",
            "first_name",
            "last_name",
            "external_id",
            "created_session_id",
            "created_user_id",
            "legal_accepted_at",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
