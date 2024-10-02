import jwt
import httpx
from cryptography.hazmat.primitives import serialization
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any, Dict, List, Union, Optional
from ..models import SDKError


class InvalidTokenException(Exception):
    """Exception raised when a token is not or no longer valid"""

class InvalidKeyException(Exception):
    """Exception raised when the provided public key is invalid."""

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
        api_url (str): The Clerk Backend API endpoint. Defaults to 'http://api.clerk.com'
        api_version (str): The version passed to the Clerk API. Defaults to 'v1'.
    """

    audience: Union[str, List[str], None] = None
    authorized_parties: Optional[List[str]] = None
    clock_skew_in_ms: int = 5000
    jwt_key: Optional[str] = None
    secret_key: Optional[str] = None
    api_url: str = 'http://api.clerk.com'
    api_version: str = 'v1'


def get_jwt_key(token: str, jwks_url: str, secret_key: str) -> str:
    """ Retrieve the JWT Public Key associated with a JWT token by fetching the JWKS from Clerk's Backend API

    Args:
        token (str): The token from which to extract the public key.
    """

    with httpx.Client() as client:
        http_res = client.get(jwks_url, headers={
            'Accept': 'application/json', 'Authorization': f'Bearer {secret_key}'
        })

        if http_res.status_code != 200:
            raise SDKError(f'Could not fetch JWKS from {jwks_url}', http_res.status_code, http_res.text, http_res)

        jwks = http_res.json()
        try:
            kid = jwt.get_unverified_header(token).get('kid')
        except Exception as e:
            raise InvalidTokenException('Could not parse kid from token.') from e

        for key in jwks['keys']:
            if key['kid'] == kid:
                public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                pem = public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
                return pem.decode('utf-8')

        raise InvalidTokenException('Public key not found in JWKS.')


def verify_token(token: str, options: VerifyTokenOptions) -> Dict[str, Any]:
    """ Verifies a Clerk-generated token signature. Networkless if the opttions.jwt_key is provided.
    Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API.

    Args:
        token (str): The token to verify.
        options (VerifyTokenOptions): Options to configure the verification.
        clerk (Optional[Clerk]): The Clerk SDK instance to use for fetching the JWKS. Defaults to None.
    """

    jwt_key = options.jwt_key

    if jwt_key is None:
        if options.secret_key is None:
            raise ValueError('Either jwt_key or secret_key must be provided.')

        jwks_url =  f'{options.api_url}/{options.api_version}/.well-known/jwks.json'
        jwt_key = get_jwt_key(token, jwks_url, options.secret_key)

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
                raise InvalidTokenException(f'Invalid Authorized Party claim (azp) "{azp}". '
                                           f'Expected one of "{options.authorized_parties}".')
        iat = payload.get("iat")
        utcnow = datetime.utcnow()

        if iat is None or datetime.utcfromtimestamp(iat) > utcnow + timedelta(milliseconds=float(options.clock_skew_in_ms)):
            raise InvalidTokenException(f'Invalid Issued At claim (iat). Issued at date: {iat}; Current date: {utcnow}.')

        return payload

    except jwt.InvalidKeyError as e:
        raise InvalidKeyException('Invalid Public Key') from e
    except jwt.ExpiredSignatureError as e:
        raise InvalidTokenException('Token is expired.') from e
    except jwt.InvalidTokenError as e:
        raise InvalidTokenException('Invalid token.') from e
