# ActorTokens
(*actor_tokens*)

## Overview

### Available Operations

* [create](#create) - Create actor token
* [revoke](#revoke) - Revoke actor token

## create

Create an actor token that can be used to impersonate the given user.
The `actor` parameter needs to include at least a "sub" key whose value is the ID of the actor (impersonating) user.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.actor_tokens.create(request=clerk_backend_api.CreateActorTokenRequestBody(
        user_id="user_1a2b3c",
        actor=clerk_backend_api.CreateActorTokenActor(
            sub="user_2OEpKhcCN1Lat9NQ0G6puh7q5Rb",
            **{
                "sub": "user_2OEpKhcCN1Lat9NQ0G6puh7q5Rb",
            },
        ),
    ))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateActorTokenRequestBody](../../models/createactortokenrequestbody.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.ActorToken](../../models/actortoken.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## revoke

Revokes a pending actor token.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.actor_tokens.revoke(actor_token_id="act_tok_abcdefghijk")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `actor_token_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The ID of the actor token to be revoked.                            | act_tok_abcdefghijk                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ActorToken](../../models/actortoken.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |