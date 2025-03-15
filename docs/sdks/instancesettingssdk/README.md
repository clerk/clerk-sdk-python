# InstanceSettingsSDK
(*instance_settings*)

## Overview

### Available Operations

* [get](#get) - Fetch the current instance
* [update](#update) - Update instance settings
* [update_restrictions](#update_restrictions) - Update instance restrictions
* [change_domain](#change_domain) - Update production instance domain
* [update_organization_settings](#update_organization_settings) - Update instance organization settings

## get

Fetches the current instance

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.get()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Instance](../../models/instance.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update

Updates the settings of an instance

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    clerk.instance_settings.update(request={
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

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 422                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update_restrictions

Updates the restriction settings of an instance

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.update_restrictions(request={
        "allowlist": False,
        "blocklist": True,
        "block_email_subaddresses": True,
        "block_disposable_email_domains": True,
        "ignore_dots_for_gmail_addresses": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.UpdateInstanceRestrictionsRequestBody](../../models/updateinstancerestrictionsrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.InstanceRestrictions](../../models/instancerestrictions.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 402, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## change_domain

Change the domain of a production instance.

Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy), updating your Social Connection's redirect URLs and setting the new keys in your code.

WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    clerk.instance_settings.change_domain(request={
        "home_url": "https://www.newdomain.com",
        "is_secondary": False,
    })

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                     | [models.ChangeProductionInstanceDomainRequestBody](../../models/changeproductioninstancedomainrequestbody.md) | :heavy_check_mark:                                                                                            | The request object to use for the request.                                                                    |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update_organization_settings

Updates the organization settings of the instance

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.update_organization_settings(request={
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

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.UpdateInstanceOrganizationSettingsRequestBody](../../models/updateinstanceorganizationsettingsrequestbody.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.OrganizationSettings](../../models/organizationsettings.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 402, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |