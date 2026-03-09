# OAuthApplicationSettings

Success


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `object`                                                                                                | [models.OAuthApplicationSettingsObject](../models/oauthapplicationsettingsobject.md)                    | :heavy_check_mark:                                                                                      | String representing the object's type. Objects of the same type share the same value.                   |
| `dynamic_oauth_client_registration`                                                                     | *bool*                                                                                                  | :heavy_check_mark:                                                                                      | Whether dynamic OAuth client registration is enabled for the instance (RFC 7591).                       |
| `oauth_jwt_access_tokens`                                                                               | *bool*                                                                                                  | :heavy_check_mark:                                                                                      | Whether OAuth JWT access tokens are enabled for the instance (disabled indicates opaque access tokens). |