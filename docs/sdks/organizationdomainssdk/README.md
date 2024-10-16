# OrganizationDomainsSDK
(*organization_domains*)

## Overview

### Available Operations

* [create_organization_domain](#create_organization_domain) - Create a new organization domain.
* [list_organization_domains](#list_organization_domains) - Get a list of all domains of an organization.
* [delete_organization_domain](#delete_organization_domain) - Remove a domain from an organization.

## create_organization_domain

Creates a new organization domain. By default the domain is verified, but can be optionally set to unverified.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization_domains.create_organization_domain(organization_id="<value>", name="<value>", enrollment_mode="<value>", verified=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The ID of the organization where the new domain will be created.                                                          |
| `name`                                                                                                                    | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | The name of the new domain                                                                                                |
| `enrollment_mode`                                                                                                         | *Optional[str]*                                                                                                           | :heavy_minus_sign:                                                                                                        | The enrollment_mode for the new domain. This can be `automatic_invitation`, `automatic_suggestion` or `manual_invitation` |
| `verified`                                                                                                                | *OptionalNullable[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                        | The status of domain's verification. Defaults to true                                                                     |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.OrganizationDomain](../../models/organizationdomain.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,403,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## list_organization_domains

Get a list of all domains of an organization.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization_domains.list_organization_domains(organization_id="<value>", limit=20, offset=10, verified="<value>", enrollment_mode="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                         | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The organization ID.                                                                                                                      |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `verified`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter domains by their verification status. `true` or `false`                                                                            |                                                                                                                                           |
| `enrollment_mode`                                                                                                                         | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter domains by their enrollment mode                                                                                                   |                                                                                                                                           |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.OrganizationDomains](../../models/organizationdomains.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## delete_organization_domain

Removes the given domain from the organization.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.organization_domains.delete_organization_domain(organization_id="<value>", domain_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization the domain belongs to                    |
| `domain_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the domain                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
