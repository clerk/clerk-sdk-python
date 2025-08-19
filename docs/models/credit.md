# Credit

Credit information (only available in PaymentAttempt events).


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `amount`                                                                                               | [OptionalNullable[models.CommerceSubscriptionItemAmount]](../models/commercesubscriptionitemamount.md) | :heavy_minus_sign:                                                                                     | Credit amount.                                                                                         |
| `cycle_remaining_percent`                                                                              | *Optional[float]*                                                                                      | :heavy_minus_sign:                                                                                     | Percentage of the billing cycle remaining.                                                             |