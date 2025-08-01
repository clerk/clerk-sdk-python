"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateUserRequestBodyTypedDict(TypedDict):
    external_id: NotRequired[Nullable[str]]
    r"""The ID of the user as used in your external systems or your previous authentication solution.
    Must be unique across your instance.
    """
    first_name: NotRequired[Nullable[str]]
    r"""The first name to assign to the user"""
    last_name: NotRequired[Nullable[str]]
    r"""The last name to assign to the user"""
    primary_email_address_id: NotRequired[Nullable[str]]
    r"""The ID of the email address to set as primary.
    It must be verified, and present on the current user.
    """
    notify_primary_email_address_changed: NotRequired[Nullable[bool]]
    r"""If set to `true`, the user will be notified that their primary email address has changed.
    By default, no notification is sent.
    """
    primary_phone_number_id: NotRequired[Nullable[str]]
    r"""The ID of the phone number to set as primary.
    It must be verified, and present on the current user.
    """
    primary_web3_wallet_id: NotRequired[Nullable[str]]
    r"""The ID of the web3 wallets to set as primary.
    It must be verified, and present on the current user.
    """
    username: NotRequired[Nullable[str]]
    r"""The username to give to the user.
    It must be unique across your instance.
    """
    profile_image_id: NotRequired[Nullable[str]]
    r"""The ID of the image to set as the user's profile image"""
    password: NotRequired[Nullable[str]]
    r"""The plaintext password to give the user.
    Must be at least 8 characters long, and cannot be in any list of hacked passwords.
    """
    password_digest: NotRequired[str]
    r"""In case you already have the password digests and not the passwords, you can use them for the newly created user via this property.
    The digests should be generated with one of the supported algorithms.
    The hashing algorithm can be specified using the `password_hasher` property.
    """
    password_hasher: NotRequired[str]
    r"""The hashing algorithm that was used to generate the password digest.

    The algorithms we support at the moment are [`bcrypt`](https://en.wikipedia.org/wiki/Bcrypt), [`bcrypt_sha256_django`](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [`md5`](https://en.wikipedia.org/wiki/MD5), `pbkdf2_sha1`, `pbkdf2_sha256`, [`pbkdf2_sha256_django`](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [`phpass`](https://www.openwall.com/phpass/), `md5_phpass`, [`scrypt_firebase`](https://firebaseopensource.com/projects/firebase/scrypt/),
    [`scrypt_werkzeug`](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash), [`sha256`](https://en.wikipedia.org/wiki/SHA-2),
    [`ldap_ssha`](https://www.openldap.org/faq/data/cache/347.html) and the [`argon2`](https://argon2.online/) variants: `argon2i` and `argon2id`.

    Each of the supported hashers expects the incoming digest to be in a particular format. See the [Clerk docs](https://clerk.com/docs/references/backend/user/create-user) for more information.
    """
    skip_password_checks: NotRequired[Nullable[bool]]
    r"""Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`."""
    sign_out_of_other_sessions: NotRequired[Nullable[bool]]
    r"""Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`."""
    totp_secret: NotRequired[Nullable[str]]
    r"""In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it.
    Please note that currently the supported options are:
    * Period: 30 seconds
    * Code length: 6 digits
    * Algorithm: SHA1
    """
    backup_codes: NotRequired[List[str]]
    r"""If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them.
    You must provide the backup codes in plain format or the corresponding bcrypt digest.
    """
    public_metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""
    private_metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Metadata saved on the user, that is only visible to your Backend API"""
    unsafe_metadata: NotRequired[Nullable[Dict[str, Any]]]
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """
    delete_self_enabled: NotRequired[Nullable[bool]]
    r"""If true, the user can delete themselves with the Frontend API."""
    create_organization_enabled: NotRequired[Nullable[bool]]
    r"""If true, the user can create organizations with the Frontend API."""
    legal_accepted_at: NotRequired[Nullable[str]]
    r"""A custom timestamps denoting _when_ the user accepted legal requirements, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""
    skip_legal_checks: NotRequired[Nullable[bool]]
    r"""When set to `true` all legal checks are skipped.
    It is not recommended to skip legal checks unless you are migrating a user to Clerk.
    """
    create_organizations_limit: NotRequired[Nullable[int]]
    r"""The maximum number of organizations the user can create. 0 means unlimited."""
    created_at: NotRequired[Nullable[str]]
    r"""A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""


