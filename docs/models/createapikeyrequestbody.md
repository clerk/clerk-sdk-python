# CreateAPIKeyRequestBody


## Fields

| Field                      | Type                       | Required                   | Description                |
| -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| `type`                     | *Optional[str]*            | :heavy_minus_sign:         | N/A                        |
| `name`                     | *str*                      | :heavy_check_mark:         | N/A                        |
| `description`              | *OptionalNullable[str]*    | :heavy_minus_sign:         | N/A                        |
| `subject`                  | *str*                      | :heavy_check_mark:         | N/A                        |
| `claims`                   | *OptionalNullable[Any]*    | :heavy_minus_sign:         | N/A                        |
| `scopes`                   | List[*str*]                | :heavy_minus_sign:         | N/A                        |
| `created_by`               | *OptionalNullable[str]*    | :heavy_minus_sign:         | N/A                        |
| `seconds_until_expiration` | *OptionalNullable[float]*  | :heavy_minus_sign:         | N/A                        |