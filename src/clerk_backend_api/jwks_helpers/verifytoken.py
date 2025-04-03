import httpx
import jwt
import re
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from jwt.algorithms import RSAAlgorithm
from dataclasses import dataclass
from datetime import timedelta
from enum import Enum
from typing import Any, Dict, List, Union, Optional, cast

from .cache import Cache

__jwkcache = Cache()


class TokenVerificationErrorReason(Enum):

    JWK_FAILED_TO_LOAD = (
        'jwk-failed-to-load',
        'Failed to load JWKS from Clerk Backend API. Contact support@clerk.com.'
    )

    JWK_REMOTE_INVALID = (
        'jwk-remote-invalid',
        'The JWKS endpoint did not contain any signing keys. Contact support@clerk.com.'
    )

    JWK_FAILED_TO_RESOLVE = (
        'jwk-failed-to-resolve',
        'Failed to resolve JWK. Public Key is not in the proper format.'
    )

    JWK_KID_MISMATCH = (
        'jwk-kid-mismatch',
        'Unable to find a signing key in JWKS that matches the kid of the provided session token.'
    )

    TOKEN_EXPIRED = (
        'token-expired',
        'Token has expired and is no longer valid.'
    )

    TOKEN_INVALID = (
        'token-invalid',
        'Token is invalid and could not be verified.'
    )

    TOKEN_INVALID_AUTHORIZED_PARTIES = (
        'token-invalid-authorized-parties',
        'Authorized party claim (azp) does not match any of the authorized parties.',
    )

    TOKEN_INVALID_AUDIENCE = (
        'token-invalid-audience',
        'Token audience claim (aud) does not match one of the expected audience values.',
    )

    TOKEN_IAT_IN_THE_FUTURE = (
        'token-iat-in-the-future',
        'Token Issued At claim (iat) represents a time in the future.'
        )

    TOKEN_NOT_ACTIVE_YET = (
        'token-not-active-yet',
        'Token is not yet valid. Not Before claim (nbf) is in the future.'
    )

    TOKEN_INVALID_SIGNATURE = (
        'token-invalid-signature',
        'Token signature is invalid and could not be verified.'
    )

    SECRET_KEY_MISSING = (
        'secret-key-missing',
        'Missing Clerk Secret Key. Go to https://dashboard.clerk.com and get your key for your instance.'
    )


class TokenVerificationError(Exception):
    """Exception raised when token verification fails"""

    def __init__(self, reason: TokenVerificationErrorReason):
        self.reason = reason
        super().__init__(self.reason.value[1])


@dataclass
class VerifyTokenOptions:
    """
    Options to configure verify_token.

    Attributes:
        audience (Union[str, List[str], None]): An audience or list of audiences to verify against.
        authorized_parties (Optional[List[str]]): An allowlist of origins to verify against.
        clock_skew_in_ms (int): Allowed time difference (in milliseconds) between the Clerk server (which generates the token)
                                and the clock of the user's application server when validating a token. Defaults to 5000 ms.
        jwt_key (Optional[str]): PEM Public Key used to verify the session token in a networkless manner.
        secret_key (Optional[str]): The Clerk secret key from the API Keys page in the Clerk Dashboard.
        api_url (str): The Clerk Backend API endpoint. Defaults to 'https://api.clerk.com'
        api_version (str): The version passed to the Clerk API. Defaults to 'v1'.
    """

    audience: Optional[Union[str, List[str]]] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000
    jwt_key: Optional[str] = None
    secret_key: Optional[str] = None
    api_url: str = 'https://api.clerk.com'
    api_version: str = 'v1'


def fetch_jwks(options: VerifyTokenOptions) -> Dict[str, Any]:
    """ Fetch JWKS from Clerk's Backend API."""

    jwks_url = f'{options.api_url}/{options.api_version}/jwks'
    transport = httpx.HTTPTransport(retries=10) # handles ConnectError and ConnectTimeout
    with httpx.Client(transport=transport) as client:
        http_res = None

        for _ in range(10):
            try:
                http_res = client.get(jwks_url, headers={
                    'Accept': 'application/json', 'Authorization': f'Bearer {options.secret_key}'
                })
            except httpx.TimeoutException:
                continue
            break

        if http_res is None or http_res.status_code != 200:
            raise TokenVerificationError(TokenVerificationErrorReason.JWK_FAILED_TO_LOAD)

        try:
            return http_res.json()
        except Exception as e:
            raise TokenVerificationError(TokenVerificationErrorReason.JWK_FAILED_TO_LOAD) from e


def get_remote_jwt_key(token: str, options: VerifyTokenOptions) -> str:
    """ Retrieve JWT Public Key from Clerk's Backend API

    Args:
        token (str): The token from which to extract the public key.
    """

    try:
        kid = jwt.get_unverified_header(token).get('kid')
    except jwt.InvalidTokenError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_INVALID) from e

    decoded_pem = __jwkcache.get(kid)
    if decoded_pem is not None:
        return decoded_pem

    jwks = fetch_jwks(options).get('keys')
    if jwks is None:
        raise TokenVerificationError(TokenVerificationErrorReason.JWK_REMOTE_INVALID)

    for key in jwks:
        if key.get('kid') == kid:
            public_key = RSAAlgorithm.from_jwk(key)
            if isinstance(public_key, RSAPublicKey):
                public_key = cast(RSAPublicKey, public_key)
                pem = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
                decoded_pem = pem.decode('utf-8')
                __jwkcache.set(kid, decoded_pem)
                return decoded_pem

    raise TokenVerificationError(TokenVerificationErrorReason.JWK_KID_MISMATCH)


def verify_token(token: str, options: VerifyTokenOptions) -> Dict[str, Any]:
    """ Verifies a Clerk-generated token signature. Networkless if the options.jwt_key is provided.
    Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API.

    Args:
        token (str): The token to verify.
        options (VerifyTokenOptions): Options to configure the verification.
    """


    if options.jwt_key is not None:
        jwt_key = re.sub(r'(\r\n|\n|\r)', '', options.jwt_key)

    elif options.secret_key is not None:
        jwt_key = get_remote_jwt_key(token, options)

    else:
        raise TokenVerificationError(TokenVerificationErrorReason.SECRET_KEY_MISSING)

    try:
        payload = jwt.decode(
            token,
            jwt_key,
            algorithms=['RS256'],
            audience=options.audience,
            options={'verify_iss': False},
            leeway=timedelta(milliseconds=float(options.clock_skew_in_ms))
        )

        if options.authorized_parties is not None:
            azp = payload.get("azp")
            if azp is None or azp not in options.authorized_parties:
                raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_INVALID_AUTHORIZED_PARTIES)

        return payload

    except jwt.InvalidKeyError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.JWK_FAILED_TO_RESOLVE) from e
    except jwt.ExpiredSignatureError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_EXPIRED) from e
    except jwt.InvalidAudienceError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_INVALID_AUDIENCE) from e
    except jwt.InvalidSignatureError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_INVALID_SIGNATURE) from e
    except jwt.InvalidIssuedAtError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_IAT_IN_THE_FUTURE) from e
    except jwt.ImmatureSignatureError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_NOT_ACTIVE_YET) from e
    except jwt.InvalidTokenError as e:
        raise TokenVerificationError(TokenVerificationErrorReason.TOKEN_INVALID) from e
