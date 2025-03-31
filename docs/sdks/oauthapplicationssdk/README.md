# OauthApplicationsSDK
(*oauth_applications*)

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


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.list()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.OAuthApplications](../../models/oauthapplications.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new OAuth application with the given name and callback URL for an instance.
The callback URL must be a valid url.
All URL schemes are allowed such as `http://`, `https://`, `myapp://`, etc...

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.create(request={
        "name": "Example App",
        "redirect_uris": [
            "<value>",
            "<value>",
        ],
        "callback_url": "https://example.com/oauth/callback",
        "public": True,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.CreateOAuthApplicationRequestBody](../../models/createoauthapplicationrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.OAuthApplicationWithSecret](../../models/oauthapplicationwithsecret.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Fetches the OAuth application whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.get(oauth_application_id="oauth_app_12345")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_application_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth application                                     | oauth_app_12345                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OAuthApplication](../../models/oauthapplication.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates an existing OAuth application

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.update(oauth_application_id="oauth_app_67890", name="Updated OAuth App Name", redirect_uris=[
        "<value>",
        "<value>",
        "<value>",
    ], callback_url="https://example.com/oauth/callback", public=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `oauth_application_id`                                                                                                                                                                                                                                                 | *str*                                                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                                                     | The ID of the OAuth application to update                                                                                                                                                                                                                              | oauth_app_67890                                                                                                                                                                                                                                                        |
| `name`                                                                                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                     | The new name of the OAuth application.<br/>Max length: 256                                                                                                                                                                                                             | Updated OAuth App Name                                                                                                                                                                                                                                                 |
| `redirect_uris`                                                                                                                                                                                                                                                        | List[*str*]                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                     | An array of redirect URIs of the new OAuth application                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                        |
| `callback_url`                                                                                                                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                     | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>The new callback URL of the OAuth application                                                                                         | https://example.com/oauth/callback                                                                                                                                                                                                                                     |
| `scopes`                                                                                                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                     | Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces. | profile email public_metadata private_metadata                                                                                                                                                                                                                         |
| `public`                                                                                                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                     | If true, this client is public and you can use the Proof Key of Code Exchange (PKCE) flow.                                                                                                                                                                             |                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                        |

### Response

**[models.OAuthApplication](../../models/oauthapplication.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Deletes the given OAuth application.
This is not reversible.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.delete(oauth_application_id="oauth_app_09876")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `oauth_application_id`                                              | *str*                                                               | :heavy_check_mark:                                                  | The ID of the OAuth application to delete                           | oauth_app_09876                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## rotate_secret

Rotates the OAuth application's client secret.
When the client secret is rotated, make sure to update it in authorized OAuth clients.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.rotate_secret(oauth_application_id="oauth_application_12345")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `oauth_application_id`                                                | *str*                                                                 | :heavy_check_mark:                                                    | The ID of the OAuth application for which to rotate the client secret | oauth_application_12345                                               |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.OAuthApplicationWithSecret](../../models/oauthapplicationwithsecret.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |