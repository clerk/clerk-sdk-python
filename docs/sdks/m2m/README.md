# M2m
(*m2m*)

## Overview

### Available Operations

* [create_token](#create_token) - Create a M2M Token
* [list_tokens](#list_tokens) - Get M2M Tokens
* [revoke_token](#revoke_token) - Revoke a M2M Token
* [verify_token](#verify_token) - Verify a M2M Token

## create_token

Creates a new M2M Token. Must be authenticated via a Machine Secret Key.

### Example Usage

<!-- UsageSnippet language="python" operationID="createM2MToken" method="post" path="/m2m_tokens" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.m2m.create_token(seconds_until_expiration=9240.85, claims="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `seconds_until_expiration`                                          | *OptionalNullable[float]*                                           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `claims`                                                            | *OptionalNullable[Any]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateM2MTokenResponseBody](../../models/createm2mtokenresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.CreateM2MTokenM2mResponseBody         | 400                                          | application/json                             |
| models.CreateM2MTokenM2mResponseResponseBody | 409                                          | application/json                             |
| models.SDKError                              | 4XX, 5XX                                     | \*/\*                                        |

## list_tokens

Fetches M2M tokens for a specific machine.

This endpoint can be authenticated by either a Machine Secret Key or by a Clerk Secret Key.

- When fetching M2M tokens with a Machine Secret Key, only tokens associated with the authenticated machine can be retrieved.
- When fetching M2M tokens with a Clerk Secret Key, tokens for any machine in the instance can be retrieved.

### Example Usage

<!-- UsageSnippet language="python" operationID="getM2MTokens" method="get" path="/m2m_tokens" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.m2m.list_tokens(subject="<value>", revoked=False, expired=False, limit=10, offset=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subject`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revoked`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expired`                                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *OptionalNullable[float]*                                           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetM2MTokensResponseBody](../../models/getm2mtokensresponsebody.md)**

### Errors

| Error Type                                    | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| models.GetM2MTokensM2mResponseBody            | 400                                           | application/json                              |
| models.GetM2MTokensM2mResponseResponseBody    | 403                                           | application/json                              |
| models.GetM2MTokensM2mResponse404ResponseBody | 404                                           | application/json                              |
| models.SDKError                               | 4XX, 5XX                                      | \*/\*                                         |

## revoke_token

Revokes a M2M Token.

This endpoint can be authenticated by either a Machine Secret Key or by a Clerk Secret Key.

- When revoking a M2M Token with a Machine Secret Key, the token must managed by the Machine associated with the Machine Secret Key.
- When revoking a M2M Token with a Clerk Secret Key, any token on the Instance can be revoked.

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeM2MToken" method="post" path="/m2m_tokens/{m2m_token_id}/revoke" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.m2m.revoke_token(m2m_token_id="<id>", revocation_reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `m2m_token_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revocation_reason`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RevokeM2MTokenResponseBody](../../models/revokem2mtokenresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.RevokeM2MTokenM2mResponseBody         | 400                                          | application/json                             |
| models.RevokeM2MTokenM2mResponseResponseBody | 404                                          | application/json                             |
| models.SDKError                              | 4XX, 5XX                                     | \*/\*                                        |

## verify_token

Verifies a M2M Token.

This endpoint can be authenticated by either a Machine Secret Key or by a Clerk Secret Key.

- When verifying a M2M Token with a Machine Secret Key, the token must be granted access to the Machine associated with the Machine Secret Key.
- When verifying a M2M Token with a Clerk Secret Key, any token on the Instance can be verified.

### Example Usage

<!-- UsageSnippet language="python" operationID="verifyM2MToken" method="post" path="/m2m_tokens/verify" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.m2m.verify_token(token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `token`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerifyM2MTokenResponseBody](../../models/verifym2mtokenresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.VerifyM2MTokenM2mResponseBody         | 400                                          | application/json                             |
| models.VerifyM2MTokenM2mResponseResponseBody | 404                                          | application/json                             |
| models.SDKError                              | 4XX, 5XX                                     | \*/\*                                        |