# EmailAndSmsTemplates
(*email_and_sms_templates*)

## Overview

### Available Operations

* [~~upsert~~](#upsert) - Update a template for a given type and slug :warning: **Deprecated**

## ~~upsert~~

Updates the existing template of the given type and slug

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_and_sms_templates.upsert(template_type=clerk_backend_api.UpsertTemplatePathParamTemplateType.SMS, slug="verification-code", request_body={
    "name": "Verification Code",
    "subject": "Your Verification Code",
    "markup": "<p>Your code: {{code}}</p>",
    "body": "Use this code to verify your email: {{code}}",
    "delivered_by_clerk": True,
    "from_email_name": "hello",
    "reply_to_email_name": "support",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                   | [models.UpsertTemplatePathParamTemplateType](../../models/upserttemplatepathparamtemplatetype.md) | :heavy_check_mark:                                                                                | The type of template to update                                                                    | sms                                                                                               |
| `slug`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The slug of the template to update                                                                | verification-code                                                                                 |
| `request_body`                                                                                    | [Optional[models.UpsertTemplateRequestBody]](../../models/upserttemplaterequestbody.md)           | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Object            | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400,401,402,403,404,422 | application/json        |
| models.SDKError         | 4xx-5xx                 | */*                     |
