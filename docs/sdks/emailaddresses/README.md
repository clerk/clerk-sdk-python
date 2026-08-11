# EmailAddresses

## Overview

### Available Operations

* [create](#create) - Create an email address
* [get](#get) - Retrieve an email address
* [delete](#delete) - Delete an email address
* [update](#update) - Update an email address
* [prepare_verification](#prepare_verification) - Send a verification code to an email address
* [attempt_verification](#attempt_verification) - Verify a code sent to an email address
* [replace_for_user](#replace_for_user) - Replace a user's email address

## create

Create a new email address

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateEmailAddress" method="post" path="/email_addresses" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.create(request={
        "user_id": "user_12345",
        "email_address": "example@clerk.com",
        "verified": False,
        "primary": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.CreateEmailAddressRequestBody](../../models/createemailaddressrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ClerkErrors           | 400, 401, 403, 404, 409, 422 | application/json             |
| models.SDKError              | 4XX, 5XX                     | \*/\*                        |

## get

Returns the details of an email address.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetEmailAddress" method="get" path="/email_addresses/{email_address_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.get(email_address_id="email_address_id_example")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to retrieve                             | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Delete the email address with the given ID

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteEmailAddress" method="delete" path="/email_addresses/{email_address_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.delete(email_address_id="email_address_id_example")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to delete                               | email_address_id_example                                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 409 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## update

Updates an email address.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateEmailAddress" method="patch" path="/email_addresses/{email_address_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.update(email_address_id="email_address_id_example", verified=False, primary=True, notify_primary_email_address_changed=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                           | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         | Example                                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email_address_id`                                                                                                                                                                  | *str*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | The ID of the email address to update                                                                                                                                               | email_address_id_example                                                                                                                                                            |
| `verified`                                                                                                                                                                          | *OptionalNullable[bool]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                  | The email address will be marked as verified.                                                                                                                                       | false                                                                                                                                                                               |
| `primary`                                                                                                                                                                           | *OptionalNullable[bool]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                  | Set this email address as the primary email address for the user.                                                                                                                   | true                                                                                                                                                                                |
| `notify_primary_email_address_changed`                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                  | If set to `true` and this update makes the email address the user's new primary,<br/>the previous primary email address is notified of the change.<br/>By default, no notification is sent. |                                                                                                                                                                                     |
| `retries`                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                 |                                                                                                                                                                                     |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 409 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## prepare_verification

Sends a one-time code to the given email address so that a backend can
verify the user controls it (for example, in a custom, backend-driven
sign-in flow). The code is tracked on its own verification; confirm it
with attempt_verification.

### Example Usage

<!-- UsageSnippet language="python" operationID="PrepareEmailAddressVerification" method="post" path="/email_addresses/{email_address_id}/prepare_verification" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.prepare_verification(email_address_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `email_address_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the email address to send the verification code to        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.VerificationResponse](../../models/verificationresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## attempt_verification

Checks a one-time code against the verification identified by
verification_id, and returns the verification with its updated status
(`verified`, `unverified`, `expired`, or `failed`) and attempt count, so a
backend driving its own frontend can react on every attempt — an incorrect
or expired code is reported through the status, not as an error. Resubmitting
a verification whose code was already accepted is rejected with a
`verification_already_verified` error. If the code
is correct and the email address is not already verified, it is also marked
as verified as a side effect (just as it would be in a frontend verification
flow); an already verified email address is left unchanged. It never creates
a session; to sign the user in afterwards, mint a sign-in token.

### Example Usage

<!-- UsageSnippet language="python" operationID="AttemptEmailAddressVerification" method="post" path="/email_addresses/{email_address_id}/attempt_verification" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.attempt_verification(email_address_id="<id>", verification_id="<id>", code="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `email_address_id`                                                                | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the email address whose code is being verified                          |
| `verification_id`                                                                 | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the verification to check, such as one returned by prepare_verification |
| `code`                                                                            | *str*                                                                             | :heavy_check_mark:                                                                | The verification code that was sent to the email address                          |
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

Replaces all of the user's email addresses with a single primary email address.
By default the new email address is created verified, with the admin verification strategy.
When `identification_status` is `reserved` it is created reserved instead: unverified but usable
for sign-in and locked so no other user can claim it. When it is `unverified` the address is
neither usable for sign-in nor locked. Any existing email addresses are deleted.
If an existing email address is linked to a connected account, the request is rejected; remove
the connected account first.

**Warning:** `identification_status: unverified` can lock the user out of their account. An
unverified email address cannot be used to sign in, so if the user has no other verified or
reserved identifier, deleting their existing email addresses leaves them unable to
authenticate — and unable to verify the new address, since that requires signing in. Recovery
then requires another admin API call.

### Example Usage

<!-- UsageSnippet language="python" operationID="ReplaceUserEmailAddress" method="put" path="/users/{user_id}/email_address" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.replace_for_user(user_id="<id>", email_address="Ines83@gmail.com", identification_status=clerk_backend_api.IdentificationStatus.VERIFIED, notify_primary_email_address_changed=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The ID of the user whose email address to replace                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `email_address`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The new email address. Must adhere to the RFC 5322 specification for email address format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `identification_status`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Optional[models.IdentificationStatus]](../../models/identificationstatus.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Controls the status of the replacement email address. Defaults to `verified`. Set to<br/>`reserved` to create it reserved (unverified but usable for sign-in and locked so no<br/>other user can claim it), or to `unverified` to create it neither usable for sign-in<br/>nor locked.<br/><br/>**Warning:** `unverified` can lock the user out of their account. An unverified email<br/>address cannot be used to sign in, so if the user has no other verified or reserved<br/>identifier, they will be unable to authenticate and unable to verify this address.<br/>Prefer `reserved` unless you specifically need the address left unclaimed — for<br/>example so that another user can also hold it until one of them verifies it. |
| `notify_primary_email_address_changed`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | If set to `true`, the user's previous primary email address is notified that the<br/>primary email address has changed. No notification is sent when the replacement<br/>is the user's current primary email address. By default, no notification is sent.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[models.EmailAddress](../../models/emailaddress.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |