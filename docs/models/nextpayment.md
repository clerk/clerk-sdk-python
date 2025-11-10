# NextPayment

Information about the next payment.


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `amount`                                                                                               | [OptionalNullable[models.CommerceSubscriptionItemAmount]](../models/commercesubscriptionitemamount.md) | :heavy_minus_sign:                                                                                     | Amount for the next payment.                                                                           |
| `date_`                                                                                                | *OptionalNullable[int]*                                                                                | :heavy_minus_sign:                                                                                     | Unix timestamp (in milliseconds) for the next payment date.                                            |