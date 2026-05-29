# PreferredSignInStrategyWhenPasswordRequired

When password is required at the instance level, sets the preferred sign-in strategy surfaced to Clerk components. Has no effect when password is not required. Defaults to `password`. Set to an empty string to clear the override.

## Example Usage

```python
from clerk_backend_api.models import PreferredSignInStrategyWhenPasswordRequired

value = PreferredSignInStrategyWhenPasswordRequired.PASSWORD
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PASSWORD` | password   |
| `OTP`      | otp        |
| `UNKNOWN`  |            |