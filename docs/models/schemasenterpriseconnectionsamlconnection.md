# SchemasEnterpriseConnectionSamlConnection

Present when the enterprise connection uses SAML


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `id`                                                            | *Optional[str]*                                                 | :heavy_minus_sign:                                              | SAML connection ID                                              |
| `name`                                                          | *Optional[str]*                                                 | :heavy_minus_sign:                                              | SAML connection display name                                    |
| `idp_entity_id`                                                 | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | IdP entity ID (optional, when connection details are loaded)    |
| `idp_sso_url`                                                   | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | IdP SSO URL (optional, when connection details are loaded)      |
| `idp_metadata_url`                                              | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | IdP metadata URL (optional, when connection details are loaded) |
| `acs_url`                                                       | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | Assertion Consumer Service URL                                  |
| `sp_entity_id`                                                  | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | Service Provider entity ID                                      |
| `sp_metadata_url`                                               | *OptionalNullable[str]*                                         | :heavy_minus_sign:                                              | Service Provider metadata URL                                   |
| `active`                                                        | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Whether the SAML connection is active                           |
| `allow_idp_initiated`                                           | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Whether IdP-initiated SSO is allowed                            |
| `allow_subdomains`                                              | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Whether subdomains are allowed for domain matching              |
| `force_authn`                                                   | *Optional[bool]*                                                | :heavy_minus_sign:                                              | Whether to force re-authentication                              |