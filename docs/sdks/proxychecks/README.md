# ProxyChecks
(*proxy_checks*)

### Available Operations

* [verify](#verify) - Verify the proxy configuration for your domain

## verify

This endpoint can be used to validate that a proxy-enabled domain is operational.
It tries to verify that the proxy URL provided in the parameters maps to a functional proxy that can reach the Clerk Frontend API.

You can use this endpoint before you set a proxy URL for a domain. This way you can ensure that switching to proxy-based
configuration will not lead to downtime for your instance.

The `proxy_url` parameter allows for testing proxy configurations for domains that don't have a proxy URL yet, or operate on
a different proxy URL than the one provided. It can also be used to re-validate a domain that is already configured to work with a proxy.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.proxy_checks.verify(domain_id="domain_32hfu3e", proxy_url="https://example.com/__clerk")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       | Example                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `domain_id`                                                                                                                       | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | The ID of the domain that will be updated.                                                                                        | domain_32hfu3e                                                                                                                    |
| `proxy_url`                                                                                                                       | *Optional[str]*                                                                                                                   | :heavy_minus_sign:                                                                                                                | The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk | https://example.com/__clerk                                                                                                       |
| `retries`                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                  | :heavy_minus_sign:                                                                                                                | Configuration to override the default retry behavior of the client.                                                               |                                                                                                                                   |


### Response

**[models.ProxyCheck](../../models/proxycheck.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
