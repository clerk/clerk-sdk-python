# SCIMGroupRoleMappingDeleted

A SCIM group role mapping was deleted.


## Fields

| Field                                                                                      | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `object`                                                                                   | [models.SCIMGroupRoleMappingDeletedObject](../models/scimgrouprolemappingdeletedobject.md) | :heavy_check_mark:                                                                         | String representing the object's type.                                                     |
| `id`                                                                                       | *str*                                                                                      | :heavy_check_mark:                                                                         | The ID of the deleted SCIM group role mapping.                                             |
| `deleted`                                                                                  | *Literal[True]*                                                                            | :heavy_check_mark:                                                                         | Whether the SCIM group role mapping was successfully deleted.                              |