# MergeUserRequestBody


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `from_user_id`                                                               | *str*                                                                        | :heavy_check_mark:                                                           | The ID of the user to merge into the user in the path. This user is deleted. |
| `dry_run`                                                                    | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Return the merged user without changing anything.                            |