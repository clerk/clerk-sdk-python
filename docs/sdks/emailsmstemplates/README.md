# EmailSMSTemplates
(*email_sms_templates*)

## Overview

### Available Operations

* [~~get~~](#get) - Retrieve a template :warning: **Deprecated**
* [~~toggle_template_delivery~~](#toggle_template_delivery) - Toggle the delivery by Clerk for a template of a given type and slug :warning: **Deprecated**

## ~~get~~

Returns the details of a template

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_sms_templates.get(template_type=clerk_backend_api.PathParamTemplateType.EMAIL, slug="welcome-email")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `template_type`                                                       | [models.PathParamTemplateType](../../models/pathparamtemplatetype.md) | :heavy_check_mark:                                                    | The type of templates to retrieve (email or SMS)                      | email                                                                 |
| `slug`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | The slug (i.e. machine-friendly name) of the template to retrieve     | welcome-email                                                         |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## ~~toggle_template_delivery~~

Toggles the delivery by Clerk for a template of a given type and slug.
If disabled, Clerk will not deliver the resulting email or SMS.
The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.email_sms_templates.toggle_template_delivery(template_type=clerk_backend_api.ToggleTemplateDeliveryPathParamTemplateType.EMAIL, slug="welcome-email", request_body={
    "delivered_by_clerk": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                                   | [models.ToggleTemplateDeliveryPathParamTemplateType](../../models/toggletemplatedeliverypathparamtemplatetype.md) | :heavy_check_mark:                                                                                                | The type of template to toggle delivery for                                                                       | email                                                                                                             |
| `slug`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The slug of the template for which to toggle delivery                                                             | welcome-email                                                                                                     |
| `request_body`                                                                                                    | [Optional[models.ToggleTemplateDeliveryRequestBody]](../../models/toggletemplatedeliveryrequestbody.md)           | :heavy_minus_sign:                                                                                                | N/A                                                                                                               |                                                                                                                   |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
