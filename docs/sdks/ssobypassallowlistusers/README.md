# SsoBypassAllowlistUsers

## Overview

### Available Operations

* [list](#list) - List the SSO bypass allowlist
* [create](#create) - Add a user to the SSO bypass allowlist
* [delete](#delete) - Remove a user from the SSO bypass allowlist

## list

Returns the users who may verify an email code instead of reaching their identity provider when
enterprise SSO is unreachable.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListSSOBypassAllowlistUsers" method="get" path="/sso_bypass_allowlist_users" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sso_bypass_allowlist_users.list(enterprise_connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enterprise_connection_id`                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Restrict the list to the users this enterprise connection serves.   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.SSOBypassAllowlistUser]](../../models/.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Puts a user on the allowlist. The request is rejected unless the user holds a verified email
address on a domain one of the instance's enterprise connections serves.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateSSOBypassAllowlistUser" method="post" path="/sso_bypass_allowlist_users" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sso_bypass_allowlist_users.create(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the user to allowlist.                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SSOBypassAllowlistUser](../../models/ssobypassallowlistuser.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Removes the user from the allowlist, across every enterprise connection that serves them.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteSSOBypassAllowlistUser" method="delete" path="/sso_bypass_allowlist_users/{userID}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.sso_bypass_allowlist_users.delete(user_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the allowlisted user                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 403, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |