# Misc
(*misc*)

## Overview

### Available Operations

* [get_public_interstitial](#get_public_interstitial) - Returns the markup for the interstitial page

## get_public_interstitial

The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's authentication state.
It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk()

s.misc.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `frontend_api`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The Frontend API key of your instance                               | frontend-api_1a2b3c4d                                               |
| `publishable_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The publishable key of your instance                                | pub_1a2b3c4d                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
