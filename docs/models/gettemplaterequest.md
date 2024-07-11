# GetTemplateRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `template_type`                                                    | [models.PathParamTemplateType](../models/pathparamtemplatetype.md) | :heavy_check_mark:                                                 | The type of templates to retrieve (email or SMS)                   | email                                                              |
| `slug`                                                             | *str*                                                              | :heavy_check_mark:                                                 | The slug (i.e. machine-friendly name) of the template to retrieve  | welcome-email                                                      |