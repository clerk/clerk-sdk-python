# SignInTokens
(*sign_in_tokens*)

### Available Operations

* [create](#create) - Create sign-in token
* [revoke](#revoke) - Revoke the given sign-in token

## create

Creates a new sign-in token and associates it with the given user.
By default, sign-in tokens expire in 30 days.
You can optionally supply a different duration in seconds using the `expires_in_seconds` property.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.sign_in_tokens.create(user_id="user_12345", expires_in_seconds=2592000)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           | Example                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                             | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | The ID of the user that can use the newly created sign in token                                                       | user_12345                                                                                                            |
| `expires_in_seconds`                                                                                                  | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | Optional parameter to specify the life duration of the sign in token in seconds.<br/>By default, the duration is 30 days. | 2592000                                                                                                               |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |                                                                                                                       |


### Response

**[models.SignInToken](../../models/signintoken.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## revoke

Revokes a pending sign-in token

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.sign_in_tokens.revoke(sign_in_token_id="tok_test_1234567890")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sign_in_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the sign-in token to be revoked                           | tok_test_1234567890                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |


### Response

**[models.SignInToken](../../models/signintoken.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
