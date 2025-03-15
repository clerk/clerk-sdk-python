# SignUps
(*sign_ups*)

## Overview

### Available Operations

* [get](#get) - Retrieve a sign-up by ID
* [update](#update) - Update a sign-up

## get

Retrieve the details of the sign-up with the given ID

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sign_ups.get(id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the sign-up to retrieve                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SignUp](../../models/signup.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Update the sign-up with the given ID

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sign_ups.update(id="signup_1234567890abcdef", external_id="ext_id_7890abcdef123456", custom_action=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                     | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                          | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | The ID of the sign-up to update                                                                                                                                                               | signup_1234567890abcdef                                                                                                                                                                       |
| `external_id`                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                            | The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution.<br/>This will be copied to the resulting user when the sign-up is completed. | ext_id_7890abcdef123456                                                                                                                                                                       |
| `custom_action`                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                            | If true, the sign-up will be marked as a custom action.                                                                                                                                       | false                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                           |                                                                                                                                                                                               |

### Response

**[models.SignUp](../../models/signup.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |