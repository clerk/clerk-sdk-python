# WaitlistEntriesSDK
(*waitlist_entries*)

## Overview

### Available Operations

* [list](#list) - List all waitlist entries
* [create](#create) - Create a waitlist entry

## list

Retrieve a list of waitlist entries for the instance.
Entries are ordered by creation date in descending order by default.
Supports filtering by email address or status and pagination with limit and offset parameters.

### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.list(query="<value>", status=clerk_backend_api.ListWaitlistEntriesQueryParamStatus.COMPLETED)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                          | Type                                                                                                                                                                               | Required                                                                                                                                                                           | Description                                                                                                                                                                        | Example                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                            | *Optional[int]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                              | 20                                                                                                                                                                                 |
| `offset`                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                  | 10                                                                                                                                                                                 |
| `query`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | Filter waitlist entries by `email_address` or `id`                                                                                                                                 |                                                                                                                                                                                    |
| `status`                                                                                                                                                                           | [Optional[models.ListWaitlistEntriesQueryParamStatus]](../../models/listwaitlistentriesqueryparamstatus.md)                                                                        | :heavy_minus_sign:                                                                                                                                                                 | Filter waitlist entries by their status                                                                                                                                            |                                                                                                                                                                                    |
| `order_by`                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                 | Specify the order of results. Supported values are:<br/>- `created_at`<br/>- `email_address`<br/>- `invited_at`<br/><br/>Use `+` for ascending or `-` for descending order. Defaults to `-created_at`. |                                                                                                                                                                                    |
| `retries`                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                                                |                                                                                                                                                                                    |

### Response

**[models.WaitlistEntries](../../models/waitlistentries.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create

Creates a new waitlist entry for the given email address.
If the email address is already on the waitlist, no new entry will be created and the existing waitlist entry will be returned.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.create(request={
        "email_address": "Demond_Willms@hotmail.com",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.CreateWaitlistEntryRequestBody](../../models/createwaitlistentryrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.WaitlistEntry](../../models/waitlistentry.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |