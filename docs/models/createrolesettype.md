# CreateRoleSetType

The type of the role set. "initial" role sets are the default for new organizations.
Only one role set can be "initial" per instance.

## Example Usage

```python
from clerk_backend_api.models import CreateRoleSetType

value = CreateRoleSetType.INITIAL
```


## Values

| Name      | Value     |
| --------- | --------- |
| `INITIAL` | initial   |
| `CUSTOM`  | custom    |