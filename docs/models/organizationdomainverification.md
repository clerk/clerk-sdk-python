# OrganizationDomainVerification

Verification details for the domain


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `status`                                                                 | [models.OrganizationDomainStatus](../models/organizationdomainstatus.md) | :heavy_check_mark:                                                       | Status of the verification. It can be `unverified` or `verified`         |
| `strategy`                                                               | *str*                                                                    | :heavy_check_mark:                                                       | Name of the strategy used to verify the domain                           |
| `attempts`                                                               | *Nullable[int]*                                                          | :heavy_check_mark:                                                       | How many attempts have been made to verify the domain                    |
| `expire_at`                                                              | *Nullable[int]*                                                          | :heavy_check_mark:                                                       | Unix timestamp of when the verification will expire                      |