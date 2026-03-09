# CommercePlanUnitPriceTier


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `starts_at_block`                                                  | *int*                                                              | :heavy_check_mark:                                                 | Start block (inclusive) for this tier                              |
| `ends_after_block`                                                 | *OptionalNullable[int]*                                            | :heavy_minus_sign:                                                 | End block (inclusive) for this tier; null means unlimited          |
| `fee_per_block`                                                    | [models.CommerceMoneyResponse](../models/commercemoneyresponse.md) | :heavy_check_mark:                                                 | N/A                                                                |