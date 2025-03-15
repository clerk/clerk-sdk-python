# SamlConnectionsSDK
(*saml_connections*)

## Overview

### Available Operations

* [list](#list) - Get a list of SAML Connections for an instance
* [create](#create) - Create a SAML Connection
* [get](#get) - Retrieve a SAML Connection by ID
* [update](#update) - Update a SAML Connection
* [delete](#delete) - Delete a SAML Connection

## list

Returns the list of SAML Connections for an instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The SAML Connections are ordered by descending creation date and the most recent will be returned first.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.saml_connections.list(query="<value>", order_by="<value>", organization_id=[
        "<id>",
        "<id>",
        "<id>",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                   | Type                                                                                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                 | Example                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                       | 20                                                                                                                                                                                                                                                                                                          |
| `offset`                                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                           | 10                                                                                                                                                                                                                                                                                                          |
| `query`                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Returns SAML connections that have a name that matches the given query, via case-insensitive partial match.                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                             |
| `order_by`                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username.<br/>By prepending one of those values with + or -,<br/>we can choose to sort in ascending (ASC) or descending (DESC) order.                                                                  |                                                                                                                                                                                                                                                                                                             |
| `organization_id`                                                                                                                                                                                                                                                                                           | List[*str*]                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Returns SAML connections that have an associated organization ID to the<br/>given organizations.<br/>For each organization id, the `+` and `-` can be<br/>prepended to the id, which denote whether the<br/>respective organization should be included or<br/>excluded from the result set.<br/>Accepts up to 100 organization ids. |                                                                                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                             |

### Response

**[models.SAMLConnections](../../models/samlconnections.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Create a new SAML Connection.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.saml_connections.create(request={
        "name": "My SAML Connection",
        "domain": "example.org",
        "provider": clerk_backend_api.Provider.SAML_CUSTOM,
        "idp_entity_id": "http://idp.example.org/",
        "idp_sso_url": "http://idp.example.org/sso",
        "idp_certificate": "MIIDdzCCAl+gAwIBAgIJAKcyBaiiz+DT...",
        "idp_metadata_url": "http://idp.example.org/metadata.xml",
        "idp_metadata": "<EntityDescriptor ...",
        "organization_id": "<id>",
        "attribute_mapping": {
            "user_id": "nameid",
            "email_address": "mail",
            "first_name": "givenName",
            "last_name": "surname",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.CreateSAMLConnectionRequestBody](../../models/createsamlconnectionrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.SchemasSAMLConnection](../../models/schemassamlconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Fetches the SAML Connection whose ID matches the provided `saml_connection_id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.saml_connections.get(saml_connection_id="saml_conn_123")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `saml_connection_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SAML Connection                                       | saml_conn_123                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SchemasSAMLConnection](../../models/schemassamlconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.saml_connections.update(saml_connection_id="saml_conn_123_update", name="Example SAML Connection", domain="example.com", idp_entity_id="entity_123", idp_sso_url="https://idp.example.com/sso", idp_certificate="MIIDBTCCAe2gAwIBAgIQ...", idp_metadata_url="https://idp.example.com/metadata", idp_metadata="<EntityDescriptor>...</EntityDescriptor>", organization_id="<id>", attribute_mapping={
        "user_id": "id123",
        "email_address": "user@example.com",
        "first_name": "Jane",
        "last_name": "Doe",
    }, active=True, sync_user_attributes=False, allow_subdomains=True, allow_idp_initiated=False, disable_additional_identifications=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `saml_connection_id`                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The ID of the SAML Connection to update                                                                                             | saml_conn_123_update                                                                                                                |
| `name`                                                                                                                              | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The name of the new SAML Connection                                                                                                 | Example SAML Connection                                                                                                             |
| `domain`                                                                                                                            | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The domain to use for the new SAML Connection                                                                                       | example.com                                                                                                                         |
| `idp_entity_id`                                                                                                                     | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The entity id as provided by the IdP                                                                                                | entity_123                                                                                                                          |
| `idp_sso_url`                                                                                                                       | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The SSO url as provided by the IdP                                                                                                  | https://idp.example.com/sso                                                                                                         |
| `idp_certificate`                                                                                                                   | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The x509 certificated as provided by the IdP                                                                                        | MIIDBTCCAe2gAwIBAgIQ...                                                                                                             |
| `idp_metadata_url`                                                                                                                  | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them | https://idp.example.com/metadata                                                                                                    |
| `idp_metadata`                                                                                                                      | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties                | <EntityDescriptor>...</EntityDescriptor>                                                                                            |
| `organization_id`                                                                                                                   | *OptionalNullable[str]*                                                                                                             | :heavy_minus_sign:                                                                                                                  | The ID of the organization to which users of this SAML Connection will be added                                                     |                                                                                                                                     |
| `attribute_mapping`                                                                                                                 | [OptionalNullable[models.UpdateSAMLConnectionAttributeMapping]](../../models/updatesamlconnectionattributemapping.md)               | :heavy_minus_sign:                                                                                                                  | Define the atrtibute name mapping between Identity Provider and Clerk's user properties                                             |                                                                                                                                     |
| `active`                                                                                                                            | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Activate or de-activate the SAML Connection                                                                                         | true                                                                                                                                |
| `sync_user_attributes`                                                                                                              | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Controls whether to update the user's attributes in each sign-in                                                                    | false                                                                                                                               |
| `allow_subdomains`                                                                                                                  | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Allow users with an email address subdomain to use this connection in order to authenticate                                         | true                                                                                                                                |
| `allow_idp_initiated`                                                                                                               | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Enable or deactivate IdP-initiated flows                                                                                            | false                                                                                                                               |
| `disable_additional_identifications`                                                                                                | *OptionalNullable[bool]*                                                                                                            | :heavy_minus_sign:                                                                                                                  | Enable or deactivate additional identifications                                                                                     |                                                                                                                                     |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |

### Response

**[models.SchemasSAMLConnection](../../models/schemassamlconnection.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Deletes the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.saml_connections.delete(saml_connection_id="saml_conn_123_delete")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `saml_connection_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SAML Connection to delete                             | saml_conn_123_delete                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 403, 404      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |