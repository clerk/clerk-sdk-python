# OrganizationsSDK
(*organizations*)

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
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.list(limit=20, offset=10, include_members_count=False, query="clerk", order_by="-name")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                                                      | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                                                          | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `include_members_count`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Flag to denote whether the member counts of each organization should be included in the response or not.                                                                                                                                                                                                                                                                                                                                                                                                   | false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Returns organizations with ID, name, or slug that match the given query.<br/>Uses exact match for organization ID and partial match for name and slug.                                                                                                                                                                                                                                                                                                                                                     | clerk                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Allows to return organizations in a particular order.<br/>At the moment, you can order the returned organizations either by their `name`, `created_at` or `members_count`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want organizations to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`. | -name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |


### Response

**[models.Organizations](../../models/organizations.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## create

Creates a new organization with the given name for an instance.
In order to successfully create an organization you need to provide the ID of the User who will become the organization administrator.
You can specify an optional slug for the new organization.
If provided, the organization slug can contain only lowercase alphanumeric characters (letters and digits) and the dash "-".
Organization slugs must be unique for the instance.
You can provide additional metadata for the organization and set any custom attribute you want.
Organizations support private and public metadata.
Private metadata can only be accessed from the Backend API.
Public metadata can be accessed from the Backend API, and are read-only from the Frontend API.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.create(name="NewOrg", created_by="user_123", private_metadata={}, public_metadata={}, slug="neworg", max_allowed_memberships=100)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                                 | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The name of the new organization                                                                                                       | NewOrg                                                                                                                                 |
| `created_by`                                                                                                                           | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | The ID of the User who will become the administrator for the new organization                                                          | user_123                                                                                                                               |
| `private_metadata`                                                                                                                     | [Optional[models.CreateOrganizationPrivateMetadata]](../../models/createorganizationprivatemetadata.md)                                | :heavy_minus_sign:                                                                                                                     | Metadata saved on the organization, accessible only from the Backend API                                                               | {<br/>"internal_code": "ABC123"<br/>}                                                                                                  |
| `public_metadata`                                                                                                                      | [Optional[models.CreateOrganizationPublicMetadata]](../../models/createorganizationpublicmetadata.md)                                  | :heavy_minus_sign:                                                                                                                     | Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API             | {<br/>"public_event": "Annual Summit"<br/>}                                                                                            |
| `slug`                                                                                                                                 | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | A slug for the new organization.<br/>Can contain only lowercase alphanumeric characters and the dash "-".<br/>Must be unique for the instance. | neworg                                                                                                                                 |
| `max_allowed_memberships`                                                                                                              | *Optional[int]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | The maximum number of memberships allowed for this organization                                                                        | 100                                                                                                                                    |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |


### Response

**[models.Organization](../../models/organization.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## get

Fetches the organization whose ID or slug matches the provided `id_or_slug` URL query parameter.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.get(organization_id="org_123")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID or slug of the organization                                  | org_123                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Organization](../../models/organization.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## update

Updates an existing organization

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.update(organization_id="org_123_update", public_metadata={}, private_metadata={}, name="New Organization Name", slug="new-org-slug", max_allowed_memberships=100, admin_delete_enabled=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                       | *str*                                                                                                   | :heavy_check_mark:                                                                                      | The ID of the organization to update                                                                    | org_123_update                                                                                          |
| `public_metadata`                                                                                       | [Optional[models.UpdateOrganizationPublicMetadata]](../../models/updateorganizationpublicmetadata.md)   | :heavy_minus_sign:                                                                                      | Metadata saved on the organization, that is visible to both your frontend and backend.                  | {}                                                                                                      |
| `private_metadata`                                                                                      | [Optional[models.UpdateOrganizationPrivateMetadata]](../../models/updateorganizationprivatemetadata.md) | :heavy_minus_sign:                                                                                      | Metadata saved on the organization that is only visible to your backend.                                | {}                                                                                                      |
| `name`                                                                                                  | *Optional[Nullable[str]]*                                                                               | :heavy_minus_sign:                                                                                      | The new name of the organization                                                                        | New Organization Name                                                                                   |
| `slug`                                                                                                  | *Optional[Nullable[str]]*                                                                               | :heavy_minus_sign:                                                                                      | The new slug of the organization, which needs to be unique in the instance                              | new-org-slug                                                                                            |
| `max_allowed_memberships`                                                                               | *Optional[Nullable[int]]*                                                                               | :heavy_minus_sign:                                                                                      | The maximum number of memberships allowed for this organization                                         | 100                                                                                                     |
| `admin_delete_enabled`                                                                                  | *Optional[Nullable[bool]]*                                                                              | :heavy_minus_sign:                                                                                      | If true, an admin can delete this organization with the Frontend API.                                   | true                                                                                                    |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |


### Response

**[models.Organization](../../models/organization.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,404,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete

Deletes the given organization.
Please note that deleting an organization will also delete all memberships and invitations.
This is not reversible.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.delete(organization_id="org_321_delete")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization to delete                                | org_321_delete                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.DeletedObject](../../models/deletedobject.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## merge_metadata

Update organization metadata attributes by merging existing values with the provided parameters.
Metadata values will be updated via a deep merge.
Deep meaning that any nested JSON objects will be merged as well.
You can remove metadata keys at any level by setting their value to `null`.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.merge_metadata(organization_id="org_12345", public_metadata={}, private_metadata={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                     | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                             | *str*                                                                                                                                         | :heavy_check_mark:                                                                                                                            | The ID of the organization for which metadata will be merged or updated                                                                       | org_12345                                                                                                                                     |
| `public_metadata`                                                                                                                             | [Optional[models.MergeOrganizationMetadataPublicMetadata]](../../models/mergeorganizationmetadatapublicmetadata.md)                           | :heavy_minus_sign:                                                                                                                            | Metadata saved on the organization, that is visible to both your frontend and backend.<br/>The new object will be merged with the existing value. | {<br/>"announcement": "We are opening a new office!"<br/>}                                                                                    |
| `private_metadata`                                                                                                                            | [Optional[models.MergeOrganizationMetadataPrivateMetadata]](../../models/mergeorganizationmetadataprivatemetadata.md)                         | :heavy_minus_sign:                                                                                                                            | Metadata saved on the organization that is only visible to your backend.<br/>The new object will be merged with the existing value.           | {<br/>"internal_use_only": "Future plans discussion."<br/>}                                                                                   |
| `retries`                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                              | :heavy_minus_sign:                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                           |                                                                                                                                               |


### Response

**[models.Organization](../../models/organization.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## upload_logo

Set or replace an organization's logo, by uploading an image file.
This endpoint uses the `multipart/form-data` request content type and accepts a file of image type.
The file size cannot exceed 10MB.
Only the following file content types are supported: `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/x-icon`, `image/vnd.microsoft.icon`.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.upload_logo(organization_id="org_12345", uploader_user_id="user_67890", file={
    "file_name": "your_file_here",
    "content": open("<file_path>", "rb"),
    "content_type": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `organization_id`                                                               | *str*                                                                           | :heavy_check_mark:                                                              | The ID of the organization for which to upload a logo                           | org_12345                                                                       |
| `uploader_user_id`                                                              | *str*                                                                           | :heavy_check_mark:                                                              | The ID of the user that will be credited with the image upload.                 | user_67890                                                                      |
| `file`                                                                          | [models.UploadOrganizationLogoFile](../../models/uploadorganizationlogofile.md) | :heavy_check_mark:                                                              | N/A                                                                             |                                                                                 |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |


### Response

**[models.OrganizationWithLogo](../../models/organizationwithlogo.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,403,404,413    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete_logo

Delete the organization's logo.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.organizations.delete_logo(organization_id="org_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization for which the logo will be deleted.      | org_12345                                                           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.Organization](../../models/organization.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |