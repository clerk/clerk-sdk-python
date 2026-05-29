# PhoneNumbers

## Overview

### Available Operations

* [create](#create) - Create a phone number
* [get](#get) - Retrieve a phone number
* [delete](#delete) - Delete a phone number
* [update](#update) - Update a phone number
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

## replace_for_user

Replaces all of the user's phone numbers with a single verified, primary phone number.
The new phone number is created with the admin verification strategy and is not reserved
for second factor. Any existing phone numbers are deleted; replacing a phone number that is
reserved for second factor disables the user's MFA.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceUserPhoneNumber" method="put" path="/users/{user_id}/phone_number" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.phone_numbers.replace_for_user(user_id="<id>", phone_number="1-440-484-8878 x689")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `user_id`                                                                        | *str*                                                                            | :heavy_check_mark:                                                               | The ID of the user whose phone number to replace                                 |
| `phone_number`                                                                   | *str*                                                                            | :heavy_check_mark:                                                               | The new phone number. Must adhere to the E.164 standard for phone number format. |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |