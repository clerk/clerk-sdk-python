# OrganizationInvitationsSDK
(*organization_invitations*)

## Overview

### Available Operations

* [create](#create) - Create and send an organization invitation
* [list](#list) - Get a list of organization invitations
* [create_bulk](#create_bulk) - Bulk create and send organization invitations
* [~~list_pending~~](#list_pending) - Get a list of pending organization invitations :warning: **Deprecated**
* [get](#get) - Retrieve an organization invitation by ID
* [revoke](#revoke) - Revoke a pending organization invitation

## create

Creates a new organization invitation and sends an email to the provided `email_address` with a link to accept the invitation and join the organization.
You can specify the `role` for the invited organization member.

New organization invitations get a "pending" status until they are revoked by an organization administrator or accepted by the invitee.

The request body supports passing an optional `redirect_url` parameter.
When the invited user clicks the link to accept the invitation, they will be redirected to the URL provided.
Use this parameter to implement a custom invitation acceptance flow.

You must specify the ID of the user that will send the invitation with the `inviter_user_id` parameter.
That user must be a member with administrator privileges in the organization.
Only "admin" members can create organization invitations.

You can optionally provide public and private metadata for the organization invitation.
The public metadata are visible by both the Frontend and the Backend whereas the private ones only by the Backend.
When the organization invitation is accepted, the metadata will be transferred to the newly created organization membership.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.create(organization_id="org_12345", email_address="user@example.com", inviter_user_id="user_67890", role="admin", public_metadata={}, private_metadata={}, redirect_url="https://example.com/welcome")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              | Example                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                        | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | The ID of the organization for which to send the invitation                                                                              | org_12345                                                                                                                                |
| `email_address`                                                                                                                          | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | The email address of the new member that is going to be invited to the organization                                                      | user@example.com                                                                                                                         |
| `inviter_user_id`                                                                                                                        | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | The ID of the user that invites the new member to the organization.<br/>Must be an administrator in the organization.                    | user_67890                                                                                                                               |
| `role`                                                                                                                                   | *str*                                                                                                                                    | :heavy_check_mark:                                                                                                                       | The role of the new member in the organization                                                                                           | admin                                                                                                                                    |
| `public_metadata`                                                                                                                        | [Optional[models.CreateOrganizationInvitationPublicMetadata]](../../models/createorganizationinvitationpublicmetadata.md)                | :heavy_minus_sign:                                                                                                                       | Metadata saved on the organization invitation, read-only from the Frontend API and fully accessible (read/write) from the Backend API.   | {<br/>"key": "value"<br/>}                                                                                                               |
| `private_metadata`                                                                                                                       | [Optional[models.CreateOrganizationInvitationPrivateMetadata]](../../models/createorganizationinvitationprivatemetadata.md)              | :heavy_minus_sign:                                                                                                                       | Metadata saved on the organization invitation, fully accessible (read/write) from the Backend API but not visible from the Frontend API. | {<br/>"private_key": "secret_value"<br/>}                                                                                                |
| `redirect_url`                                                                                                                           | *Optional[str]*                                                                                                                          | :heavy_minus_sign:                                                                                                                       | Optional URL that the invitee will be redirected to once they accept the invitation by clicking the join link in the invitation email.   | https://example.com/welcome                                                                                                              |
| `retries`                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                         | :heavy_minus_sign:                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                      |                                                                                                                                          |

### Response

**[models.OrganizationInvitation](../../models/organizationinvitation.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError63 | 400,403,404,422           | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## list

This request returns the list of organization invitations.
Results can be paginated using the optional `limit` and `offset` query parameters.
You can filter them by providing the 'status' query parameter, that accepts multiple values.
The organization invitations are ordered by descending creation date.
Most recent invitations will be returned first.
Any invitations created as a result of an Organization Domain are not included in the results.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.list(organization_id="org_12345", limit=20, offset=10, status=clerk_backend_api.ListOrganizationInvitationsQueryParamStatus.PENDING)

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                         | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The organization ID.                                                                                                                      | org_12345                                                                                                                                 |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `status`                                                                                                                                  | [Optional[models.ListOrganizationInvitationsQueryParamStatus]](../../models/listorganizationinvitationsqueryparamstatus.md)               | :heavy_minus_sign:                                                                                                                        | Filter organization invitations based on their status                                                                                     | pending                                                                                                                                   |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.ListOrganizationInvitationsResponse](../../models/listorganizationinvitationsresponse.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError64 | 400,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## create_bulk

Creates new organization invitations in bulk and sends out emails to the provided email addresses with a link to accept the invitation and join the organization.
You can specify a different `role` for each invited organization member.
New organization invitations get a "pending" status until they are revoked by an organization administrator or accepted by the invitee.
The request body supports passing an optional `redirect_url` parameter for each invitation.
When the invited user clicks the link to accept the invitation, they will be redirected to the provided URL.
Use this parameter to implement a custom invitation acceptance flow.
You must specify the ID of the user that will send the invitation with the `inviter_user_id` parameter. Each invitation
can have a different inviter user.
Inviter users must be members with administrator privileges in the organization.
Only "admin" members can create organization invitations.
You can optionally provide public and private metadata for each organization invitation. The public metadata are visible
by both the Frontend and the Backend, whereas the private metadata are only visible by the Backend.
When the organization invitation is accepted, the metadata will be transferred to the newly created organization membership.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.create_bulk(organization_id="org_12345", request_body=[
    {
        "email_address": "newmember@example.com",
        "inviter_user_id": "user_67890",
        "role": "admin",
        "public_metadata": {},
        "private_metadata": {},
        "redirect_url": "https://example.com/welcome",
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The organization ID.                                                | org_12345                                                           |
| `request_body`                                                      | List[[models.RequestBody](../../models/requestbody.md)]             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationInvitations](../../models/organizationinvitations.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError65 | 400,403,404,422           | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## ~~list_pending~~

This request returns the list of organization invitations with "pending" status.
These are the organization invitations that can still be used to join the organization, but have not been accepted by the invited user yet.
Results can be paginated using the optional `limit` and `offset` query parameters.
The organization invitations are ordered by descending creation date.
Most recent invitations will be returned first.
Any invitations created as a result of an Organization Domain are not included in the results.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.list_pending(organization_id="org_12345", limit=20, offset=10)

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                         | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The organization ID.                                                                                                                      | org_12345                                                                                                                                 |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.ListPendingOrganizationInvitationsResponse](../../models/listpendingorganizationinvitationsresponse.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError66 | 400,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## get

Use this request to get an existing organization invitation by ID.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.get(organization_id="org_123456789", invitation_id="inv_987654321")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The organization ID.                                                | org_123456789                                                       |
| `invitation_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The organization invitation ID.                                     | inv_987654321                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationInvitation](../../models/organizationinvitation.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError67 | 400,403,404               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## revoke

Use this request to revoke a previously issued organization invitation.
Revoking an organization invitation makes it invalid; the invited user will no longer be able to join the organization with the revoked invitation.
Only organization invitations with "pending" status can be revoked.
The request needs the `requesting_user_id` parameter to specify the user which revokes the invitation.
Only users with "admin" role can revoke invitations.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.organization_invitations.revoke(organization_id="org_123456", invitation_id="inv_123456", requesting_user_id="usr_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `organization_id`                                                                             | *str*                                                                                         | :heavy_check_mark:                                                                            | The organization ID.                                                                          | org_123456                                                                                    |
| `invitation_id`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | The organization invitation ID.                                                               | inv_123456                                                                                    |
| `requesting_user_id`                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The ID of the user that revokes the invitation.<br/>Must be an administrator in the organization. | usr_12345                                                                                     |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.OrganizationInvitation](../../models/organizationinvitation.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError68 | 400,403,404               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |
