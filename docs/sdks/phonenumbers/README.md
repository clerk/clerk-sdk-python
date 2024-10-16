# PhoneNumbers
(*phone_numbers*)

## Overview

A user can be associated with one or more phone numbers, which allows them to be contacted via SMS.
<https://clerk.com/docs/reference/clerkjs/phonenumber>

### Available Operations

* [create_phone_number](#create_phone_number) - Create a phone number
* [get_phone_number](#get_phone_number) - Retrieve a phone number
* [delete_phone_number](#delete_phone_number) - Delete a phone number
* [update_phone_number](#update_phone_number) - Update a phone number

## create_phone_number

Create a new phone number

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.phone_numbers.create_phone_number(request={
    "user_id": "usr_12345",
    "phone_number": "+11234567890",
    "verified": True,
    "primary": False,
    "reserved_for_second_factor": False,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreatePhoneNumberRequestBody](../../models/createphonenumberrequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ClerkErrors  | 400,401,403,404,422 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |


## get_phone_number

Returns the details of a phone number

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.phone_numbers.get_phone_number(phone_number_id="phone_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the phone number to retrieve                              | phone_12345                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## delete_phone_number

Delete the phone number with the given ID

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.phone_numbers.delete_phone_number(phone_number_id="phone_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `phone_number_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the phone number to delete                                | phone_12345                                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## update_phone_number

Updates a phone number

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.phone_numbers.update_phone_number(phone_number_id="phone_12345", request_body={
    "verified": False,
    "primary": True,
    "reserved_for_second_factor": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   | Example                                                                                       |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `phone_number_id`                                                                             | *str*                                                                                         | :heavy_check_mark:                                                                            | The ID of the phone number to update                                                          | phone_12345                                                                                   |
| `request_body`                                                                                | [Optional[models.UpdatePhoneNumberRequestBody]](../../models/updatephonenumberrequestbody.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |                                                                                               |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |                                                                                               |

### Response

**[models.PhoneNumber](../../models/phonenumber.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
