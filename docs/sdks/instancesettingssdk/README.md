# InstanceSettings

## Overview

Modify the settings of your instance.

### Available Operations

* [get](#get) - Fetch the current instance
* [update](#update) - Update instance settings
* [update_restrictions](#update_restrictions) - Update instance restrictions
* [change_domain](#change_domain) - Update production instance domain
* [update_organization_settings](#update_organization_settings) - Update instance organization settings
* [get_instance_protect](#get_instance_protect) - Get instance protect settings
* [update_instance_protect](#update_instance_protect) - Update instance protect settings

## get

Fetches the current instance

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstance" method="get" path="/instance" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.get()

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

<!-- UsageSnippet language="python" operationID="UpdateInstance" method="patch" path="/instance" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    clerk.instance_settings.update(request={
        "test_mode": True,
        "hibp": False,
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

<!-- UsageSnippet language="python" operationID="UpdateInstanceRestrictions" method="patch" path="/instance/restrictions" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.update_restrictions(request={
        "allowlist": False,
        "blocklist": True,
        "allowlist_blocklist_disabled_on_sign_in": True,
        "block_email_subaddresses": True,
        "block_disposable_email_domains": True,
    })

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

Changing the domain requires updating the [DNS records](https://clerk.com/docs/deployments/overview#dns-records) accordingly, deploying new [SSL certificates](https://clerk.com/docs/deployments/overview#deploy-certificates), updating your Social Connection's redirect URLs and setting the new keys in your code.

WARNING: Changing your domain will invalidate all current user sessions (i.e. users will be logged out). Also, while your application is being deployed, a small downtime is expected to occur.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChangeProductionInstanceDomain" method="post" path="/instance/change_domain" -->
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

<!-- UsageSnippet language="python" operationID="UpdateInstanceOrganizationSettings" method="patch" path="/instance/organization_settings" -->
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
        "slug_disabled": True,
        "domains_enrollment_modes": [
            "automatic_invitation",
            "automatic_suggestion",
        ],
        "creator_role_id": "creator_role",
        "domains_default_role_id": "member_role",
    })

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

## get_instance_protect

Get instance protect settings

### Example Usage

<!-- UsageSnippet language="python" operationID="GetInstanceProtect" method="get" path="/instance/protect" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.get_instance_protect()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InstanceProtect](../../models/instanceprotect.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## update_instance_protect

Update instance protect settings

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateInstanceProtect" method="patch" path="/instance/protect" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.instance_settings.update_instance_protect(request={
        "rules_enabled": True,
        "specter_enabled": True,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.UpdateInstanceProtectRequestBody](../../models/updateinstanceprotectrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.InstanceProtect](../../models/instanceprotect.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 422                | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |