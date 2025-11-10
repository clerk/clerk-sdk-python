# OrganizationDomainsSDK
(*organization_domains*)

## Overview

### Available Operations

* [create](#create) - Create a new organization domain.
* [list](#list) - Get a list of all domains of an organization.
* [update](#update) - Update an organization domain.
* [delete](#delete) - Remove a domain from an organization.
* [list_all](#list_all) - List all organization domains

## create

Creates a new organization domain. By default the domain is verified, but can be optionally set to unverified.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrganizationDomain" method="post" path="/organizations/{organization_id}/domains" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.create(organization_id="<id>", name="<value>", enrollment_mode="<value>", verified=False)

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

<!-- UsageSnippet language="python" operationID="ListOrganizationDomains" method="get" path="/organizations/{organization_id}/domains" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.list(organization_id="<id>", verified="<value>", enrollment_mode="<value>", limit=20, offset=10)

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

<!-- UsageSnippet language="python" operationID="UpdateOrganizationDomain" method="patch" path="/organizations/{organization_id}/domains/{domain_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.update(organization_id="<id>", domain_id="<id>", enrollment_mode="<value>", verified=True)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                         | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | The ID of the organization to which the domain belongs                                                                    |
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

<!-- UsageSnippet language="python" operationID="DeleteOrganizationDomain" method="delete" path="/organizations/{organization_id}/domains/{domain_id}" -->
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
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization to which the domain belongs              |
| `domain_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The ID of the domain                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list_all

Retrieves a list of all organization domains within the current instance.
This endpoint can be used to list all domains across all organizations
or filter domains by organization, verification status, enrollment mode, or search query.

The response includes pagination information and details about each domain
including its verification status, enrollment mode, and associated counts.


### Example Usage

<!-- UsageSnippet language="python" operationID="ListAllOrganizationDomains" method="get" path="/organization_domains" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_domains.list_all(organization_id="<id>", verified=clerk_backend_api.Verified.TRUE, enrollment_mode=[
        clerk_backend_api.QueryParamEnrollmentMode.AUTOMATIC_SUGGESTION,
    ], query="<value>", order_by="-created_at", offset=10, limit=20)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The ID of the organization to filter domains by                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `verified`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [Optional[models.Verified]](../../models/verified.md)                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Filter by verification status                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `enrollment_mode`                                                                                                                                                                                                                                                                                                                                                                                                                                                              | List[[models.QueryParamEnrollmentMode](../../models/queryparamenrollmentmode.md)]                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Filter by enrollment mode                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Search domains by name or organization ID.<br/>If the query starts with "org_", it will search by exact organization ID match.<br/>Otherwise, it performs a case-insensitive partial match on the domain name.<br/><br/>Note: An empty string or whitespace-only value is not allowed and will result in a validation error.<br/>                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Allows to return organization domains in a particular order.<br/>At the moment, you can order the returned domains by their `name` or `created_at`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended to the property to order by.<br/>For example, if you want domains to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`.<br/> |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                              | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                          | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.OrganizationDomains](../../models/organizationdomains.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |