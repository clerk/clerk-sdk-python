# JwtTemplates
(*jwt_templates*)

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

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.jwt_templates.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.JWTTemplate]](../../models/.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## create

Create a new JWT template

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.jwt_templates.create(request={
    "name": "Example Template",
    "claims": {},
    "lifetime": 3600,
    "allowed_clock_skew": 5,
    "custom_signing_key": False,
    "signing_algorithm": "RS256",
    "signing_key": "PRIVATE_KEY_PLACEHOLDER",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.CreateJWTTemplateRequestBody](../../models/createjwttemplaterequestbody.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError53 | 400,402,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## get

Retrieve the details of a given JWT template

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.jwt_templates.get(template_id="template_123")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | JWT Template ID                                                     | template_123                                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError54 | 404                       | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## update

Updates an existing JWT template

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.jwt_templates.update(template_id="<id>", name="<value>", claims={}, lifetime=8574.77, allowed_clock_skew=5971.29, custom_signing_key=True, signing_algorithm="<value>", signing_key="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `template_id`                                                                       | *str*                                                                               | :heavy_check_mark:                                                                  | The ID of the JWT template to update                                                |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | JWT template name                                                                   |
| `claims`                                                                            | [Optional[models.UpdateJWTTemplateClaims]](../../models/updatejwttemplateclaims.md) | :heavy_minus_sign:                                                                  | JWT template claims in JSON format                                                  |
| `lifetime`                                                                          | *OptionalNullable[float]*                                                           | :heavy_minus_sign:                                                                  | JWT token lifetime                                                                  |
| `allowed_clock_skew`                                                                | *OptionalNullable[float]*                                                           | :heavy_minus_sign:                                                                  | JWT token allowed clock skew                                                        |
| `custom_signing_key`                                                                | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether a custom signing key/algorithm is also provided for this template           |
| `signing_algorithm`                                                                 | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The custom signing algorithm to use when minting JWTs                               |
| `signing_key`                                                                       | *OptionalNullable[str]*                                                             | :heavy_minus_sign:                                                                  | The custom signing private key to use when minting JWTs                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError55 | 400,402,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## delete

Delete a Template

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.jwt_templates.delete(template_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `template_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | JWT Template ID                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError56 | 403,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |
