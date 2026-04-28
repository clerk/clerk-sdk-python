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
Each version is identified by its release date, e.g. `2025-04-10`. For more information, please see [Clerk API Versions](https://clerk.com/docs/versioning/available-versions).

Please see https://clerk.com/docs for more information.

More information about the API can be found at https://clerk.com/docs
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [SDK Installation](https://github.com/clerk/clerk-sdk-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/clerk/clerk-sdk-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/clerk/clerk-sdk-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/clerk/clerk-sdk-python/blob/master/#authentication)
  * [Request Authentication](https://github.com/clerk/clerk-sdk-python/blob/master/#request-authentication)
  * [Available Resources and Operations](https://github.com/clerk/clerk-sdk-python/blob/master/#available-resources-and-operations)
  * [File uploads](https://github.com/clerk/clerk-sdk-python/blob/master/#file-uploads)
  * [Retries](https://github.com/clerk/clerk-sdk-python/blob/master/#retries)
  * [Error Handling](https://github.com/clerk/clerk-sdk-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/clerk/clerk-sdk-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/clerk/clerk-sdk-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/clerk/clerk-sdk-python/blob/master/#resource-management)
  * [Debugging](https://github.com/clerk/clerk-sdk-python/blob/master/#debugging)
* [Development](https://github.com/clerk/clerk-sdk-python/blob/master/#development)
  * [Maturity](https://github.com/clerk/clerk-sdk-python/blob/master/#maturity)
  * [Contributions](https://github.com/clerk/clerk-sdk-python/blob/master/#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add clerk-backend-api
```

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
# requires-python = ">=3.10"
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


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.get(email_address_id="email_address_id_example")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():

    async with Clerk(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as clerk:

        res = await clerk.email_addresses.get_async(email_address_id="email_address_id_example")

        # Handle response
        print(res)

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

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="<value>", proxy_url="https://fine-tarragon.info", domain="great-director.net", sign_in_url="https://likable-freckle.net/", use_domain_for_script=False)

    # Use the SDK ...

```
<!-- End Authentication [security] -->

## Request Authentication

Use the client's `authenticate_request` method to authenticate a request from your app's frontend (when using a Clerk frontend SDK) to a Python backend (Django, Flask, and other Python web frameworks). For example the following utility function checks if the user is effectively signed in:

```python
import os
import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.security import authenticate_request
from clerk_backend_api.security.types import AuthenticateRequestOptions

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

### Authenticating Machine Tokens

If you need to authenticate a machine token rather than a session token, this can be done using the `accepts_token` param as such:

```python
import os
import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.security import authenticate_request
from clerk_backend_api.security.types import AuthenticateRequestOptions

def verify_machine_token(request: httpx.Request):
    sdk = Clerk(bearer_auth=os.getenv('CLERK_SECRET_KEY'))
    request_state = sdk.authenticate_request(
        request,
        AuthenticateRequestOptions(
            accepts_token=['oauth_token']  # Only accepts oauth access tokens
        )
    )
    return request_state.is_signed_in
```

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [ActorTokens](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/actortokens/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/actortokens/README.md#create) - Create actor token
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/actortokens/README.md#revoke) - Revoke actor token

### [AgentTasks](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/agenttasks/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/agenttasks/README.md#create) - Create agent task
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/agenttasks/README.md#revoke) - Revoke agent task

### [AllowlistIdentifiers](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/allowlistidentifiers/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/allowlistidentifiers/README.md#list) - List all identifiers on the allow-list
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/allowlistidentifiers/README.md#create) - Add identifier to the allow-list
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/allowlistidentifiers/README.md#delete) - Delete identifier from allow-list

### [APIKeys](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md)

* [create_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#create_api_key) - Create an API Key
* [get_api_keys](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#get_api_keys) - Get API Keys
* [get_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#get_api_key) - Get an API Key by ID
* [update_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#update_api_key) - Update an API Key
* [delete_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#delete_api_key) - Delete an API Key
* [get_api_key_secret](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#get_api_key_secret) - Get an API Key Secret
* [revoke_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#revoke_api_key) - Revoke an API Key
* [verify_api_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/apikeys/README.md#verify_api_key) - Verify an API Key

### [BetaFeatures](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/betafeatures/README.md)

* [update_instance_settings](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/betafeatures/README.md#update_instance_settings) - Update instance settings
* [~~update_production_instance_domain~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/betafeatures/README.md#update_production_instance_domain) - Update production instance domain :warning: **Deprecated**

### [Billing](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md)

* [list_plans](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#list_plans) - List all billing plans
* [list_prices](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#list_prices) - List all billing prices
* [create_price](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#create_price) - Create a custom billing price
* [list_subscription_items](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#list_subscription_items) - List all subscription items
* [cancel_subscription_item](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#cancel_subscription_item) - Cancel a subscription item
* [extend_subscription_item_free_trial](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#extend_subscription_item_free_trial) - Extend free trial for a subscription item
* [create_price_transition](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#create_price_transition) - Create a price transition for a subscription item
* [list_statements](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#list_statements) - List all billing statements
* [get_statement](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#get_statement) - Retrieve a billing statement
* [get_statement_payment_attempts](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/billing/README.md#get_statement_payment_attempts) - List payment attempts for a billing statement

### [BlocklistIdentifiers](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/blocklistidentifierssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/blocklistidentifierssdk/README.md#list) - List all identifiers on the block-list
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/blocklistidentifierssdk/README.md#create) - Add identifier to the block-list
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/blocklistidentifierssdk/README.md#delete) - Delete identifier from block-list

### [Clients](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/clients/README.md)

* [~~list~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/clients/README.md#list) - List all clients :warning: **Deprecated**
* [verify](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/clients/README.md#verify) - Verify a client
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/clients/README.md#get) - Get a client

### [Domains](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/domainssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/domainssdk/README.md#list) - List all instance domains
* [add](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/domainssdk/README.md#add) - Add a domain
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/domainssdk/README.md#delete) - Delete a satellite domain
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/domainssdk/README.md#update) - Update a domain

### [EmailAddresses](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailaddresses/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailaddresses/README.md#create) - Create an email address
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailaddresses/README.md#get) - Retrieve an email address
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailaddresses/README.md#delete) - Delete an email address
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailaddresses/README.md#update) - Update an email address

### [~~EmailAndSmsTemplates~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailandsmstemplates/README.md)

* [~~upsert~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailandsmstemplates/README.md#upsert) - Update a template for a given type and slug :warning: **Deprecated**

### [~~EmailSMSTemplates~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailsmstemplates/README.md)

* [~~list~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailsmstemplates/README.md#list) - List all templates :warning: **Deprecated**
* [~~get~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailsmstemplates/README.md#get) - Retrieve a template :warning: **Deprecated**
* [~~revert~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailsmstemplates/README.md#revert) - Revert a template :warning: **Deprecated**
* [~~toggle_template_delivery~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/emailsmstemplates/README.md#toggle_template_delivery) - Toggle the delivery by Clerk for a template of a given type and slug :warning: **Deprecated**

### [EnterpriseConnections](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md#list) - List enterprise connections
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md#create) - Create an enterprise connection
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md#get) - Retrieve an enterprise connection
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md#update) - Update an enterprise connection
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/enterpriseconnectionssdk/README.md#delete) - Delete an enterprise connection

### [InstanceSettings](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md)

* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#get) - Fetch the current instance
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#update) - Update instance settings
* [update_restrictions](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#update_restrictions) - Update instance restrictions
* [get_o_auth_application_settings](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#get_o_auth_application_settings) - Get OAuth application settings
* [update_o_auth_application_settings](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#update_o_auth_application_settings) - Update OAuth application settings
* [change_domain](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#change_domain) - Update production instance domain
* [update_organization_settings](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#update_organization_settings) - Update instance organization settings
* [get_instance_protect](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#get_instance_protect) - Get instance protect settings
* [update_instance_protect](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/instancesettingssdk/README.md#update_instance_protect) - Update instance protect settings

### [Invitations](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/invitations/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/invitations/README.md#create) - Create an invitation
* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/invitations/README.md#list) - List all invitations
* [bulk_create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/invitations/README.md#bulk_create) - Create multiple invitations
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/invitations/README.md#revoke) - Revokes an invitation

### [Jwks](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwkssdk/README.md)

* [get_jwks](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwkssdk/README.md#get_jwks) - Retrieve the JSON Web Key Set of the instance

### [JwtTemplates](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md#list) - List all templates
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md#create) - Create a JWT template
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md#get) - Retrieve a template
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md#update) - Update a JWT template
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/jwttemplates/README.md#delete) - Delete a Template

### [M2m](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/m2m/README.md)

* [create_token](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/m2m/README.md#create_token) - Create a M2M Token
* [list_tokens](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/m2m/README.md#list_tokens) - Get M2M Tokens
* [revoke_token](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/m2m/README.md#revoke_token) - Revoke a M2M Token
* [verify_token](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/m2m/README.md#verify_token) - Verify a M2M Token

### [Machines](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#list) - Get a list of machines for an instance
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#create) - Create a machine
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#get) - Retrieve a machine
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#update) - Update a machine
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#delete) - Delete a machine
* [get_secret_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#get_secret_key) - Retrieve a machine secret key
* [rotate_secret_key](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#rotate_secret_key) - Rotate a machine's secret key
* [create_scope](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#create_scope) - Create a machine scope
* [delete_scope](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/machines/README.md#delete_scope) - Delete a machine scope

### [Miscellaneous](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/miscellaneous/README.md)

* [get_public_interstitial](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/miscellaneous/README.md#get_public_interstitial) - Returns the markup for the interstitial page

### [OauthAccessTokens](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthaccesstokens/README.md)

* [verify](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthaccesstokens/README.md#verify) - Verify an OAuth Access Token

### [OauthApplications](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#list) - Get a list of OAuth applications for an instance
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#create) - Create an OAuth application
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#get) - Retrieve an OAuth application by ID
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#update) - Update an OAuth application
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#delete) - Delete an OAuth application
* [upload_logo](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#upload_logo) - Upload a logo for the OAuth application
* [rotate_secret](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/oauthapplicationssdk/README.md#rotate_secret) - Rotate the client secret of the given OAuth application

### [OrganizationDomains](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md#create) - Create a new organization domain.
* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md#list) - Get a list of all domains of an organization.
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md#update) - Update an organization domain.
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md#delete) - Remove a domain from an organization.
* [list_all](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationdomainssdk/README.md#list_all) - List all organization domains

### [OrganizationInvitations](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md)

* [get_all](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#get_all) - Get a list of organization invitations for the current instance
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#create) - Create and send an organization invitation
* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#list) - Get a list of organization invitations
* [bulk_create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#bulk_create) - Bulk create and send organization invitations
* [~~list_pending~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#list_pending) - Get a list of pending organization invitations :warning: **Deprecated**
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#get) - Retrieve an organization invitation by ID
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationinvitationssdk/README.md#revoke) - Revoke a pending organization invitation

### [OrganizationMemberships](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md#create) - Create a new organization membership
* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md#list) - Get a list of all members of an organization
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md#update) - Update an organization membership
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md#delete) - Remove a member from an organization
* [update_metadata](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationmembershipssdk/README.md#update_metadata) - Merge and update organization membership metadata

### [OrganizationPermissions](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md#list) - Get a list of all organization permissions
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md#create) - Create a new organization permission
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md#get) - Get an organization permission
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md#update) - Update an organization permission
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationpermissions/README.md#delete) - Delete an organization permission

### [OrganizationRoles](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#list) - Get a list of organization roles
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#create) - Create an organization role
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#get) - Retrieve an organization role
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#update) - Update an organization role
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#delete) - Delete an organization role
* [assign_permission](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#assign_permission) - Assign a permission to an organization role
* [remove_permission](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationroles/README.md#remove_permission) - Remove a permission from an organization role

### [Organizations](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#list) - Get a list of organizations for an instance
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#create) - Create an organization
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#get) - Retrieve an organization by ID or slug
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#update) - Update an organization
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#delete) - Delete an organization
* [merge_metadata](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#merge_metadata) - Merge and update metadata for an organization
* [upload_logo](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#upload_logo) - Upload a logo for the organization
* [delete_logo](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#delete_logo) - Delete the organization's logo.
* [get_billing_subscription](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#get_billing_subscription) - Retrieve an organization's billing subscription
* [get_billing_credit_balance](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#get_billing_credit_balance) - Retrieve an organization's credit balance
* [adjust_billing_credit_balance](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/organizationssdk/README.md#adjust_billing_credit_balance) - Adjust an organization's credit balance

### [PhoneNumbers](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/phonenumbers/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/phonenumbers/README.md#create) - Create a phone number
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/phonenumbers/README.md#get) - Retrieve a phone number
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/phonenumbers/README.md#delete) - Delete a phone number
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/phonenumbers/README.md#update) - Update a phone number

### [ProxyChecks](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/proxychecks/README.md)

* [verify](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/proxychecks/README.md#verify) - Verify the proxy configuration for your domain

### [RedirectUrls](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/redirecturls/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/redirecturls/README.md#list) - List all redirect URLs
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/redirecturls/README.md#create) - Create a redirect URL
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/redirecturls/README.md#get) - Retrieve a redirect URL
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/redirecturls/README.md#delete) - Delete a redirect URL

### [RoleSets](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#list) - Get a list of role sets
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#create) - Create a role set
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#get) - Retrieve a role set
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#update) - Update a role set
* [replace](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#replace) - Replace a role set
* [add_roles](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#add_roles) - Add roles to a role set
* [replace_role](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/rolesetssdk/README.md#replace_role) - Replace a role in a role set

### [~~SamlConnections~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md)

* [~~list~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md#list) - Get a list of SAML Connections for an instance :warning: **Deprecated**
* [~~create~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md#create) - Create a SAML Connection :warning: **Deprecated**
* [~~get~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md#get) - Retrieve a SAML Connection by ID :warning: **Deprecated**
* [~~update~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md#update) - Update a SAML Connection :warning: **Deprecated**
* [~~delete~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/samlconnectionssdk/README.md#delete) - Delete a SAML Connection :warning: **Deprecated**

### [Sessions](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#list) - List all sessions
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#create) - Create a new active session
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#get) - Retrieve a session
* [refresh](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#refresh) - Refresh a session
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#revoke) - Revoke a session
* [create_token](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#create_token) - Create a session token
* [create_token_from_template](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/sessions/README.md#create_token_from_template) - Create a session token from a JWT template

### [SignInTokens](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signintokens/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signintokens/README.md#create) - Create sign-in token
* [revoke](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signintokens/README.md#revoke) - Revoke the given sign-in token

### [SignUps](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signups/README.md)

* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signups/README.md#get) - Retrieve a sign-up by ID
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/signups/README.md#update) - Update a sign-up

### [~~Templates~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/templates/README.md)

* [~~preview~~](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/templates/README.md#preview) - Preview changes to a template :warning: **Deprecated**

### [TestingTokens](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/testingtokens/README.md)

* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/testingtokens/README.md#create) - Retrieve a new testing token

### [Users](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#list) - List all users
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#create) - Create a new user
* [count](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#count) - Count users
* [get](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get) - Retrieve a user
* [update](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#update) - Update a user
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete) - Delete a user
* [ban](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#ban) - Ban a user
* [unban](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#unban) - Unban a user
* [bulk_ban](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#bulk_ban) - Ban multiple users
* [bulk_unban](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#bulk_unban) - Unban multiple users
* [lock](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#lock) - Lock a user
* [unlock](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#unlock) - Unlock a user
* [set_profile_image](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#set_profile_image) - Set user profile image
* [delete_profile_image](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_profile_image) - Delete user profile image
* [update_metadata](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#update_metadata) - Merge and update a user's metadata
* [get_billing_subscription](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_billing_subscription) - Retrieve a user's billing subscription
* [get_billing_credit_balance](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_billing_credit_balance) - Retrieve a user's credit balance
* [adjust_billing_credit_balance](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#adjust_billing_credit_balance) - Adjust a user's credit balance
* [get_o_auth_access_token](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_o_auth_access_token) - Retrieve the OAuth access token of a user
* [get_organization_memberships](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_organization_memberships) - Retrieve all memberships for a user
* [get_organization_invitations](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_organization_invitations) - Retrieve all invitations for a user
* [verify_password](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#verify_password) - Verify the password of a user
* [verify_totp](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#verify_totp) - Verify a TOTP or backup code for a user
* [disable_mfa](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#disable_mfa) - Disable a user's MFA methods
* [delete_backup_codes](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_backup_codes) - Disable all user's Backup codes
* [delete_passkey](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_passkey) - Delete a user passkey
* [delete_web3_wallet](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_web3_wallet) - Delete a user web3 wallet
* [delete_totp](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_totp) - Delete all the user's TOTPs
* [delete_external_account](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#delete_external_account) - Delete External Account
* [set_password_compromised](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#set_password_compromised) - Set a user's password as compromised
* [unset_password_compromised](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#unset_password_compromised) - Unset a user's password as compromised
* [get_instance_organization_memberships](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/users/README.md#get_instance_organization_memberships) - Get a list of all organization memberships within an instance.

### [WaitlistEntries](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md)

* [list](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#list) - List all waitlist entries
* [create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#create) - Create a waitlist entry
* [bulk_create](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#bulk_create) - Create multiple waitlist entries
* [delete](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#delete) - Delete a pending waitlist entry
* [invite](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#invite) - Invite a waitlist entry
* [reject](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/waitlistentriessdk/README.md#reject) - Reject a waitlist entry

### [Webhooks](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/webhooks/README.md)

* [create_svix_app](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/webhooks/README.md#create_svix_app) - Create a Svix app
* [delete_svix_app](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/webhooks/README.md#delete_svix_app) - Delete a Svix app
* [generate_svix_auth_url](https://github.com/clerk/clerk-sdk-python/blob/master/docs/sdks/webhooks/README.md#generate_svix_auth_url) - Create a Svix Dashboard URL

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
    })

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

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="<value>", proxy_url="https://fine-tarragon.info", domain="great-director.net", sign_in_url="https://likable-freckle.net/", use_domain_for_script=False,
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

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="<value>", proxy_url="https://fine-tarragon.info", domain="great-director.net", sign_in_url="https://likable-freckle.net/", use_domain_for_script=False)

    # Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`ClerkBaseError`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/clerkbaseerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/clerk/clerk-sdk-python/blob/master/#error-classes). |

### Example
```python
import clerk_backend_api
from clerk_backend_api import Clerk, models


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:
    res = None
    try:

        res = clerk.clients.verify(request={
            "token": "jwt_token_example",
        })

        # Handle response
        print(res)


    except models.ClerkBaseError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, models.ClerkErrors):
            print(e.data.errors)  # List[clerk_backend_api.ClerkError]
            print(e.data.meta)  # Optional[clerk_backend_api.ClerkErrorsMeta]
```

### Error Classes
**Primary errors:**
* [`ClerkBaseError`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/clerkbaseerror.py): The base class for HTTP error responses.
  * [`ClerkErrors`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/clerkerrors.py): Request was not successful. *

<details><summary>Less common errors (32)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`ClerkBaseError`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/clerkbaseerror.py)**:
* [`CreateAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/createapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`GetAPIKeysAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeysapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`GetAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`UpdateAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/updateapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`DeleteAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/deleteapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`GetAPIKeySecretAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeysecretapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`RevokeAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/revokeapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`VerifyAPIKeyAPIKeysResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifyapikeyapikeysresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`CreateM2MTokenM2mResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/createm2mtokenm2mresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`GetM2MTokensM2mResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getm2mtokensm2mresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`RevokeM2MTokenM2mResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/revokem2mtokenm2mresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`VerifyM2MTokenM2mResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifym2mtokenm2mresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`VerifyOAuthAccessTokenOauthAccessTokensResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifyoauthaccesstokenoauthaccesstokensresponsebody.py): 400 Bad Request. Status code `400`. Applicable to 1 of 207 methods.*
* [`GetM2MTokensM2mResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getm2mtokensm2mresponseresponsebody.py): 403 Forbidden. Status code `403`. Applicable to 1 of 207 methods.*
* [`GetAPIKeysAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeysapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`GetAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeyapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`UpdateAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/updateapikeyapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`DeleteAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/deleteapikeyapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`GetAPIKeySecretAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getapikeysecretapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`RevokeAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/revokeapikeyapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`VerifyAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifyapikeyapikeysresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`GetM2MTokensM2mResponse404ResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/getm2mtokensm2mresponse404responsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`RevokeM2MTokenM2mResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/revokem2mtokenm2mresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`VerifyM2MTokenM2mResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifym2mtokenm2mresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`VerifyOAuthAccessTokenOauthAccessTokensResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/verifyoauthaccesstokenoauthaccesstokensresponseresponsebody.py): 404 Not Found. Status code `404`. Applicable to 1 of 207 methods.*
* [`CreateAPIKeyAPIKeysResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/createapikeyapikeysresponseresponsebody.py): 409 Conflict. Status code `409`. Applicable to 1 of 207 methods.*
* [`CreateM2MTokenM2mResponseResponseBody`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/createm2mtokenm2mresponseresponsebody.py): 409 Conflict. Status code `409`. Applicable to 1 of 207 methods.*
* [`ResponseValidationError`](https://github.com/clerk/clerk-sdk-python/blob/master/./src/clerk_backend_api/models/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/clerk/clerk-sdk-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
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

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="<value>", proxy_url="https://fine-tarragon.info", domain="great-director.net", sign_in_url="https://likable-freckle.net/", use_domain_for_script=False)

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

    with Clerk(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as clerk:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Clerk(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as clerk:
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
