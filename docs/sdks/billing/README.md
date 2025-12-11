# Billing

## Overview

### Available Operations

* [list_plans](#list_plans) - List all billing plans
* [list_subscription_items](#list_subscription_items) - List all subscription items
* [cancel_subscription_item](#cancel_subscription_item) - Cancel a subscription item
* [extend_subscription_item_free_trial](#extend_subscription_item_free_trial) - Extend free trial for a subscription item
* [list_statements](#list_statements) - List all billing statements
* [get_statement](#get_statement) - Retrieve a billing statement
* [get_statement_payment_attempts](#get_statement_payment_attempts) - List payment attempts for a billing statement

## list_plans

Returns a list of all billing plans for the instance. The plans are returned sorted by creation date,
with the newest plans appearing first. This includes both free and paid plans. Pagination is supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetCommercePlanList" method="get" path="/billing/plans" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.list_plans(paginated=True, limit=20, offset=10, payer_type=clerk_backend_api.PayerType.ORG)

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

<!-- UsageSnippet language="python" operationID="GetCommerceSubscriptionItemList" method="get" path="/billing/subscription_items" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.list_subscription_items(paginated=False, limit=20, offset=10, status=clerk_backend_api.GetCommerceSubscriptionItemListQueryParamStatus.FREE_TRIAL, payer_type=clerk_backend_api.QueryParamPayerType.ORG, plan_id="<id>", include_free=False, query="<value>")

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
| `query`                                                                                                                                   | *Optional[str]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Search query to filter subscription items                                                                                                 |                                                                                                                                           |
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

<!-- UsageSnippet language="python" operationID="CancelCommerceSubscriptionItem" method="delete" path="/billing/subscription_items/{subscription_item_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.cancel_subscription_item(subscription_item_id="<id>", end_now=False)

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

<!-- UsageSnippet language="python" operationID="ExtendBillingSubscriptionItemFreeTrial" method="post" path="/billing/subscription_items/{subscription_item_id}/extend_free_trial" -->
```python
from clerk_backend_api import Clerk
from clerk_backend_api.utils import parse_datetime


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.extend_subscription_item_free_trial(subscription_item_id="<id>", extend_to=parse_datetime("2026-01-08T00:00:00Z"))

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

**[models.SchemasCommerceSubscriptionItem](../../models/schemascommercesubscriptionitem.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.ClerkErrors      | 500                     | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## list_statements

Returns a list of all billing statements for the instance. The statements are returned sorted by creation date,
with the newest statements appearing first. Pagination is supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetBillingStatementList" method="get" path="/billing/statements" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.list_statements(paginated=False, limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PaginatedBillingStatementResponse](../../models/paginatedbillingstatementresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 422      | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_statement

Retrieves the details of a billing statement.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetBillingStatement" method="get" path="/billing/statements/{statementID}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.get_statement(statement_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `statement_id`                                                      | *str*                                                               | :heavy_check_mark:                                                  | The ID of the statement to retrieve.                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BillingStatement](../../models/billingstatement.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404, 422 | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_statement_payment_attempts

Returns a list of all payment attempts for a specific billing statement. The payment attempts are returned sorted by creation date,
with the newest payment attempts appearing first. Pagination is supported.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetBillingStatementPaymentAttempts" method="get" path="/billing/statements/{statementID}/payment_attempts" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.billing.get_statement_payment_attempts(statement_id="<id>", paginated=True, limit=20, offset=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                 | Type                                                                                                                                      | Required                                                                                                                                  | Description                                                                                                                               | Example                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `statement_id`                                                                                                                            | *str*                                                                                                                                     | :heavy_check_mark:                                                                                                                        | The ID of the statement to retrieve payment attempts for.                                                                                 |                                                                                                                                           |
| `paginated`                                                                                                                               | *Optional[bool]*                                                                                                                          | :heavy_minus_sign:                                                                                                                        | Whether to paginate the results.<br/>If true, the results will be paginated.<br/>If false, the results will not be paginated.             |                                                                                                                                           |
| `limit`                                                                                                                                   | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                     | 20                                                                                                                                        |
| `offset`                                                                                                                                  | *Optional[int]*                                                                                                                           | :heavy_minus_sign:                                                                                                                        | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`. | 10                                                                                                                                        |
| `retries`                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                          | :heavy_minus_sign:                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                       |                                                                                                                                           |

### Response

**[models.PaginatedBillingPaymentAttemptResponse](../../models/paginatedbillingpaymentattemptresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 404, 422 | application/json   |
| models.ClerkErrors | 500                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |