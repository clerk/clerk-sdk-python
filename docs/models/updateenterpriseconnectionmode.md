# UpdateEnterpriseConnectionMode

Controls the login_hint sent to the IdP on SSO sign-in

## Example Usage

```python
from clerk_backend_api.models import UpdateEnterpriseConnectionMode

value = UpdateEnterpriseConnectionMode.EMAIL_ADDRESS
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `EMAIL_ADDRESS`    | email_address      |
| `CUSTOM_ATTRIBUTE` | custom_attribute   |
| `OFF`              | off                |