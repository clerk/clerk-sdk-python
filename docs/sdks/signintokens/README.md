# SignInTokens
(*sign_in_tokens*)

## Overview

Sign-in tokens are JWTs that can be used to sign in to an application without specifying any credentials.
A sign-in token can be used at most once and they can be consumed from the Frontend API using the `ticket` strategy.

### Available Operations

* [create_sign_in_token](#create_sign_in_token) - Create sign-in token
* [revoke_sign_in_token](#revoke_sign_in_token) - Revoke the given sign-in token

## create_sign_in_token

Creates a new sign-in token and associates it with the given user.
By default, sign-in tokens expire in 30 days.
You can optionally supply a different duration in seconds using the `expires_in_seconds` property.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sign_in_tokens.create_sign_in_token(request={
    "user_id": "user_12345",
    "expires_in_seconds": 2592000,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateSignInTokenRequestBody](../../models/createsignintokenrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.SignInToken](../../models/signintoken.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## revoke_sign_in_token

Revokes a pending sign-in token

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sign_in_tokens.revoke_sign_in_token(sign_in_token_id="tok_test_1234567890")

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
