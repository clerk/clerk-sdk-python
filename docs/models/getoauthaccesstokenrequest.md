# GetOAuthAccessTokenRequest


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `user_id`                                                       | *str*                                                           | :heavy_check_mark:                                              | The ID of the user for which to retrieve the OAuth access token | user_123                                                        |
| `provider`                                                      | *str*                                                           | :heavy_check_mark:                                              | The ID of the OAuth provider (e.g. `oauth_google`)              | oauth_google                                                    |