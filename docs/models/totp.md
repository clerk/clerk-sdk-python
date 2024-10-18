# Totp


## Fields

| Field                | Type                 | Required             | Description          |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `object`             | *str*                | :heavy_check_mark:   | N/A                  |
| `id`                 | *str*                | :heavy_check_mark:   | N/A                  |
| `secret`             | *Nullable[str]*      | :heavy_check_mark:   | N/A                  |
| `uri`                | *Nullable[str]*      | :heavy_check_mark:   | N/A                  |
| `verified`           | *bool*               | :heavy_check_mark:   | N/A                  |
| `backup_codes`       | List[*str*]          | :heavy_minus_sign:   | N/A                  |
| `__pydantic_extra__` | Dict[str, *Any*]     | :heavy_minus_sign:   | N/A                  |