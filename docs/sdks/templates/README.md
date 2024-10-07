# Templates
(*templates*)

## Overview

### Available Operations

* [list](#list) - List all templates
* [get](#get) - Retrieve a template
* [upsert](#upsert) - Update a template for a given type and slug
* [revert](#revert) - Revert a template
* [preview](#preview) - Preview changes to a template
* [toggle_delivery](#toggle_delivery) - Toggle the delivery by Clerk for a template of a given type and slug

## list

Returns a list of all templates.
The templates are returned sorted by position.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.list(template_type=clerk_backend_api.TemplateType.EMAIL)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_type`                                                     | [models.TemplateType](../../models/templatetype.md)                 | :heavy_check_mark:                                                  | The type of templates to list (email or SMS)                        | email                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.Template]](../../models/.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError16 | 400, 401, 422             | application/json          |
| models.SDKError           | 4XX, 5XX                  | \*/\*                     |

## get

Returns the details of a template

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.get(template_type=clerk_backend_api.PathParamTemplateType.EMAIL, slug="welcome-email")

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError17 | 400, 401, 404             | application/json          |
| models.SDKError           | 4XX, 5XX                  | \*/\*                     |

## upsert

Updates the existing template of the given type and slug

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.upsert(template_type=clerk_backend_api.UpsertTemplatePathParamTemplateType.SMS, slug="verification-code", name="Verification Code", subject="Your Verification Code", markup="<p>Your code: {{code}}</p>", body="Use this code to verify your email: {{code}}", delivered_by_clerk=True, from_email_name="hello", reply_to_email_name="support")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `template_type`                                                                                                                                                                            | [models.UpsertTemplatePathParamTemplateType](../../models/upserttemplatepathparamtemplatetype.md)                                                                                          | :heavy_check_mark:                                                                                                                                                                         | The type of template to update                                                                                                                                                             | sms                                                                                                                                                                                        |
| `slug`                                                                                                                                                                                     | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | The slug of the template to update                                                                                                                                                         | verification-code                                                                                                                                                                          |
| `name`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The user-friendly name of the template                                                                                                                                                     | Verification Code                                                                                                                                                                          |
| `subject`                                                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | The email subject.<br/>Applicable only to email templates.                                                                                                                                 | Your Verification Code                                                                                                                                                                     |
| `markup`                                                                                                                                                                                   | *OptionalNullable[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                         | The editor markup used to generate the body of the template                                                                                                                                | <p>Your code: {{code}}</p>                                                                                                                                                                 |
| `body`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The template body before variable interpolation                                                                                                                                            | Use this code to verify your email: {{code}}                                                                                                                                               |
| `delivered_by_clerk`                                                                                                                                                                       | *OptionalNullable[bool]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | Whether Clerk should deliver emails or SMS messages based on the current template                                                                                                          | true                                                                                                                                                                                       |
| `from_email_name`                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the From email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | hello                                                                                                                                                                                      |
| `reply_to_email_name`                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                         | The local part of the Reply To email address that will be used for emails.<br/>For example, in the address 'hello@example.com', the local part is 'hello'.<br/>Applicable only to email templates. | support                                                                                                                                                                                    |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ClerkErrorsError18    | 400, 401, 402, 403, 404, 422 | application/json             |
| models.SDKError              | 4XX, 5XX                     | \*/\*                        |

## revert

Reverts an updated template to its default state

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.revert(template_type=clerk_backend_api.RevertTemplatePathParamTemplateType.EMAIL, slug="welcome-email")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                   | [models.RevertTemplatePathParamTemplateType](../../models/reverttemplatepathparamtemplatetype.md) | :heavy_check_mark:                                                                                | The type of template to revert                                                                    | email                                                                                             |
| `slug`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The slug of the template to revert                                                                | welcome-email                                                                                     |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError19 | 400, 401, 402, 404        | application/json          |
| models.SDKError           | 4XX, 5XX                  | \*/\*                     |

## preview

Returns a preview of a template for a given template_type, slug and body

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.preview(template_type="email", slug="welcome-email", subject="Welcome to our service!", body="Hi, thank you for joining our service.", from_email_name="hello", reply_to_email_name="support")

if res is not None:
    # handle response
    pass

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

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError20 | 400, 401, 404, 422        | application/json          |
| models.SDKError           | 4XX, 5XX                  | \*/\*                     |

## toggle_delivery

Toggles the delivery by Clerk for a template of a given type and slug.
If disabled, Clerk will not deliver the resulting email or SMS.
The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.templates.toggle_delivery(template_type=clerk_backend_api.ToggleTemplateDeliveryPathParamTemplateType.EMAIL, slug="welcome-email", delivered_by_clerk=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                                   | [models.ToggleTemplateDeliveryPathParamTemplateType](../../models/toggletemplatedeliverypathparamtemplatetype.md) | :heavy_check_mark:                                                                                                | The type of template to toggle delivery for                                                                       | email                                                                                                             |
| `slug`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The slug of the template for which to toggle delivery                                                             | welcome-email                                                                                                     |
| `delivered_by_clerk`                                                                                              | *OptionalNullable[bool]*                                                                                          | :heavy_minus_sign:                                                                                                | Whether Clerk should deliver emails or SMS messages based on the current template                                 | true                                                                                                              |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError21 | 400, 401, 404             | application/json          |
| models.SDKError           | 4XX, 5XX                  | \*/\*                     |