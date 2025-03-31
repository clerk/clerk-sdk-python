# EmailSMSTemplates
(*email_sms_templates*)

## Overview

### Available Operations

* [~~list~~](#list) - List all templates :warning: **Deprecated**
* [~~get~~](#get) - Retrieve a template :warning: **Deprecated**
* [~~revert~~](#revert) - Revert a template :warning: **Deprecated**
* [~~toggle_template_delivery~~](#toggle_template_delivery) - Toggle the delivery by Clerk for a template of a given type and slug :warning: **Deprecated**

## ~~list~~

Returns a list of all templates.
The templates are returned sorted by position.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_sms_templates.list(template_type=clerk_backend_api.TemplateType.EMAIL, paginated=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                                                           | [models.TemplateType](../../models/templatetype.md)                                                                                       | :heavy_check_mark:                                                                                                                        | The type of templates to list (email or SMS)                                                                                              | email                                                                                                                                     |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[List[models.Template]](../../models/.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## ~~get~~

Returns the details of a template

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_sms_templates.get(template_type=clerk_backend_api.PathParamTemplateType.EMAIL, slug="welcome-email")

    assert res is not None

    # Handle response
    print(res)

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## ~~revert~~

Reverts an updated template to its default state

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_sms_templates.revert(template_type=clerk_backend_api.RevertTemplatePathParamTemplateType.EMAIL, slug="welcome-email")

    assert res is not None

    # Handle response
    print(res)

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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 402, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## ~~toggle_template_delivery~~

Toggles the delivery by Clerk for a template of a given type and slug.
If disabled, Clerk will not deliver the resulting email or SMS.
The app developer will need to listen to the `email.created` or `sms.created` webhooks in order to handle delivery themselves.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_sms_templates.toggle_template_delivery(template_type=clerk_backend_api.ToggleTemplateDeliveryPathParamTemplateType.EMAIL, slug="welcome-email", delivered_by_clerk=True)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       | Example                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `template_type`                                                                                                   | [models.ToggleTemplateDeliveryPathParamTemplateType](../../models/toggletemplatedeliverypathparamtemplatetype.md) | :heavy_check_mark:                                                                                                | The type of template to toggle delivery for                                                                       | email                                                                                                             |
| `slug`                                                                                                            | *str*                                                                                                             | :heavy_check_mark:                                                                                                | The slug of the template for which to toggle delivery                                                             | welcome-email                                                                                                     |
| `delivered_by_clerk`                                                                                              | *Optional[bool]*                                                                                                  | :heavy_minus_sign:                                                                                                | Whether Clerk should deliver emails or SMS messages based on the current template                                 | true                                                                                                              |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |                                                                                                                   |

### Response

**[models.Template](../../models/template.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |