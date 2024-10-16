# Sessions
(*sessions*)

## Overview

The Session object is an abstraction over an HTTP session.
It models the period of information exchange between a user and the server.
Sessions are created when a user successfully goes through the sign in or sign up flows.
<https://clerk.com/docs/reference/clerkjs/session>

### Available Operations

* [get_session_list](#get_session_list) - List all sessions
* [get_session](#get_session) - Retrieve a session
* [revoke_session](#revoke_session) - Revoke a session
* [~~verify_session~~](#verify_session) - Verify a session :warning: **Deprecated**
* [create_session_token_from_template](#create_session_token_from_template) - Create a session token from a jwt template

## get_session_list

Returns a list of all sessions.
The sessions are returned sorted by creation date, with the newest sessions appearing first.
**Deprecation Notice (2024-01-01):** All parameters were initially considered optional, however
moving forward at least one of `client_id` or `user_id` parameters should be provided.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sessions.get_session_list(client_id="client_123", user_id="user_456", status=clerk_backend_api.QueryParamStatus.ACTIVE, limit=20, offset=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`                                                                                                                               | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | List sessions for the given client                                                                                                        | client_123                                                                                                                                |
| `user_id`                                                                                                                                 | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | List sessions for the given user                                                                                                          | user_456                                                                                                                                  |
| `status`                                                                                                                                  | [Optional[models.QueryParamStatus]](../../models/queryparamstatus.md)                                                                     | :heavy_minus_sign:                                                                                                                        | Filter sessions by the provided status                                                                                                    | active                                                                                                                                    |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[List[models.Session]](../../models/.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## get_session

Retrieve the details of a session

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sessions.get_session(session_id="sess_1234567890abcdef")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the session                                               | sess_1234567890abcdef                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## revoke_session

Sets the status of a session as "revoked", which is an unauthenticated state.
In multi-session mode, a revoked session will still be returned along with its client object, however the user will need to sign in again.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sessions.revoke_session(session_id="sess_1234567890abcdef")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `session_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the session                                               | sess_1234567890abcdef                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## ~~verify_session~~

Returns the session if it is authenticated, otherwise returns an error.
WARNING: This endpoint is deprecated and will be removed in future versions. We strongly recommend switching to networkless verification using short-lived session tokens,
         which is implemented transparently in all recent SDK versions (e.g. [NodeJS SDK](https://clerk.com/docs/backend-requests/handling/nodejs#clerk-express-require-auth)).
         For more details on how networkless verification works, refer to our [Session Tokens documentation](https://clerk.com/docs/backend-requests/resources/session-tokens).

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sessions.verify_session(session_id="sess_w8q4g9s60j28fghv00f3", request_body={
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uX2lkIjoic2Vzc193OHF4ZzZzNm9qMjhmZ2h2MDBmMyIsImlhdCI6MTU4MjY0OTg2Mn0.J4KP2L6bEZ6YccHFW4E2vKbOLw_mmO0gF_GNRw-wtLM",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           | Example                                                                               |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `session_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | The ID of the session                                                                 | sess_w8q4g9s60j28fghv00f3                                                             |
| `request_body`                                                                        | [Optional[models.VerifySessionRequestBody]](../../models/verifysessionrequestbody.md) | :heavy_minus_sign:                                                                    | Parameters.                                                                           |                                                                                       |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |                                                                                       |

### Response

**[models.Session](../../models/session.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,404,410    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## create_session_token_from_template

Creates a JSON Web Token(JWT) based on a session and a JWT Template name defined for your instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.sessions.create_session_token_from_template(session_id="ses_123abcd4567", template_name="custom_hasura")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `session_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | The ID of the session                                                         | ses_123abcd4567                                                               |
| `template_name`                                                               | *str*                                                                         | :heavy_check_mark:                                                            | The name of the JWT Template defined in your instance (e.g. `custom_hasura`). | custom_hasura                                                                 |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.CreateSessionTokenFromTemplateResponseBody](../../models/createsessiontokenfromtemplateresponsebody.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401,404            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
