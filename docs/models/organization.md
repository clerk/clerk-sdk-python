# Organization


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `object`                                                                       | [models.OrganizationObject](../models/organizationobject.md)                   | :heavy_check_mark:                                                             | N/A                                                                            | organization                                                                   |
| `id`                                                                           | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            | org_123                                                                        |
| `name`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            | Acme Corp                                                                      |
| `slug`                                                                         | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            | acme-corp                                                                      |
| `max_allowed_memberships`                                                      | *int*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            | 300                                                                            |
| `public_metadata`                                                              | [models.OrganizationPublicMetadata](../models/organizationpublicmetadata.md)   | :heavy_check_mark:                                                             | N/A                                                                            | {<br/>"public_info": "Info visible to everyone"<br/>}                          |
| `private_metadata`                                                             | [models.OrganizationPrivateMetadata](../models/organizationprivatemetadata.md) | :heavy_check_mark:                                                             | N/A                                                                            | {<br/>"internal_use_only": "Sensitive data"<br/>}                              |
| `created_at`                                                                   | *int*                                                                          | :heavy_check_mark:                                                             | Unix timestamp of creation.<br/>                                               | 1625078400                                                                     |
| `updated_at`                                                                   | *int*                                                                          | :heavy_check_mark:                                                             | Unix timestamp of last update.<br/>                                            | 1625164800                                                                     |
| `members_count`                                                                | *Optional[Nullable[int]]*                                                      | :heavy_minus_sign:                                                             | N/A                                                                            | 150                                                                            |
| `admin_delete_enabled`                                                         | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | N/A                                                                            | true                                                                           |
| `created_by`                                                                   | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | N/A                                                                            | user_123456                                                                    |