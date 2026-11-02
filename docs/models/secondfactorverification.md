# SecondFactorVerification

Optional parameter that lets a user with a second factor enabled complete the sign in without being prompted for it.
When omitted, redeeming the token completes only the first factor, and the user must still complete their second factor.
`fresh`: the second factor is treated as verified at sign in. The session token's `fva` claim reports a second factor age of 0.
`stale`: the second factor is treated as unverified. The session token's `fva` claim reports the maximum second factor age of 99999, so any reverification that requires a second factor prompts the user to complete one.
Has no effect for users without a second factor enabled.
A token created with this parameter signs in a user with a second factor enabled without prompting for it, so `expires_in_seconds` defaults to 10 minutes. We recommend keeping it short.

## Example Usage

```python
from clerk_backend_api.models import SecondFactorVerification

value = SecondFactorVerification.FRESH
```


## Values

| Name    | Value   |
| ------- | ------- |
| `FRESH` | fresh   |
| `STALE` | stale   |