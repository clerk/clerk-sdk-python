# OrganizationPermissions
(*organization_permissions*)

## Overview

### Available Operations

* [list](#list) - Get a list of all organization permissions
* [create](#create) - Create a new organization permission
* [get](#get) - Get an organization permission
* [update](#update) - Update an organization permission
* [delete](#delete) - Delete an organization permission

## list

Retrieves all organization permissions for the given instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListOrganizationPermissions" method="get" path="/organization_permissions" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_permissions.list(query="<value>", order_by="<value>", limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                   | Returns organization permissions with ID, name, or key that match the given query.<br/>Uses exact match for permission ID and partial match for name and key.                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                   | Allows to return organization permissions in a particular order.<br/>At the moment, you can order the returned permissions by their `created_at`, `name`, or `key`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want permissions to be returned in descending order according to their `created_at` property, you can use `-created_at`. |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                   | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                | 20                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                   | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                    | 10                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.Permissions](../../models/permissions.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new organization permission for the given instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrganizationPermission" method="post" path="/organization_permissions" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_permissions.create(name="<value>", key="<key>", description="descent information whereas settler while publicity like")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The name of the permission.                                                                                                                                                                                                                                                                              |
| `key`                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | The key of the permission. Must have the format "org:feature:action" where feature and action are segments consisting of lowercase letters, digits, or underscores, for example "org:billing:manage" or "org:team:read". Cannot begin with "org:sys_" as that prefix is reserved for system permissions. |
| `description`                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | A description of the permission.                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                      |

### Response

**[models.Permission](../../models/permission.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 402, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## get

Retrieves the details of an organization permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrganizationPermission" method="get" path="/organization_permissions/{permission_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_permissions.get(permission_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `permission_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the permission to retrieve                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Permission](../../models/permission.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates the properties of an existing organization permission.
System permissions cannot be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateOrganizationPermission" method="patch" path="/organization_permissions/{permission_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_permissions.update(permission_id="<id>", name="<value>", key="<key>", description="nor that save before oof and far inside")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `permission_id`                                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                  | The ID of the permission to update                                                                                                                                                                                                                  |
| `name`                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                  | The name of the permission.                                                                                                                                                                                                                         |
| `key`                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                  | The key of the permission. Must have the format "org:feature:action" where feature and action are segments consisting of lowercase letters, digits, or underscores. Cannot begin with "org:sys_" as that prefix is reserved for system permissions. |
| `description`                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                  | A description of the permission.                                                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                 |

### Response

**[models.Permission](../../models/permission.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes an organization permission.
System permissions cannot be deleted.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteOrganizationPermission" method="delete" path="/organization_permissions/{permission_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_permissions.delete(permission_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `permission_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the permission to delete                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |