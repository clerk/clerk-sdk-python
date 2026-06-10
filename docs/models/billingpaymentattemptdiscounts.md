# BillingPaymentAttemptDiscounts

Information about the discounts applied to the payment


## Fields

| Field                                                                                                      | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `proration`                                                                                                | [Nullable[models.BillingPaymentAttemptTotalsProration]](../models/billingpaymentattempttotalsproration.md) | :heavy_check_mark:                                                                                         | Proration details from passed subscription time                                                            |
| `total`                                                                                                    | [models.CommerceMoneyResponse](../models/commercemoneyresponse.md)                                         | :heavy_check_mark:                                                                                         | N/A                                                                                                        |