# Machines
(*machines*)

## Overview

### Available Operations

* [list](#list) - Get a list of machines for an instance
* [create](#create) - Create a machine
* [get](#get) - Retrieve a machine
* [update](#update) - Update a machine
* [delete](#delete) - Delete a machine
* [get_secret_key](#get_secret_key) - Retrieve a machine secret key
* [rotate_secret_key](#rotate_secret_key) - Rotate a machine's secret key
* [create_scope](#create_scope) - Create a machine scope
* [delete_scope](#delete_scope) - Delete a machine scope

## list

This request returns the list of machines for an instance. The machines are
ordered by descending creation date (i.e. most recent machines will be
returned first)

### Example Usage

<!-- UsageSnippet language="python" operationID="ListMachines" method="get" path="/machines" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.list(limit=20, offset=10, query="<value>", order_by="-created_at")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Applies a limit to the number of results returned.<br/>Can be used for paginating the results together with `offset`.                                                                                                                                                                                                                                                                  | 20                                                                                                                                                                                                                                                                                                                                                                                     |
| `offset`                                                                                                                                                                                                                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Skip the first `offset` results when paginating.<br/>Needs to be an integer greater or equal to zero.<br/>To be used in conjunction with `limit`.                                                                                                                                                                                                                                      | 10                                                                                                                                                                                                                                                                                                                                                                                     |
| `query`                                                                                                                                                                                                                                                                                                                                                                                | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Returns machines with ID or name that match the given query. Uses exact match for machine ID and partial match for name.                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                                                                                                                                        |
| `order_by`                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Allows to return machines in a particular order.<br/>You can order the returned machines by their `name` or `created_at`.<br/>To specify the direction, use the `+` or `-` symbols prepended to the property to order by.<br/>For example, to return machines in descending order by `created_at`, use `-created_at`.<br/>If you don't use `+` or `-`, then `+` is implied.<br/>Defaults to `-created_at`. |                                                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                        |

### Response

**[models.MachineList](../../models/machinelist.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## create

Creates a new machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateMachine" method="post" path="/machines" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.create(request={
        "name": "<value>",
        "scoped_machines": [
            "<value 1>",
            "<value 2>",
            "<value 3>",
        ],
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateMachineRequestBody](../../models/createmachinerequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.MachineCreated](../../models/machinecreated.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 422 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## get

Returns the details of a machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetMachine" method="get" path="/machines/{machine_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.get(machine_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine to retrieve                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Machine](../../models/machine.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## update

Updates an existing machine.
Only the provided fields will be updated.

### Example Usage

<!-- UsageSnippet language="python" operationID="UpdateMachine" method="patch" path="/machines/{machine_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.update(machine_id="<id>", name="<value>", default_token_ttl=754540)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `machine_id`                                                                                             | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The ID of the machine to update                                                                          |
| `name`                                                                                                   | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The name of the machine                                                                                  |
| `default_token_ttl`                                                                                      | *Optional[int]*                                                                                          | :heavy_minus_sign:                                                                                       | The default time-to-live (TTL) in seconds for tokens created by this machine. Must be at least 1 second. |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[models.Machine](../../models/machine.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## delete

Deletes a machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteMachine" method="delete" path="/machines/{machine_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.delete(machine_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine to delete                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MachineDeleted](../../models/machinedeleted.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## get_secret_key

Returns the secret key for a machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="GetMachineSecretKey" method="get" path="/machines/{machine_id}/secret_key" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.get_secret_key(machine_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine to retrieve the secret key for                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MachineSecretKey](../../models/machinesecretkey.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 401, 403, 404 | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## rotate_secret_key

Rotates the machine's secret key.
When the secret key is rotated, make sure to update it in your machine/application.
The previous secret key will remain valid for the duration specified by the previous_token_ttl parameter.

### Example Usage

<!-- UsageSnippet language="python" operationID="RotateMachineSecretKey" method="post" path="/machines/{machine_id}/secret_key/rotate" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.rotate_secret_key(machine_id="<id>", previous_token_ttl=632625)

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                       | Required                                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `machine_id`                                                                                                                                                                                                                                                               | *str*                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                         | The ID of the machine to rotate the secret key for                                                                                                                                                                                                                         |
| `previous_token_ttl`                                                                                                                                                                                                                                                       | *int*                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                         | The time in seconds that the previous secret key will remain valid after rotation.<br/>This ensures a graceful transition period for updating applications with the new secret key.<br/>Set to 0 to immediately expire the previous key. Maximum value is 8 hours (28800 seconds). |
| `retries`                                                                                                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                        |

### Response

**[models.MachineSecretKey](../../models/machinesecretkey.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |

## create_scope

Creates a new machine scope, allowing the specified machine to access another machine.
Maximum of 25 scopes per machine.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateMachineScope" method="post" path="/machines/{machine_id}/scopes" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.create_scope(machine_id="<id>", to_machine_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine that will have access to another machine      |
| `to_machine_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine that will be scoped to the current machine    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MachineScope](../../models/machinescope.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| models.ClerkErrors           | 400, 401, 403, 404, 409, 422 | application/json             |
| models.SDKError              | 4XX, 5XX                     | \*/\*                        |

## delete_scope

Deletes a machine scope, removing access from one machine to another.

### Example Usage

<!-- UsageSnippet language="python" operationID="DeleteMachineScope" method="delete" path="/machines/{machine_id}/scopes/{other_machine_id}" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.machines.delete_scope(machine_id="<id>", other_machine_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `machine_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine that has access to another machine            |
| `other_machine_id`                                                  | *str*                                                               | :heavy_check_mark:                                                  | The ID of the machine that is being accessed                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MachineScopeDeleted](../../models/machinescopedeleted.md)**

### Errors

| Error Type              | Status Code             | Content Type            |
| ----------------------- | ----------------------- | ----------------------- |
| models.ClerkErrors      | 400, 401, 403, 404, 422 | application/json        |
| models.SDKError         | 4XX, 5XX                | \*/\*                   |