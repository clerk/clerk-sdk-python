# SignInToken

Success


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `object`                                                   | [models.SignInTokenObject](../models/signintokenobject.md) | :heavy_check_mark:                                         | N/A                                                        | sign_in_token                                              |
| `id`                                                       | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        | token_12345                                                |
| `status`                                                   | [models.SignInTokenStatus](../models/signintokenstatus.md) | :heavy_check_mark:                                         | N/A                                                        | pending                                                    |
| `user_id`                                                  | *str*                                                      | :heavy_check_mark:                                         | N/A                                                        | user_12345                                                 |
| `created_at`                                               | *int*                                                      | :heavy_check_mark:                                         | Unix timestamp of creation.<br/>                           | 1609459200                                                 |
| `updated_at`                                               | *int*                                                      | :heavy_check_mark:                                         | Unix timestamp of last update.<br/>                        | 1612137600                                                 |
| `token`                                                    | *Optional[str]*                                            | :heavy_minus_sign:                                         | N/A                                                        | secret_token                                               |
| `url`                                                      | *OptionalNullable[str]*                                    | :heavy_minus_sign:                                         | N/A                                                        | https://example.com/signin/token                           |