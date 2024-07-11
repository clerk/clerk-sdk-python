# BetaFeatures
(*beta_features*)

### Available Operations

* [update_instance_auth_config](#update_instance_auth_config) - Update instance settings
* [~~update_production_instance_domain~~](#update_production_instance_domain) - Update production instance domain :warning: **Deprecated**
* [change_production_instance_domain](#change_production_instance_domain) - Update production instance domain

## update_instance_auth_config

Updates the settings of an instance

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.beta_features.update_instance_auth_config(restricted_to_allowlist=False, from_email_address="noreply", progressive_sign_up=True, session_token_template="defaultSessionToken", enhanced_email_deliverability=True, test_mode=True)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                | Type                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `restricted_to_allowlist`                                                                                                                                                                                                                                                | *Optional[Nullable[bool]]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist.                                                                                                                                                                 | false                                                                                                                                                                                                                                                                    |
| `from_email_address`                                                                                                                                                                                                                                                     | *Optional[Nullable[str]]*                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                       | The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent.<br/>Only alphanumeric values are allowed.<br/>Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`). | noreply                                                                                                                                                                                                                                                                  |
| `progressive_sign_up`                                                                                                                                                                                                                                                    | *Optional[Nullable[bool]]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info.                                                                                                                                  | true                                                                                                                                                                                                                                                                     |
| `session_token_template`                                                                                                                                                                                                                                                 | *Optional[Nullable[str]]*                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                       | The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string.                                                                                                                                                                 | defaultSessionToken                                                                                                                                                                                                                                                      |
| `enhanced_email_deliverability`                                                                                                                                                                                                                                          | *Optional[Nullable[bool]]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                       | The "enhanced_email_deliverability" feature will send emails from "verifications@clerk.dev" instead of your domain.<br/>This can be helpful if you do not have a high domain reputation.                                                                                 | true                                                                                                                                                                                                                                                                     |
| `test_mode`                                                                                                                                                                                                                                                              | *Optional[Nullable[bool]]*                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Toggles test mode for this instance, allowing the use of test email addresses and phone numbers.<br/>Defaults to true for development instances.                                                                                                                         | true                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                          |


### Response

**[models.InstanceSettings](../../models/instancesettings.md)**
### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## ~~update_production_instance_domain~~

Change the domain of a production instance.

Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.

WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


s.beta_features.update_production_instance_domain(home_url="https://www.example.com")

# Use the SDK ...

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `home_url`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The new home URL of the production instance e.g. https://www.example.com | https://www.example.com                                                  |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |                                                                          |

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

## change_production_instance_domain

Change the domain of a production instance.

Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.

WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example Usage

```python
from clerk import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


s.beta_features.change_production_instance_domain(home_url="https://www.newdomain.com")

# Use the SDK ...

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `home_url`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The new home URL of the production instance e.g. https://www.example.com | https://www.newdomain.com                                                |
| `retries`                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)         | :heavy_minus_sign:                                                       | Configuration to override the default retry behavior of the client.      |                                                                          |

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
