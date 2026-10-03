# SSOBypassAllowlistUser

A user who may verify an email code instead of reaching their identity provider when enterprise SSO is unreachable.



## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `object`                                                                                 | [models.SSOBypassAllowlistUserObject](../models/ssobypassallowlistuserobject.md)         | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `user_id`                                                                                | *str*                                                                                    | :heavy_check_mark:                                                                       | The allowlisted user, and the identifier the delete endpoint takes.                      |
| `public_user_data`                                                                       | [models.SSOBypassAllowlistPublicUserData](../models/ssobypassallowlistpublicuserdata.md) | :heavy_check_mark:                                                                       | The allowlisted user's public data.                                                      |
| `created_at`                                                                             | *int*                                                                                    | :heavy_check_mark:                                                                       | Unix timestamp of creation.                                                              |
| `updated_at`                                                                             | *int*                                                                                    | :heavy_check_mark:                                                                       | Unix timestamp of last update.                                                           |