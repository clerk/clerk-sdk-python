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

Clerk Backend API: The Clerk REST Backend API, meant to be accessed by backend
servers.

### Versions

When the API changes in a way that isn't compatible with older versions, a new version is released.
Each version is identified by its release date, e.g. `2021-02-05`. For more information, please see [Clerk API Versions](https://clerk.com/docs/backend-requests/versioning/overview).


Please see https://clerk.com/docs for more information.

More information about the API can be found at https://clerk.com/docs
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [File uploads](#file-uploads)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

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

s = Clerk()


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():
    s = Clerk()
    await s.miscellaneous.get_public_interstitial_async(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [miscellaneous](docs/sdks/miscellaneous/README.md)

* [get_public_interstitial](docs/sdks/miscellaneous/README.md#get_public_interstitial) - Returns the markup for the interstitial page

### [jwks](docs/sdks/jwks/README.md)

* [get_jwks](docs/sdks/jwks/README.md#get_jwks) - Retrieve the JSON Web Key Set of the instance

### [clients](docs/sdks/clients/README.md)

* [~~get_client_list~~](docs/sdks/clients/README.md#get_client_list) - List all clients :warning: **Deprecated**
* [verify_client](docs/sdks/clients/README.md#verify_client) - Verify a client
* [get_client](docs/sdks/clients/README.md#get_client) - Get a client

### [email_addresses](docs/sdks/emailaddresses/README.md)

* [create_email_address](docs/sdks/emailaddresses/README.md#create_email_address) - Create an email address
* [get_email_address](docs/sdks/emailaddresses/README.md#get_email_address) - Retrieve an email address
* [delete_email_address](docs/sdks/emailaddresses/README.md#delete_email_address) - Delete an email address
* [update_email_address](docs/sdks/emailaddresses/README.md#update_email_address) - Update an email address

### [phone_numbers](docs/sdks/phonenumbers/README.md)

* [create_phone_number](docs/sdks/phonenumbers/README.md#create_phone_number) - Create a phone number
* [get_phone_number](docs/sdks/phonenumbers/README.md#get_phone_number) - Retrieve a phone number
* [delete_phone_number](docs/sdks/phonenumbers/README.md#delete_phone_number) - Delete a phone number
* [update_phone_number](docs/sdks/phonenumbers/README.md#update_phone_number) - Update a phone number

### [sessions](docs/sdks/sessions/README.md)

* [get_session_list](docs/sdks/sessions/README.md#get_session_list) - List all sessions
* [get_session](docs/sdks/sessions/README.md#get_session) - Retrieve a session
* [revoke_session](docs/sdks/sessions/README.md#revoke_session) - Revoke a session
* [~~verify_session~~](docs/sdks/sessions/README.md#verify_session) - Verify a session :warning: **Deprecated**
* [create_session_token_from_template](docs/sdks/sessions/README.md#create_session_token_from_template) - Create a session token from a jwt template

### [email_and_sms_templates](docs/sdks/emailandsmstemplates/README.md)

* [~~get_template_list~~](docs/sdks/emailandsmstemplates/README.md#get_template_list) - List all templates :warning: **Deprecated**
* [~~get_template~~](docs/sdks/emailandsmstemplates/README.md#get_template) - Retrieve a template :warning: **Deprecated**
* [~~upsert_template~~](docs/sdks/emailandsmstemplates/README.md#upsert_template) - Update a template for a given type and slug :warning: **Deprecated**
* [~~revert_template~~](docs/sdks/emailandsmstemplates/README.md#revert_template) - Revert a template :warning: **Deprecated**
* [~~preview_template~~](docs/sdks/emailandsmstemplates/README.md#preview_template) - Preview changes to a template :warning: **Deprecated**
* [~~toggle_template_delivery~~](docs/sdks/emailandsmstemplates/README.md#toggle_template_delivery) - Toggle the delivery by Clerk for a template of a given type and slug :warning: **Deprecated**

### [users](docs/sdks/users/README.md)

* [get_user_list](docs/sdks/users/README.md#get_user_list) - List all users
* [create_user](docs/sdks/users/README.md#create_user) - Create a new user
* [get_users_count](docs/sdks/users/README.md#get_users_count) - Count users
* [get_user](docs/sdks/users/README.md#get_user) - Retrieve a user
* [update_user](docs/sdks/users/README.md#update_user) - Update a user
* [delete_user](docs/sdks/users/README.md#delete_user) - Delete a user
* [ban_user](docs/sdks/users/README.md#ban_user) - Ban a user
* [unban_user](docs/sdks/users/README.md#unban_user) - Unban a user
* [lock_user](docs/sdks/users/README.md#lock_user) - Lock a user
* [unlock_user](docs/sdks/users/README.md#unlock_user) - Unlock a user
* [set_user_profile_image](docs/sdks/users/README.md#set_user_profile_image) - Set user profile image
* [delete_user_profile_image](docs/sdks/users/README.md#delete_user_profile_image) - Delete user profile image
* [update_user_metadata](docs/sdks/users/README.md#update_user_metadata) - Merge and update a user's metadata
* [get_o_auth_access_token](docs/sdks/users/README.md#get_o_auth_access_token) - Retrieve the OAuth access token of a user
* [users_get_organization_memberships](docs/sdks/users/README.md#users_get_organization_memberships) - Retrieve all memberships for a user
* [users_get_organization_invitations](docs/sdks/users/README.md#users_get_organization_invitations) - Retrieve all invitations for a user
* [verify_password](docs/sdks/users/README.md#verify_password) - Verify the password of a user
* [verify_totp](docs/sdks/users/README.md#verify_totp) - Verify a TOTP or backup code for a user
* [disable_mfa](docs/sdks/users/README.md#disable_mfa) - Disable a user's MFA methods
* [delete_backup_code](docs/sdks/users/README.md#delete_backup_code) - Disable all user's Backup codes
* [user_passkey_delete](docs/sdks/users/README.md#user_passkey_delete) - Delete a user passkey
* [user_web3_wallet_delete](docs/sdks/users/README.md#user_web3_wallet_delete) - Delete a user web3 wallet
* [create_user_totp](docs/sdks/users/README.md#create_user_totp) - Create a TOTP for a user
* [delete_totp](docs/sdks/users/README.md#delete_totp) - Delete all the user's TOTPs
* [delete_external_account](docs/sdks/users/README.md#delete_external_account) - Delete External Account

### [invitations](docs/sdks/invitations/README.md)

* [create_invitation](docs/sdks/invitations/README.md#create_invitation) - Create an invitation
* [list_invitations](docs/sdks/invitations/README.md#list_invitations) - List all invitations
* [revoke_invitation](docs/sdks/invitations/README.md#revoke_invitation) - Revokes an invitation

### [organization_invitations](docs/sdks/organizationinvitationssdk/README.md)

* [list_instance_organization_invitations](docs/sdks/organizationinvitationssdk/README.md#list_instance_organization_invitations) - Get a list of organization invitations for the current instance
* [create_organization_invitation](docs/sdks/organizationinvitationssdk/README.md#create_organization_invitation) - Create and send an organization invitation
* [list_organization_invitations](docs/sdks/organizationinvitationssdk/README.md#list_organization_invitations) - Get a list of organization invitations
* [create_organization_invitation_bulk](docs/sdks/organizationinvitationssdk/README.md#create_organization_invitation_bulk) - Bulk create and send organization invitations
* [~~list_pending_organization_invitations~~](docs/sdks/organizationinvitationssdk/README.md#list_pending_organization_invitations) - Get a list of pending organization invitations :warning: **Deprecated**
* [get_organization_invitation](docs/sdks/organizationinvitationssdk/README.md#get_organization_invitation) - Retrieve an organization invitation by ID
* [revoke_organization_invitation](docs/sdks/organizationinvitationssdk/README.md#revoke_organization_invitation) - Revoke a pending organization invitation

### [allow_list_block_list](docs/sdks/allowlistblocklist/README.md)

* [list_allowlist_identifiers](docs/sdks/allowlistblocklist/README.md#list_allowlist_identifiers) - List all identifiers on the allow-list
* [create_allowlist_identifier](docs/sdks/allowlistblocklist/README.md#create_allowlist_identifier) - Add identifier to the allow-list
* [delete_allowlist_identifier](docs/sdks/allowlistblocklist/README.md#delete_allowlist_identifier) - Delete identifier from allow-list
* [list_blocklist_identifiers](docs/sdks/allowlistblocklist/README.md#list_blocklist_identifiers) - List all identifiers on the block-list
* [create_blocklist_identifier](docs/sdks/allowlistblocklist/README.md#create_blocklist_identifier) - Add identifier to the block-list
* [delete_blocklist_identifier](docs/sdks/allowlistblocklist/README.md#delete_blocklist_identifier) - Delete identifier from block-list

### [beta_features](docs/sdks/betafeatures/README.md)

* [update_instance_auth_config](docs/sdks/betafeatures/README.md#update_instance_auth_config) - Update instance settings
* [~~update_production_instance_domain~~](docs/sdks/betafeatures/README.md#update_production_instance_domain) - Update production instance domain :warning: **Deprecated**
* [change_production_instance_domain](docs/sdks/betafeatures/README.md#change_production_instance_domain) - Update production instance domain

### [actor_tokens](docs/sdks/actortokens/README.md)

* [create_actor_token](docs/sdks/actortokens/README.md#create_actor_token) - Create actor token
* [revoke_actor_token](docs/sdks/actortokens/README.md#revoke_actor_token) - Revoke actor token

### [domains](docs/sdks/domainssdk/README.md)

* [list_domains](docs/sdks/domainssdk/README.md#list_domains) - List all instance domains
* [add_domain](docs/sdks/domainssdk/README.md#add_domain) - Add a domain
* [delete_domain](docs/sdks/domainssdk/README.md#delete_domain) - Delete a satellite domain
* [update_domain](docs/sdks/domainssdk/README.md#update_domain) - Update a domain

### [instance_settings](docs/sdks/instancesettingssdk/README.md)

* [update_instance](docs/sdks/instancesettingssdk/README.md#update_instance) - Update instance settings
* [update_instance_restrictions](docs/sdks/instancesettingssdk/README.md#update_instance_restrictions) - Update instance restrictions
* [update_instance_organization_settings](docs/sdks/instancesettingssdk/README.md#update_instance_organization_settings) - Update instance organization settings

### [webhooks](docs/sdks/webhooks/README.md)

* [create_svix_app](docs/sdks/webhooks/README.md#create_svix_app) - Create a Svix app
* [delete_svix_app](docs/sdks/webhooks/README.md#delete_svix_app) - Delete a Svix app
* [generate_svix_auth_url](docs/sdks/webhooks/README.md#generate_svix_auth_url) - Create a Svix Dashboard URL

### [jwt_templates](docs/sdks/jwttemplates/README.md)

* [list_jwt_templates](docs/sdks/jwttemplates/README.md#list_jwt_templates) - List all templates
* [create_jwt_template](docs/sdks/jwttemplates/README.md#create_jwt_template) - Create a JWT template
* [get_jwt_template](docs/sdks/jwttemplates/README.md#get_jwt_template) - Retrieve a template
* [update_jwt_template](docs/sdks/jwttemplates/README.md#update_jwt_template) - Update a JWT template
* [delete_jwt_template](docs/sdks/jwttemplates/README.md#delete_jwt_template) - Delete a Template

### [organizations](docs/sdks/organizationssdk/README.md)

* [list_organizations](docs/sdks/organizationssdk/README.md#list_organizations) - Get a list of organizations for an instance
* [create_organization](docs/sdks/organizationssdk/README.md#create_organization) - Create an organization
* [get_organization](docs/sdks/organizationssdk/README.md#get_organization) - Retrieve an organization by ID or slug
* [update_organization](docs/sdks/organizationssdk/README.md#update_organization) - Update an organization
* [delete_organization](docs/sdks/organizationssdk/README.md#delete_organization) - Delete an organization
* [merge_organization_metadata](docs/sdks/organizationssdk/README.md#merge_organization_metadata) - Merge and update metadata for an organization
* [upload_organization_logo](docs/sdks/organizationssdk/README.md#upload_organization_logo) - Upload a logo for the organization
* [delete_organization_logo](docs/sdks/organizationssdk/README.md#delete_organization_logo) - Delete the organization's logo.

### [organization_memberships](docs/sdks/organizationmembershipssdk/README.md)

* [create_organization_membership](docs/sdks/organizationmembershipssdk/README.md#create_organization_membership) - Create a new organization membership
* [list_organization_memberships](docs/sdks/organizationmembershipssdk/README.md#list_organization_memberships) - Get a list of all members of an organization
* [update_organization_membership](docs/sdks/organizationmembershipssdk/README.md#update_organization_membership) - Update an organization membership
* [delete_organization_membership](docs/sdks/organizationmembershipssdk/README.md#delete_organization_membership) - Remove a member from an organization
* [update_organization_membership_metadata](docs/sdks/organizationmembershipssdk/README.md#update_organization_membership_metadata) - Merge and update organization membership metadata
* [instance_get_organization_memberships](docs/sdks/organizationmembershipssdk/README.md#instance_get_organization_memberships) - Get a list of all organization memberships within an instance.

### [organization_domains](docs/sdks/organizationdomainssdk/README.md)

* [create_organization_domain](docs/sdks/organizationdomainssdk/README.md#create_organization_domain) - Create a new organization domain.
* [list_organization_domains](docs/sdks/organizationdomainssdk/README.md#list_organization_domains) - Get a list of all domains of an organization.
* [delete_organization_domain](docs/sdks/organizationdomainssdk/README.md#delete_organization_domain) - Remove a domain from an organization.

### [organization_domain](docs/sdks/organizationdomainsdk/README.md)

* [update_organization_domain](docs/sdks/organizationdomainsdk/README.md#update_organization_domain) - Update an organization domain.

### [proxy_checks](docs/sdks/proxychecks/README.md)

* [verify_domain_proxy](docs/sdks/proxychecks/README.md#verify_domain_proxy) - Verify the proxy configuration for your domain

### [redirect_ur_ls](docs/sdks/redirecturls/README.md)

* [list_redirect_ur_ls](docs/sdks/redirecturls/README.md#list_redirect_ur_ls) - List all redirect URLs
* [create_redirect_url](docs/sdks/redirecturls/README.md#create_redirect_url) - Create a redirect URL
* [get_redirect_url](docs/sdks/redirecturls/README.md#get_redirect_url) - Retrieve a redirect URL
* [delete_redirect_url](docs/sdks/redirecturls/README.md#delete_redirect_url) - Delete a redirect URL

### [sign_in_tokens](docs/sdks/signintokens/README.md)

* [create_sign_in_token](docs/sdks/signintokens/README.md#create_sign_in_token) - Create sign-in token
* [revoke_sign_in_token](docs/sdks/signintokens/README.md#revoke_sign_in_token) - Revoke the given sign-in token

### [sign_ups](docs/sdks/signups/README.md)

* [update_sign_up](docs/sdks/signups/README.md#update_sign_up) - Update a sign-up

### [o_auth_applications](docs/sdks/oauthapplicationssdk/README.md)

* [list_o_auth_applications](docs/sdks/oauthapplicationssdk/README.md#list_o_auth_applications) - Get a list of OAuth applications for an instance
* [create_o_auth_application](docs/sdks/oauthapplicationssdk/README.md#create_o_auth_application) - Create an OAuth application
* [get_o_auth_application](docs/sdks/oauthapplicationssdk/README.md#get_o_auth_application) - Retrieve an OAuth application by ID
* [update_o_auth_application](docs/sdks/oauthapplicationssdk/README.md#update_o_auth_application) - Update an OAuth application
* [delete_o_auth_application](docs/sdks/oauthapplicationssdk/README.md#delete_o_auth_application) - Delete an OAuth application
* [rotate_o_auth_application_secret](docs/sdks/oauthapplicationssdk/README.md#rotate_o_auth_application_secret) - Rotate the client secret of the given OAuth application

### [saml_connections](docs/sdks/samlconnectionssdk/README.md)

* [list_saml_connections](docs/sdks/samlconnectionssdk/README.md#list_saml_connections) - Get a list of SAML Connections for an instance
* [create_saml_connection](docs/sdks/samlconnectionssdk/README.md#create_saml_connection) - Create a SAML Connection
* [get_saml_connection](docs/sdks/samlconnectionssdk/README.md#get_saml_connection) - Retrieve a SAML Connection by ID
* [update_saml_connection](docs/sdks/samlconnectionssdk/README.md#update_saml_connection) - Update a SAML Connection
* [delete_saml_connection](docs/sdks/samlconnectionssdk/README.md#delete_saml_connection) - Delete a SAML Connection

### [testing_tokens](docs/sdks/testingtokens/README.md)

* [create_testing_token](docs/sdks/testingtokens/README.md#create_testing_token) - Retrieve a new testing token
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

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.set_user_profile_image(user_id="usr_test123", file={
    "file_name": "your_file_here",
    "content": open("<file_path>", "rb"),
    "content_type": "<value>",
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from clerk.utils import BackoffStrategy, RetryConfig
from clerk_backend_api import Clerk

s = Clerk()


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d",
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

# Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from clerk.utils import BackoffStrategy, RetryConfig
from clerk_backend_api import Clerk

s = Clerk(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
)


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object       | Status Code        | Content Type       |
| ------------------ | ------------------ | ------------------ |
| models.ClerkErrors | 400,401,410,422    | application/json   |
| models.SDKError    | 4xx-5xx            | */*                |

### Example

```python
from clerk_backend_api import Clerk, models

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

res = None
try:
    res = s.clients.get_client_list(limit=20, offset=10)

except models.ClerkErrors as e:
    # handle e.data: models.ClerkErrorsData
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.clerk.com/v1` | None |

#### Example

```python
from clerk_backend_api import Clerk

s = Clerk(
    server_idx=0,
)


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from clerk_backend_api import Clerk

s = Clerk(
    server_url="https://api.clerk.com/v1",
)


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
from clerk_backend_api import Clerk

s = Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...

```
<!-- End Authentication [security] -->

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

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
