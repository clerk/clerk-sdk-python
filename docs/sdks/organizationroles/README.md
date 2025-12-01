# OrganizationRoles
(*organization_roles*)

## Overview

### Available Operations

* [list](#list) - Get a list of organization roles
* [create](#create) - Create an organization role
* [get](#get) - Retrieve an organization role
* [update](#update) - Update an organization role
* [delete](#delete) - Delete an organization role
* [assign_permission](#assign_permission) - Assign a permission to an organization role
* [remove_permission](#remove_permission) - Remove a permission from an organization role

## list

This request returns the list of organization roles for the instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The organization roles are ordered by descending creation date.
Most recent roles will be returned first.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListOrganizationRoles" method="get" path="/organization_roles" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.list(query="<value>", order_by="-created_at", limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Returns organization roles with ID, name, or key that match the given query.<br/>Uses exact match for organization role ID and partial match for name and key.                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Allows to return organization roles in a particular order.<br/>At the moment, you can order the returned organization roles by their `created_at`, `name`, or `key`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want organization roles to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                                                     | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                                                         | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Response

**[models.Roles](../../models/roles.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new organization role with the given name and permissions for an instance.
The key must be unique for the instance and start with the 'org:' prefix, followed by lowercase alphanumeric characters and underscores only.
You can optionally provide a description for the role and specify whether it should be included in the initial role set.
Organization roles support permissions that can be assigned to control access within the organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOrganizationRole" method="post" path="/organization_roles" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.create(name="<value>", key="<key>", description=None, permissions=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ], include_in_initial_role_set=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                             | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | The name of the new organization role                                                                                              |
| `key`                                                                                                                              | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | A unique key for the organization role. Must start with 'org:' and contain only lowercase alphanumeric characters and underscores. |
| `description`                                                                                                                      | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Optional description for the role                                                                                                  |
| `permissions`                                                                                                                      | List[*str*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Array of permission IDs to assign to the role                                                                                      |
| `include_in_initial_role_set`                                                                                                      | *OptionalNullable[bool]*                                                                                                           | :heavy_minus_sign:                                                                                                                 | Whether this role should be included in the initial role set                                                                       |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ClerkErrors           | 400, 401, 402, 403, 404, 422 | application/json             |
| models.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get

Use this request to retrieve an existing organization role by its ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetOrganizationRole" method="get" path="/organization_roles/{organization_role_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.get(organization_role_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_role_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization role                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates an existing organization role.
You can update the name, key, description, and permissions of the role.
All parameters are optional - you can update only the fields you want to change.
If the role is used as a creator role or domain default role, updating the key will cascade the update to the organization settings.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateOrganizationRole" method="patch" path="/organization_roles/{organization_role_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.update(organization_role_id="<id>", name="<value>", key=None, description="granny lively upon suitcase save whereas very generously ick variable", permissions=[
        "<value 1>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `organization_role_id`                                                                                                             | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | The ID of the organization role to update                                                                                          |
| `name`                                                                                                                             | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | The new name for the organization role                                                                                             |
| `key`                                                                                                                              | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | A unique key for the organization role. Must start with 'org:' and contain only lowercase alphanumeric characters and underscores. |
| `description`                                                                                                                      | *OptionalNullable[str]*                                                                                                            | :heavy_minus_sign:                                                                                                                 | Optional description for the role                                                                                                  |
| `permissions`                                                                                                                      | List[*str*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Array of permission IDs to assign to the role. If provided, this will replace the existing permissions.                            |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes the organization role.
The role cannot be deleted if it is currently used as the default creator role, domain default role, assigned to any members, or exists in any invitations.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteOrganizationRole" method="delete" path="/organization_roles/{organization_role_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.delete(organization_role_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_role_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization role to delete                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## assign_permission

Assigns a permission to an organization role

### Example Usage

<!-- UsageSnippet language="python" operationID="AssignPermissionToOrganizationRole" method="post" path="/organization_roles/{organization_role_id}/permissions/{permission_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.assign_permission(organization_role_id="<id>", permission_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_role_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization role                                     |
| `permission_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the permission to assign                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404, 409 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## remove_permission

Removes a permission from an organization role

### Example Usage

<!-- UsageSnippet language="python" operationID="RemovePermissionFromOrganizationRole" method="delete" path="/organization_roles/{organization_role_id}/permissions/{permission_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_roles.remove_permission(organization_role_id="<id>", permission_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_role_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization role                                     |
| `permission_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the permission to remove                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Role](../../models/role.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |