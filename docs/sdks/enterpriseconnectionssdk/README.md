# EnterpriseConnections

## Overview

### Available Operations

* [list](#list) - List enterprise connections
* [create](#create) - Create an enterprise connection
* [get](#get) - Retrieve an enterprise connection
* [update](#update) - Update an enterprise connection
* [delete](#delete) - Delete an enterprise connection

## list

Returns the list of enterprise connections for the instance.
Results can be paginated using the optional `limit` and `offset` query parameters.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListEnterpriseConnections" method="get" path="/enterprise_connections" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.enterprise_connections.list(limit=20, offset=10, organization_id="<id>", active=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                           | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         | Example                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                             | *Optional[int]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                               | 20                                                                                                                                                                  |
| `offset`                                                                                                                                                            | *Optional[int]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                   | 10                                                                                                                                                                  |
| `organization_id`                                                                                                                                                   | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | Filter enterprise connections by organization ID                                                                                                                    |                                                                                                                                                                     |
| `active`                                                                                                                                                            | *Optional[bool]*                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Filter by active status. If true, only active connections are returned. If false, only inactive connections are returned. If omitted, all connections are returned. |                                                                                                                                                                     |
| `retries`                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                 |                                                                                                                                                                     |

### Response

**[models.EnterpriseConnections](../../models/enterpriseconnections.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Create a new enterprise connection.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateEnterpriseConnection" method="post" path="/enterprise_connections" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.enterprise_connections.create(request={
        "name": "<value>",
        "provider": clerk_backend_api.Provider.SAML_GOOGLE,
        "domains": [
            "<value 1>",
            "<value 2>",
        ],
        "organization_id": "<id>",
        "allow_organization_account_linking": False,
        "active": True,
        "saml": None,
        "oidc": {
            "client_id": "<id>",
            "client_secret": "<value>",
            "discovery_url": "https://frugal-brush.org",
            "auth_url": "https://failing-epic.biz",
            "token_url": "https://outrageous-haircut.name/",
            "user_info_url": "https://adolescent-tooth.com",
            "requires_pkce": True,
        },
        "custom_attributes": [
            {
                "name": "<value>",
                "key": "<key>",
                "sso_path": "<value>",
                "scim_path": "<value>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.CreateEnterpriseConnectionRequestBody](../../models/createenterpriseconnectionrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.SchemasEnterpriseConnection](../../models/schemasenterpriseconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Fetches the enterprise connection whose ID matches the provided `enterprise_connection_id` in the path.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetEnterpriseConnection" method="get" path="/enterprise_connections/{enterprise_connection_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.enterprise_connections.get(enterprise_connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enterprise_connection_id`                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the enterprise connection                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SchemasEnterpriseConnection](../../models/schemasenterpriseconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates the enterprise connection whose ID matches the provided `enterprise_connection_id` in the path.
When enabling the connection (setting `active` to true), any existing verified organization domains that match the connection's domains (e.g. used for enrollment modes like automatic invitation) may be deleted so the connection can be enabled.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateEnterpriseConnection" method="patch" path="/enterprise_connections/{enterprise_connection_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.enterprise_connections.update(enterprise_connection_id="<id>", name="<value>", domains=None, active=False, sync_user_attributes=True, disable_additional_identifications=True, allow_organization_account_linking=True, organization_id="<id>", saml={
        "name": "<value>",
        "idp_entity_id": "<id>",
        "idp_sso_url": "https://animated-experience.name/",
        "idp_certificate": "<value>",
        "idp_metadata_url": "https://alert-atrium.com/",
        "idp_metadata": "<value>",
        "attribute_mapping": {
            "user_id": "<id>",
            "email_address": "Eula82@hotmail.com",
            "first_name": "Pierre",
            "last_name": "Hoeger",
        },
        "allow_subdomains": False,
        "allow_idp_initiated": False,
        "force_authn": False,
    }, oidc={
        "client_id": "<id>",
        "client_secret": "<value>",
        "discovery_url": "https://excitable-vista.info",
        "auth_url": "https://obedient-pasta.org/",
        "token_url": "https://helpless-gradient.info/",
        "user_info_url": "https://neglected-chapel.name/",
        "requires_pkce": False,
    }, custom_attributes=[
        {
            "name": "<value>",
            "key": "<key>",
            "sso_path": "<value>",
            "scim_path": "<value>",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                              | Type                                                                                                                                                                                                   | Required                                                                                                                                                                                               | Description                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enterprise_connection_id`                                                                                                                                                                             | *str*                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                     | The ID of the enterprise connection to update                                                                                                                                                          |
| `name`                                                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                     | The display name of the enterprise connection                                                                                                                                                          |
| `domains`                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                     | Domains associated with the enterprise connection. Values are normalized to lowercase.<br/>Empty array means ignored (no change); non-empty array means set domains to the given list (replaces existing). |
| `active`                                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                     | Whether the enterprise connection is active. When set to true (enabling), any existing verified organization domains for the same domain(s) will be removed so the connection can be enabled.          |
| `sync_user_attributes`                                                                                                                                                                                 | *OptionalNullable[bool]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                     | Whether to sync user attributes on sign-in                                                                                                                                                             |
| `disable_additional_identifications`                                                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                     | Whether to disable additional identifications                                                                                                                                                          |
| `allow_organization_account_linking`                                                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                     | Whether this connection supports account linking via organization membership                                                                                                                           |
| `organization_id`                                                                                                                                                                                      | *OptionalNullable[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                     | Organization ID to link to this enterprise connection. Only linking is supported; sending this field sets or changes the linked organization. There is no way to unlink an organization once linked.   |
| `saml`                                                                                                                                                                                                 | [OptionalNullable[models.UpdateEnterpriseConnectionSaml]](../../models/updateenterpriseconnectionsaml.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                                                     | SAML connection-specific properties. Only applied when the enterprise connection uses SAML.<br/>Use this to update IdP configuration, attribute mapping, and other SAML-specific settings.             |
| `oidc`                                                                                                                                                                                                 | [OptionalNullable[models.UpdateEnterpriseConnectionOidc]](../../models/updateenterpriseconnectionoidc.md)                                                                                              | :heavy_minus_sign:                                                                                                                                                                                     | OIDC connection-specific properties. Only applied when the enterprise connection uses OIDC (e.g. oidc_custom, oidc_github_enterprise, or oidc_gitlab).                                                 |
| `custom_attributes`                                                                                                                                                                                    | List[[models.UpdateEnterpriseConnectionCustomAttributes](../../models/updateenterpriseconnectioncustomattributes.md)]                                                                                  | :heavy_minus_sign:                                                                                                                                                                                     | Custom attributes to map from the IdP to the user's profile via SSO or SCIM provisioning. Requires the custom attributes feature to be enabled for the instance.                                       |
| `retries`                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                    |

### Response

**[models.SchemasEnterpriseConnection](../../models/schemasenterpriseconnection.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 402, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes the enterprise connection whose ID matches the provided `enterprise_connection_id` in the path.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteEnterpriseConnection" method="delete" path="/enterprise_connections/{enterprise_connection_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.enterprise_connections.delete(enterprise_connection_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enterprise_connection_id`                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the enterprise connection to delete                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |