# Directories

## Overview

### Available Operations

* [list](#list) - List all directories
* [create](#create) - Create a directory
* [get](#get) - Retrieve a directory
* [update](#update) - Update a directory
* [delete](#delete) - Delete a directory
* [rotate_api_key](#rotate_api_key) - Rotate a directory's API key
* [list_group_role_mappings](#list_group_role_mappings) - List directory group role mappings
* [create_group_role_mapping](#create_group_role_mapping) - Create a directory group role mapping
* [replace_group_role_mappings](#replace_group_role_mappings) - Replace directory group role mappings
* [delete_group_role_mapping](#delete_group_role_mapping) - Delete a directory group role mapping

## list

Returns a list of all directories for the instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListDirectories" method="get" path="/directories" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.list(limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.DirectoryList](../../models/directorylist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Create a new directory for the instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDirectory" method="post" path="/directories" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.create(request={
        "enterprise_connection_id": "<id>",
        "name": "<value>",
        "provider": "<value>",
        "group_role_mappings": [
            {
                "directory_group_id": "<id>",
                "scim_group_id": "<id>",
                "directory_group_display_name": "<value>",
                "scim_group_display_name": "<value>",
                "role_id": "<id>",
                "precedence": 68591,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CreateDirectoryRequestBody](../../models/createdirectoryrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.Directory](../../models/directory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Returns the details of a directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetDirectory" method="get" path="/directories/{directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.get(directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `directory_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory to retrieve                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Directory](../../models/directory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates a directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateDirectory" method="patch" path="/directories/{directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.update(directory_id="<id>", name="<value>", enabled=True, provider="<value>", attribute_mapping={
        "key": "<value>",
    }, group_role_mapping_enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                               | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `directory_id`                                                                                                                          | *str*                                                                                                                                   | :heavy_check_mark:                                                                                                                      | The ID of the directory to update                                                                                                       |
| `name`                                                                                                                                  | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | A human-friendly name for the directory.                                                                                                |
| `enabled`                                                                                                                               | *Optional[bool]*                                                                                                                        | :heavy_minus_sign:                                                                                                                      | Whether the directory is enabled.                                                                                                       |
| `provider`                                                                                                                              | *Optional[str]*                                                                                                                         | :heavy_minus_sign:                                                                                                                      | The identity provider for this directory.                                                                                               |
| `attribute_mapping`                                                                                                                     | Dict[str, *Nullable[str]*]                                                                                                              | :heavy_minus_sign:                                                                                                                      | Attribute-to-directory-path entries to merge into the directory's attribute mapping.<br/>Set a key to `null` to remove it from the mapping. |
| `group_role_mapping_enabled`                                                                                                            | *Optional[bool]*                                                                                                                        | :heavy_minus_sign:                                                                                                                      | Whether group-to-role mapping is enabled for this directory.                                                                            |
| `retries`                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                        | :heavy_minus_sign:                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                     |

### Response

**[models.Directory](../../models/directory.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes a directory and stops provisioning for it. Provisioning requests authenticated
with the directory's API key are rejected afterwards.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDirectory" method="delete" path="/directories/{directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.delete(directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `directory_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory to delete                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## rotate_api_key

Generates a new API key for the directory and returns it in the `api_key` field.
This is the only way to obtain the key after creation, so make sure to update it in
your identity provider. The previous key remains valid for a short grace period before
it expires.

### Example Usage

<!-- UsageSnippet language="python" operationID="RotateDirectoryAPIKey" method="post" path="/directories/{directory_id}/rotate_api_key" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.rotate_api_key(directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `directory_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory whose API key to rotate                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Directory](../../models/directory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list_group_role_mappings

Returns the list of directory group to organization role mappings for a directory, ordered by precedence.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListDirectoryGroupRoleMappings" method="get" path="/directories/{directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.list_group_role_mappings(directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `directory_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory.                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DirectoryGroupRoleMappingList](../../models/directorygrouprolemappinglist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_group_role_mapping

Creates a new directory group to organization role mapping for a directory.
Group role mapping must be enabled on the directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateDirectoryGroupRoleMapping" method="post" path="/directories/{directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.create_group_role_mapping(directory_id="<id>", role_id="<id>", directory_group_id="<id>", scim_group_id="<id>", precedence=213856)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `directory_id`                                                                                                                                                                   | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The ID of the directory.                                                                                                                                                         |
| `role_id`                                                                                                                                                                        | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The ID of the organization role to assign to members of the group.                                                                                                               |
| `directory_group_id`                                                                                                                                                             | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The group ID from the identity provider. Exactly one of `directory_group_id` or `scim_group_id` is required.                                                                     |
| `scim_group_id`                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The legacy name for `directory_group_id`. Send either one, or both with the same value; sending both with different values is rejected.                                          |
| `precedence`                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The precedence for this mapping. Lower values take priority when a user belongs<br/>to multiple mapped groups. If omitted, the mapping is appended with the<br/>next-highest precedence. |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.DirectoryGroupRoleMapping](../../models/directorygrouprolemapping.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## replace_group_role_mappings

Replaces the entire set of directory group role mappings for a directory. The position of
each item in the `mappings` array determines its precedence (the first item gets
precedence 1). Passing an empty array removes all mappings. Group role mapping must be
enabled on the directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceDirectoryGroupRoleMappings" method="put" path="/directories/{directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.replace_group_role_mappings(directory_id="<id>", mappings=[
        {
            "directory_group_id": "<id>",
            "scim_group_id": "<id>",
            "role_id": "<id>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `directory_id`                                                                                                      | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | The ID of the directory.                                                                                            |
| `mappings`                                                                                                          | List[[models.ReplaceDirectoryGroupRoleMappingsMappings](../../models/replacedirectorygrouprolemappingsmappings.md)] | :heavy_check_mark:                                                                                                  | The desired set of mappings. Array order sets precedence (1-indexed). An empty array clears all mappings.           |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.DirectoryGroupRoleMappingList](../../models/directorygrouprolemappinglist.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_group_role_mapping

Deletes a single directory group role mapping. Group role mapping must be enabled on the
directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteDirectoryGroupRoleMapping" method="delete" path="/directories/{directory_id}/group_role_mappings/{mapping_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.directories.delete_group_role_mapping(directory_id="<id>", mapping_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `directory_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory.                                            |
| `mapping_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the directory group role mapping to delete.               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DirectoryGroupRoleMappingDeleted](../../models/directorygrouprolemappingdeleted.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |