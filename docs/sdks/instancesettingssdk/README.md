# InstanceSettingsSDK
(*instance_settings*)

## Overview

Modify the settings of your instance.

### Available Operations

* [update_instance](#update_instance) - Update instance settings
* [update_instance_restrictions](#update_instance_restrictions) - Update instance restrictions
* [update_instance_organization_settings](#update_instance_organization_settings) - Update instance organization settings

## update_instance

Updates the settings of an instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.instance_settings.update_instance(request={
    "test_mode": True,
    "hibp": False,
    "enhanced_email_deliverability": True,
    "support_email": "support@example.com",
    "clerk_js_version": "2.3.1",
    "development_origin": "http://localhost:3000",
    "allowed_origins": [
        "http://localhost:3000",
        "chrome-extension://extension_uiid",
        "capacitor://localhost",
    ],
    "url_based_session_syncing": True,
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.UpdateInstanceRequestBody](../../models/updateinstancerequestbody.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 422                | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## update_instance_restrictions

Updates the restriction settings of an instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.instance_settings.update_instance_restrictions(request={
    "allowlist": False,
    "blocklist": True,
    "block_email_subaddresses": True,
    "block_disposable_email_domains": True,
    "ignore_dots_for_gmail_addresses": False,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.UpdateInstanceRestrictionsRequestBody](../../models/updateinstancerestrictionsrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.InstanceRestrictions](../../models/instancerestrictions.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,422            | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |


## update_instance_organization_settings

Updates the organization settings of the instance

### Example Usage

```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.instance_settings.update_instance_organization_settings(request={
    "enabled": True,
    "max_allowed_memberships": 10,
    "admin_delete_enabled": False,
    "domains_enabled": True,
    "domains_enrollment_modes": [
        "automatic_invitation",
        "automatic_suggestion",
    ],
    "creator_role_id": "creator_role",
    "domains_default_role_id": "member_role",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.UpdateInstanceOrganizationSettingsRequestBody](../../models/updateinstanceorganizationsettingsrequestbody.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.OrganizationSettings](../../models/organizationsettings.md)**

### Errors

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402,404,422        | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |
