# OauthAccessTokens

## Overview

### Available Operations

* [verify](#verify) - Verify an OAuth Access Token

## verify

Verify an OAuth Access Token

### Example Usage

<!-- UsageSnippet language="python" operationID="verifyOAuthAccessToken" method="post" path="/oauth_applications/access_tokens/verify" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_access_tokens.verify(access_token="XXXXXXXXXXXXXX")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                            | Type                                                                                                                                                                                                 | Required                                                                                                                                                                                             | Description                                                                                                                                                                                          | Example                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | The access token to verify.                                                                                                                                                                          | XXXXXXXXXXXXXX                                                                                                                                                                                       |
| `secret`                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                   | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>The access token to verify. This is deprecated, use `access_token` instead. | XXXXXXXXXXXXXX                                                                                                                                                                                       |
| `retries`                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                  |                                                                                                                                                                                                      |

### Response

**[models.VerifyOAuthAccessTokenResponseBody](../../models/verifyoauthaccesstokenresponsebody.md)**

### Errors

| Error Type                                                         | Status Code                                                        | Content Type                                                       |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| models.VerifyOAuthAccessTokenOauthAccessTokensResponseBody         | 400                                                                | application/json                                                   |
| models.VerifyOAuthAccessTokenOauthAccessTokensResponseResponseBody | 404                                                                | application/json                                                   |
| models.SDKError                                                    | 4XX, 5XX                                                           | \*/\*                                                              |