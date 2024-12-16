# BlocklistIdentifiersSDK
(*blocklist_identifiers*)

## Overview

### Available Operations

* [list](#list) - List all identifiers on the block-list

## list

Get a list of all identifiers which are not allowed to access an instance

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.blocklist_identifiers.list()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BlocklistIdentifiers](../../models/blocklistidentifiers.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 402           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |