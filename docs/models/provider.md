# Provider

The identity provider (e.g. saml_custom, oidc_custom, oidc_github_enterprise, oidc_gitlab)

## Example Usage

```python
from clerk_backend_api.models import Provider

value = Provider.SAML_CUSTOM
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `SAML_CUSTOM`            | saml_custom              |
| `SAML_OKTA`              | saml_okta                |
| `SAML_GOOGLE`            | saml_google              |
| `SAML_MICROSOFT`         | saml_microsoft           |
| `OIDC_CUSTOM`            | oidc_custom              |
| `OIDC_GITHUB_ENTERPRISE` | oidc_github_enterprise   |
| `OIDC_GITLAB`            | oidc_gitlab              |