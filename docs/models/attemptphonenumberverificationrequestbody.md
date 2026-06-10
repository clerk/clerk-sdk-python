# AttemptPhoneNumberVerificationRequestBody


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `verification_id`                                                                 | *str*                                                                             | :heavy_check_mark:                                                                | The ID of the verification to check, such as one returned by prepare_verification |
| `code`                                                                            | *str*                                                                             | :heavy_check_mark:                                                                | The verification code that was sent to the phone number                           |