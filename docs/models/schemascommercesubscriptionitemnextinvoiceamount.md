# SchemasCommerceSubscriptionItemNextInvoiceAmount

Base plan fee for the next payment. Does not include per-unit (e.g. seat) charges; see `totals.grand_total` for the full amount.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `amount`                                           | *int*                                              | :heavy_check_mark:                                 | The amount in cents.                               |
| `amount_formatted`                                 | *str*                                              | :heavy_check_mark:                                 | The formatted amount as a string (e.g., "$49.99"). |
| `currency`                                         | *str*                                              | :heavy_check_mark:                                 | The currency code (e.g., "USD").                   |
| `currency_symbol`                                  | *str*                                              | :heavy_check_mark:                                 | The currency symbol (e.g., "$").                   |