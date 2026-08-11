# EnterpriseConnectionMode

Controls the login_hint sent to the IdP on SSO sign-in

## Example Usage

```python
from clerk_backend_api.models import EnterpriseConnectionMode

value = EnterpriseConnectionMode.EMAIL_ADDRESS
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EMAIL_ADDRESS`    | email_address      |
| `CUSTOM_ATTRIBUTE` | custom_attribute   |
| `OFF`              | off                |