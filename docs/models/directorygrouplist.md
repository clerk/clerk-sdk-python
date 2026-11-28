# DirectoryGroupList

A cursor-paginated list of groups for a directory.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `data`                                                                   | List[[models.DirectoryGroup](../models/directorygroup.md)]               | :heavy_check_mark:                                                       | N/A                                                                      |
| `cursor`                                                                 | [models.DirectoryGroupListCursor](../models/directorygrouplistcursor.md) | :heavy_check_mark:                                                       | Cursor information for pagination.                                       |