class UpdateUserRequestBody(BaseModel):
    external_id: OptionalNullable[str] = UNSET
    r"""The ID of the user as used in your external systems or your previous authentication solution.
    Must be unique across your instance.
    """

    first_name: OptionalNullable[str] = UNSET
    r"""The first name to assign to the user"""

    last_name: OptionalNullable[str] = UNSET
    r"""The last name to assign to the user"""

    primary_email_address_id: OptionalNullable[str] = UNSET
    r"""The ID of the email address to set as primary.
    It must be verified, and present on the current user.
    """

    notify_primary_email_address_changed: OptionalNullable[bool] = False
    r"""If set to `true`, the user will be notified that their primary email address has changed.
    By default, no notification is sent.
    """

    primary_phone_number_id: OptionalNullable[str] = UNSET
    r"""The ID of the phone number to set as primary.
    It must be verified, and present on the current user.
    """

    primary_web3_wallet_id: OptionalNullable[str] = UNSET
    r"""The ID of the web3 wallets to set as primary.
    It must be verified, and present on the current user.
    """

    username: OptionalNullable[str] = UNSET
    r"""The username to give to the user.
    It must be unique across your instance.
    """

    profile_image_id: OptionalNullable[str] = UNSET
    r"""The ID of the image to set as the user's profile image"""

    password: OptionalNullable[str] = UNSET
    r"""The plaintext password to give the user.
    Must be at least 8 characters long, and cannot be in any list of hacked passwords.
    """

    password_digest: Optional[str] = None
    r"""In case you already have the password digests and not the passwords, you can use them for the newly created user via this property.
    The digests should be generated with one of the supported algorithms.
    The hashing algorithm can be specified using the `password_hasher` property.
    """

    password_hasher: Optional[str] = None
    r"""The hashing algorithm that was used to generate the password digest.

    The algorithms we support at the moment are [`bcrypt`](https://en.wikipedia.org/wiki/Bcrypt), [`bcrypt_sha256_django`](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/), [`md5`](https://en.wikipedia.org/wiki/MD5), `pbkdf2_sha1`, `pbkdf2_sha256`, [`pbkdf2_sha256_django`](https://docs.djangoproject.com/en/4.0/topics/auth/passwords/),
    [`phpass`](https://www.openwall.com/phpass/), `md5_phpass`, [`scrypt_firebase`](https://firebaseopensource.com/projects/firebase/scrypt/),
    [`scrypt_werkzeug`](https://werkzeug.palletsprojects.com/en/3.0.x/utils/#werkzeug.security.generate_password_hash), [`sha256`](https://en.wikipedia.org/wiki/SHA-2),
    [`ldap_ssha`](https://www.openldap.org/faq/data/cache/347.html) and the [`argon2`](https://argon2.online/) variants: `argon2i` and `argon2id`.

    Each of the supported hashers expects the incoming digest to be in a particular format. See the [Clerk docs](https://clerk.com/docs/references/backend/user/create-user) for more information.
    """

    skip_password_checks: OptionalNullable[bool] = UNSET
    r"""Set it to `true` if you're updating the user's password and want to skip any password policy settings check. This parameter can only be used when providing a `password`."""

    sign_out_of_other_sessions: OptionalNullable[bool] = UNSET
    r"""Set to `true` to sign out the user from all their active sessions once their password is updated. This parameter can only be used when providing a `password`."""

    totp_secret: OptionalNullable[str] = UNSET
    r"""In case TOTP is configured on the instance, you can provide the secret to enable it on the specific user without the need to reset it.
    Please note that currently the supported options are:
    * Period: 30 seconds
    * Code length: 6 digits
    * Algorithm: SHA1
    """

    backup_codes: Optional[List[str]] = None
    r"""If Backup Codes are configured on the instance, you can provide them to enable it on the specific user without the need to reset them.
    You must provide the backup codes in plain format or the corresponding bcrypt digest.
    """

    public_metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Metadata saved on the user, that is visible to both your Frontend and Backend APIs"""

    private_metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Metadata saved on the user, that is only visible to your Backend API"""

    unsafe_metadata: OptionalNullable[Dict[str, Any]] = UNSET
    r"""Metadata saved on the user, that can be updated from both the Frontend and Backend APIs.
    Note: Since this data can be modified from the frontend, it is not guaranteed to be safe.
    """

    delete_self_enabled: OptionalNullable[bool] = UNSET
    r"""If true, the user can delete themselves with the Frontend API."""

    create_organization_enabled: OptionalNullable[bool] = UNSET
    r"""If true, the user can create organizations with the Frontend API."""

    legal_accepted_at: OptionalNullable[str] = UNSET
    r"""A custom timestamps denoting _when_ the user accepted legal requirements, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""

    skip_legal_checks: OptionalNullable[bool] = UNSET
    r"""When set to `true` all legal checks are skipped.
    It is not recommended to skip legal checks unless you are migrating a user to Clerk.
    """

    create_organizations_limit: OptionalNullable[int] = UNSET
    r"""The maximum number of organizations the user can create. 0 means unlimited."""

    created_at: OptionalNullable[str] = UNSET
    r"""A custom date/time denoting _when_ the user signed up to the application, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "external_id",
            "first_name",
            "last_name",
            "primary_email_address_id",
            "notify_primary_email_address_changed",
            "primary_phone_number_id",
            "primary_web3_wallet_id",
            "username",
            "profile_image_id",
            "password",
            "password_digest",
            "password_hasher",
            "skip_password_checks",
            "sign_out_of_other_sessions",
            "totp_secret",
            "backup_codes",
            "public_metadata",
            "private_metadata",
            "unsafe_metadata",
            "delete_self_enabled",
            "create_organization_enabled",
            "legal_accepted_at",
            "skip_legal_checks",
            "create_organizations_limit",
            "created_at",
        ]
        nullable_fields = [
            "external_id",
            "first_name",
            "last_name",
            "primary_email_address_id",
            "notify_primary_email_address_changed",
            "primary_phone_number_id",
            "primary_web3_wallet_id",
            "username",
            "profile_image_id",
            "password",
            "skip_password_checks",
            "sign_out_of_other_sessions",
            "totp_secret",
            "public_metadata",
            "private_metadata",
            "unsafe_metadata",
            "delete_self_enabled",
            "create_organization_enabled",
            "legal_accepted_at",
            "skip_legal_checks",
            "create_organizations_limit",
            "created_at",
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


class UpdateUserRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user to update"""
    request_body: UpdateUserRequestBodyTypedDict


class UpdateUserRequest(BaseModel):
    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user to update"""

    request_body: Annotated[
        UpdateUserRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
