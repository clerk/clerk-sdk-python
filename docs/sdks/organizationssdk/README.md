# OrganizationsSDK
(*organizations*)

## Overview

### Available Operations

* [list](#list) - Get a list of organizations for an instance
* [create](#create) - Create an organization
* [get](#get) - Retrieve an organization by ID or slug
* [update](#update) - Update an organization
* [delete](#delete) - Delete an organization
* [merge_metadata](#merge_metadata) - Merge and update metadata for an organization
* [upload_logo](#upload_logo) - Upload a logo for the organization
* [delete_logo](#delete_logo) - Delete the organization's logo.

## list

This request returns the list of organizations for an instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The organizations are ordered by descending creation date.
Most recent organizations will be returned first.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.list(include_members_count=False, include_missing_member_with_elevated_permissions=False, query="false", user_id=[
        "clerk",
    ], organization_id=[
        "-name",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include_members_count`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Flag to denote whether the member counts of each organization should be included in the response or not.                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `include_missing_member_with_elevated_permissions`                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Flag to denote whether or not to include a member with elevated permissions who is not currently a member of the organization.                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Returns organizations with ID, name, or slug that match the given query.<br/>Uses exact match for organization ID and partial match for name and slug.                                                                                                                                                                                                                                                                                                                                                     | false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `user_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Returns organizations with the user ids specified. Any user ids not found are ignored.<br/>For each user id, the `+` and `-` can be prepended to the id, which denote whether the<br/>respective organization should be included or excluded from the result set.                                                                                                                                                                                                                                          | clerk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `organization_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Returns organizations with the organization ids specified. Any organization ids not found are ignored.<br/>For each organization id, the `+` and `-` can be prepended to the id, which denote whether the<br/>respective organization should be included or excluded from the result set. Accepts up to 100 organization ids.<br/>Example: ?organization_id=+org_1&organization_id=-org_2                                                                                                                  | -name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Allows to return organizations in a particular order.<br/>At the moment, you can order the returned organizations either by their `name`, `created_at` or `members_count`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want organizations to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                                                      | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                                                          | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Response

**[models.Organizations](../../models/organizations.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new organization with the given name for an instance.
You can specify an optional slug for the new organization.
If provided, the organization slug can contain only lowercase alphanumeric characters (letters and digits) and the dash "-".
Organization slugs must be unique for the instance.
You can provide additional metadata for the organization and set any custom attribute you want.
Organizations support private and public metadata.
Private metadata can only be accessed from the Backend API.
Public metadata can be accessed from the Backend API, and are read-only from the Frontend API.
The `created_by` user will see this as their [active organization] (https://clerk.com/docs/organizations/overview#active-organization)
the next time they create a session, presuming they don't explicitly set a different organization as active before then.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.create(request={
        "name": "NewOrg",
        "created_by": "user_123",
        "private_metadata": {
            "internal_code": "ABC123",
        },
        "public_metadata": {
            "public_event": "Annual Summit",
        },
        "slug": "neworg",
        "max_allowed_memberships": 100,
        "created_at": "1721474962525",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.CreateOrganizationRequestBody](../../models/createorganizationrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Fetches the organization whose ID or slug matches the provided `id_or_slug` URL query parameter.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.get(organization_id="org_123", include_members_count=False, include_missing_member_with_elevated_permissions=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                              | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | The ID or slug of the organization                                                                                             | org_123                                                                                                                        |
| `include_members_count`                                                                                                        | *Optional[bool]*                                                                                                               | :heavy_minus_sign:                                                                                                             | Flag to denote whether or not the organization's members count should be included in the response.                             |                                                                                                                                |
| `include_missing_member_with_elevated_permissions`                                                                             | *Optional[bool]*                                                                                                               | :heavy_minus_sign:                                                                                                             | Flag to denote whether or not to include a member with elevated permissions who is not currently a member of the organization. |                                                                                                                                |
| `retries`                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                               | :heavy_minus_sign:                                                                                                             | Configuration to override the default retry behavior of the client.                                                            |                                                                                                                                |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates an existing organization

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.update(organization_id="org_123_update", public_metadata={

    }, private_metadata={

    }, name="New Organization Name", slug="new-org-slug", max_allowed_memberships=100, admin_delete_enabled=True, created_at="1733171278360")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     | Example                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                               | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | The ID of the organization to update                                                                                            | org_123_update                                                                                                                  |
| `public_metadata`                                                                                                               | Dict[str, *Any*]                                                                                                                | :heavy_minus_sign:                                                                                                              | Metadata saved on the organization, that is visible to both your frontend and backend.                                          | {}                                                                                                                              |
| `private_metadata`                                                                                                              | Dict[str, *Any*]                                                                                                                | :heavy_minus_sign:                                                                                                              | Metadata saved on the organization that is only visible to your backend.                                                        | {}                                                                                                                              |
| `name`                                                                                                                          | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The new name of the organization.<br/>May not contain URLs or HTML.<br/>Max length: 256                                         | New Organization Name                                                                                                           |
| `slug`                                                                                                                          | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The new slug of the organization, which needs to be unique in the instance                                                      | new-org-slug                                                                                                                    |
| `max_allowed_memberships`                                                                                                       | *OptionalNullable[int]*                                                                                                         | :heavy_minus_sign:                                                                                                              | The maximum number of memberships allowed for this organization                                                                 | 100                                                                                                                             |
| `admin_delete_enabled`                                                                                                          | *OptionalNullable[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                              | If true, an admin can delete this organization with the Frontend API.                                                           | true                                                                                                                            |
| `created_at`                                                                                                                    | *OptionalNullable[str]*                                                                                                         | :heavy_minus_sign:                                                                                                              | A custom date/time denoting _when_ the organization was created, specified in RFC3339 format (e.g. `2012-10-20T07:15:20.902Z`). |                                                                                                                                 |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |                                                                                                                                 |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 404, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Deletes the given organization.
Please note that deleting an organization will also delete all memberships and invitations.
This is not reversible.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.delete(organization_id="org_321_delete")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization to delete                                | org_321_delete                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## merge_metadata

Update organization metadata attributes by merging existing values with the provided parameters.
Metadata values will be updated via a deep merge.
Deep meaning that any nested JSON objects will be merged as well.
You can remove metadata keys at any level by setting their value to `null`.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.merge_metadata(organization_id="org_12345", public_metadata={
        "announcement": "We are opening a new office!",
    }, private_metadata={
        "internal_use_only": "Future plans discussion.",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                             | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The ID of the organization for which metadata will be merged or updated                                                                       | org_12345                                                                                                                                     |
| `public_metadata`                                                                                                                             | Dict[str, *Any*]                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Metadata saved on the organization, that is visible to both your frontend and backend.<br/>The new object will be merged with the existing value. | {<br/>"announcement": "We are opening a new office!"<br/>}                                                                                    |
| `private_metadata`                                                                                                                            | Dict[str, *Any*]                                                                                                                              | :heavy_minus_sign:                                                                                                                            | Metadata saved on the organization that is only visible to your backend.<br/>The new object will be merged with the existing value.           | {<br/>"internal_use_only": "Future plans discussion."<br/>}                                                                                   |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## upload_logo

Set or replace an organization's logo, by uploading an image file.
This endpoint uses the `multipart/form-data` request content type and accepts a file of image type.
The file size cannot exceed 10MB.
Only the following file content types are supported: `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/x-icon`, `image/vnd.microsoft.icon`.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.upload_logo(organization_id="org_12345", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
        "content_type": "<value>",
    }, uploader_user_id="user_67890")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `organization_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | The ID of the organization for which to upload a logo                           | org_12345                                                                       |
| `file`                                                                          | [models.UploadOrganizationLogoFile](../../models/uploadorganizationlogofile.md) | :heavy_check_mark:                                                              | N/A                                                                             | path/to/your/logo.png                                                           |
| `uploader_user_id`                                                              | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The ID of the user that will be credited with the image upload.                 | user_67890                                                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.OrganizationWithLogo](../../models/organizationwithlogo.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 404, 413 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete_logo

Delete the organization's logo.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organizations.delete_logo(organization_id="org_12345")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization for which the logo will be deleted.      | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |