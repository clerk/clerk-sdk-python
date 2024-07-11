# JwtTemplates
(*jwt_templates*)

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
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
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
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.jwt_templates.create(name="Example Template", claims={}, lifetime=3600, allowed_clock_skew=5, custom_signing_key=False, signing_algorithm="RS256", signing_key="PRIVATE_KEY_PLACEHOLDER")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `name`                                                                              | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | JWT template name                                                                   | Example Template                                                                    |
| `claims`                                                                            | [Optional[models.CreateJWTTemplateClaims]](../../models/createjwttemplateclaims.md) | :heavy_minus_sign:                                                                  | JWT template claims in JSON format                                                  | {}                                                                                  |
| `lifetime`                                                                          | *Optional[Nullable[float]]*                                                         | :heavy_minus_sign:                                                                  | JWT token lifetime                                                                  | 3600                                                                                |
| `allowed_clock_skew`                                                                | *Optional[Nullable[float]]*                                                         | :heavy_minus_sign:                                                                  | JWT token allowed clock skew                                                        | 5                                                                                   |
| `custom_signing_key`                                                                | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether a custom signing key/algorithm is also provided for this template           | false                                                                               |
| `signing_algorithm`                                                                 | *Optional[Nullable[str]]*                                                           | :heavy_minus_sign:                                                                  | The custom signing algorithm to use when minting JWTs                               | RS256                                                                               |
| `signing_key`                                                                       | *Optional[Nullable[str]]*                                                           | :heavy_minus_sign:                                                                  | The custom signing private key to use when minting JWTs                             | PRIVATE_KEY_PLACEHOLDER                                                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |


### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,402,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## get

Retrieve the details of a given JWT template

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
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

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## update

Updates an existing JWT template

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.jwt_templates.update(template_id="<value>", name="<value>", claims={}, lifetime=8574.78, allowed_clock_skew=245.55, custom_signing_key=False, signing_algorithm="<value>", signing_key="<value>")

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
| `lifetime`                                                                          | *Optional[Nullable[float]]*                                                         | :heavy_minus_sign:                                                                  | JWT token lifetime                                                                  |
| `allowed_clock_skew`                                                                | *Optional[Nullable[float]]*                                                         | :heavy_minus_sign:                                                                  | JWT token allowed clock skew                                                        |
| `custom_signing_key`                                                                | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether a custom signing key/algorithm is also provided for this template           |
| `signing_algorithm`                                                                 | *Optional[Nullable[str]]*                                                           | :heavy_minus_sign:                                                                  | The custom signing algorithm to use when minting JWTs                               |
| `signing_key`                                                                       | *Optional[Nullable[str]]*                                                           | :heavy_minus_sign:                                                                  | The custom signing private key to use when minting JWTs                             |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |


### Response

**[models.JWTTemplate](../../models/jwttemplate.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,402,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete

Delete a Template

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.jwt_templates.delete(template_id="<value>")

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

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
