# Miscellaneous
(*miscellaneous*)

## Overview

### Available Operations

* [get_public_interstitial](#get_public_interstitial) - Returns the markup for the interstitial page

## get_public_interstitial

The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's authentication state.
It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk() as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                                                                  | Type                                                                                                                                                       | Required                                                                                                                                                   | Description                                                                                                                                                | Example                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `frontend_api_query_parameter`                                                                                                                             | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Please use `frontend_api` instead | frontend-api_1a2b3c4d                                                                                                                                      |
| `frontend_api_query_parameter1`                                                                                                                            | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The Frontend API key of your instance                                                                                                                      | pub_1a2b3c4d                                                                                                                                               |
| `publishable_key`                                                                                                                                          | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The publishable key of your instance                                                                                                                       |                                                                                                                                                            |
| `proxy_url`                                                                                                                                                | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The proxy URL of your instance                                                                                                                             |                                                                                                                                                            |
| `domain`                                                                                                                                                   | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The domain of your instance                                                                                                                                |                                                                                                                                                            |
| `sign_in_url`                                                                                                                                              | *Optional[str]*                                                                                                                                            | :heavy_minus_sign:                                                                                                                                         | The sign in URL of your instance                                                                                                                           |                                                                                                                                                            |
| `use_domain_for_script`                                                                                                                                    | *Optional[bool]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                         | Whether to use the domain for the script URL                                                                                                               |                                                                                                                                                            |
| `retries`                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                           | :heavy_minus_sign:                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                        |                                                                                                                                                            |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |