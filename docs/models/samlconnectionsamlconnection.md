# SAMLConnectionSAMLConnection


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | N/A                                  | sc_1234567890                        |
| `name`                               | *str*                                | :heavy_check_mark:                   | N/A                                  | My Company SAML Config               |
| `domain`                             | *str*                                | :heavy_check_mark:                   | N/A                                  | mycompany.com                        |
| `active`                             | *bool*                               | :heavy_check_mark:                   | N/A                                  | true                                 |
| `provider`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | saml_custom                          |
| `sync_user_attributes`               | *bool*                               | :heavy_check_mark:                   | N/A                                  | true                                 |
| `created_at`                         | *int*                                | :heavy_check_mark:                   | Unix timestamp of creation.<br/>     | 1614768000                           |
| `updated_at`                         | *int*                                | :heavy_check_mark:                   | Unix timestamp of last update.<br/>  | 1622540800                           |
| `allow_subdomains`                   | *Optional[bool]*                     | :heavy_minus_sign:                   | N/A                                  | false                                |
| `allow_idp_initiated`                | *Optional[bool]*                     | :heavy_minus_sign:                   | N/A                                  | true                                 |
| `disable_additional_identifications` | *Optional[bool]*                     | :heavy_minus_sign:                   | N/A                                  |                                      |