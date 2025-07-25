# Management
(*management*)

## Overview

### Available Operations

* [upsert_user](#upsert_user) - Upsert a user
* [create_organization](#create_organization) - Create an organization
* [create_application](#create_application) - Create an application (instance)

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
    ), name="<value>", slug="<value>", created_by="<value>", max_allowed_memberships=337266, public_metadata={}, private_metadata={}, created_at=parse_datetime("2024-04-10T20:37:41.925Z"))

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ManagementCreateOrganizationSecurity](../../models/managementcreateorganizationsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `name`                                                                                              | *str*                                                                                               | :heavy_check_mark:                                                                                  | The name of the organization.                                                                       |
| `slug`                                                                                              | *str*                                                                                               | :heavy_check_mark:                                                                                  | The slug of the organization.                                                                       |
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
    ], paid_externally=False, test_mode=True, max_allowed_users=623638, max_allowed_organizations=122319, subscription_metadata={
        "key": "<value>",
    }, environment_types=[
        clerk_backend_api.EnvironmentTypes.DEVELOPMENT,
    ])

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `security`                                                                                        | [models.ManagementCreateApplicationSecurity](../../models/managementcreateapplicationsecurity.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `name`                                                                                            | *str*                                                                                             | :heavy_check_mark:                                                                                | The name of the application.                                                                      |
| `owner_id`                                                                                        | *str*                                                                                             | :heavy_check_mark:                                                                                | The owner ID (organization ID) of the application.                                                |
| `plan_id`                                                                                         | *str*                                                                                             | :heavy_check_mark:                                                                                | The plan ID for the application (e.g., "free_2022_06", "pro_2023_11").                            |
| `addon_ids`                                                                                       | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | List of add-on IDs (e.g., ["enhanced_auth_2023_11", "enhanced_orgs_2023_11"]).                    |
| `paid_externally`                                                                                 | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Whether the application is paid externally.                                                       |
| `test_mode`                                                                                       | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Whether the application is in test mode.                                                          |
| `max_allowed_users`                                                                               | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Maximum allowed users for the application.                                                        |
| `max_allowed_organizations`                                                                       | *Optional[int]*                                                                                   | :heavy_minus_sign:                                                                                | Maximum allowed organizations for the application.                                                |
| `subscription_metadata`                                                                           | Dict[str, *str*]                                                                                  | :heavy_minus_sign:                                                                                | Subscription metadata for the application.                                                        |
| `environment_types`                                                                               | List[[models.EnvironmentTypes](../../models/environmenttypes.md)]                                 | :heavy_minus_sign:                                                                                | List of environment types to create instances for.                                                |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.ManagementApplicationResponse](../../models/managementapplicationresponse.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |