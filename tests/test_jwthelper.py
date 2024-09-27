import jwt
import pytest
from datetime import datetime, timedelta
from helpers.jwthelper import JwtHelper, TokenVerificationException

def test_verifies_ok():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        audience="aud1",
        expiration=datetime.utcnow() + timedelta(minutes=1),
        not_before=datetime.utcnow() - timedelta(minutes=1),
        issued_at=datetime.utcnow() - timedelta(minutes=1)
    )
    options = JwtHelper.VerifyJwtOptions(key = key)
    JwtHelper.verify_jwt(token, options)

def test_fails_no_subject():
    key = "secret"
    token = jwt.encode({}, key, algorithm="HS256")
    options = JwtHelper.VerifyJwtOptions(key=key)

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert excinfo.value.args[0].startswith("Subject (sub) missing")
    assert excinfo.value.__cause__ is None

def test_fails_null_key():
    with pytest.raises(ValueError):
        JwtHelper.VerifyJwtOptions(None)

def test_fails_verify_expired():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        expiration=datetime.utcnow() - timedelta(minutes=1)
    )
    options = JwtHelper.VerifyJwtOptions(key=key, clock_skew_in_ms=0)

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert excinfo.value.args[0].startswith("JWT expired")

def test_verify_does_not_expire_with_large_clock_skew():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        expiration=datetime.utcnow() - timedelta(minutes=1)
    )
    options = JwtHelper.VerifyJwtOptions(key=key, clock_skew_in_ms=180000)
    JwtHelper.verify_jwt(token, options)  # Should not raise an value

def test_fails_verify_not_before():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        not_before=datetime.utcnow() + timedelta(minutes=1),
        issued_at=datetime.utcnow() - timedelta(minutes=1)
    )
    options = JwtHelper.VerifyJwtOptions(key=key)

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert excinfo.value.args[0], "Invalid token: The token is not yet valid (nbf)"
    assert isinstance(excinfo.value.__cause__, jwt.exceptions.ImmatureSignatureError)

def test_fails_issued_at():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        issued_at=datetime.utcnow() + timedelta(minutes=1)
    )
    options = JwtHelper.VerifyJwtOptions(key=key)

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert (
        excinfo.value.args[0].startswith("JWT issued-at-date claim (iat) is in the future")
        or excinfo.value.args[0].startswith("Invalid token: The token is not yet valid (iat)")
    )

def test_fails_audience():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        audience=["aud1", "aud2"]
    )
    options = JwtHelper.VerifyJwtOptions(key=key, audience="aud3")

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert excinfo.value.args[0].startswith("Audience (aud) \"aud3\" not found")

def test_verifies_empty_authorized_parties():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        audience=["aud1", "aud2"],
        azp="partyparty"
    )
    options = JwtHelper.VerifyJwtOptions(key=key)
    JwtHelper.verify_jwt(token, options)

def test_verifies_non_empty_authorized_parties():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        audience=["aud1", "aud2"],
        azp="partyparty"
    )
    options = JwtHelper.VerifyJwtOptions(key=key, authorized_parties = {"boo", "partyparty"})
    JwtHelper.verify_jwt(token, options)  # Should not raise an value

def test_fails_authorized_parties():
    key = "secret"
    token = JwtHelper.generate_token(
        key=key,
        subject="Joe",
        audience=["aud1", "aud2"],
        azp="partyparty"
    )
    options = JwtHelper.VerifyJwtOptions(key=key, authorized_parties = {"bill"})

    with pytest.raises(TokenVerificationException) as excinfo:
        JwtHelper.verify_jwt(token, options)

    assert excinfo.value.args[0].startswith("Invalid JWT Authorized party claim (azp)")
