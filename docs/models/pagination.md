# Pagination

`cursor` pages by cursor, with any `order_by` and any filter, including `metadata`. The response is
then an object in place of the array of users: `data` holds the users, and `cursor` is
`{"starting_after": <string or null>, "ending_before": <string or null>, "has_next_page": <boolean>}`.
Pass its `starting_after` back as `starting_after` for the next page, or its `ending_before` back
as `ending_before` for the previous one, keeping every other parameter identical. Stop when
`has_next_page` is `false`; `ending_before` is null on the first page. In this mode
`starting_after` is that cursor, not a user ID; a cursor from a different `order_by` is rejected
with a 422, as is a non-zero `offset`.

Results in this mode are eventually consistent. A user created, updated or deleted a short time
ago may not yet be reflected in which users are returned, in their order, or in any count. To
read a user right after writing it, fetch it by ID.

Without this parameter the list pages by offset, and `starting_after` takes a user ID.
`offset` pages the same way, except that it does not accept `starting_after`.

## Example Usage

```python
from clerk_backend_api.models import Pagination

value = Pagination.OFFSET
```


## Values

| Name     | Value    |
| -------- | -------- |
| `OFFSET` | offset   |
| `CURSOR` | cursor   |