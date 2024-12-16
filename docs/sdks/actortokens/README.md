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
from clerk_backend_api import Clerk

with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.actor_tokens.create(user_id="user_1a2b3c", actor={}, expires_in_seconds=3600, session_max_duration_in_seconds=1800)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                 | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                                 | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The ID of the user being impersonated.                                                                                                                                                    | user_1a2b3c                                                                                                                                                                               |
| `actor`                                                                                                                                                                                   | [models.CreateActorTokenActor](../../models/createactortokenactor.md)                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The actor payload. It needs to include a sub property which should contain the ID of the actor.<br/>This whole payload will be also included in the JWT session token.                    | {<br/>"sub": "user_2OEpKhcCN1Lat9NQ0G6puh7q5Rb"<br/>}                                                                                                                                     |
| `expires_in_seconds`                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | Optional parameter to specify the life duration of the actor token in seconds.<br/>By default, the duration is 1 hour.                                                                    | 3600                                                                                                                                                                                      |
| `session_max_duration_in_seconds`                                                                                                                                                         | *Optional[int]*                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                        | The maximum duration that the session which will be created by the generated actor token should last.<br/>By default, the duration of a session created via an actor token, lasts 30 minutes. | 1800                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                       |                                                                                                                                                                                           |

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