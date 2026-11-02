# View

`grouped`, the default, lists each event group (a flow such as a
sign-in) as a single item, next to the logs that belong to no
group, newest first: a group sorts by when it started, a log by
when it happened. Groups and logs are told apart by `object`.
`flat` lists every log on its own.

Parameters that only work in one view are rejected with a 422
rather than ignored:
- The grouped view only pages forward: `ending_before` is not
  allowed, and `starting_after` takes only a cursor from a grouped
  page.
- The flat list takes only flat cursors.
- `group_type` and `status` aren't allowed with `view=flat`.
- The grouped view takes a `limit` of at most 100, since each group
  brings its first logs along.

In the grouped view, event filters keep the groups with at least
one matching log, each group lists only its matching logs, and time
filters pick groups by when they started.

## Example Usage

```python
from clerk_backend_api.models import View

value = View.FLAT
```


## Values

| Name      | Value     |
| --------- | --------- |
| `FLAT`    | flat      |
| `GROUPED` | grouped   |