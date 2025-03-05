# CreateActorTokenActor

The actor payload. It needs to include a sub property which should contain the ID of the actor.
This whole payload will be also included in the JWT session token.


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   | Example                                       |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `sub`                                         | *str*                                         | :heavy_check_mark:                            | The ID of the actor.                          |                                               |
| `__pydantic_extra__`                          | Dict[str, *Any*]                              | :heavy_minus_sign:                            | N/A                                           | {<br/>"sub": "user_2OEpKhcCN1Lat9NQ0G6puh7q5Rb"<br/>} |