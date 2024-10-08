# OrganizationMembershipsSDK
(*organization_memberships*)

## Overview

### Available Operations

* [create](#create) - Create a new organization membership
* [list](#list) - Get a list of all members of an organization
* [update](#update) - Update an organization membership
* [delete](#delete) - Remove a member from an organization
* [update_metadata](#update_metadata) - Merge and update organization membership metadata

## create

Adds a user as a member to the given organization.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_memberships.create(organization_id="org_123", user_id="user_456", role="admin")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `organization_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the organization where the new membership will be created    | org_123                                                                |
| `user_id`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the user that will be added as a member in the organization. | user_456                                                               |
| `role`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | The role that the new member will have in the organization.            | admin                                                                  |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError69 | 400,403,404,422           | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## list

Retrieves all user memberships for the given organization

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_memberships.list(organization_id="org_789", limit=20, offset=10, order_by="+created_at")

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                  | The organization ID.                                                                                                                                                                                                                | org_789                                                                                                                                                                                                                             |
| `limit`                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                               | 20                                                                                                                                                                                                                                  |
| `offset`                                                                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                   | 10                                                                                                                                                                                                                                  |
| `order_by`                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                  | Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username.<br/>By prepending one of those values with + or -,<br/>we can choose to sort in ascending (ASC) or descending (DESC) order." | +created_at                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                 |                                                                                                                                                                                                                                     |

### Response

**[models.ListOrganizationMembershipsResponse](../../models/listorganizationmembershipsresponse.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError70 | 401,422                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## update

Updates the properties of an existing organization membership

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_memberships.update(organization_id="org_12345", user_id="user_67890", role="admin")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization the membership belongs to                | org_12345                                                           |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the user that this membership belongs to                  | user_67890                                                          |
| `role`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The new role of the given membership.                               | admin                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError71 | 400,404,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## delete

Removes the given membership from the organization

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_memberships.delete(organization_id="org_12345", user_id="user_67890")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization the membership belongs to                | org_12345                                                           |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the user that this membership belongs to                  | user_67890                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError72 | 400,401,404               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## update_metadata

Update an organization membership's metadata attributes by merging existing values with the provided parameters.
Metadata values will be updated via a deep merge. Deep means that any nested JSON objects will be merged as well.
You can remove metadata keys at any level by setting their value to `null`.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_memberships.update_metadata(organization_id="org_123456", user_id="user_654321", public_metadata={}, private_metadata={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              | Example                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                        | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The ID of the organization the membership belongs to                                                                                                     | org_123456                                                                                                                                               |
| `user_id`                                                                                                                                                | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The ID of the user that this membership belongs to                                                                                                       | user_654321                                                                                                                                              |
| `public_metadata`                                                                                                                                        | [Optional[models.UpdateOrganizationMembershipMetadataPublicMetadata]](../../models/updateorganizationmembershipmetadatapublicmetadata.md)                | :heavy_minus_sign:                                                                                                                                       | Metadata saved on the organization membership, that is visible to both your frontend and backend.<br/>The new object will be merged with the existing value. | {}                                                                                                                                                       |
| `private_metadata`                                                                                                                                       | [Optional[models.UpdateOrganizationMembershipMetadataPrivateMetadata]](../../models/updateorganizationmembershipmetadataprivatemetadata.md)              | :heavy_minus_sign:                                                                                                                                       | Metadata saved on the organization membership that is only visible to your backend.<br/>The new object will be merged with the existing value.           | {}                                                                                                                                                       |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |                                                                                                                                                          |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError73 | 400,404,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |
