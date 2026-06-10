# PhoneNumbers

## Overview

### Available Operations

* [create](#create) - Create a phone number
* [get](#get) - Retrieve a phone number
* [delete](#delete) - Delete a phone number
* [update](#update) - Update a phone number
* [prepare_verification](#prepare_verification) - Send a verification code to a phone number
* [attempt_verification](#attempt_verification) - Verify a code sent to a phone number
* [replace_for_user](#replace_for_user) - Replace a user's phone number

## create

Create a new phone number

### Example Usage

<!-- UsageSnippet language="python" operationID="CreatePhoneNumber" method="post" path="/phone_numbers" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.create(request={
        "user_id": "usr_12345",
        "phone_number": "+11234567890",
        "verified": True,
        "primary": False,
        "reserved_for_second_factor": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreatePhoneNumberRequestBody](../../models/createphonenumberrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## get

Returns the details of a phone number

### Example Usage

<!-- UsageSnippet language="python" operationID="GetPhoneNumber" method="get" path="/phone_numbers/{phone_number_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.get(phone_number_id="phone_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the phone number to retrieve                              | phone_12345                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Delete the phone number with the given ID

### Example Usage

<!-- UsageSnippet language="python" operationID="DeletePhoneNumber" method="delete" path="/phone_numbers/{phone_number_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.delete(phone_number_id="phone_12345")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the phone number to delete                                | phone_12345                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates a phone number

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdatePhoneNumber" method="patch" path="/phone_numbers/{phone_number_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.update(phone_number_id="phone_12345", verified=False, primary=True, reserved_for_second_factor=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                            | Type                                                                                                                                                                                                                 | Required                                                                                                                                                                                                             | Description                                                                                                                                                                                                          | Example                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `phone_number_id`                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                                                   | The ID of the phone number to update                                                                                                                                                                                 | phone_12345                                                                                                                                                                                                          |
| `verified`                                                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                   | The phone number will be marked as verified.                                                                                                                                                                         | false                                                                                                                                                                                                                |
| `primary`                                                                                                                                                                                                            | *OptionalNullable[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                   | Set this phone number as the primary phone number for the user.                                                                                                                                                      | true                                                                                                                                                                                                                 |
| `reserved_for_second_factor`                                                                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                   | Set this phone number as reserved for multi-factor authentication.<br/>The phone number must also be verified.<br/>If there are no other reserved second factors, the phone number will be set as the default second factor. | true                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                  |                                                                                                                                                                                                                      |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## prepare_verification

Sends a one-time code to the given phone number so that a backend can
verify the user controls it (for example, in a custom, backend-driven
sign-in flow). The code is tracked on its own verification; confirm it
with attempt_verification.

### Example Usage

<!-- UsageSnippet language="python" operationID="PreparePhoneNumberVerification" method="post" path="/phone_numbers/{phone_number_id}/prepare_verification" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.prepare_verification(phone_number_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the phone number to send the verification code to         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerificationResponse](../../models/verificationresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 429 | application/json        |
| models.ClerkErrors      | 500                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## attempt_verification

Checks a one-time code against the verification identified by
verification_id, and returns the verification with its updated status
(`verified`, `unverified`, `expired`, or `failed`) and attempt count, so a
backend driving its own frontend can react on every attempt — an incorrect
or expired code is reported through the status, not as an error. Resubmitting
a verification whose code was already accepted is rejected with a
`verification_already_verified` error. If the code
is correct and the phone number is not already verified, it is also marked
as verified as a side effect (just as it would be in a frontend verification
flow); an already verified phone number is left unchanged. It never creates
a session; to sign the user in afterwards, mint a sign-in token.

### Example Usage

<!-- UsageSnippet language="python" operationID="AttemptPhoneNumberVerification" method="post" path="/phone_numbers/{phone_number_id}/attempt_verification" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.attempt_verification(phone_number_id="<id>", verification_id="<id>", code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `phone_number_id`                                                                 | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the phone number whose code is being verified                           |
| `verification_id`                                                                 | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the verification to check, such as one returned by prepare_verification |
| `code`                                                                            | *str*                                                                             | :heavy_check_mark:                                                                | The verification code that was sent to the phone number                           |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.VerificationResponse](../../models/verificationresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## replace_for_user

Replaces all of the user's phone numbers with a single primary phone number.
By default the new phone number is created verified, with the admin verification strategy.
When `identification_status` is `reserved` it is created reserved instead: unverified but usable
for sign-in and locked so no other user can claim it. The new phone number is never reserved for
second factor. Any existing phone numbers are deleted; replacing a phone number that is reserved
for second factor disables the user's MFA.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceUserPhoneNumber" method="put" path="/users/{user_id}/phone_number" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.replace_for_user(user_id="<id>", phone_number="1-440-484-8878 x689", identification_status=clerk_backend_api.ReplaceUserPhoneNumberIdentificationStatus.VERIFIED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                | Type                                                                                                                                                                                     | Required                                                                                                                                                                                 | Description                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                                | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The ID of the user whose phone number to replace                                                                                                                                         |
| `phone_number`                                                                                                                                                                           | *str*                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                       | The new phone number. Must adhere to the E.164 standard for phone number format.                                                                                                         |
| `identification_status`                                                                                                                                                                  | [Optional[models.ReplaceUserPhoneNumberIdentificationStatus]](../../models/replaceuserphonenumberidentificationstatus.md)                                                                | :heavy_minus_sign:                                                                                                                                                                       | Controls the status of the replacement phone number. Defaults to `verified`. Set to<br/>`reserved` to create it reserved (unverified but usable for sign-in and locked)<br/>instead of verified. |
| `retries`                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                      |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |