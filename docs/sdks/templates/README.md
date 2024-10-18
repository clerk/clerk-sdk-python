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

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.templates.preview(template_type="email", slug="welcome-email", request_body={
    "subject": "Welcome to our service!",
    "body": "Hi, thank you for joining our service.",
    "from_email_name": "hello",
    "reply_to_email_name": "support",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `template_type`                                                                           | *str*                                                                                     | :heavy_check_mark:                                                                        | The type of template to preview                                                           | email                                                                                     |
| `slug`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | The slug of the template to preview                                                       | welcome-email                                                                             |
| `request_body`                                                                            | [Optional[models.PreviewTemplateRequestBody]](../../models/previewtemplaterequestbody.md) | :heavy_minus_sign:                                                                        | Required parameters                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.PreviewTemplateResponseBody](../../models/previewtemplateresponsebody.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
