# SAMLConnectionIdpCertificates


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `certificate`                                        | *str*                                                | :heavy_check_mark:                                   | The X.509 certificate, base64 DER without PEM armor  |
| `issued_at`                                          | *Nullable[int]*                                      | :heavy_check_mark:                                   | Unix timestamp (milliseconds) of the X.509 NotBefore |
| `expires_at`                                         | *Nullable[int]*                                      | :heavy_check_mark:                                   | Unix timestamp (milliseconds) of the X.509 NotAfter  |