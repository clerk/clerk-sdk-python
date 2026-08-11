# IdentificationStatus

Controls the status of the replacement email address. Defaults to `verified`. Set to
`reserved` to create it reserved (unverified but usable for sign-in and locked so no
other user can claim it), or to `unverified` to create it neither usable for sign-in
nor locked.

**Warning:** `unverified` can lock the user out of their account. An unverified email
address cannot be used to sign in, so if the user has no other verified or reserved
identifier, they will be unable to authenticate and unable to verify this address.
Prefer `reserved` unless you specifically need the address left unclaimed — for
example so that another user can also hold it until one of them verifies it.

## Example Usage

```python
from clerk_backend_api.models import IdentificationStatus

value = IdentificationStatus.VERIFIED
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `VERIFIED`   | verified     |
| `RESERVED`   | reserved     |
| `UNVERIFIED` | unverified   |