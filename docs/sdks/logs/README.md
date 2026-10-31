# Logs

## Overview

### Available Operations

* [list](#list) - List all logs
* [get_schema](#get_schema) - Retrieve the payload schema of a log event type
* [list_group_events](#list_group_events) - List an event group's logs
* [get](#get) - Retrieve a single log

## list

Returns a list of logs for the authenticated instance.

Use it to find specific events, such as one user's failed sign-ins or
every event in a trace. Narrow the search with filters and a time range
(`event_time_after` and `event_time_before`), and stop paginating once
you have what you need. Syncing or exporting logs through this endpoint
isn't allowed; use log drains, part of the Enterprise plan, instead.

Results are paginated with cursors. The `next_page_status` field in the
cursor object says whether more results exist:
- `"true"`: more results are available. Pass `starting_after` to get the
  next page.
- `"unknown"`: to keep latency predictable, the server read only part of
  the time range, reported as `searched_from` and `searched_to`. More
  matches may exist in the rest of the range; pass `starting_after` to
  keep searching.
- `"false"`: no more results exist within the requested range.

Results never go back further than the plan's log retention.
`retention_floor` in the cursor object is the oldest timestamp the plan
can return. `retention_limit_reached` is `true` when `next_page_status`
is `"false"` because the search ended at that floor, either because
`event_time_after` asked for older events or because it was omitted.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListLogs" method="get" path="/logs" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.logs.list(request={
        "starting_after": "<value>",
        "ending_before": "<value>",
        "subject": "<value>",
        "actor": "<value>",
        "user_id": "user_2abcDEF",
        "identifier": "ana@example.com",
        "trace_id": "1234567890abcdef1234567890abcdef",
        "type": "<value>",
        "client_id": "<id>",
        "session_id": "sess_2abcDEF",
        "impersonator_user_id": "<id>",
        "ip_address": "146.43.160.181",
        "payload_filter": {
            "key": "<value>",
        },
        "payload_fields": "<value>",
        "event_time_after": 1705315800000,
        "event_time_before": 1705319400000,
        "end_user_facing_only": False,
        "group_type": [
            "<value 1>",
            "<value 2>",
        ],
        "status": [
            "<value 1>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ListLogsRequest](../../models/listlogsrequest.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LogList](../../models/loglist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 422, 429 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_schema

Returns the payload schema of a log event type: which fields its
payload carries, addressed by the dot-paths that the `payload_filter`
and `payload_fields` parameters of the list endpoint accept.

`type` accepts a concrete event type (`sign_in.completed`), a
trailing-`*` wildcard (`sign_in.*`), or a bare family name (`sign_in`,
normalized to `sign_in.*` when no concrete type matches — the
response's `event_type`
echoes the normalized form). For wildcard lookups the fields are the
intersection across every matching event type, and `matched_event_types`
lists what the intersection was computed over; per-type metadata
(description, severity, docs_group) is present only for concrete types.

The response is the same for every instance.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetLogSchema" method="get" path="/logs/schemas" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.logs.get_schema(type_="sign_in.*")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                 | Type                                                                                                                                                                                      | Required                                                                                                                                                                                  | Description                                                                                                                                                                               | Example                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type_`                                                                                                                                                                                   | *str*                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                        | The event type to describe: concrete (`sign_in.completed`),<br/>trailing-`*` wildcard (`sign_in.*`), or bare family name<br/>(`sign_in`). Unknown types return a 422. A bare `*` is not<br/>accepted. | sign_in.*                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                                                       |                                                                                                                                                                                           |

### Response

**[models.LogSchema](../../models/logschema.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 422, 429 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list_group_events

Returns the log entries of one event group past the ones a grouped
page of `GET /logs` includes, oldest first, for loading
more of a group. Accepts the same event filters as listing logs, so a
filtered page keeps loading only matching events.

### Example Usage

<!-- UsageSnippet language="python" operationID="ListLogGroupEvents" method="get" path="/logs/groups/{group_id}/events" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.logs.list_group_events(group_id="<id>", started_at=797022, limit=10, starting_after="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `group_id`                                                                                                                                      | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | The ID of the event group, e.g. a sign-in ID.                                                                                                   |
| `started_at`                                                                                                                                    | *int*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | When the group started (Unix timestamp in milliseconds), the<br/>`started_at` of the group item. It bounds the time range searched.             |
| `limit`                                                                                                                                         | *Optional[int]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | Applies a limit to the number of results returned.                                                                                              |
| `starting_after`                                                                                                                                | *Optional[str]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                              | The group's `events_cursor` from the grouped view, or the<br/>`starting_after` cursor this endpoint returned. Only forward<br/>pagination is supported. |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.LogList](../../models/loglist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 422, 429 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Returns a single log entry by its composite key ({event_time_ms}:{event_id}).
Unlike the list endpoint, this returns the full payload for the event.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetLog" method="get" path="/logs/{event_time_and_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.logs.get(event_time_and_id="1776207110588:019d8e31-a1bc-7e07-9347-0fd20b25c475")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                | Example                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `event_time_and_id`                                                                                                                                                                        | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | Composite identifier in the format `{event_time_ms}:{event_id}`, where<br/>`event_time_ms` is the event timestamp as a Unix timestamp in milliseconds<br/>and `event_id` is the UUID of the event. | 1776207110588:019d8e31-a1bc-7e07-9347-0fd20b25c475                                                                                                                                         |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |                                                                                                                                                                                            |

### Response

**[models.LogWithPayload](../../models/logwithpayload.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 403, 404, 429 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |