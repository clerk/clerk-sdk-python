# Templates
(*templates*)

## Overview

### Available Operations

* [~~preview~~](#preview) - Preview changes to a template :warning: **Deprecated**

## ~~preview~~

Returns a preview of a template for a given template_type, slug and body

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.templates.preview(template_type="email", slug="welcome-email", subject="Welcome to our service!", body="Hi, thank you for joining our service.", from_email_name="hello", reply_to_email_name="support")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `template_type`                                                                                                                                                                            | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The type of template to preview                                                                                                                                                            | email                                                                                                                                                                                      |
| `slug`                                                                                                                                                                                     | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The slug of the template to preview                                                                                                                                                        | welcome-email                                                                                                                                                                              |
| `subject`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | The email subject.<br/>Applicable only to email templates.                                                                                                                                 | Welcome to our service!                                                                                                                                                                    |
| `body`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The template body before variable interpolation                                                                                                                                            | Hi, thank you for joining our service.                                                                                                                                                     |
| `from_email_name`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the From email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | hello                                                                                                                                                                                      |
| `reply_to_email_name`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the Reply To email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | support                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.PreviewTemplateResponseBody](../../models/previewtemplateresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |