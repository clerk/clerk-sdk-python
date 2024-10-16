# Jwks
(*jwks*)

## Overview

Retrieve the JSON Web Key Set which can be used to verify the token signatures of the instance.

### Available Operations

* [get_jwks](#get_jwks) - Retrieve the JSON Web Key Set of the instance

## get_jwks

Retrieve the JSON Web Key Set of the instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.jwks.get_jwks()

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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
