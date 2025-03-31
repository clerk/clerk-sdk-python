# ActorToken

Success


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `object`                                                 | [models.ActorTokenObject](../models/actortokenobject.md) | :heavy_check_mark:                                       | N/A                                                      | actor_token                                              |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | actor_tok_1a2b3c                                         |
| `status`                                                 | [models.ActorTokenStatus](../models/actortokenstatus.md) | :heavy_check_mark:                                       | N/A                                                      | pending                                                  |
| `user_id`                                                | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | user_1a2b3c                                              |
| `actor`                                                  | [models.ActorTokenActor](../models/actortokenactor.md)   | :heavy_check_mark:                                       | N/A                                                      | {<br/>"sub": "user_2OEpKhcCN1Lat9NQ0G6puh7q5Rb"<br/>}    |
| `created_at`                                             | *int*                                                    | :heavy_check_mark:                                       | Unix timestamp of creation.<br/>                         | 1609459200                                               |
| `updated_at`                                             | *int*                                                    | :heavy_check_mark:                                       | Unix timestamp of last update.<br/>                      | 1612137600                                               |
| `token`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | token_string                                             |
| `url`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | https://example.com/token                                |