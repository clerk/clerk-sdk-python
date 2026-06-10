# ReplaceUserPhoneNumberIdentificationStatus

Controls the status of the replacement phone number. Defaults to `verified`. Set to
`reserved` to create it reserved (unverified but usable for sign-in and locked)
instead of verified.

## Example Usage

```python
from clerk_backend_api.models import ReplaceUserPhoneNumberIdentificationStatus

value = ReplaceUserPhoneNumberIdentificationStatus.VERIFIED
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `VERIFIED` | verified   |
| `RESERVED` | reserved   |