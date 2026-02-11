# CreateBillingPriceRequest


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `plan_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the plan this price belongs to.                           |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The currency code (e.g., "USD"). Defaults to USD.                   |
| `amount`                                                            | *int*                                                               | :heavy_check_mark:                                                  | The amount in cents for the price. Must be at least $1 (100 cents). |
| `annual_monthly_amount`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | The monthly amount in cents when billed annually. Optional.         |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | An optional description for this custom price.                      |