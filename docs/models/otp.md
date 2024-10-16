# Otp


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `status`                                                     | [models.VerificationStatus](../models/verificationstatus.md) | :heavy_check_mark:                                           | N/A                                                          | verified                                                     |
| `strategy`                                                   | [models.Strategy](../models/strategy.md)                     | :heavy_check_mark:                                           | N/A                                                          | email_code                                                   |
| `attempts`                                                   | *int*                                                        | :heavy_check_mark:                                           | N/A                                                          | 1                                                            |
| `expire_at`                                                  | *int*                                                        | :heavy_check_mark:                                           | N/A                                                          | 1615462399                                                   |