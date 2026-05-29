# Scim

Metadata describing a user's linkage to a SCIM directory. This object is only delivered on `user.created` and `user.updated` webhook events, and only when the user is provisioned through a SCIM directory. Its absence does not necessarily mean the user is not SCIM-managed.



## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `directory_id`                                                        | *str*                                                                 | :heavy_check_mark:                                                    | The ID of the SCIM directory the user is provisioned from.<br/>       |
| `directory_enabled`                                                   | *Optional[bool]*                                                      | :heavy_minus_sign:                                                    | Whether the SCIM directory is currently enabled. Omitted when false.<br/> |
| `external_id`                                                         | *Nullable[str]*                                                       | :heavy_check_mark:                                                    | The user's external ID as reported by the SCIM directory, if any.<br/> |