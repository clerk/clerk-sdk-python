# OAuthApplicationsSDK
(*o_auth_applications*)

## Overview

### Available Operations

* [list](#list) - Get a list of OAuth applications for an instance
* [create](#create) - Create an OAuth application
* [get](#get) - Retrieve an OAuth application by ID
* [update](#update) - Update an OAuth application
* [delete](#delete) - Delete an OAuth application
* [rotate_secret](#rotate_secret) - Rotate the client secret of the given OAuth application

## list

This request returns the list of OAuth applications for an instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The OAuth applications are ordered by descending creation date.
Most recent OAuth applications will be returned first.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.list(limit=20, offset=10)

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.ListOAuthApplicationsResponse](../../models/listoauthapplicationsresponse.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError79 | 400,403,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## create

Creates a new OAuth application with the given name and callback URL for an instance.
The callback URL must be a valid url.
All URL schemes are allowed such as `http://`, `https://`, `myapp://`, etc...

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.create(request={
    "name": "Example App",
    "callback_url": "https://example.com/oauth/callback",
    "scopes": "profile email public_metadata",
    "public": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.CreateOAuthApplicationRequestBody](../../models/createoauthapplicationrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.OAuthApplicationWithSecret](../../models/oauthapplicationwithsecret.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError80 | 400,403,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## get

Fetches the OAuth application whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.get(oauth_application_id="oauth_app_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_application_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth application                                     | oauth_app_12345                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OAuthApplication](../../models/oauthapplication.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError81 | 403,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## update

Updates an existing OAuth application

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.update(oauth_application_id="oauth_app_67890", name="Updated OAuth App Name", callback_url="https://example.com/oauth/callback", scopes="profile email public_metadata private_metadata")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `oauth_application_id`                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                     | The ID of the OAuth application to update                                                                                                                                                                                                                              | oauth_app_67890                                                                                                                                                                                                                                                        |
| `name`                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                     | The new name of the OAuth application                                                                                                                                                                                                                                  | Updated OAuth App Name                                                                                                                                                                                                                                                 |
| `callback_url`                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                     | The new callback URL of the OAuth application                                                                                                                                                                                                                          | https://example.com/oauth/callback                                                                                                                                                                                                                                     |
| `scopes`                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                     | Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces. | profile email public_metadata private_metadata                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                        |

### Response

**[models.OAuthApplication](../../models/oauthapplication.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError82 | 403,404,422               | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## delete

Deletes the given OAuth application.
This is not reversible.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.delete(oauth_application_id="oauth_app_09876")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_application_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth application to delete                           | oauth_app_09876                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError83 | 403,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |


## rotate_secret

Rotates the OAuth application's client secret.
When the client secret is rotated, make sure to update it in authorized OAuth clients.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = s.o_auth_applications.rotate_secret(oauth_application_id="oauth_application_12345")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `oauth_application_id`                                                | *str*                                                                 | :heavy_check_mark:                                                    | The ID of the OAuth application for which to rotate the client secret | oauth_application_12345                                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.OAuthApplicationWithSecret](../../models/oauthapplicationwithsecret.md)**

### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ClerkErrorsError84 | 403,404                   | application/json          |
| models.SDKError           | 4xx-5xx                   | */*                       |
