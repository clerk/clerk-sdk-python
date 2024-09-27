import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from typing import Optional, Set, Dict, Any
import time


class TokenVerificationException(Exception):
    """Exception raised for token verification errors."""


class JwtHelper:
    "JWT Helper class."

    class VerifyJwtOptions:
        """JWT Verification Options"""

        DEFAULT_CLOCK_SKEW_MS = 5000

        def __init__(
                self,
                key: Any,
                audience: Optional[str] = None,
                authorized_parties: Optional[Set[str]] = None,
                clock_skew_in_ms: int = DEFAULT_CLOCK_SKEW_MS
        ):
            if key is None:
                raise ValueError("key cannot be None.")
            self.key = key
            self.audience = audience
            self.authorized_parties = authorized_parties if authorized_parties else set()
            self.clock_skew_in_ms = clock_skew_in_ms

    @staticmethod
    def generate_token(
            key,
            subject = None,
            audience = None,
            expiration = None,
            not_before = None,
            issued_at = None,
            azp = None
    ):
        """Generates a JWT token with the given claims."""

        payload = {
            k: v for k, v in {
                'sub': subject,
                'aud': audience,
                'exp': expiration,
                'nbf': not_before,
                'iat': issued_at,
                'azp': azp
            }.items() if v is not None
        }
        return jwt.encode(payload, key, algorithm="HS256")

    @staticmethod
    def verify_jwt(token: str, options: VerifyJwtOptions) -> Dict[str, Any]:
        """Verifies JWT according to the given options. If verification succeeeds, returns the decoded payload."""

        try:
            payload = jwt.decode(
                token,
                options.key,
                algorithms=["HS256"],
                audience=options.audience,
                options={"verify_exp": True, "verify_nbf": True, "verify_iss": False, "verify_aud": False, "verify_iat": True},
                leeway=timedelta(milliseconds=float(options.clock_skew_in_ms))
            )
        except ExpiredSignatureError as e:
            raise TokenVerificationException("JWT expired.") from e
        except InvalidTokenError as e:
            raise TokenVerificationException(f"Invalid token: {str(e)}") from e

        ## Subject is theoretically optional but generally recommended, this check might be removed after review
        subject = payload.get("sub")
        if subject is None:
            raise TokenVerificationException("Subject (sub) missing")

        audience = payload.get("aud")
        if audience and options.audience and audience != options.audience:
            raise TokenVerificationException(f"Audience (aud) \"{options.audience}\" not found. Expected \"{audience}\"")

        azp = payload.get("azp")
        if azp and options.authorized_parties and azp not in options.authorized_parties:
            raise TokenVerificationException(f"Invalid JWT Authorized party claim (azp) \"{azp}\". "
                                             f"Expected one of \"{options.authorized_parties}\".")

        iat = payload.get("iat")
        if iat and datetime.utcfromtimestamp(iat) > datetime.utcnow() + timedelta(milliseconds=float(options.clock_skew_in_ms)):
            raise TokenVerificationException(f"JWT issued-at-date claim (iat) is in the future. Issued at date: {iat}; Current date: {datetime.utcnow()}.")

        return payload


# Example usage
if __name__ == "__main__":
    # Mock data for testing
    key = "your-secret-key"
    options = JwtHelper.VerifyJwtOptions(
            key = key,
            audience = "your-audience",
            authorized_parties = {"your-authorized-party"}
        )

    # JWT token (example, use a real token in actual tests)
    token = JwtHelper.generate_token(
        key = key,
        subject="1234567890",
        audience="your-audience",
        azp="your-authorized-party",
        issued_at=time.time()
    )

    try:
        claims = JwtHelper.verify_jwt(token, options)
        print(f"Token is valid. Claims: {claims}")
    except TokenVerificationException as e:
        print(f"Token verification failed: {e}")
