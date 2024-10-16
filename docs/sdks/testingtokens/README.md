# TestingTokens
(*testing_tokens*)

## Overview

Tokens meant for use by end-to-end test suites in requests to the Frontend API, so as to bypass bot detection measures.
<https://clerk.com/docs/testing/overview#testing-tokens>

### Available Operations

* [create_testing_token](#create_testing_token) - Retrieve a new testing token

## create_testing_token

Retrieve a new testing token. Only available for development instances.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.testing_tokens.create_testing_token()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TestingToken](../../models/testingtoken.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
