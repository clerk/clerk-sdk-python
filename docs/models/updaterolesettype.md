# UpdateRoleSetType

Set to "initial" to make this the default role set for new organizations.
Only one role set can be "initial" per instance; setting this will change any existing initial role set to "custom".

## Example Usage

```python
from clerk_backend_api.models import UpdateRoleSetType

value = UpdateRoleSetType.INITIAL
```


## Values

| Name      | Value     |
| --------- | --------- |
| `INITIAL` | initial   |