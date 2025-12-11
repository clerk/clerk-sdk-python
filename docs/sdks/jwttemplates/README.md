# JwtTemplates

## Overview

### Available Operations

* [list](#list) - List all templates
* [create](#create) - Create a JWT template
* [get](#get) - Retrieve a template
* [update](#update) - Update a JWT template
* [delete](#delete) - Delete a Template

## list

List all templates

### Example Usage

<!-- UsageSnippet language="python" operationID="ListJWTTemplates" method="get" path="/jwt_templates" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.jwt_templates.list(paginated=True, limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[List[models.JWTTemplate]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create

Create a new JWT template

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateJWTTemplate" method="post" path="/jwt_templates" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.jwt_templates.create(request={
        "name": "Example Template",
        "claims": {},
        "lifetime": 3600,
        "allowed_clock_skew": 5,
        "custom_signing_key": False,
        "signing_algorithm": "RS256",
        "signing_key": "PRIVATE_KEY_PLACEHOLDER",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateJWTTemplateRequestBody](../../models/createjwttemplaterequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Retrieve the details of a given JWT template

### Example Usage

<!-- UsageSnippet language="python" operationID="GetJWTTemplate" method="get" path="/jwt_templates/{template_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.jwt_templates.get(template_id="template_123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | JWT Template ID                                                     | template_123                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates an existing JWT template

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateJWTTemplate" method="patch" path="/jwt_templates/{template_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.jwt_templates.update(template_id="<id>", name="<value>", claims={}, lifetime=62.24, allowed_clock_skew=258.27, custom_signing_key=False, signing_algorithm="<value>", signing_key=None)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `template_id`                                                                                        | *str*                                                                                                | :heavy_check_mark:                                                                                   | The ID of the JWT template to update                                                                 |
| `name`                                                                                               | *str*                                                                                                | :heavy_check_mark:                                                                                   | JWT template name                                                                                    |
| `claims`                                                                                             | [models.UpdateJWTTemplateClaims](../../models/updatejwttemplateclaims.md)                            | :heavy_check_mark:                                                                                   | JWT template claims in JSON format                                                                   |
| `lifetime`                                                                                           | *OptionalNullable[int]*                                                                              | :heavy_minus_sign:                                                                                   | JWT lifetime                                                                                         |
| `allowed_clock_skew`                                                                                 | *OptionalNullable[int]*                                                                              | :heavy_minus_sign:                                                                                   | JWT allowed clock skew                                                                               |
| `custom_signing_key`                                                                                 | *Optional[bool]*                                                                                     | :heavy_minus_sign:                                                                                   | Whether a custom signing key/algorithm is also provided for this template                            |
| `signing_algorithm`                                                                                  | *OptionalNullable[str]*                                                                              | :heavy_minus_sign:                                                                                   | The custom signing algorithm to use when minting JWTs. Required if `custom_signing_key` is `true`.   |
| `signing_key`                                                                                        | *OptionalNullable[str]*                                                                              | :heavy_minus_sign:                                                                                   | The custom signing private key to use when minting JWTs. Required if `custom_signing_key` is `true`. |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Delete a Template

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteJWTTemplate" method="delete" path="/jwt_templates/{template_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.jwt_templates.delete(template_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | JWT Template ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |