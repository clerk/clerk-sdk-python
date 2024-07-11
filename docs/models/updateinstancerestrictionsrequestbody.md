# UpdateInstanceRestrictionsRequestBody


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `allowlist`                       | *Optional[Nullable[bool]]*        | :heavy_minus_sign:                | N/A                               | false                             |
| `blocklist`                       | *Optional[Nullable[bool]]*        | :heavy_minus_sign:                | N/A                               | true                              |
| `block_email_subaddresses`        | *Optional[Nullable[bool]]*        | :heavy_minus_sign:                | N/A                               | true                              |
| `block_disposable_email_domains`  | *Optional[Nullable[bool]]*        | :heavy_minus_sign:                | N/A                               | true                              |
| `ignore_dots_for_gmail_addresses` | *Optional[Nullable[bool]]*        | :heavy_minus_sign:                | N/A                               | false                             |