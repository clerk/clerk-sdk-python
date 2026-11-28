# UserCursorPage

A page of users from `GET /v1/users` with `pagination=cursor`.


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `data`                                 | List[[models.User](../models/user.md)] | :heavy_check_mark:                     | N/A                                    |
| `cursor`                               | [models.Cursor](../models/cursor.md)   | :heavy_check_mark:                     | Cursor information for pagination.     |