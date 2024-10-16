# Invitations
(*invitations*)

## Overview

Invitations allow you to invite someone to sign up to your application, via email.
<https://clerk.com/docs/authentication/invitations>

### Available Operations

* [create_invitation](#create_invitation) - Create an invitation
* [list_invitations](#list_invitations) - List all invitations
* [revoke_invitation](#revoke_invitation) - Revokes an invitation

## create_invitation

Creates a new invitation for the given email address and sends the invitation email.
Keep in mind that you cannot create an invitation if there is already one for the given email address.
Also, trying to create an invitation for an email address that already exists in your application will result to an error.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.invitations.create_invitation(request={
    "email_address": "user@example.com",
    "public_metadata": {},
    "redirect_url": "https://example.com/welcome",
    "notify": True,
    "ignore_existing": True,
    "expires_in_days": 818183,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateInvitationRequestBody](../../models/createinvitationrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.Invitation](../../models/invitation.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## list_invitations

Returns all non-revoked invitations for your application, sorted by creation date

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.invitations.list_invitations(limit=20, offset=10, status=clerk_backend_api.ListInvitationsQueryParamStatus.PENDING)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `status`                                                                                                                                  | [Optional[models.ListInvitationsQueryParamStatus]](../../models/listinvitationsqueryparamstatus.md)                                       | :heavy_minus_sign:                                                                                                                        | Filter invitations based on their status                                                                                                  | pending                                                                                                                                   |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[List[models.Invitation]](../../models/.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## revoke_invitation

Revokes the given invitation.
Revoking an invitation will prevent the user from using the invitation link that was sent to them.
However, it doesn't prevent the user from signing up if they follow the sign up flow.
Only active (i.e. non-revoked) invitations can be revoked.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.invitations.revoke_invitation(invitation_id="inv_123")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `invitation_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the invitation to be revoked                              | inv_123                                                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.InvitationRevoked](../../models/invitationrevoked.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
