# ~~Scim~~

Alias of directory. Use directories for all links.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The user's resource ID in this directory.                                       |
| `directory_name`                                                                | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `provider`                                                                      | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `enterprise_connection_id`                                                      | *Nullable[str]*                                                                 | :heavy_check_mark:                                                              | N/A                                                                             |
| `groups`                                                                        | List[[models.UserScimGroups](../models/userscimgroups.md)]                      | :heavy_minus_sign:                                                              | Omitted when groups were not loaded; an empty array means no group memberships. |
| `directory_id`                                                                  | *str*                                                                           | :heavy_check_mark:                                                              | The ID of the directory the user is provisioned from.<br/>                      |
| `directory_enabled`                                                             | *bool*                                                                          | :heavy_check_mark:                                                              | Whether the directory is currently enabled.<br/>                                |
| `external_id`                                                                   | *Nullable[str]*                                                                 | :heavy_check_mark:                                                              | The user's external ID as reported by the directory, if any.<br/>               |