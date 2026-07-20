# ScimDirectories

## Overview

### Available Operations

* [list](#list) - List all SCIM directories
* [create](#create) - Create a SCIM directory
* [get](#get) - Retrieve a SCIM directory
* [update](#update) - Update a SCIM directory
* [delete](#delete) - Delete a SCIM directory
* [rotate_api_key](#rotate_api_key) - Rotate a SCIM directory's API key
* [list_group_role_mappings](#list_group_role_mappings) - List SCIM group role mappings
* [create_group_role_mapping](#create_group_role_mapping) - Create a SCIM group role mapping
* [replace_group_role_mappings](#replace_group_role_mappings) - Replace SCIM group role mappings
* [delete_group_role_mapping](#delete_group_role_mapping) - Delete a SCIM group role mapping

## list

Returns a list of all SCIM directories for the instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListSCIMDirectories" method="get" path="/scim_directories" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.list(limit=20, offset=10)

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

**[models.SCIMDirectoryList](../../models/scimdirectorylist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Create a new SCIM directory for the instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateSCIMDirectory" method="post" path="/scim_directories" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.create(request={
        "enterprise_connection_id": "<id>",
        "name": "<value>",
        "provider": "<value>",
        "group_role_mappings": [
            {
                "scim_group_id": "<id>",
                "scim_group_display_name": "<value>",
                "role_id": "<id>",
                "precedence": 919086,
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.CreateSCIMDirectoryRequestBody](../../models/createscimdirectoryrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.SCIMDirectory](../../models/scimdirectory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Returns the details of a SCIM directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetSCIMDirectory" method="get" path="/scim_directories/{scim_directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.get(scim_directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scim_directory_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM directory to retrieve                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SCIMDirectory](../../models/scimdirectory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates a SCIM directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateSCIMDirectory" method="patch" path="/scim_directories/{scim_directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.update(scim_directory_id="<id>", name="<value>", enabled=False, provider="<value>", attribute_mapping={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, group_role_mapping_enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `scim_directory_id`                                                                                                                | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | The ID of the SCIM directory to update                                                                                             |
| `name`                                                                                                                             | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | A human-friendly name for the SCIM directory.                                                                                      |
| `enabled`                                                                                                                          | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | Whether the SCIM directory is enabled.                                                                                             |
| `provider`                                                                                                                         | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | The identity provider for this SCIM directory.                                                                                     |
| `attribute_mapping`                                                                                                                | Dict[str, *Nullable[str]*]                                                                                                         | :heavy_minus_sign:                                                                                                                 | Attribute-to-SCIM-path entries to merge into the directory's attribute mapping.<br/>Set a key to `null` to remove it from the mapping. |
| `group_role_mapping_enabled`                                                                                                       | *Optional[bool]*                                                                                                                   | :heavy_minus_sign:                                                                                                                 | Whether group-to-role mapping is enabled for this SCIM directory.                                                                  |
| `retries`                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                   | :heavy_minus_sign:                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                |

### Response

**[models.SCIMDirectory](../../models/scimdirectory.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes a SCIM directory and stops provisioning for it. SCIM requests authenticated
with the directory's API key are rejected afterwards.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteSCIMDirectory" method="delete" path="/scim_directories/{scim_directory_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.delete(scim_directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scim_directory_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM directory to delete                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## rotate_api_key

Generates a new API key for the SCIM directory and returns it in the `api_key` field.
This is the only way to obtain the key after creation, so make sure to update it in
your identity provider. The previous key remains valid for a short grace period before
it expires.

### Example Usage

<!-- UsageSnippet language="python" operationID="RotateSCIMDirectoryAPIKey" method="post" path="/scim_directories/{scim_directory_id}/rotate_api_key" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.rotate_api_key(scim_directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scim_directory_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM directory whose API key to rotate                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SCIMDirectory](../../models/scimdirectory.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list_group_role_mappings

Returns the list of SCIM group to organization role mappings for a SCIM directory, ordered by precedence.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListSCIMGroupRoleMappings" method="get" path="/scim_directories/{scim_directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.list_group_role_mappings(scim_directory_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scim_directory_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM directory.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SCIMGroupRoleMappingList](../../models/scimgrouprolemappinglist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_group_role_mapping

Creates a new SCIM group to organization role mapping for a SCIM directory.
Group role mapping must be enabled on the directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateSCIMGroupRoleMapping" method="post" path="/scim_directories/{scim_directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.create_group_role_mapping(scim_directory_id="<id>", scim_group_id="<id>", role_id="<id>", precedence=722732)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                        | Type                                                                                                                                                                             | Required                                                                                                                                                                         | Description                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scim_directory_id`                                                                                                                                                              | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The ID of the SCIM directory.                                                                                                                                                    |
| `scim_group_id`                                                                                                                                                                  | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The SCIM group ID from the identity provider.                                                                                                                                    |
| `role_id`                                                                                                                                                                        | *str*                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                               | The ID of the organization role to assign to members of the SCIM group.                                                                                                          |
| `precedence`                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                               | The precedence for this mapping. Lower values take priority when a user belongs<br/>to multiple mapped groups. If omitted, the mapping is appended with the<br/>next-highest precedence. |
| `retries`                                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                                              |

### Response

**[models.SCIMGroupRoleMapping](../../models/scimgrouprolemapping.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## replace_group_role_mappings

Replaces the entire set of SCIM group role mappings for a directory. The position of
each item in the `mappings` array determines its precedence (the first item gets
precedence 1). Passing an empty array removes all mappings. Group role mapping must be
enabled on the directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceSCIMGroupRoleMappings" method="put" path="/scim_directories/{scim_directory_id}/group_role_mappings" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.replace_group_role_mappings(scim_directory_id="<id>", mappings=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `scim_directory_id`                                                                                       | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the SCIM directory.                                                                             |
| `mappings`                                                                                                | List[[models.Mappings](../../models/mappings.md)]                                                         | :heavy_check_mark:                                                                                        | The desired set of mappings. Array order sets precedence (1-indexed). An empty array clears all mappings. |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.SCIMGroupRoleMappingList](../../models/scimgrouprolemappinglist.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_group_role_mapping

Deletes a single SCIM group role mapping. Group role mapping must be enabled on the
directory.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteSCIMGroupRoleMapping" method="delete" path="/scim_directories/{scim_directory_id}/group_role_mappings/{mapping_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.scim_directories.delete_group_role_mapping(scim_directory_id="<id>", mapping_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `scim_directory_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM directory.                                       |
| `mapping_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SCIM group role mapping to delete.                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SCIMGroupRoleMappingDeleted](../../models/scimgrouprolemappingdeleted.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |