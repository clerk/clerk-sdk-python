# AdjustOrganizationBillingCreditBalanceRequest


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `organization_id`                                                            | *str*                                                                        | :heavy_check_mark:                                                           | The ID of the organization whose credit balance to adjust                    |
| `adjust_credit_balance_request`                                              | [models.AdjustCreditBalanceRequest](../models/adjustcreditbalancerequest.md) | :heavy_check_mark:                                                           | Parameters for the credit balance adjustment                                 |