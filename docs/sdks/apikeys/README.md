# APIKeys

## Overview

Endpoints for managing API Keys

### Available Operations

* [create_api_key](#create_api_key) - Create an API Key
* [get_api_keys](#get_api_keys) - Get API Keys
* [get_api_key](#get_api_key) - Get an API Key by ID
* [update_api_key](#update_api_key) - Update an API Key
* [delete_api_key](#delete_api_key) - Delete an API Key
* [get_api_key_secret](#get_api_key_secret) - Get an API Key Secret
* [revoke_api_key](#revoke_api_key) - Revoke an API Key
* [verify_api_key](#verify_api_key) - Verify an API Key

## create_api_key

Create an API Key

### Example Usage

<!-- UsageSnippet language="python" operationID="createApiKey" method="post" path="/api_keys" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.create_api_key(name="<value>", subject="<value>", type_="api_key", description="um solace recklessly", claims="<value>", scopes=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], created_by="<value>", seconds_until_expiration=9695.91)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `subject`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `claims`                                                            | *OptionalNullable[Any]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scopes`                                                            | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `created_by`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `seconds_until_expiration`                                          | *OptionalNullable[float]*                                           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAPIKeyResponseBody](../../models/createapikeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.CreateAPIKeyAPIKeysResponseBody         | 400                                            | application/json                               |
| models.CreateAPIKeyAPIKeysResponseResponseBody | 409                                            | application/json                               |
| models.SDKError                                | 4XX, 5XX                                       | \*/\*                                          |

## get_api_keys

Get API Keys

### Example Usage

<!-- UsageSnippet language="python" operationID="getApiKeys" method="get" path="/api_keys" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.get_api_keys(subject="<value>", type_="api_key", include_invalid=clerk_backend_api.IncludeInvalid.FALSE, limit=10, offset=0, query="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subject`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `type`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_invalid`                                                   | [Optional[models.IncludeInvalid]](../../models/includeinvalid.md)   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *OptionalNullable[float]*                                           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `query`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAPIKeysResponseBody](../../models/getapikeysresponsebody.md)**

### Errors

| Error Type                                   | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| models.GetAPIKeysAPIKeysResponseBody         | 400                                          | application/json                             |
| models.GetAPIKeysAPIKeysResponseResponseBody | 404                                          | application/json                             |
| models.SDKError                              | 4XX, 5XX                                     | \*/\*                                        |

## get_api_key

Get an API Key by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="getApiKey" method="get" path="/api_keys/{apiKeyID}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.get_api_key(api_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAPIKeyResponseBody](../../models/getapikeyresponsebody.md)**

### Errors

| Error Type                                  | Status Code                                 | Content Type                                |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| models.GetAPIKeyAPIKeysResponseBody         | 400                                         | application/json                            |
| models.GetAPIKeyAPIKeysResponseResponseBody | 404                                         | application/json                            |
| models.SDKError                             | 4XX, 5XX                                    | \*/\*                                       |

## update_api_key

Update an API Key

### Example Usage

<!-- UsageSnippet language="python" operationID="updateApiKey" method="patch" path="/api_keys/{apiKeyID}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.update_api_key(api_key_id="<id>", claims="<value>", scopes=[
        "<value 1>",
        "<value 2>",
    ], description=None, subject="<value>", seconds_until_expiration=7782.19)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `claims`                                                            | *OptionalNullable[Any]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scopes`                                                            | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `subject`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `seconds_until_expiration`                                          | *OptionalNullable[float]*                                           | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UpdateAPIKeyResponseBody](../../models/updateapikeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.UpdateAPIKeyAPIKeysResponseBody         | 400                                            | application/json                               |
| models.UpdateAPIKeyAPIKeysResponseResponseBody | 404                                            | application/json                               |
| models.SDKError                                | 4XX, 5XX                                       | \*/\*                                          |

## delete_api_key

Delete an API Key

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteApiKey" method="delete" path="/api_keys/{apiKeyID}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.delete_api_key(api_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteAPIKeyResponseBody](../../models/deleteapikeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.DeleteAPIKeyAPIKeysResponseBody         | 400                                            | application/json                               |
| models.DeleteAPIKeyAPIKeysResponseResponseBody | 404                                            | application/json                               |
| models.SDKError                                | 4XX, 5XX                                       | \*/\*                                          |

## get_api_key_secret

Get an API Key Secret

### Example Usage

<!-- UsageSnippet language="python" operationID="getApiKeySecret" method="get" path="/api_keys/{apiKeyID}/secret" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.get_api_key_secret(api_key_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAPIKeySecretResponseBody](../../models/getapikeysecretresponsebody.md)**

### Errors

| Error Type                                        | Status Code                                       | Content Type                                      |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| models.GetAPIKeySecretAPIKeysResponseBody         | 400                                               | application/json                                  |
| models.GetAPIKeySecretAPIKeysResponseResponseBody | 404                                               | application/json                                  |
| models.SDKError                                   | 4XX, 5XX                                          | \*/\*                                             |

## revoke_api_key

Revoke an API Key

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeApiKey" method="post" path="/api_keys/{apiKeyID}/revoke" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.revoke_api_key(api_key_id="<id>", revocation_reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `api_key_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revocation_reason`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RevokeAPIKeyResponseBody](../../models/revokeapikeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.RevokeAPIKeyAPIKeysResponseBody         | 400                                            | application/json                               |
| models.RevokeAPIKeyAPIKeysResponseResponseBody | 404                                            | application/json                               |
| models.SDKError                                | 4XX, 5XX                                       | \*/\*                                          |

## verify_api_key

Verify an API Key

### Example Usage

<!-- UsageSnippet language="python" operationID="verifyApiKey" method="post" path="/api_keys/verify" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.api_keys.verify_api_key(secret="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `secret`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerifyAPIKeyResponseBody](../../models/verifyapikeyresponsebody.md)**

### Errors

| Error Type                                     | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| models.VerifyAPIKeyAPIKeysResponseBody         | 400                                            | application/json                               |
| models.VerifyAPIKeyAPIKeysResponseResponseBody | 404                                            | application/json                               |
| models.SDKError                                | 4XX, 5XX                                       | \*/\*                                          |