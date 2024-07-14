# UpdateInstanceRestrictionsRequestBody


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `allowlist`                       | *OptionalNullable[bool]*          | :heavy_minus_sign:                | N/A                               | false                             |
| `blocklist`                       | *OptionalNullable[bool]*          | :heavy_minus_sign:                | N/A                               | true                              |
| `block_email_subaddresses`        | *OptionalNullable[bool]*          | :heavy_minus_sign:                | N/A                               | true                              |
| `block_disposable_email_domains`  | *OptionalNullable[bool]*          | :heavy_minus_sign:                | N/A                               | true                              |
| `ignore_dots_for_gmail_addresses` | *OptionalNullable[bool]*          | :heavy_minus_sign:                | N/A                               | false                             |