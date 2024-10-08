# SignUps
(*sign_ups*)

## Overview

### Available Operations

* [update](#update) - Update a sign-up

## update

Update the sign-up with the given ID

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sign_ups.update(id="signup_1234567890abcdef", request_body={
    "custom_action": False,
    "external_id": "ext_id_7890abcdef123456",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the sign-up to update                                                     | signup_1234567890abcdef                                                             |
| `request_body`                                                                      | [Optional[models.UpdateSignUpRequestBody]](../../models/updatesignuprequestbody.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |                                                                                     |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[models.SignUp](../../models/signup.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
