# LogEnvironmentContext

Environment context for the log event.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `type`                                                                       | *OptionalNullable[str]*                                                      | :heavy_minus_sign:                                                           | The environment type (e.g., "development", "production").                    |
| `application`                                                                | [Optional[models.LogApplicationContext]](../models/logapplicationcontext.md) | :heavy_minus_sign:                                                           | Application context information.                                             |
| `domain`                                                                     | [Optional[models.LogDomainContext]](../models/logdomaincontext.md)           | :heavy_minus_sign:                                                           | Domain context information.                                                  |
| `primary_domain`                                                             | [Optional[models.LogDomainContext]](../models/logdomaincontext.md)           | :heavy_minus_sign:                                                           | Domain context information.                                                  |