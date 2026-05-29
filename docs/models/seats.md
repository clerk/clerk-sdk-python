# Seats

Seat quantity for seat-based billing.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `quantity`                                                                     | *Nullable[int]*                                                                | :heavy_check_mark:                                                             | Seat quantity being billed; null means unlimited                               |
| `tiers`                                                                        | List[[models.CommercePerUnitTotalTier](../models/commerceperunittotaltier.md)] | :heavy_minus_sign:                                                             | Per-unit cost breakdown by pricing tier                                        |