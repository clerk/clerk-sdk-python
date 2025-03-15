# Invitation

Success


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `object`                                                 | [models.InvitationObject](../models/invitationobject.md) | :heavy_check_mark:                                       | N/A                                                      | invitation                                               |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | inv_f02930r3                                             |
| `email_address`                                          | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      | invitee@example.com                                      |
| `public_metadata`                                        | Dict[str, *Any*]                                         | :heavy_check_mark:                                       | N/A                                                      | {}                                                       |
| `status`                                                 | [models.InvitationStatus](../models/invitationstatus.md) | :heavy_check_mark:                                       | N/A                                                      | pending                                                  |
| `created_at`                                             | *int*                                                    | :heavy_check_mark:                                       | Unix timestamp of creation.<br/>                         | 1622549600                                               |
| `updated_at`                                             | *int*                                                    | :heavy_check_mark:                                       | Unix timestamp of last update.<br/>                      | 1622553200                                               |
| `revoked`                                                | *Optional[bool]*                                         | :heavy_minus_sign:                                       | N/A                                                      | false                                                    |
| `url`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | N/A                                                      | https://example.com/invitations/accept?code=abcd1234     |
| `expires_at`                                             | *OptionalNullable[int]*                                  | :heavy_minus_sign:                                       | Unix timestamp of expiration.<br/>                       |                                                          |