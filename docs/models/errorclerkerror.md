# ErrorClerkError


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `message`                                            | *str*                                                | :heavy_check_mark:                                   | N/A                                                  | Invalid input                                        |
| `long_message`                                       | *str*                                                | :heavy_check_mark:                                   | N/A                                                  | The input provided does not meet the requirements.   |
| `code`                                               | *str*                                                | :heavy_check_mark:                                   | N/A                                                  | 400_bad_request                                      |
| `meta`                                               | [Optional[models.ErrorMeta]](../models/errormeta.md) | :heavy_minus_sign:                                   | N/A                                                  | {}                                                   |