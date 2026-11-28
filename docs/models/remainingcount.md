# RemainingCount

With `pagination=cursor`, also counts the users from the start of this page onward, this page
included. On the first page that is every user the request matches.

A number counts up to that many. The response's `cursor` then carries one of two
fields: `remaining_count_exact` when there are fewer users than the number given, and otherwise
`remaining_count_at_least`, set to that number. Larger numbers make the request slower.

`exact` counts them all, with no ceiling, and the `cursor` carries `remaining_count_exact`. The
count takes longer the more users match, and a request whose count does not finish in time is
rejected with a 422 `users_exact_count_timed_out`; retry it with a number, or without this
parameter.

The count is computed separately from the page and is subject to the same delay. Treat it as a
close estimate: it can differ slightly from the number of users that paging through the results
returns.

## Example Usage

```python
from clerk_backend_api.models import RemainingCount

value = RemainingCount.ONE_HUNDRED
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `ONE_HUNDRED`  | 100            |
| `ONE_THOUSAND` | 1000           |
| `TEN_THOUSAND` | 10000          |
| `EXACT`        | exact          |