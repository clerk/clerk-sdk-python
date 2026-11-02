# DirectoryGroupMemberListCursor

Cursor information for pagination.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `starting_after`                                                                                   | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | Cursor to fetch the next page of results. Pass it back as `starting_after` on the next request.    |
| `ending_before`                                                                                    | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | Cursor to fetch the previous page of results. Pass it back as `ending_before` on the next request. |
| `has_next_page`                                                                                    | *bool*                                                                                             | :heavy_check_mark:                                                                                 | Whether more results can be fetched using the `starting_after` cursor.                             |