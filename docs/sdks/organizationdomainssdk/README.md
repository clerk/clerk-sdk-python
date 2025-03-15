# OrganizationDomainsSDK
(*organization_domains*)

## Overview

### Available Operations

* [create](#create) - Create a new organization domain.
* [list](#list) - Get a list of all domains of an organization.
* [update](#update) - Update an organization domain.
* [delete](#delete) - Remove a domain from an organization.

## create

Creates a new organization domain. By default the domain is verified, but can be optionally set to unverified.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.create(organization_id="<id>", name="<value>", enrollment_mode="<value>", verified=True)

    assert res is not None

    # Handle response
    print(res)

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list

Get a list of all domains of an organization.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.list(organization_id="<id>", verified="<value>", enrollment_mode="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                         | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The organization ID.                                                                                                                      |                                                                                                                                           |
| `verified`                                                                                                                                | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter domains by their verification status. `true` or `false`                                                                            |                                                                                                                                           |
| `enrollment_mode`                                                                                                                         | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter domains by their enrollment mode                                                                                                   |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.OrganizationDomains](../../models/organizationdomains.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates the properties of an existing organization domain.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.update(organization_id="<id>", domain_id="<id>", enrollment_mode="<value>", verified=False)

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

## delete

Removes the given domain from the organization.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.delete(organization_id="<id>", domain_id="<id>")

    assert res is not None

    # Handle response
    print(res)

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |