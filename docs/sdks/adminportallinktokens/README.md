# AdminPortalLinkTokens

## Overview

### Available Operations

* [create_admin_portal_link_token](#create_admin_portal_link_token) - Create an Admin Portal Link Token
* [revoke_admin_portal_link_token](#revoke_admin_portal_link_token) - Revoke an Admin Portal Link Token

## create_admin_portal_link_token

Create an Admin Portal Link Token

### Example Usage

<!-- UsageSnippet language="python" operationID="createAdminPortalLinkToken" method="post" path="/admin_portal_link_tokens" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.admin_portal_link_tokens.create_admin_portal_link_token(organization_id="<id>", it_contact_id="<id>", scopes=[
        "<value 1>",
        "<value 2>",
    ], seconds_until_expiration=3600)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `it_contact_id`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `scopes`                                                            | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `seconds_until_expiration`                                          | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateAdminPortalLinkTokenResponseBody](../../models/createadminportallinktokenresponsebody.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.CreateAdminPortalLinkTokenAdminPortalLinkTokensResponseBody            | 400                                                                           | application/json                                                              |
| models.CreateAdminPortalLinkTokenAdminPortalLinkTokensResponseResponseBody    | 401                                                                           | application/json                                                              |
| models.CreateAdminPortalLinkTokenAdminPortalLinkTokensResponse403ResponseBody | 403                                                                           | application/json                                                              |
| models.CreateAdminPortalLinkTokenAdminPortalLinkTokensResponse409ResponseBody | 409                                                                           | application/json                                                              |
| models.SDKError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |

## revoke_admin_portal_link_token

Revoke an Admin Portal Link Token

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeAdminPortalLinkToken" method="post" path="/admin_portal_link_tokens/{adminPortalLinkTokenID}/revoke" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.admin_portal_link_tokens.revoke_admin_portal_link_token(admin_portal_link_token_id="<id>", revocation_reason="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `admin_portal_link_token_id`                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `revocation_reason`                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RevokeAdminPortalLinkTokenResponseBody](../../models/revokeadminportallinktokenresponsebody.md)**

### Errors

| Error Type                                                                    | Status Code                                                                   | Content Type                                                                  |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| models.RevokeAdminPortalLinkTokenAdminPortalLinkTokensResponseBody            | 400                                                                           | application/json                                                              |
| models.RevokeAdminPortalLinkTokenAdminPortalLinkTokensResponseResponseBody    | 401                                                                           | application/json                                                              |
| models.RevokeAdminPortalLinkTokenAdminPortalLinkTokensResponse403ResponseBody | 403                                                                           | application/json                                                              |
| models.RevokeAdminPortalLinkTokenAdminPortalLinkTokensResponse404ResponseBody | 404                                                                           | application/json                                                              |
| models.SDKError                                                               | 4XX, 5XX                                                                      | \*/\*                                                                         |