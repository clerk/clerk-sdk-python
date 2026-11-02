# DirectoryGroup

A group reported by the identity provider for a directory.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `object`                                                                                   | [models.DirectoryGroupObject](../models/directorygroupobject.md)                           | :heavy_check_mark:                                                                         | String representing the object's type. Always "directory_group".                           |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The group ID from the identity provider.                                                   |
| `display_name`                                                                             | *str*                                                                                      | :heavy_check_mark:                                                                         | The display name of the group.                                                             |
| `updated_at`                                                                               | *int*                                                                                      | :heavy_check_mark:                                                                         | Unix timestamp (milliseconds) of when the group was last updated on the identity provider. |