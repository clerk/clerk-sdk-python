<div align="center">
  <a href="https://clerk.com?utm_source=github&utm_medium=clerk_javascript" target="_blank" rel="noopener noreferrer">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://images.clerk.com/static/logo-dark-mode-400x400.png">
      <img src="https://images.clerk.com/static/logo-light-mode-400x400.png" height="100">
    </picture>
  </a>
   <p>The most comprehensive User Management Platform</p>
   <a href="https://clerk.com/docs/reference/backend-api"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>
<br></br>

[![chat on Discord](https://img.shields.io/discord/856971667393609759.svg?logo=discord)](https://clerk.com/discord)
[![twitter](https://img.shields.io/twitter/follow/ClerkDev?style=social)](https://twitter.com/intent/follow?screen_name=ClerkDev)

<!-- Start Summary [summary] -->
## Summary

Clerk Backend API: The Clerk REST Backend API, meant to be accessed by backend servers.

### Versions

When the API changes in a way that isn't compatible with older versions, a new version is released.
Each version is identified by its release date, e.g. `2024-10-01`. For more information, please see [Clerk API Versions](https://clerk.com/docs/versioning/available-versions).

Please see https://clerk.com/docs for more information.

More information about the API can be found at https://clerk.com/docs
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Request Authentication](#request-authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [File uploads](#file-uploads)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install clerk-backend-api
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add clerk-backend-api
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from clerk-backend-api python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "clerk-backend-api",
# ]
# ///

from clerk_backend_api import Clerk

sdk = Clerk(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from clerk_backend_api import Clerk


with Clerk() as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():

    async with Clerk() as clerk:

        await clerk.miscellaneous.get_public_interstitial_async(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type | Scheme      |
| ------------- | ---- | ----------- |
| `bearer_auth` | http | HTTP Bearer |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...

```
<!-- End Authentication [security] -->

## Request Authentication

Use the client's `authenticate_request` method to authenticate a request from your app's frontend (when using a Clerk frontend SDK) to a Python backend (Django, Flask, and other Python web frameworks). For example the following utility function checks if the user is effectively signed in:

```python
import os
import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import authenticate_request, AuthenticateRequestOptions

def is_signed_in(request: httpx.Request):
    sdk = Clerk(bearer_auth=os.getenv('CLERK_SECRET_KEY'))
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            authorized_parties=['https://example.com']
        )
    )
    return request_state.is_signed_in
```

If the request is correctly authenticated, the token's payload is made available in `request_state.payload`. Otherwise the reason for the token verification failure is given by `request_state.reason`.

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [actor_tokens](docs/sdks/actortokens/README.md)

* [create](docs/sdks/actortokens/README.md#create) - Create actor token
* [revoke](docs/sdks/actortokens/README.md#revoke) - Revoke actor token

### [allowlist_identifiers](docs/sdks/allowlistidentifiers/README.md)

* [list](docs/sdks/allowlistidentifiers/README.md#list) - List all identifiers on the allow-list
* [create](docs/sdks/allowlistidentifiers/README.md#create) - Add identifier to the allow-list
* [delete](docs/sdks/allowlistidentifiers/README.md#delete) - Delete identifier from allow-list

### [beta_features](docs/sdks/betafeatures/README.md)

* [update_instance_settings](docs/sdks/betafeatures/README.md#update_instance_settings) - Update instance settings
* [~~update_production_instance_domain~~](docs/sdks/betafeatures/README.md#update_production_instance_domain) - Update production instance domain :warning: **Deprecated**

### [blocklist_identifiers](docs/sdks/blocklistidentifierssdk/README.md)

* [list](docs/sdks/blocklistidentifierssdk/README.md#list) - List all identifiers on the block-list
* [create](docs/sdks/blocklistidentifierssdk/README.md#create) - Add identifier to the block-list
* [delete](docs/sdks/blocklistidentifierssdk/README.md#delete) - Delete identifier from block-list


### [clients](docs/sdks/clients/README.md)

* [~~list~~](docs/sdks/clients/README.md#list) - List all clients :warning: **Deprecated**
* [verify](docs/sdks/clients/README.md#verify) - Verify a client
* [get](docs/sdks/clients/README.md#get) - Get a client

### [domains](docs/sdks/domainssdk/README.md)

* [list](docs/sdks/domainssdk/README.md#list) - List all instance domains
* [add](docs/sdks/domainssdk/README.md#add) - Add a domain
* [delete](docs/sdks/domainssdk/README.md#delete) - Delete a satellite domain
* [update](docs/sdks/domainssdk/README.md#update) - Update a domain

### [email_addresses](docs/sdks/emailaddresses/README.md)

* [create](docs/sdks/emailaddresses/README.md#create) - Create an email address
* [get](docs/sdks/emailaddresses/README.md#get) - Retrieve an email address
* [delete](docs/sdks/emailaddresses/README.md#delete) - Delete an email address
* [update](docs/sdks/emailaddresses/README.md#update) - Update an email address

### [~~email_and_sms_templates~~](docs/sdks/emailandsmstemplates/README.md)

* [~~upsert~~](docs/sdks/emailandsmstemplates/README.md#upsert) - Update a template for a given type and slug :warning: **Deprecated**

### [~~email_sms_templates~~](docs/sdks/emailsmstemplates/README.md)

* [~~list~~](docs/sdks/emailsmstemplates/README.md#list) - List all templates :warning: **Deprecated**
* [~~get~~](docs/sdks/emailsmstemplates/README.md#get) - Retrieve a template :warning: **Deprecated**
* [~~revert~~](docs/sdks/emailsmstemplates/README.md#revert) - Revert a template :warning: **Deprecated**
* [~~toggle_template_delivery~~](docs/sdks/emailsmstemplates/README.md#toggle_template_delivery) - Toggle the delivery by Clerk for a template of a given type and slug :warning: **Deprecated**

### [instance_settings](docs/sdks/instancesettingssdk/README.md)

* [get](docs/sdks/instancesettingssdk/README.md#get) - Fetch the current instance
* [update](docs/sdks/instancesettingssdk/README.md#update) - Update instance settings
* [update_restrictions](docs/sdks/instancesettingssdk/README.md#update_restrictions) - Update instance restrictions
* [change_domain](docs/sdks/instancesettingssdk/README.md#change_domain) - Update production instance domain
* [update_organization_settings](docs/sdks/instancesettingssdk/README.md#update_organization_settings) - Update instance organization settings

### [invitations](docs/sdks/invitations/README.md)

* [create](docs/sdks/invitations/README.md#create) - Create an invitation
* [list](docs/sdks/invitations/README.md#list) - List all invitations
* [bulk_create](docs/sdks/invitations/README.md#bulk_create) - Create multiple invitations
* [revoke](docs/sdks/invitations/README.md#revoke) - Revokes an invitation

### [jwks](docs/sdks/jwkssdk/README.md)

* [get_jwks](docs/sdks/jwkssdk/README.md#get_jwks) - Retrieve the JSON Web Key Set of the instance

### [jwt_templates](docs/sdks/jwttemplates/README.md)

* [list](docs/sdks/jwttemplates/README.md#list) - List all templates
* [create](docs/sdks/jwttemplates/README.md#create) - Create a JWT template
* [get](docs/sdks/jwttemplates/README.md#get) - Retrieve a template
* [update](docs/sdks/jwttemplates/README.md#update) - Update a JWT template
* [delete](docs/sdks/jwttemplates/README.md#delete) - Delete a Template

### [miscellaneous](docs/sdks/miscellaneous/README.md)

* [get_public_interstitial](docs/sdks/miscellaneous/README.md#get_public_interstitial) - Returns the markup for the interstitial page

### [oauth_applications](docs/sdks/oauthapplicationssdk/README.md)

* [list](docs/sdks/oauthapplicationssdk/README.md#list) - Get a list of OAuth applications for an instance
* [create](docs/sdks/oauthapplicationssdk/README.md#create) - Create an OAuth application
* [get](docs/sdks/oauthapplicationssdk/README.md#get) - Retrieve an OAuth application by ID
* [update](docs/sdks/oauthapplicationssdk/README.md#update) - Update an OAuth application
* [delete](docs/sdks/oauthapplicationssdk/README.md#delete) - Delete an OAuth application
* [rotate_secret](docs/sdks/oauthapplicationssdk/README.md#rotate_secret) - Rotate the client secret of the given OAuth application

### [organization_domains](docs/sdks/organizationdomainssdk/README.md)

* [create](docs/sdks/organizationdomainssdk/README.md#create) - Create a new organization domain.
* [list](docs/sdks/organizationdomainssdk/README.md#list) - Get a list of all domains of an organization.
* [update](docs/sdks/organizationdomainssdk/README.md#update) - Update an organization domain.
* [delete](docs/sdks/organizationdomainssdk/README.md#delete) - Remove a domain from an organization.

### [organization_invitations](docs/sdks/organizationinvitationssdk/README.md)

* [get_all](docs/sdks/organizationinvitationssdk/README.md#get_all) - Get a list of organization invitations for the current instance
* [create](docs/sdks/organizationinvitationssdk/README.md#create) - Create and send an organization invitation
* [list](docs/sdks/organizationinvitationssdk/README.md#list) - Get a list of organization invitations
* [bulk_create](docs/sdks/organizationinvitationssdk/README.md#bulk_create) - Bulk create and send organization invitations
* [~~list_pending~~](docs/sdks/organizationinvitationssdk/README.md#list_pending) - Get a list of pending organization invitations :warning: **Deprecated**
* [get](docs/sdks/organizationinvitationssdk/README.md#get) - Retrieve an organization invitation by ID
* [revoke](docs/sdks/organizationinvitationssdk/README.md#revoke) - Revoke a pending organization invitation

### [organization_memberships](docs/sdks/organizationmembershipssdk/README.md)

* [create](docs/sdks/organizationmembershipssdk/README.md#create) - Create a new organization membership
* [list](docs/sdks/organizationmembershipssdk/README.md#list) - Get a list of all members of an organization
* [update](docs/sdks/organizationmembershipssdk/README.md#update) - Update an organization membership
* [delete](docs/sdks/organizationmembershipssdk/README.md#delete) - Remove a member from an organization
* [update_metadata](docs/sdks/organizationmembershipssdk/README.md#update_metadata) - Merge and update organization membership metadata

### [organizations](docs/sdks/organizationssdk/README.md)

* [list](docs/sdks/organizationssdk/README.md#list) - Get a list of organizations for an instance
* [create](docs/sdks/organizationssdk/README.md#create) - Create an organization
* [get](docs/sdks/organizationssdk/README.md#get) - Retrieve an organization by ID or slug
* [update](docs/sdks/organizationssdk/README.md#update) - Update an organization
* [delete](docs/sdks/organizationssdk/README.md#delete) - Delete an organization
* [merge_metadata](docs/sdks/organizationssdk/README.md#merge_metadata) - Merge and update metadata for an organization
* [upload_logo](docs/sdks/organizationssdk/README.md#upload_logo) - Upload a logo for the organization
* [delete_logo](docs/sdks/organizationssdk/README.md#delete_logo) - Delete the organization's logo.

### [phone_numbers](docs/sdks/phonenumbers/README.md)

* [create](docs/sdks/phonenumbers/README.md#create) - Create a phone number
* [get](docs/sdks/phonenumbers/README.md#get) - Retrieve a phone number
* [delete](docs/sdks/phonenumbers/README.md#delete) - Delete a phone number
* [update](docs/sdks/phonenumbers/README.md#update) - Update a phone number

### [proxy_checks](docs/sdks/proxychecks/README.md)

* [verify](docs/sdks/proxychecks/README.md#verify) - Verify the proxy configuration for your domain

### [redirect_urls](docs/sdks/redirecturls/README.md)

* [list](docs/sdks/redirecturls/README.md#list) - List all redirect URLs
* [create](docs/sdks/redirecturls/README.md#create) - Create a redirect URL
* [get](docs/sdks/redirecturls/README.md#get) - Retrieve a redirect URL
* [delete](docs/sdks/redirecturls/README.md#delete) - Delete a redirect URL

### [saml_connections](docs/sdks/samlconnectionssdk/README.md)

* [list](docs/sdks/samlconnectionssdk/README.md#list) - Get a list of SAML Connections for an instance
* [create](docs/sdks/samlconnectionssdk/README.md#create) - Create a SAML Connection
* [get](docs/sdks/samlconnectionssdk/README.md#get) - Retrieve a SAML Connection by ID
* [update](docs/sdks/samlconnectionssdk/README.md#update) - Update a SAML Connection
* [delete](docs/sdks/samlconnectionssdk/README.md#delete) - Delete a SAML Connection

### [sessions](docs/sdks/sessions/README.md)

* [list](docs/sdks/sessions/README.md#list) - List all sessions
* [create](docs/sdks/sessions/README.md#create) - Create a new active session
* [get](docs/sdks/sessions/README.md#get) - Retrieve a session
* [revoke](docs/sdks/sessions/README.md#revoke) - Revoke a session
* [~~verify~~](docs/sdks/sessions/README.md#verify) - Verify a session :warning: **Deprecated**
* [create_token](docs/sdks/sessions/README.md#create_token) - Create a session token
* [create_token_from_template](docs/sdks/sessions/README.md#create_token_from_template) - Create a session token from a jwt template

### [sign_in_tokens](docs/sdks/signintokens/README.md)

* [create](docs/sdks/signintokens/README.md#create) - Create sign-in token
* [revoke](docs/sdks/signintokens/README.md#revoke) - Revoke the given sign-in token

### [sign_ups](docs/sdks/signups/README.md)

* [get](docs/sdks/signups/README.md#get) - Retrieve a sign-up by ID
* [update](docs/sdks/signups/README.md#update) - Update a sign-up

### [~~templates~~](docs/sdks/templates/README.md)

* [~~preview~~](docs/sdks/templates/README.md#preview) - Preview changes to a template :warning: **Deprecated**

### [testing_tokens](docs/sdks/testingtokens/README.md)

* [create](docs/sdks/testingtokens/README.md#create) - Retrieve a new testing token

### [users](docs/sdks/users/README.md)

* [list](docs/sdks/users/README.md#list) - List all users
* [create](docs/sdks/users/README.md#create) - Create a new user
* [count](docs/sdks/users/README.md#count) - Count users
* [get](docs/sdks/users/README.md#get) - Retrieve a user
* [update](docs/sdks/users/README.md#update) - Update a user
* [delete](docs/sdks/users/README.md#delete) - Delete a user
* [ban](docs/sdks/users/README.md#ban) - Ban a user
* [unban](docs/sdks/users/README.md#unban) - Unban a user
* [lock](docs/sdks/users/README.md#lock) - Lock a user
* [unlock](docs/sdks/users/README.md#unlock) - Unlock a user
* [set_profile_image](docs/sdks/users/README.md#set_profile_image) - Set user profile image
* [delete_profile_image](docs/sdks/users/README.md#delete_profile_image) - Delete user profile image
* [update_metadata](docs/sdks/users/README.md#update_metadata) - Merge and update a user's metadata
* [get_o_auth_access_token](docs/sdks/users/README.md#get_o_auth_access_token) - Retrieve the OAuth access token of a user
* [get_organization_memberships](docs/sdks/users/README.md#get_organization_memberships) - Retrieve all memberships for a user
* [get_organization_invitations](docs/sdks/users/README.md#get_organization_invitations) - Retrieve all invitations for a user
* [verify_password](docs/sdks/users/README.md#verify_password) - Verify the password of a user
* [verify_totp](docs/sdks/users/README.md#verify_totp) - Verify a TOTP or backup code for a user
* [disable_mfa](docs/sdks/users/README.md#disable_mfa) - Disable a user's MFA methods
* [delete_backup_codes](docs/sdks/users/README.md#delete_backup_codes) - Disable all user's Backup codes
* [delete_passkey](docs/sdks/users/README.md#delete_passkey) - Delete a user passkey
* [delete_web3_wallet](docs/sdks/users/README.md#delete_web3_wallet) - Delete a user web3 wallet
* [delete_totp](docs/sdks/users/README.md#delete_totp) - Delete all the user's TOTPs
* [delete_external_account](docs/sdks/users/README.md#delete_external_account) - Delete External Account
* [get_instance_organization_memberships](docs/sdks/users/README.md#get_instance_organization_memberships) - Get a list of all organization memberships within an instance.

### [waitlist_entries](docs/sdks/waitlistentriessdk/README.md)

* [list](docs/sdks/waitlistentriessdk/README.md#list) - List all waitlist entries
* [create](docs/sdks/waitlistentriessdk/README.md#create) - Create a waitlist entry

### [webhooks](docs/sdks/webhooks/README.md)

* [create_svix_app](docs/sdks/webhooks/README.md#create_svix_app) - Create a Svix app
* [delete_svix_app](docs/sdks/webhooks/README.md#delete_svix_app) - Delete a Svix app
* [generate_svix_auth_url](docs/sdks/webhooks/README.md#generate_svix_auth_url) - Create a Svix Dashboard URL

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.users.set_profile_image(user_id="usr_test123", file={
        "file_name": "example.file",
        "content": open("example.file", "rb"),
        "content_type": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from clerk_backend_api import Clerk
from clerk_backend_api.utils import BackoffStrategy, RetryConfig


with Clerk() as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from clerk_backend_api import Clerk
from clerk_backend_api.utils import BackoffStrategy, RetryConfig


with Clerk(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
) as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `verify_async` method may raise the following exceptions:

| Error Type         | Status Code   | Content Type     |
| ------------------ | ------------- | ---------------- |
| models.ClerkErrors | 400, 401, 404 | application/json |
| models.SDKError    | 4XX, 5XX      | \*/\*            |

### Example

```python
from clerk_backend_api import Clerk, models


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:
    res = None
    try:

        res = clerk.clients.verify(request={
            "token": "jwt_token_example",
        })

        assert res is not None

        # Handle response
        print(res)

    except models.ClerkErrors as e:
        # handle e.data: models.ClerkErrorsData
        raise(e)
    except models.SDKError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from clerk_backend_api import Clerk


with Clerk(
    server_url="https://api.clerk.com/v1",
) as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from clerk_backend_api import Clerk
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Clerk(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from clerk_backend_api import Clerk
from clerk_backend_api.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Clerk(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Clerk` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from clerk_backend_api import Clerk
def main():

    with Clerk() as clerk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Clerk() as clerk:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from clerk_backend_api import Clerk
import logging

logging.basicConfig(level=logging.DEBUG)
s = Clerk(debug_logger=logging.getLogger("clerk_backend_api"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in GA. We recommend pinning usage to a specific package version. This way, you can install the same version each time without breaking changes between major versions unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
