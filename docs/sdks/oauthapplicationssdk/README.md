# OauthApplications

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

<!-- UsageSnippet language="python" operationID="ListOAuthApplications" method="get" path="/oauth_applications" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.list(limit=20, offset=10, order_by="+created_at", name_query="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `offset`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Allows to return OAuth applications in a particular order.<br/>At the moment, you can order the returned OAuth applications by their `created_at` and `name`.<br/>In order to specify the direction, you can use the `+/-` symbols prepended in the property to order by.<br/>For example, if you want OAuth applications to be returned in descending order according to their `created_at` property, you can use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied. We only support one `order_by` parameter, and if multiple `order_by` parameters are provided, we will only keep the first one. For example,<br/>if you pass `order_by=name&order_by=created_at`, we will consider only the first `order_by` parameter, which is `name`. The `created_at` parameter will be ignored in this case. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `name_query`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Returns OAuth applications with names that match the given query, via case-insensitive partial match.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### Response

**[models.OAuthApplications](../../models/oauthapplications.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new OAuth application with the given name and callback URL for an instance.
The callback URL must be a valid URL.
All URL schemes are allowed such as `http://`, `https://`, `myapp://`, etc...

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateOAuthApplication" method="post" path="/oauth_applications" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.create(request={
        "name": "Example App",
        "redirect_uris": [
            "<value 1>",
        ],
        "scopes": "profile email public_metadata",
        "public": True,
    })

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

<!-- UsageSnippet language="python" operationID="GetOAuthApplication" method="get" path="/oauth_applications/{oauth_application_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.get(oauth_application_id="oauth_app_12345")

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

<!-- UsageSnippet language="python" operationID="UpdateOAuthApplication" method="patch" path="/oauth_applications/{oauth_application_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.update(oauth_application_id="oauth_app_67890", name="Updated OAuth App Name", redirect_uris=None, scopes="profile email public_metadata private_metadata", consent_screen_enabled=None, pkce_required=None, public=None)

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
| `consent_screen_enabled`                                                                                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                     | True to enable a consent screen to display in the authentication flow. This cannot be disabled for dynamically registered OAuth Applications.                                                                                                                          |                                                                                                                                                                                                                                                                        |
| `pkce_required`                                                                                                                                                                                                                                                        | *OptionalNullable[bool]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                     | True to require the Proof Key of Code Exchange (PKCE) flow.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                        |
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

<!-- UsageSnippet language="python" operationID="DeleteOAuthApplication" method="delete" path="/oauth_applications/{oauth_application_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.delete(oauth_application_id="oauth_app_09876")

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

<!-- UsageSnippet language="python" operationID="RotateOAuthApplicationSecret" method="post" path="/oauth_applications/{oauth_application_id}/rotate_secret" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.oauth_applications.rotate_secret(oauth_application_id="oauth_application_12345")

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