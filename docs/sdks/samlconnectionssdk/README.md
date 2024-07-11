# SamlConnectionsSDK
(*saml_connections*)

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
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.saml_connections.list(limit=20, offset=10)

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                   | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[float]*                                                                                                                         | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |


### Response

**[models.ListSAMLConnectionsResponse](../../models/listsamlconnectionsresponse.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## create

Create a new SAML Connection.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.saml_connections.create(name="My SAML Connection", domain="example.org", provider=clerk_backend_api.Provider.SAML_CUSTOM, idp_entity_id="http://idp.example.org/", idp_sso_url="http://idp.example.org/sso", idp_certificate="MIIDdzCCAl+gAwIBAgIJAKcyBaiiz+DT...", idp_metadata_url="http://idp.example.org/metadata.xml", idp_metadata="<EntityDescriptor ...", attribute_mapping={
    "user_id": "nameid",
    "email_address": "mail",
    "first_name": "givenName",
    "last_name": "surname",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             | Example                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                  | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The name to use as a label for this SAML Connection                                                                     | My SAML Connection                                                                                                      |
| `domain`                                                                                                                | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | The domain of your organization. Sign in flows using an email with this domain, will use this SAML Connection.          | example.org                                                                                                             |
| `provider`                                                                                                              | [models.Provider](../../models/provider.md)                                                                             | :heavy_check_mark:                                                                                                      | The IdP provider of the connection.                                                                                     | saml_custom                                                                                                             |
| `idp_entity_id`                                                                                                         | *Optional[Nullable[str]]*                                                                                               | :heavy_minus_sign:                                                                                                      | The Entity ID as provided by the IdP                                                                                    | http://idp.example.org/                                                                                                 |
| `idp_sso_url`                                                                                                           | *Optional[Nullable[str]]*                                                                                               | :heavy_minus_sign:                                                                                                      | The Single-Sign On URL as provided by the IdP                                                                           | http://idp.example.org/sso                                                                                              |
| `idp_certificate`                                                                                                       | *Optional[Nullable[str]]*                                                                                               | :heavy_minus_sign:                                                                                                      | The X.509 certificate as provided by the IdP                                                                            | MIIDdzCCAl+gAwIBAgIJAKcyBaiiz+DT...                                                                                     |
| `idp_metadata_url`                                                                                                      | *Optional[Nullable[str]]*                                                                                               | :heavy_minus_sign:                                                                                                      | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties       | http://idp.example.org/metadata.xml                                                                                     |
| `idp_metadata`                                                                                                          | *Optional[Nullable[str]]*                                                                                               | :heavy_minus_sign:                                                                                                      | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties    | <EntityDescriptor ...                                                                                                   |
| `attribute_mapping`                                                                                                     | [Optional[Nullable[models.CreateSAMLConnectionAttributeMapping]]](../../models/createsamlconnectionattributemapping.md) | :heavy_minus_sign:                                                                                                      | Define the attribute name mapping between Identity Provider and Clerk's user properties                                 |                                                                                                                         |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |                                                                                                                         |


### Response

**[models.SAMLConnection](../../models/samlconnection.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## get

Fetches the SAML Connection whose ID matches the provided `saml_connection_id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.saml_connections.get(saml_connection_id="saml_conn_123")

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

**[models.SAMLConnection](../../models/samlconnection.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,404        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## update

Updates the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.saml_connections.update(saml_connection_id="saml_conn_123_update", name="Example SAML Connection", domain="example.com", idp_entity_id="entity_123", idp_sso_url="https://idp.example.com/sso", idp_certificate="MIIDBTCCAe2gAwIBAgIQ...", idp_metadata_url="https://idp.example.com/metadata", idp_metadata="<EntityDescriptor>...</EntityDescriptor>", attribute_mapping={
    "user_id": "id123",
    "email_address": "user@example.com",
    "first_name": "Jane",
    "last_name": "Doe",
}, active=True, sync_user_attributes=False, allow_subdomains=True, allow_idp_initiated=False)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `saml_connection_id`                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The ID of the SAML Connection to update                                                                                             | saml_conn_123_update                                                                                                                |
| `name`                                                                                                                              | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The name of the new SAML Connection                                                                                                 | Example SAML Connection                                                                                                             |
| `domain`                                                                                                                            | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The domain to use for the new SAML Connection                                                                                       | example.com                                                                                                                         |
| `idp_entity_id`                                                                                                                     | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The entity id as provided by the IdP                                                                                                | entity_123                                                                                                                          |
| `idp_sso_url`                                                                                                                       | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The SSO url as provided by the IdP                                                                                                  | https://idp.example.com/sso                                                                                                         |
| `idp_certificate`                                                                                                                   | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The x509 certificated as provided by the IdP                                                                                        | MIIDBTCCAe2gAwIBAgIQ...                                                                                                             |
| `idp_metadata_url`                                                                                                                  | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The URL which serves the IdP metadata. If present, it takes priority over the corresponding individual properties and replaces them | https://idp.example.com/metadata                                                                                                    |
| `idp_metadata`                                                                                                                      | *Optional[Nullable[str]]*                                                                                                           | :heavy_minus_sign:                                                                                                                  | The XML content of the IdP metadata file. If present, it takes priority over the corresponding individual properties                | <EntityDescriptor>...</EntityDescriptor>                                                                                            |
| `attribute_mapping`                                                                                                                 | [Optional[Nullable[models.UpdateSAMLConnectionAttributeMapping]]](../../models/updatesamlconnectionattributemapping.md)             | :heavy_minus_sign:                                                                                                                  | Define the atrtibute name mapping between Identity Provider and Clerk's user properties                                             |                                                                                                                                     |
| `active`                                                                                                                            | *Optional[Nullable[bool]]*                                                                                                          | :heavy_minus_sign:                                                                                                                  | Activate or de-activate the SAML Connection                                                                                         | true                                                                                                                                |
| `sync_user_attributes`                                                                                                              | *Optional[Nullable[bool]]*                                                                                                          | :heavy_minus_sign:                                                                                                                  | Controls whether to update the user's attributes in each sign-in                                                                    | false                                                                                                                               |
| `allow_subdomains`                                                                                                                  | *Optional[Nullable[bool]]*                                                                                                          | :heavy_minus_sign:                                                                                                                  | Allow users with an email address subdomain to use this connection in order to authenticate                                         | true                                                                                                                                |
| `allow_idp_initiated`                                                                                                               | *Optional[Nullable[bool]]*                                                                                                          | :heavy_minus_sign:                                                                                                                  | Enable or deactivate IdP-initiated flows                                                                                            | false                                                                                                                               |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |                                                                                                                                     |


### Response

**[models.SAMLConnection](../../models/samlconnection.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,403,404,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## delete

Deletes the SAML Connection whose ID matches the provided `id` in the path.

### Example Usage

```python
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.saml_connections.delete(saml_connection_id="saml_conn_123_delete")

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
