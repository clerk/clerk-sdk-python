# ProxyChecks
(*proxy_checks*)

## Overview

### Available Operations

* [verify_domain_proxy](#verify_domain_proxy) - Verify the proxy configuration for your domain

## verify_domain_proxy

This endpoint can be used to validate that a proxy-enabled domain is operational.
It tries to verify that the proxy URL provided in the parameters maps to a functional proxy that can reach the Clerk Frontend API.

You can use this endpoint before you set a proxy URL for a domain. This way you can ensure that switching to proxy-based
configuration will not lead to downtime for your instance.

The `proxy_url` parameter allows for testing proxy configurations for domains that don't have a proxy URL yet, or operate on
a different proxy URL than the one provided. It can also be used to re-validate a domain that is already configured to work with a proxy.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.proxy_checks.verify_domain_proxy(request={
    "domain_id": "domain_32hfu3e",
    "proxy_url": "https://example.com/__clerk",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.VerifyDomainProxyRequestBody](../../models/verifydomainproxyrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.ProxyCheck](../../models/proxycheck.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
