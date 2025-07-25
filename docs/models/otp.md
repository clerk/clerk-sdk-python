# Otp


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `object`                                                               | [Optional[models.VerificationObject]](../models/verificationobject.md) | :heavy_minus_sign:                                                     | N/A                                                                    |
| `status`                                                               | [models.VerificationStatus](../models/verificationstatus.md)           | :heavy_check_mark:                                                     | N/A                                                                    |
| `strategy`                                                             | [models.Strategy](../models/strategy.md)                               | :heavy_check_mark:                                                     | N/A                                                                    |
| `attempts`                                                             | *Nullable[int]*                                                        | :heavy_check_mark:                                                     | N/A                                                                    |
| `expire_at`                                                            | *Nullable[int]*                                                        | :heavy_check_mark:                                                     | N/A                                                                    |
| `verified_at_client`                                                   | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | N/A                                                                    |