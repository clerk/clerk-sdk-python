# OauthConfig

Present when the enterprise connection uses OIDC


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | OAuth config ID                                                      |
| `name`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Custom OIDC provider display name                                    |
| `provider_key`                                                       | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | OAuth provider key (e.g. oidc_custom, oidc_ghe_*, oidc_gitlab_ent_*) |
| `client_id`                                                          | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | OAuth client ID                                                      |
| `discovery_url`                                                      | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | OIDC discovery URL                                                   |
| `logo_public_url`                                                    | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | Logo URL for the provider                                            |
| `created_at`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Unix timestamp in milliseconds when the config was created           |
| `updated_at`                                                         | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | Unix timestamp in milliseconds when the config was last updated      |