# Groups

A statement group.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `object`                                                                               | [models.BillingStatementGroupsObject](../models/billingstatementgroupsobject.md)       | :heavy_check_mark:                                                                     | String representing the object's type. Objects of the same type share the same value.  |
| `timestamp`                                                                            | *int*                                                                                  | :heavy_check_mark:                                                                     | Unix timestamp (in milliseconds) of the date the group's payment attempts were created |
| `items`                                                                                | List[[models.BillingPaymentAttempt](../models/billingpaymentattempt.md)]               | :heavy_check_mark:                                                                     | The payment attempts included in the group                                             |