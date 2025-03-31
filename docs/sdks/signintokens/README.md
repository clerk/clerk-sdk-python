# SignInTokens
(*sign_in_tokens*)

## Overview

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


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sign_in_tokens.create(request={
        "user_id": "user_12345",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateSignInTokenRequestBody](../../models/createsignintokenrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.SignInToken](../../models/signintoken.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## revoke

Revokes a pending sign-in token

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sign_in_tokens.revoke(sign_in_token_id="tok_test_1234567890")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `sign_in_token_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the sign-in token to be revoked                           | tok_test_1234567890                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SignInToken](../../models/signintoken.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |