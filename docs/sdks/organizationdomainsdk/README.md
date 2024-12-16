# OrganizationDomainSDK
(*organization_domain*)

## Overview

### Available Operations

* [update](#update) - Update an organization domain.

## update

Updates the properties of an existing organization domain.

### Example Usage

```python
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domain.update(organization_id="<id>", domain_id="<id>", enrollment_mode="<value>", verified=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The ID of the organization the domain belongs to                                                                          |
| `domain_id`                                                                                                               | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The ID of the domain                                                                                                      |
| `enrollment_mode`                                                                                                         | *OptionalNullable[str]*                                                                                                   | :heavy_minus_sign:                                                                                                        | The enrollment_mode for the new domain. This can be `automatic_invitation`, `automatic_suggestion` or `manual_invitation` |
| `verified`                                                                                                                | *OptionalNullable[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                        | The status of the domain's verification                                                                                   |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.OrganizationDomain](../../models/organizationdomain.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |