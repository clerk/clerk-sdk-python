# Seats

Seat quantity for seat-based billing.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `quantity`                                                                       | *Nullable[int]*                                                                  | :heavy_check_mark:                                                               | Seat quantity being billed; null means unlimited                                 |
| `tiers`                                                                          | List[[models.CommercePerUnitTotalTier2](../models/commerceperunittotaltier2.md)] | :heavy_minus_sign:                                                               | Per-unit cost breakdown by pricing tier                                          |