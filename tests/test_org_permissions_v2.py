"""Tests for decoding v2 session token org permissions (`fea` / `o.per` / `o.fpm`).

A permission key is `org:<feature>:<action>`. The token factors these into an
ordered feature list, a shared action vocabulary, and one bitmask per feature
over that vocabulary. Bit j of mask i means feature i grants action j, with
bit 0 least significant.
"""

import pytest

from clerk_backend_api.security.authenticaterequest import _compute_org_permissions


def claims(fea: str, per: str, fpm: str):
    return {"fea": fea, "o": {"per": per, "fpm": fpm}}


def test_decodes_a_normal_mask():
    assert _compute_org_permissions(
        claims("o:leads,o:whatsapp", "read,manage", "3,1")
    ) == ["org:leads:read", "org:leads:manage", "org:whatsapp:read"]


def test_decodes_bit_62():
    perms = ",".join(f"p{i:02d}" for i in range(80))
    assert _compute_org_permissions(
        claims("o:repositories", perms, str((1 << 62) | 1))
    ) == ["org:repositories:p00", "org:repositories:p62"]


def test_decodes_a_positive_bignum_at_bit_63():
    """Python ints are arbitrary-precision, so a wide positive mask is exact."""
    perms = ",".join(f"p{i:02d}" for i in range(80))
    assert _compute_org_permissions(
        claims("o:repositories", perms, str((1 << 63) | 1))
    ) == ["org:repositories:p00", "org:repositories:p63"]


def test_decodes_beyond_64_bits():
    perms = ",".join(f"p{i:02d}" for i in range(80))
    assert _compute_org_permissions(
        claims("o:repositories", perms, str((1 << 72) | 1))
    ) == ["org:repositories:p00", "org:repositories:p72"]


@pytest.mark.parametrize(
    "mask",
    [
        "-9223372036854775807",
        "-9223372036854775808",
        "-1",
    ],
)
def test_negative_masks_grant_nothing(mask):
    """A negative mask can only come from an issuer that overflowed a signed
    integer. bin() renders it as "-0b111...", so slicing off two characters
    leaves a stray "b" and the magnitude's bits, which previously granted
    permissions that were never assigned -- 63 of them for the first case."""
    perms = ",".join(f"p{i:02d}" for i in range(80))
    assert _compute_org_permissions(claims("o:repositories", perms, mask)) == []


@pytest.mark.parametrize("mask", ["0x1f", "1.5", "", " 3", "3 ", "abc", "+3", "１"])
def test_non_decimal_masks_grant_nothing(mask):
    assert _compute_org_permissions(claims("o:repositories", "read,manage", mask)) == []


def test_zero_mask_grants_nothing():
    assert _compute_org_permissions(claims("o:repositories", "read,manage", "0")) == []


def test_mask_wider_than_the_vocabulary_is_bounded():
    """Extra high bits must not emit permissions with no action name."""
    assert _compute_org_permissions(
        claims("o:repositories", "read,manage", str((1 << 40) | 1))
    ) == ["org:repositories:read"]


def test_user_scoped_features_are_skipped():
    assert _compute_org_permissions(
        claims("u:impersonation,o:leads", "read,manage", "1,1")
    ) == ["org:leads:read"]


def test_more_masks_than_features_are_ignored():
    assert _compute_org_permissions(claims("o:leads", "read,manage", "1,3")) == [
        "org:leads:read"
    ]
