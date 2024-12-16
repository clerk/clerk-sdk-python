# AllowlistBlocklist
(*allowlist_blocklist*)

## Overview

### Available Operations

* [list_allowlist_identifiers](#list_allowlist_identifiers) - List all identifiers on the allow-list
* [create_allowlist_identifier](#create_allowlist_identifier) - Add identifier to the allow-list
* [create_blocklist_identifier](#create_blocklist_identifier) - Add identifier to the block-list
* [delete_blocklist_identifier](#delete_blocklist_identifier) - Delete identifier from block-list

## list_allowlist_identifiers

Get a list of all identifiers allowed to sign up to an instance

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.allowlist_blocklist.list_allowlist_identifiers()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.AllowlistIdentifier]](../../models/.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 402           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_allowlist_identifier

Create an identifier allowed to sign up to an instance

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.allowlist_blocklist.create_allowlist_identifier(identifier="user@example.com", notify=True)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                    | Type                                                                                                                                                                         | Required                                                                                                                                                                     | Description                                                                                                                                                                  | Example                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `identifier`                                                                                                                                                                 | *str*                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                           | The identifier to be added in the allow-list.<br/>This can be an email address, a phone number or a web3 wallet.                                                             | user@example.com                                                                                                                                                             |
| `notify`                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | This flag denotes whether the given identifier will receive an invitation to join the application.<br/>Note that this only works for email address and phone number identifiers. | true                                                                                                                                                                         |
| `retries`                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                             | :heavy_minus_sign:                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                          |                                                                                                                                                                              |

### Response

**[models.AllowlistIdentifier](../../models/allowlistidentifier.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_blocklist_identifier

Create an identifier that is blocked from accessing an instance

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.allowlist_blocklist.create_blocklist_identifier(identifier="example@example.com")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `identifier`                                                                                                 | *str*                                                                                                        | :heavy_check_mark:                                                                                           | The identifier to be added in the block-list.<br/>This can be an email address, a phone number or a web3 wallet. | example@example.com                                                                                          |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |                                                                                                              |

### Response

**[models.BlocklistIdentifier](../../models/blocklistidentifier.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete_blocklist_identifier

Delete an identifier from the instance block-list

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.allowlist_blocklist.delete_blocklist_identifier(identifier_id="identifier123")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the identifier to delete from the block-list              | identifier123                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |