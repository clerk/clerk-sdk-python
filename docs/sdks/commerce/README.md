# Commerce
(*commerce*)

## Overview

### Available Operations

* [list_plans](#list_plans) - List all commerce plans
* [list_subscription_items](#list_subscription_items) - List all subscription items
* [cancel_subscription_item](#cancel_subscription_item) - Cancel a subscription item
* [extend_subscription_item_free_trial](#extend_subscription_item_free_trial) - Extend free trial for a subscription item

## list_plans

Returns a list of all commerce plans for the instance. The plans are returned sorted by creation date,
with the newest plans appearing first. This includes both free and paid plans. Pagination is supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCommercePlanList" method="get" path="/commerce/plans" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.commerce.list_plans(paginated=True, limit=20, offset=10, payer_type=clerk_backend_api.PayerType.ORG)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `payer_type`                                                                                                                              | [Optional[models.PayerType]](../../models/payertype.md)                                                                                   | :heavy_minus_sign:                                                                                                                        | Filter plans by payer type                                                                                                                |                                                                                                                                           |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PaginatedCommercePlanResponse](../../models/paginatedcommerceplanresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 422      | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list_subscription_items

Returns a list of all subscription items for the instance. The subscription items are returned sorted by creation date,
with the newest appearing first. This includes subscriptions for both users and organizations. Pagination is supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCommerceSubscriptionItemList" method="get" path="/commerce/subscription_items" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.commerce.list_subscription_items(paginated=False, limit=20, offset=10, status=clerk_backend_api.GetCommerceSubscriptionItemListQueryParamStatus.FREE_TRIAL, payer_type=clerk_backend_api.QueryParamPayerType.ORG, plan_id="<id>", include_free=False, query="<value>", user_id="<id>", organization_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `status`                                                                                                                                  | [Optional[models.GetCommerceSubscriptionItemListQueryParamStatus]](../../models/getcommercesubscriptionitemlistqueryparamstatus.md)       | :heavy_minus_sign:                                                                                                                        | Filter subscription items by status                                                                                                       |                                                                                                                                           |
| `payer_type`                                                                                                                              | [Optional[models.QueryParamPayerType]](../../models/queryparampayertype.md)                                                               | :heavy_minus_sign:                                                                                                                        | Filter subscription items by payer type                                                                                                   |                                                                                                                                           |
| `plan_id`                                                                                                                                 | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter subscription items by plan ID                                                                                                      |                                                                                                                                           |
| `include_free`                                                                                                                            | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to include free plan subscription items                                                                                           |                                                                                                                                           |
| `query`                                                                                                                                   | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Search query to filter subscription items by email, user first name, user last name, or organization name.<br/>Supports partial matching. |                                                                                                                                           |
| `user_id`                                                                                                                                 | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter subscription items by user ID                                                                                                      |                                                                                                                                           |
| `organization_id`                                                                                                                         | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Filter subscription items by organization ID                                                                                              |                                                                                                                                           |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PaginatedCommerceSubscriptionItemResponse](../../models/paginatedcommercesubscriptionitemresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 422      | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## cancel_subscription_item

Cancel a specific subscription item. The subscription item can be canceled immediately or at the end of the current billing period.

### Example Usage

<!-- UsageSnippet language="python" operationID="CancelCommerceSubscriptionItem" method="delete" path="/commerce/subscription_items/{subscription_item_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.commerce.cancel_subscription_item(subscription_item_id="<id>", end_now=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `subscription_item_id`                                                                                             | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | The ID of the subscription item to cancel                                                                          |
| `end_now`                                                                                                          | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | Whether to cancel the subscription immediately (true) or at the end of the current billing period (false, default) |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[models.CommerceSubscriptionItem](../../models/commercesubscriptionitem.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.ClerkErrors      | 500                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## extend_subscription_item_free_trial

Extends the free trial period for a specific subscription item to the specified timestamp.
The subscription item must be currently in a free trial period, and the plan must support free trials.
The timestamp must be in the future and not more than 365 days from the end of the current trial period
This operation is idempotent - repeated requests with the same timestamp will not change the trial period.

### Example Usage

<!-- UsageSnippet language="python" operationID="ExtendCommerceSubscriptionItemFreeTrial" method="post" path="/billing/subscription_items/{subscription_item_id}/extend_free_trial" -->
```python
from clerk_backend_api import Clerk
from clerk_backend_api.utils import parse_datetime


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.commerce.extend_subscription_item_free_trial(subscription_item_id="<id>", extend_to=parse_datetime("2026-01-08T00:00:00Z"))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `subscription_item_id`                                                                                    | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The ID of the subscription item to extend the free trial for                                              |                                                                                                           |
| `extend_to`                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                      | :heavy_check_mark:                                                                                        | RFC3339 timestamp to extend the free trial to.<br/>Must be in the future and not more than 365 days from now. | 2026-01-08T00:00:00Z                                                                                      |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.CommerceSubscriptionItem](../../models/commercesubscriptionitem.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.ClerkErrors      | 500                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |