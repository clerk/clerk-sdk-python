# ActorTokens
(*actor_tokens*)

## Overview

Allow your users to sign in on behalf of other users.
<https://clerk.com/docs/authentication/user-impersonation#actor-tokens>

### Available Operations

* [create_actor_token](#create_actor_token) - Create actor token
* [revoke_actor_token](#revoke_actor_token) - Revoke actor token

## create_actor_token

Create an actor token that can be used to impersonate the given user.
The `actor` parameter needs to include at least a "sub" key whose value is the ID of the actor (impersonating) user.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.actor_tokens.create_actor_token(request={
    "user_id": "user_1a2b3c",
    "actor": {},
    "expires_in_seconds": 3600,
    "session_max_duration_in_seconds": 1800,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateActorTokenRequestBody](../../models/createactortokenrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ActorToken](../../models/actortoken.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,402,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## revoke_actor_token

Revokes a pending actor token.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.actor_tokens.revoke_actor_token(actor_token_id="act_tok_abcdefghijk")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `actor_token_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the actor token to be revoked.                            | act_tok_abcdefghijk                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ActorToken](../../models/actortoken.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
