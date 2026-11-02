# LogContext

Context information about the environment and device where the event occurred.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `environment`                                                                | [Optional[models.LogEnvironmentContext]](../models/logenvironmentcontext.md) | :heavy_minus_sign:                                                           | Environment context for the log event.                                       |
| `device`                                                                     | [Optional[models.LogDeviceContext]](../models/logdevicecontext.md)           | :heavy_minus_sign:                                                           | Device information for the log event.                                        |