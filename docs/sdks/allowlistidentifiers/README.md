# AllowlistIdentifiers
(*allowlist_identifiers*)

## Overview

### Available Operations

* [list](#list) - List all identifiers on the allow-list
* [create](#create) - Add identifier to the allow-list
* [delete](#delete) - Delete identifier from allow-list

## list

Get a list of all identifiers allowed to sign up to an instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.allowlist_identifiers.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AllowlistIdentifier]](../../models/.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError36 | 401,402                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## create

Create an identifier allowed to sign up to an instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.allowlist_identifiers.create(request={
    "identifier": "user@example.com",
    "notify": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.CreateAllowlistIdentifierRequestBody](../../models/createallowlistidentifierrequestbody.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.AllowlistIdentifier](../../models/allowlistidentifier.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError37 | 400,402,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## delete

Delete an identifier from the instance allow-list

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.allowlist_identifiers.delete(identifier_id="example_identifier_id")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the identifier to delete from the allow-list              | example_identifier_id                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError38 | 402,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |
