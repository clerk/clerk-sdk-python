# RoleSets

## Overview

### Available Operations

* [list](#list) - Get a list of role sets
* [create](#create) - Create a role set
* [get](#get) - Retrieve a role set
* [update](#update) - Update a role set
* [replace](#replace) - Replace a role set
* [add_roles](#add_roles) - Add roles to a role set
* [replace_role](#replace_role) - Replace a role in a role set

## list

Returns a list of role sets for the instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The role sets are ordered by descending creation date by default.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListRoleSets" method="get" path="/role_sets" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.list(query="<value>", order_by="-created_at", limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Returns role sets with ID, name, or key that match the given query.<br/>Uses exact match for role set ID and partial match for name and key.                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Allows to return role sets in a particular order.<br/>At the moment, you can order the returned role sets by their `created_at`, `name`, or `key`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want role sets to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                          | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                              | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Response

**[models.RoleSets](../../models/rolesets.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new role set with the given name and roles.
The key must be unique for the instance and start with the 'role_set:' prefix, followed by lowercase alphanumeric characters and underscores only.
You must provide at least one role and specify a default role key and creator role key.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateRoleSet" method="post" path="/role_sets" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.create(name="<value>", default_role_key="<value>", creator_role_key="<value>", roles=[
        "<value 1>",
    ], key="<key>", description="coarse minor like whopping jazz concerning questioningly loose", type_=clerk_backend_api.CreateRoleSetType.CUSTOM)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                              | Type                                                                                                                                                                                   | Required                                                                                                                                                                               | Description                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                                                                 | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The name of the new role set                                                                                                                                                           |
| `default_role_key`                                                                                                                                                                     | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The key of the role to use as the default role for new organization members.<br/>Must be one of the roles in the `roles` array.                                                        |
| `creator_role_key`                                                                                                                                                                     | *str*                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                     | The key of the role to assign to organization creators.<br/>Must be one of the roles in the `roles` array.                                                                             |
| `roles`                                                                                                                                                                                | List[*str*]                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                     | Array of role keys to include in the role set.<br/>Must contain at least one role and no more than 10 roles.                                                                           |
| `key`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                     | A unique key for the role set. Must start with 'role_set:' and contain only lowercase alphanumeric characters and underscores.<br/>If not provided, a key will be generated from the name. |
| `description`                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                     | Optional description for the role set                                                                                                                                                  |
| `type`                                                                                                                                                                                 | [Optional[models.CreateRoleSetType]](../../models/createrolesettype.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                     | The type of the role set. "initial" role sets are the default for new organizations.<br/>Only one role set can be "initial" per instance.                                              |
| `retries`                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                    |

### Response

**[models.RoleSet](../../models/roleset.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ClerkErrors           | 400, 401, 402, 403, 404, 422 | application/json             |
| models.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get

Retrieves an existing role set by its key or ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetRoleSet" method="get" path="/role_sets/{role_set_key_or_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.get(role_set_key_or_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_set_key_or_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The key or ID of the role set                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoleSet](../../models/roleset.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates an existing role set.
You can update the name, key, description, type, default role, or creator role.
All parameters are optional - you can update only the fields you want to change.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateRoleSet" method="patch" path="/role_sets/{role_set_key_or_id}" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.update(role_set_key_or_id="<id>", name="<value>", key=None, description="airbus atop ouch gadzooks anti talkative mould", type_=clerk_backend_api.UpdateRoleSetType.INITIAL, default_role_key="<value>", creator_role_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `role_set_key_or_id`                                                                                                                                                                           | *str*                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                             | The key or ID of the role set to update                                                                                                                                                        |
| `name`                                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | The new name for the role set                                                                                                                                                                  |
| `key`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | A unique key for the role set. Must start with 'role_set:' and contain only lowercase alphanumeric characters and underscores.                                                                 |
| `description`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | Optional description for the role set                                                                                                                                                          |
| `type`                                                                                                                                                                                         | [OptionalNullable[models.UpdateRoleSetType]](../../models/updaterolesettype.md)                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Set to "initial" to make this the default role set for new organizations.<br/>Only one role set can be "initial" per instance; setting this will change any existing initial role set to "custom". |
| `default_role_key`                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | The key of the role to use as the default role for new organization members.<br/>Must be an existing role in the role set.                                                                     |
| `creator_role_key`                                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                             | The key of the role to assign to organization creators.<br/>Must be an existing role in the role set.                                                                                          |
| `retries`                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                            |

### Response

**[models.RoleSet](../../models/roleset.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## replace

Replaces a role set with another role set. This is functionally equivalent to deleting
the role set but allows for atomic replacement with migration support.
Organizations using this role set will be migrated to the destination role set.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceRoleSet" method="post" path="/role_sets/{role_set_key_or_id}/replace" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.replace(role_set_key_or_id="<id>", dest_role_set_key="<value>", reassignment_mappings={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `role_set_key_or_id`                                                                                                | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The key or ID of the role set to replace                                                                            |
| `dest_role_set_key`                                                                                                 | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The key of the destination role set                                                                                 |
| `reassignment_mappings`                                                                                             | Dict[str, *str*]                                                                                                    | :heavy_minus_sign:                                                                                                  | Mappings from source role keys to destination role keys.<br/>Required if members have roles that need to be reassigned. |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## add_roles

Adds one or more roles to an existing role set.
You can optionally update the default role or creator role when adding new roles.

### Example Usage

<!-- UsageSnippet language="python" operationID="AddRolesToRoleSet" method="post" path="/role_sets/{role_set_key_or_id}/roles" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.add_roles(role_set_key_or_id="<id>", role_keys=[
        "<value 1>",
        "<value 2>",
    ], default_role_key="<value>", creator_role_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `role_set_key_or_id`                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | The key or ID of the role set                                                                        |
| `role_keys`                                                                                          | List[*str*]                                                                                          | :heavy_check_mark:                                                                                   | Array of role keys to add to the role set.<br/>Must contain at least one role and no more than 10 roles. |
| `default_role_key`                                                                                   | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | Optionally update the default role to one of the newly added roles.                                  |
| `creator_role_key`                                                                                   | *Optional[str]*                                                                                      | :heavy_minus_sign:                                                                                   | Optionally update the creator role to one of the newly added roles.                                  |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[models.RoleSet](../../models/roleset.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## replace_role

Replaces a role in a role set with another role. This atomically removes
the source role and reassigns any members to the destination role.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceRoleInRoleSet" method="post" path="/role_sets/{role_set_key_or_id}/roles/replace" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.role_sets.replace_role(role_set_key_or_id="<id>", role_key="<value>", to_role_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `role_set_key_or_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The key or ID of the role set                                       |
| `role_key`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The key of the role to remove from the role set                     |
| `to_role_key`                                                       | *str*                                                               | :heavy_check_mark:                                                  | The key of the role to reassign members to                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RoleSet](../../models/roleset.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |