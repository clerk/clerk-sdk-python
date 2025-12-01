# Role


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `object`                                                         | [models.RoleObject](../models/roleobject.md)                     | :heavy_check_mark:                                               | N/A                                                              |
| `id`                                                             | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `key`                                                            | *str*                                                            | :heavy_check_mark:                                               | N/A                                                              |
| `description`                                                    | *Nullable[str]*                                                  | :heavy_check_mark:                                               | N/A                                                              |
| `is_creator_eligible`                                            | *bool*                                                           | :heavy_check_mark:                                               | Whether this role is eligible to be an organization creator role |
| `permissions`                                                    | List[[models.Permission](../models/permission.md)]               | :heavy_check_mark:                                               | N/A                                                              |
| `created_at`                                                     | *int*                                                            | :heavy_check_mark:                                               | Unix timestamp of creation.<br/>                                 |
| `updated_at`                                                     | *int*                                                            | :heavy_check_mark:                                               | Unix timestamp of last update.<br/>                              |