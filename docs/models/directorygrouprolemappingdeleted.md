# DirectoryGroupRoleMappingDeleted

A directory group role mapping was deleted.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `object`                                                                                             | [models.DirectoryGroupRoleMappingDeletedObject](../models/directorygrouprolemappingdeletedobject.md) | :heavy_check_mark:                                                                                   | String representing the object's type.                                                               |
| `id`                                                                                                 | *str*                                                                                                | :heavy_check_mark:                                                                                   | The ID of the deleted directory group role mapping.                                                  |
| `deleted`                                                                                            | *Literal[True]*                                                                                      | :heavy_check_mark:                                                                                   | Whether the directory group role mapping was successfully deleted.                                   |