# SAMLConnectionsSDK
(*saml_connections*)

## Overview

A SAML Connection holds configuration data required for facilitating a SAML SSO flow between your
Clerk Instance (SP) and a particular SAML IdP.

### Available Operations

* [list_saml_connections](#list_saml_connections) - Get a list of SAML Connections for an instance
* [create_saml_connection](#create_saml_connection) - Create a SAML Connection
* [get_saml_connection](#get_saml_connection) - Retrieve a SAML Connection by ID
* [update_saml_connection](#update_saml_connection) - Update a SAML Connection
* [delete_saml_connection](#delete_saml_connection) - Delete a SAML Connection

## list_saml_connections

Returns the list of SAML Connections for an instance.
Results can be paginated using the optional `limit` and `offset` query parameters.
The SAML Connections are ordered by descending creation date and the most recent will be returned first.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saml_connections.list_saml_connections(limit=20, offset=10)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.SAMLConnections](../../models/samlconnections.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## create_saml_connection

Create a new SAML Connection.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saml_connections.create_saml_connection(request={
    "name": "My SAML Connection",
    "domain": "example.org",
    "provider": clerk_backend_api.Provider.SAML_CUSTOM,
    "idp_entity_id": "http://idp.example.org/",
    "idp_sso_url": "http://idp.example.org/sso",
    "idp_certificate": "MIIDdzCCAl+gAwIBAgIJAKcyBaiiz+DT...",
    "idp_metadata_url": "http://idp.example.org/metadata.xml",
    "idp_metadata": "<EntityDescriptor ...",
    "attribute_mapping": {
        "user_id": "nameid",
        "email_address": "mail",
        "first_name": "givenName",
        "last_name": "surname",
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.CreateSAMLConnectionRequestBody](../../models/createsamlconnectionrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.SchemasSAMLConnection](../../models/schemassamlconnection.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## get_saml_connection

Fetches the SAML Connection whose ID matches the provided `saml_connection_id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saml_connections.get_saml_connection(saml_connection_id="saml_conn_123")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `saml_connection_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SAML Connection                                       | saml_conn_123                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.SchemasSAMLConnection](../../models/schemassamlconnection.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## update_saml_connection

Updates the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saml_connections.update_saml_connection(saml_connection_id="saml_conn_123_update", name="Example SAML Connection", domain="example.com", idp_entity_id="entity_123", idp_sso_url="https://idp.example.com/sso", idp_certificate="MIIDBTCCAe2gAwIBAgIQ...", idp_metadata_url="https://idp.example.com/metadata", idp_metadata="<EntityDescriptor>...</EntityDescriptor>", attribute_mapping={
    "user_id": "id123",
    "email_address": "user@example.com",
    "first_name": "Jane",
    "last_name": "Doe",
}, active=True, sync_user_attributes=False, allow_subdomains=True, allow_idp_initiated=False, disable_additional_identifications=False)

if res is not None:
    # handle response
    pass

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

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## delete_saml_connection

Deletes the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.saml_connections.delete_saml_connection(saml_connection_id="saml_conn_123_delete")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `saml_connection_id`                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the SAML Connection to delete                             | saml_conn_123_delete                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
