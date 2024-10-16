# EmailAddresses
(*email_addresses*)

## Overview

A user can be associated with one or more email addresses, which allows them to be contacted via email.
<https://clerk.com/docs/reference/clerkjs/emailaddress>

### Available Operations

* [create_email_address](#create_email_address) - Create an email address
* [get_email_address](#get_email_address) - Retrieve an email address
* [delete_email_address](#delete_email_address) - Delete an email address
* [update_email_address](#update_email_address) - Update an email address

## create_email_address

Create a new email address

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_addresses.create_email_address(request={
    "user_id": "user_12345",
    "email_address": "example@clerk.com",
    "verified": False,
    "primary": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.CreateEmailAddressRequestBody](../../models/createemailaddressrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Object        | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.ClerkErrors  | 400,401,403,404,422 | application/json    |
| models.SDKError     | 4xx-5xx             | */*                 |


## get_email_address

Returns the details of an email address.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_addresses.get_email_address(email_address_id="email_address_id_example")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to retrieve                             | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## delete_email_address

Delete the email address with the given ID

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_addresses.delete_email_address(email_address_id="email_address_id_example")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to delete                               | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## update_email_address

Updates an email address.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_addresses.update_email_address(email_address_id="email_address_id_example", request_body={
    "verified": False,
    "primary": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `email_address_id`                                                                              | *str*                                                                                           | :heavy_check_mark:                                                                              | The ID of the email address to update                                                           | email_address_id_example                                                                        |
| `request_body`                                                                                  | [Optional[models.UpdateEmailAddressRequestBody]](../../models/updateemailaddressrequestbody.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |                                                                                                 |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,403,404    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
