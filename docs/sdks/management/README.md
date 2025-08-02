# Management
(*management*)

## Overview

### Available Operations

* [upsert_user](#upsert_user) - Upsert a user
* [create_organization](#create_organization) - Create an organization
* [create_application](#create_application) - Create an application (instance)
* [delete_organization](#delete_organization) - Delete an organization
* [get_application](#get_application) - Get an application
* [update_application](#update_application) - Update an application
* [delete_application](#delete_application) - Delete an application
* [get_application_usage](#get_application_usage) - Get application usage
* [update_application_domain](#update_application_domain) - Update application domain
* [get_application_domain](#get_application_domain) - Get application domain
* [get_application_domain_status](#get_application_domain_status) - Get application domain status

## upsert_user

Upsert a user using the provided information. If a user with the same email_address exists, it will be updated. Otherwise, a new user will be created.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.upsert_user(security=clerk_backend_api.ManagementUpsertUserSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), email_address="Roger_OReilly-Dibbert10@hotmail.com", first_name="Diana", last_name="Schmidt-Kutch")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `security`                                                                          | [models.ManagementUpsertUserSecurity](../../models/managementupsertusersecurity.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `email_address`                                                                     | *str*                                                                               | :heavy_check_mark:                                                                  | The email address of the user.                                                      |
| `first_name`                                                                        | *str*                                                                               | :heavy_check_mark:                                                                  | The first name of the user.                                                         |
| `last_name`                                                                         | *str*                                                                               | :heavy_check_mark:                                                                  | The last name of the user.                                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.User](../../models/user.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_organization

Create a new organization.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk
from clerk_backend_api.utils import parse_datetime


with Clerk() as clerk:

    res = clerk.management.create_organization(security=clerk_backend_api.ManagementCreateOrganizationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), slug="<value>", name="<value>", created_by="<value>", max_allowed_memberships=337266, public_metadata={}, private_metadata={}, created_at=parse_datetime("2024-04-10T20:37:41.925Z"))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ManagementCreateOrganizationSecurity](../../models/managementcreateorganizationsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `slug`                                                                                              | *str*                                                                                               | :heavy_check_mark:                                                                                  | The slug of the organization.                                                                       |
| `name`                                                                                              | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | The name of the organization.                                                                       |
| `created_by`                                                                                        | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | The ID of the user who created the organization.                                                    |
| `max_allowed_memberships`                                                                           | *Optional[int]*                                                                                     | :heavy_minus_sign:                                                                                  | The maximum allowed memberships for the organization.                                               |
| `public_metadata`                                                                                   | [Optional[models.PublicMetadata]](../../models/publicmetadata.md)                                   | :heavy_minus_sign:                                                                                  | Public metadata for the organization.                                                               |
| `private_metadata`                                                                                  | [Optional[models.PrivateMetadata]](../../models/privatemetadata.md)                                 | :heavy_minus_sign:                                                                                  | Private metadata for the organization.                                                              |
| `created_at`                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                | :heavy_minus_sign:                                                                                  | The creation timestamp in RFC3339 format.                                                           |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create_application

Create a new application (instance).
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.create_application(security=clerk_backend_api.ManagementCreateApplicationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), name="<value>", owner_id="<id>", plan_id="<id>", addon_ids=[
        "<value 1>",
    ], domain="bustling-license.info", paid_externally=False, test_mode=True, max_allowed_users=623638, max_allowed_organizations=122319, user_settings={}, organization_settings={}, session_settings={}, native_settings={}, experimental_settings={}, fraud_settings={}, billing_settings={}, subscription_metadata={
        "key": "<value>",
    }, environment_types=[
        clerk_backend_api.EnvironmentTypes.DEVELOPMENT,
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                        | [models.ManagementCreateApplicationSecurity](../../models/managementcreateapplicationsecurity.md)                                                 | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `name`                                                                                                                                            | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The name of the application.                                                                                                                      |
| `owner_id`                                                                                                                                        | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The owner ID (organization ID) of the application.                                                                                                |
| `plan_id`                                                                                                                                         | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The plan ID for the application (e.g., "free_2022_06", "pro_2023_11").                                                                            |
| `addon_ids`                                                                                                                                       | List[*str*]                                                                                                                                       | :heavy_minus_sign:                                                                                                                                | List of add-on IDs (e.g., ["enhanced_auth_2023_11", "enhanced_orgs_2023_11"]).                                                                    |
| `domain`                                                                                                                                          | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The domain for the application (optional).                                                                                                        |
| `paid_externally`                                                                                                                                 | *Optional[bool]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Whether the application is paid externally.                                                                                                       |
| `test_mode`                                                                                                                                       | *Optional[bool]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Whether the application is in test mode.                                                                                                          |
| `max_allowed_users`                                                                                                                               | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Maximum allowed users for the application.                                                                                                        |
| `max_allowed_organizations`                                                                                                                       | *Optional[int]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Maximum allowed organizations for the application.                                                                                                |
| `user_settings`                                                                                                                                   | [Optional[models.UserSettings]](../../models/usersettings.md)                                                                                     | :heavy_minus_sign:                                                                                                                                | User settings for the application.                                                                                                                |
| `organization_settings`                                                                                                                           | [Optional[models.ManagementCreateApplicationRequestOrganizationSettings]](../../models/managementcreateapplicationrequestorganizationsettings.md) | :heavy_minus_sign:                                                                                                                                | Organization settings for the application.                                                                                                        |
| `session_settings`                                                                                                                                | [Optional[models.SessionSettings]](../../models/sessionsettings.md)                                                                               | :heavy_minus_sign:                                                                                                                                | Session settings for the application.                                                                                                             |
| `native_settings`                                                                                                                                 | [Optional[models.NativeSettings]](../../models/nativesettings.md)                                                                                 | :heavy_minus_sign:                                                                                                                                | Native settings for the application.                                                                                                              |
| `experimental_settings`                                                                                                                           | [Optional[models.ExperimentalSettings]](../../models/experimentalsettings.md)                                                                     | :heavy_minus_sign:                                                                                                                                | Experimental settings for the application.                                                                                                        |
| `fraud_settings`                                                                                                                                  | [Optional[models.FraudSettings]](../../models/fraudsettings.md)                                                                                   | :heavy_minus_sign:                                                                                                                                | Fraud settings for the application.                                                                                                               |
| `billing_settings`                                                                                                                                | [Optional[models.BillingSettings]](../../models/billingsettings.md)                                                                               | :heavy_minus_sign:                                                                                                                                | Billing settings for the application.                                                                                                             |
| `subscription_metadata`                                                                                                                           | Dict[str, *str*]                                                                                                                                  | :heavy_minus_sign:                                                                                                                                | Subscription metadata for the application.                                                                                                        |
| `environment_types`                                                                                                                               | List[[models.EnvironmentTypes](../../models/environmenttypes.md)]                                                                                 | :heavy_minus_sign:                                                                                                                                | List of environment types to create instances for.                                                                                                |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[models.ManagementApplicationResponse](../../models/managementapplicationresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete_organization

Delete an organization.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.delete_organization(security=clerk_backend_api.ManagementDeleteOrganizationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), organization_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ManagementDeleteOrganizationSecurity](../../models/managementdeleteorganizationsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `organization_id`                                                                                   | *str*                                                                                               | :heavy_check_mark:                                                                                  | Organization ID.                                                                                    |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.ManagementDeletedObjectResponse](../../models/managementdeletedobjectresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_application

Get application details.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.get_application(security=clerk_backend_api.ManagementGetApplicationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", owner_id="<id>", include_secret_keys=False)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                              | [models.ManagementGetApplicationSecurity](../../models/managementgetapplicationsecurity.md)                             | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `application_id`                                                                                                        | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | Application ID.                                                                                                         |
| `owner_id`                                                                                                              | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | Owner ID of the application (organization ID).                                                                          |
| `include_secret_keys`                                                                                                   | *Optional[bool]*                                                                                                        | :heavy_minus_sign:                                                                                                      | Whether to include secret keys in the response. If 'true', the response will include the secret keys for each instance. |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[models.ManagementApplicationResponse](../../models/managementapplicationresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update_application

Update an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.update_application(security=clerk_backend_api.ManagementUpdateApplicationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", owner_id="<id>", name="<value>", plan_id="<id>", addon_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.ManagementUpdateApplicationSecurity](../../models/managementupdateapplicationsecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `application_id`                                                                                  | *str*                                                                                             | :heavy_check_mark:                                                                                | Application ID.                                                                                   |
| `owner_id`                                                                                        | *str*                                                                                             | :heavy_check_mark:                                                                                | Owner ID of the application (organization ID).                                                    |
| `name`                                                                                            | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | The name of the application.                                                                      |
| `plan_id`                                                                                         | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | The plan ID for the application.                                                                  |
| `addon_ids`                                                                                       | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | List of add-on IDs for the application.                                                           |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.ManagementApplicationResponse](../../models/managementapplicationresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete_application

Delete an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.delete_application(security=clerk_backend_api.ManagementDeleteApplicationSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", owner_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.ManagementDeleteApplicationSecurity](../../models/managementdeleteapplicationsecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `application_id`                                                                                  | *str*                                                                                             | :heavy_check_mark:                                                                                | Application ID.                                                                                   |
| `owner_id`                                                                                        | *str*                                                                                             | :heavy_check_mark:                                                                                | Owner ID of the application (organization ID).                                                    |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.ManagementDeletedObjectResponse](../../models/managementdeletedobjectresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_application_usage

Get usage report for an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.get_application_usage(security=clerk_backend_api.ManagementGetApplicationUsageSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", owner_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.ManagementGetApplicationUsageSecurity](../../models/managementgetapplicationusagesecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Application ID.                                                                                       |
| `owner_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Owner ID of the application (organization ID).                                                        |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ManagementUsageReportResponse](../../models/managementusagereportresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update_application_domain

Update the domain for an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.update_application_domain(security=clerk_backend_api.ManagementUpdateApplicationDomainSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", owner_id="<id>", name="<value>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                    | [models.ManagementUpdateApplicationDomainSecurity](../../models/managementupdateapplicationdomainsecurity.md) | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `application_id`                                                                                              | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Application ID.                                                                                               |
| `owner_id`                                                                                                    | *str*                                                                                                         | :heavy_check_mark:                                                                                            | Owner ID of the application (organization ID).                                                                |
| `name`                                                                                                        | *str*                                                                                                         | :heavy_check_mark:                                                                                            | The domain name.                                                                                              |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.ManagementDomainResponse](../../models/managementdomainresponse.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_application_domain

Get domain information for an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.get_application_domain(security=clerk_backend_api.ManagementGetApplicationDomainSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", domain_name="elderly-disk.name", owner_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.ManagementGetApplicationDomainSecurity](../../models/managementgetapplicationdomainsecurity.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `application_id`                                                                                        | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Application ID.                                                                                         |
| `domain_name`                                                                                           | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Domain name.                                                                                            |
| `owner_id`                                                                                              | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Owner ID of the application (organization ID).                                                          |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.ManagementDomainResponse](../../models/managementdomainresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get_application_domain_status

Get the status of a domain for an application.
This endpoint is internal and requires a specific management token for authorization.


### Example Usage

```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk() as clerk:

    res = clerk.management.get_application_domain_status(security=clerk_backend_api.ManagementGetApplicationDomainStatusSecurity(
        management_token="<YOUR_BEARER_TOKEN_HERE>",
    ), application_id="<id>", domain_name="fatal-arcade.org", owner_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                          | [models.ManagementGetApplicationDomainStatusSecurity](../../models/managementgetapplicationdomainstatussecurity.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `application_id`                                                                                                    | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Application ID.                                                                                                     |
| `domain_name`                                                                                                       | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Domain name.                                                                                                        |
| `owner_id`                                                                                                          | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Owner ID of the application (organization ID).                                                                      |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.ManagementDomainStatusResponse](../../models/managementdomainstatusresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |