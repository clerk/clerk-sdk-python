# VerifyTOTPResponseBody

The provided TOTP or backup code was correct.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `verified`                                         | *Optional[bool]*                                   | :heavy_minus_sign:                                 | N/A                                                | true                                               |
| `code_type`                                        | [Optional[models.CodeType]](../models/codetype.md) | :heavy_minus_sign:                                 | N/A                                                | totp                                               |