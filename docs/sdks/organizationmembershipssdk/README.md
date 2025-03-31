# OrganizationMembershipsSDK
(*organization_memberships*)

## Overview

### Available Operations

* [create](#create) - Create a new organization membership
* [list](#list) - Get a list of all members of an organization
* [update](#update) - Update an organization membership
* [delete](#delete) - Remove a member from an organization
* [update_metadata](#update_metadata) - Merge and update organization membership metadata

## create

Adds a user as a member to the given organization.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_memberships.create(organization_id="org_123", user_id="user_456", role="admin")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `organization_id`                                                      | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the organization where the new membership will be created    | org_123                                                                |
| `user_id`                                                              | *str*                                                                  | :heavy_check_mark:                                                     | The ID of the user that will be added as a member in the organization. | user_456                                                               |
| `role`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | The role that the new member will have in the organization.            | admin                                                                  |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 403, 404, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## list

Retrieves all user memberships for the given organization

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_memberships.list(organization_id="org_789", order_by="+created_at", user_id=[
        "<id>",
        "<id>",
        "<id>",
    ], email_address=[
        "+created_at",
    ], phone_number=[
        "1-321-760-7006 x5600",
        "(509) 684-0380 x849",
    ], username=[
        "Aracely.Collins",
    ], web3_wallet=[
        "<value>",
        "<value>",
    ], role=[
        "<value>",
    ], query="<value>", email_address_query="<value>", phone_number_query="<value>", username_query="<value>", name_query="<value>", last_active_at_before=1700690400000, last_active_at_after=1700690400000, created_at_before=1730160000000, created_at_after=1730160000000)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `organization_id`                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                         | The organization ID.                                                                                                                                                                                                                                                                       | org_789                                                                                                                                                                                                                                                                                    |
| `order_by`                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Sorts organizations memberships by phone_number, email_address, created_at, first_name, last_name or username.<br/>By prepending one of those values with + or -, we can choose to sort in ascending (ASC) or descending (DESC) order."                                                    |                                                                                                                                                                                                                                                                                            |
| `user_id`                                                                                                                                                                                                                                                                                  | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the user ids specified. For each user id, the `+` and `-` can be<br/>prepended to the id, which denote whether the respective user id should be included or<br/>excluded from the result set. Accepts up to 100 user ids. Any user ids not found are ignored.           |                                                                                                                                                                                                                                                                                            |
| `email_address`                                                                                                                                                                                                                                                                            | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the specified email addresses. Accepts up to 100 email addresses. Any email addresses not found are ignored.                                                                                                                                                            | +created_at                                                                                                                                                                                                                                                                                |
| `phone_number`                                                                                                                                                                                                                                                                             | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the specified phone numbers. Accepts up to 100 phone numbers. Any phone numbers not found are ignored.                                                                                                                                                                  |                                                                                                                                                                                                                                                                                            |
| `username`                                                                                                                                                                                                                                                                                 | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the specified usernames.<br/>Accepts up to 100 usernames.<br/>Any usernames not found are ignored.                                                                                                                                                                      |                                                                                                                                                                                                                                                                                            |
| `web3_wallet`                                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the specified web3 wallet addresses.<br/>Accepts up to 100 web3 wallet addresses.<br/>Any web3 wallet addressed not found are ignored.                                                                                                                                  |                                                                                                                                                                                                                                                                                            |
| `role`                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with the specified roles. Accepts up to 100 roles. Any roles not found are ignored.                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                            |
| `query`                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users that match the given query.<br/>For possible matches, we check the email addresses, phone numbers, usernames, web3 wallets, user ids, first and last names.<br/>The query value doesn't need to match the exact value you are looking for, it is capable of partial matches as well. |                                                                                                                                                                                                                                                                                            |
| `email_address_query`                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with emails that match the given query, via case-insensitive partial match.<br/>For example, `email_address_query=ello` will match a user with the email `HELLO@example.com`.                                                                                                |                                                                                                                                                                                                                                                                                            |
| `phone_number_query`                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with phone numbers that match the given query, via case-insensitive partial match.<br/>For example, `phone_number_query=555` will match a user with the phone number `+1555xxxxxxx`.                                                                                         |                                                                                                                                                                                                                                                                                            |
| `username_query`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with usernames that match the given query, via case-insensitive partial match.<br/>For example, `username_query=CoolUser` will match a user with the username `SomeCoolUser`.                                                                                                |                                                                                                                                                                                                                                                                                            |
| `name_query`                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users with names that match the given query, via case-insensitive partial match.                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                            |
| `last_active_at_before`                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users whose last session activity was before the given date (with millisecond precision).<br/>Example: use 1700690400000 to retrieve users whose last session activity was before 2023-11-23.                                                                                      | 1700690400000                                                                                                                                                                                                                                                                              |
| `last_active_at_after`                                                                                                                                                                                                                                                                     | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users whose last session activity was after the given date (with millisecond precision).<br/>Example: use 1700690400000 to retrieve users whose last session activity was after 2023-11-23.                                                                                        | 1700690400000                                                                                                                                                                                                                                                                              |
| `created_at_before`                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users who have been created before the given date (with millisecond precision).<br/>Example: use 1730160000000 to retrieve users who have been created before 2024-10-29.                                                                                                          | 1730160000000                                                                                                                                                                                                                                                                              |
| `created_at_after`                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Returns users who have been created after the given date (with millisecond precision).<br/>Example: use 1730160000000 to retrieve users who have been created after 2024-10-29.                                                                                                            | 1730160000000                                                                                                                                                                                                                                                                              |
| `limit`                                                                                                                                                                                                                                                                                    | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                      | 20                                                                                                                                                                                                                                                                                         |
| `offset`                                                                                                                                                                                                                                                                                   | *Optional[int]*                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                          | 10                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                            |

### Response

**[models.OrganizationMemberships](../../models/organizationmemberships.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update

Updates the properties of an existing organization membership

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_memberships.update(organization_id="org_12345", user_id="user_67890", role="admin")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization the membership belongs to                | org_12345                                                           |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the user that this membership belongs to                  | user_67890                                                          |
| `role`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The new role of the given membership.                               | admin                                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 404, 422           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## delete

Removes the given membership from the organization

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_memberships.delete(organization_id="org_12345", user_id="user_67890")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `organization_id`                                                   | *str*                                                               | :heavy_check_mark:                                                  | The ID of the organization the membership belongs to                | org_12345                                                           |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The ID of the user that this membership belongs to                  | user_67890                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 401, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## update_metadata

Update an organization membership's metadata attributes by merging existing values with the provided parameters.
Metadata values will be updated via a deep merge. Deep means that any nested JSON objects will be merged as well.
You can remove metadata keys at any level by setting their value to `null`.

### Example Usage

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.organization_memberships.update_metadata(organization_id="org_123456", user_id="user_654321", public_metadata={

    }, private_metadata={

    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                | Type                                                                                                                                                     | Required                                                                                                                                                 | Description                                                                                                                                              | Example                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                        | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The ID of the organization the membership belongs to                                                                                                     | org_123456                                                                                                                                               |
| `user_id`                                                                                                                                                | *str*                                                                                                                                                    | :heavy_check_mark:                                                                                                                                       | The ID of the user that this membership belongs to                                                                                                       | user_654321                                                                                                                                              |
| `public_metadata`                                                                                                                                        | Dict[str, *Any*]                                                                                                                                         | :heavy_minus_sign:                                                                                                                                       | Metadata saved on the organization membership, that is visible to both your frontend and backend.<br/>The new object will be merged with the existing value. | {}                                                                                                                                                       |
| `private_metadata`                                                                                                                                       | Dict[str, *Any*]                                                                                                                                         | :heavy_minus_sign:                                                                                                                                       | Metadata saved on the organization membership that is only visible to your backend.<br/>The new object will be merged with the existing value.           | {}                                                                                                                                                       |
| `retries`                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                         | :heavy_minus_sign:                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                      |                                                                                                                                                          |

### Response

**[models.OrganizationMembership](../../models/organizationmembership.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |