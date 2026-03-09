# AgentTasks

## Overview

### Available Operations

* [create](#create) - Create agent task
* [revoke](#revoke) - Revoke agent task

## create

Create an agent task on behalf of a user.
The response contains a URL that, when visited, creates a session for the user.
The agent_id is stable per agent_name within an instance. The task_id is unique per call.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateAgentTask" method="post" path="/agents/tasks" -->
```python
import clerk_backend_api
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.agent_tasks.create(request={
        "on_behalf_of": {
            "user_id": "<id>",
            "identifier": "<value>",
        },
        "permissions": clerk_backend_api.CreateAgentTaskPermissions.WILDCARD_,
        "agent_name": "<value>",
        "task_description": "<value>",
        "redirect_url": "https://brilliant-typewriter.net",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CreateAgentTaskRequestBody](../../models/createagenttaskrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.AgentTask](../../models/agenttask.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404, 422      | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |

## revoke

Revokes a pending agent task.

### Example Usage

<!-- UsageSnippet language="python" operationID="RevokeAgentTask" method="post" path="/agents/tasks/{agent_task_id}/revoke" -->
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.agent_tasks.revoke(agent_task_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `agent_task_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | The ID of the agent task to be revoked.                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentTask](../../models/agenttask.md)**

### Errors

| Error Type         | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400, 404           | application/json   |
| models.SDKError    | 4XX, 5XX           | \*/\*              |