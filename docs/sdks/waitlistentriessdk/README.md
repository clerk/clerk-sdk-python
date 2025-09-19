# WaitlistEntriesSDK
(*waitlist_entries*)

## Overview

### Available Operations

* [list](#list) - List all waitlist entries
* [create](#create) - Create a waitlist entry
* [delete](#delete) - Delete a pending waitlist entry
* [invite](#invite) - Invite a waitlist entry
* [reject](#reject) - Reject a waitlist entry

## list

Retrieve a list of waitlist entries for the instance.
Entries are ordered by creation date in descending order by default.
Supports filtering by email address or status and pagination with limit and offset parameters.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListWaitlistEntries" method="get" path="/waitlist_entries" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.list(limit=20, offset=10, query="<value>", status=clerk_backend_api.ListWaitlistEntriesQueryParamStatus.INVITED, order_by="-created_at")

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

<!-- UsageSnippet language="python" operationID="CreateWaitlistEntry" method="post" path="/waitlist_entries" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.create(request={
        "email_address": "Victoria21@gmail.com",
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

## delete

Delete a pending waitlist entry.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteWaitlistEntry" method="delete" path="/waitlist_entries/{waitlist_entry_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.delete(waitlist_entry_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `waitlist_entry_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the waitlist entry to delete                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeletedObject](../../models/deletedobject.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 409, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## invite

Send an invite to the email address in a waitlist entry.

### Example Usage

<!-- UsageSnippet language="python" operationID="InviteWaitlistEntry" method="post" path="/waitlist_entries/{waitlist_entry_id}/invite" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.invite(waitlist_entry_id="<id>", ignore_existing=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `waitlist_entry_id`                                                                                                                         | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | The ID of the waitlist entry to invite                                                                                                      |
| `ignore_existing`                                                                                                                           | *OptionalNullable[bool]*                                                                                                                    | :heavy_minus_sign:                                                                                                                          | Whether an invitation should be created if there is already an existing invitation for this email address, or it's claimed by another user. |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[models.WaitlistEntry](../../models/waitlistentry.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 409, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## reject

Reject a waitlist entry.

### Example Usage

<!-- UsageSnippet language="python" operationID="RejectWaitlistEntry" method="post" path="/waitlist_entries/{waitlist_entry_id}/reject" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.waitlist_entries.reject(waitlist_entry_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `waitlist_entry_id`                                                 | *str*                                                               | :heavy_check_mark:                                                  | The ID of the waitlist entry to reject                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WaitlistEntry](../../models/waitlistentry.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 409, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |