# Jwks
(*jwks*)

## Overview

### Available Operations

* [get](#get) - Retrieve the JSON Web Key Set of the instance

## get

Retrieve the JSON Web Key Set of the instance

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.jwks.get()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WellKnownJWKS](../../models/wellknownjwks.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |