# CommercePlanUnitPrice


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `name`                                                                           | *str*                                                                            | :heavy_check_mark:                                                               | Name of the billable unit (for example, seats)                                   |
| `block_size`                                                                     | *int*                                                                            | :heavy_check_mark:                                                               | Number of units included in each pricing block                                   |
| `tiers`                                                                          | List[[models.CommercePlanUnitPriceTier](../models/commerceplanunitpricetier.md)] | :heavy_check_mark:                                                               | Tiered pricing configuration for this unit                                       |