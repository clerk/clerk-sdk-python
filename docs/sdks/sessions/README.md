# Sessions
(*sessions*)

## Overview

### Available Operations

* [list](#list) - List all sessions
* [create](#create) - Create a new active session
* [get](#get) - Retrieve a session
* [refresh](#refresh) - Refresh a session
* [revoke](#revoke) - Revoke a session
* [create_token](#create_token) - Create a session token
* [create_token_from_template](#create_token_from_template) - Create a session token from a jwt template

## list

Returns a list of all sessions.
The sessions are returned sorted by creation date, with the newest sessions appearing first.
**Deprecation Notice (2024-01-01):** All parameters were initially considered optional, however
moving forward at least one of `client_id` or `user_id` parameters should be provided.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.list(client_id="client_123", user_id="user_456", status=clerk_backend_api.QueryParamStatus.ACTIVE, paginated=True, limit=20, offset=10)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                               | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | List sessions for the given client                                                                                                        | client_123                                                                                                                                |
| `user_id`                                                                                                                                 | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | List sessions for the given user                                                                                                          | user_456                                                                                                                                  |
| `status`                                                                                                                                  | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md)                                                                     | :heavy_minus_sign:                                                                                                                        | Filter sessions by the provided status                                                                                                    | active                                                                                                                                    |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[List[models.Session]](../../models/.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Create a new active session for the provided user ID.

**This operation is intended only for use in testing, and is not available for production instances.** If you are looking to generate a user session from the backend,
we recommend using the [Sign-in Tokens](https://clerk.com/docs/reference/backend-api/tag/Sign-in-Tokens#operation/CreateSignInToken) resource instead.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.create(request={
        "user_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateSessionRequestBody](../../models/createsessionrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Retrieve the details of a session

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.get(session_id="sess_1234567890abcdef")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the session                                               | sess_1234567890abcdef                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## refresh

Refreshes a session by creating a new session token. A 401 is returned when there
are validation errors, which signals the SDKs to fall back to the handshake flow.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.refresh(session_id="<id>", expired_token="<value>", refresh_token="<value>", request_origin="<value>", request_headers={
        "key": "<value>",
        "key1": "<value>",
        "key2": "<value>",
    }, format_=clerk_backend_api.Format.TOKEN, request_originating_ip="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `session_id`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The ID of the session                                                                                                               |
| `expired_token`                                                                                                                     | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The JWT that is sent via the `__session` cookie from your frontend.<br/>Note: this JWT must be associated with the supplied session ID. |
| `refresh_token`                                                                                                                     | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The JWT that is sent via the `__session` cookie from your frontend.                                                                 |
| `request_origin`                                                                                                                    | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The origin of the request.                                                                                                          |
| `request_headers`                                                                                                                   | Dict[str, *Any*]                                                                                                                    | :heavy_minus_sign:                                                                                                                  | The headers of the request.                                                                                                         |
| `format_`                                                                                                                           | [OptionalNullable[models.Format]](../../models/format_.md)                                                                          | :heavy_minus_sign:                                                                                                                  | The format of the response.                                                                                                         |
| `request_originating_ip`                                                                                                            | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The IP address of the request.                                                                                                      |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.SessionRefresh](../../models/sessionrefresh.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## revoke

Sets the status of a session as "revoked", which is an unauthenticated state.
In multi-session mode, a revoked session will still be returned along with its client object, however the user will need to sign in again.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.revoke(session_id="sess_1234567890abcdef")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the session                                               | sess_1234567890abcdef                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_token

Creates a session JSON Web Token (JWT) based on a session.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.create_token(session_id="<id>", expires_in_seconds=None)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the session                                               |
| `expires_in_seconds`                                                | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Use this parameter to override the default session token lifetime.  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateSessionTokenResponseBody](../../models/createsessiontokenresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_token_from_template

Creates a JSON Web Token(JWT) based on a session and a JWT Template name defined for your instance

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sessions.create_token_from_template(session_id="ses_123abcd4567", template_name="custom_hasura", expires_in_seconds=1880.22)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `session_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | The ID of the session                                                         | ses_123abcd4567                                                               |
| `template_name`                                                               | *str*                                                                         | :heavy_check_mark:                                                            | The name of the JWT Template defined in your instance (e.g. `custom_hasura`). | custom_hasura                                                                 |
| `expires_in_seconds`                                                          | *OptionalNullable[int]*                                                       | :heavy_minus_sign:                                                            | Use this parameter to override the JWT token lifetime.                        |                                                                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.CreateSessionTokenFromTemplateResponseBody](../../models/createsessiontokenfromtemplateresponsebody.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |