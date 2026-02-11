# CreateBillingPriceTransitionRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `subscription_item_id`                                               | *str*                                                                | :heavy_check_mark:                                                   | The ID of the subscription item to transition                        |
| `price_transition_request`                                           | [models.PriceTransitionRequest](../models/pricetransitionrequest.md) | :heavy_check_mark:                                                   | Parameters for the price transition                                  |