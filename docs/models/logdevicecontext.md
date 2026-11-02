# LogDeviceContext

Device information for the log event.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `ip_address`                                                           | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The IP address of the client.                                          |
| `user_agent`                                                           | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The user agent string of the client.                                   |
| `browser`                                                              | [Optional[models.LogBrowserContext]](../models/logbrowsercontext.md)   | :heavy_minus_sign:                                                     | Browser information.                                                   |
| `device_type`                                                          | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The type of device (e.g., "desktop", "mobile", "tablet").              |
| `is_mobile`                                                            | *OptionalNullable[bool]*                                               | :heavy_minus_sign:                                                     | Whether the device is a mobile device.                                 |
| `location`                                                             | [Optional[models.LogLocationContext]](../models/loglocationcontext.md) | :heavy_minus_sign:                                                     | Geographic location information.                                       |
| `clerk_js_version`                                                     | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | The version of Clerk.js used by the client.                            |
| `is_native`                                                            | *OptionalNullable[bool]*                                               | :heavy_minus_sign:                                                     | Whether the client is a native application.                            |