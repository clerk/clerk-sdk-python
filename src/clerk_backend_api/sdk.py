"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from clerk_backend_api import models, utils
from clerk_backend_api._hooks import SDKHooks
from clerk_backend_api.types import OptionalNullable, UNSET
import httpx
import importlib
from typing import Any, Callable, Dict, Optional, TYPE_CHECKING, Union, cast
import weakref

# region imports
from .security import (
    AuthenticateRequestOptions,
    RequestState,
    authenticate_request,
    Requestish,
)
# endregion imports

if TYPE_CHECKING:
    from clerk_backend_api.actortokens import ActorTokens
    from clerk_backend_api.allowlistidentifiers import AllowlistIdentifiers
    from clerk_backend_api.awscredentials import AwsCredentials
    from clerk_backend_api.betafeatures import BetaFeatures
    from clerk_backend_api.blocklistidentifiers_sdk import BlocklistIdentifiersSDK
    from clerk_backend_api.clients import Clients
    from clerk_backend_api.domains_sdk import DomainsSDK
    from clerk_backend_api.emailaddresses import EmailAddresses
    from clerk_backend_api.emailandsmstemplates import EmailAndSmsTemplates
    from clerk_backend_api.emailsmstemplates import EmailSMSTemplates
    from clerk_backend_api.experimentalaccountlessapplications import (
        ExperimentalAccountlessApplications,
    )
    from clerk_backend_api.instancesettings_sdk import InstanceSettingsSDK
    from clerk_backend_api.invitations import Invitations
    from clerk_backend_api.jwks_sdk import JwksSDK
    from clerk_backend_api.jwttemplates import JwtTemplates
    from clerk_backend_api.machines import Machines
    from clerk_backend_api.machinetokens import MachineTokens
    from clerk_backend_api.management import Management
    from clerk_backend_api.miscellaneous import Miscellaneous
    from clerk_backend_api.oauthaccesstokens import OauthAccessTokens
    from clerk_backend_api.oauthapplications_sdk import OauthApplicationsSDK
    from clerk_backend_api.organizationdomains_sdk import OrganizationDomainsSDK
    from clerk_backend_api.organizationinvitations_sdk import OrganizationInvitationsSDK
    from clerk_backend_api.organizationmemberships_sdk import OrganizationMembershipsSDK
    from clerk_backend_api.organizations_sdk import OrganizationsSDK
    from clerk_backend_api.phonenumbers import PhoneNumbers
    from clerk_backend_api.proxychecks import ProxyChecks
    from clerk_backend_api.redirecturls import RedirectUrls
    from clerk_backend_api.samlconnections_sdk import SamlConnectionsSDK
    from clerk_backend_api.sessions import Sessions
    from clerk_backend_api.signintokens import SignInTokens
    from clerk_backend_api.signups import SignUps
    from clerk_backend_api.templates import Templates
    from clerk_backend_api.testingtokens import TestingTokens
    from clerk_backend_api.users import Users
    from clerk_backend_api.waitlistentries_sdk import WaitlistEntriesSDK
    from clerk_backend_api.webhooks import Webhooks


class Clerk(BaseSDK):
    r"""Clerk Backend API: The Clerk REST Backend API, meant to be accessed by backend servers.

    ### Versions

    When the API changes in a way that isn't compatible with older versions, a new version is released.
    Each version is identified by its release date, e.g. `2025-04-10`. For more information, please see [Clerk API Versions](https://clerk.com/docs/versioning/available-versions).

    Please see https://clerk.com/docs for more information.
    https://clerk.com/docs
    """

    miscellaneous: "Miscellaneous"
    jwks: "JwksSDK"
    aws_credentials: "AwsCredentials"
    clients: "Clients"
    email_addresses: "EmailAddresses"
    phone_numbers: "PhoneNumbers"
    sessions: "Sessions"
    email_sms_templates: "EmailSMSTemplates"
    email_and_sms_templates: "EmailAndSmsTemplates"
    templates: "Templates"
    users: "Users"
    invitations: "Invitations"
    organization_invitations: "OrganizationInvitationsSDK"
    allowlist_identifiers: "AllowlistIdentifiers"
    blocklist_identifiers: "BlocklistIdentifiersSDK"
    beta_features: "BetaFeatures"
    actor_tokens: "ActorTokens"
    domains: "DomainsSDK"
    instance_settings: "InstanceSettingsSDK"
    webhooks: "Webhooks"
    jwt_templates: "JwtTemplates"
    machine_tokens: "MachineTokens"
    machines: "Machines"
    organizations: "OrganizationsSDK"
    organization_memberships: "OrganizationMembershipsSDK"
    organization_domains: "OrganizationDomainsSDK"
    proxy_checks: "ProxyChecks"
    redirect_urls: "RedirectUrls"
    sign_in_tokens: "SignInTokens"
    sign_ups: "SignUps"
    oauth_applications: "OauthApplicationsSDK"
    saml_connections: "SamlConnectionsSDK"
    testing_tokens: "TestingTokens"
    waitlist_entries: "WaitlistEntriesSDK"
    experimental_accountless_applications: "ExperimentalAccountlessApplications"
    management: "Management"
    oauth_access_tokens: "OauthAccessTokens"
    _sub_sdk_map = {
        "miscellaneous": ("clerk_backend_api.miscellaneous", "Miscellaneous"),
        "jwks": ("clerk_backend_api.jwks_sdk", "JwksSDK"),
        "aws_credentials": ("clerk_backend_api.awscredentials", "AwsCredentials"),
        "clients": ("clerk_backend_api.clients", "Clients"),
        "email_addresses": ("clerk_backend_api.emailaddresses", "EmailAddresses"),
        "phone_numbers": ("clerk_backend_api.phonenumbers", "PhoneNumbers"),
        "sessions": ("clerk_backend_api.sessions", "Sessions"),
        "email_sms_templates": (
            "clerk_backend_api.emailsmstemplates",
            "EmailSMSTemplates",
        ),
        "email_and_sms_templates": (
            "clerk_backend_api.emailandsmstemplates",
            "EmailAndSmsTemplates",
        ),
        "templates": ("clerk_backend_api.templates", "Templates"),
        "users": ("clerk_backend_api.users", "Users"),
        "invitations": ("clerk_backend_api.invitations", "Invitations"),
        "organization_invitations": (
            "clerk_backend_api.organizationinvitations_sdk",
            "OrganizationInvitationsSDK",
        ),
        "allowlist_identifiers": (
            "clerk_backend_api.allowlistidentifiers",
            "AllowlistIdentifiers",
        ),
        "blocklist_identifiers": (
            "clerk_backend_api.blocklistidentifiers_sdk",
            "BlocklistIdentifiersSDK",
        ),
        "beta_features": ("clerk_backend_api.betafeatures", "BetaFeatures"),
        "actor_tokens": ("clerk_backend_api.actortokens", "ActorTokens"),
        "domains": ("clerk_backend_api.domains_sdk", "DomainsSDK"),
        "instance_settings": (
            "clerk_backend_api.instancesettings_sdk",
            "InstanceSettingsSDK",
        ),
        "webhooks": ("clerk_backend_api.webhooks", "Webhooks"),
        "jwt_templates": ("clerk_backend_api.jwttemplates", "JwtTemplates"),
        "machine_tokens": ("clerk_backend_api.machinetokens", "MachineTokens"),
        "machines": ("clerk_backend_api.machines", "Machines"),
        "organizations": ("clerk_backend_api.organizations_sdk", "OrganizationsSDK"),
        "organization_memberships": (
            "clerk_backend_api.organizationmemberships_sdk",
            "OrganizationMembershipsSDK",
        ),
        "organization_domains": (
            "clerk_backend_api.organizationdomains_sdk",
            "OrganizationDomainsSDK",
        ),
        "proxy_checks": ("clerk_backend_api.proxychecks", "ProxyChecks"),
        "redirect_urls": ("clerk_backend_api.redirecturls", "RedirectUrls"),
        "sign_in_tokens": ("clerk_backend_api.signintokens", "SignInTokens"),
        "sign_ups": ("clerk_backend_api.signups", "SignUps"),
        "oauth_applications": (
            "clerk_backend_api.oauthapplications_sdk",
            "OauthApplicationsSDK",
        ),
        "saml_connections": (
            "clerk_backend_api.samlconnections_sdk",
            "SamlConnectionsSDK",
        ),
        "testing_tokens": ("clerk_backend_api.testingtokens", "TestingTokens"),
        "waitlist_entries": (
            "clerk_backend_api.waitlistentries_sdk",
            "WaitlistEntriesSDK",
        ),
        "experimental_accountless_applications": (
            "clerk_backend_api.experimentalaccountlessapplications",
            "ExperimentalAccountlessApplications",
        ),
        "management": ("clerk_backend_api.management", "Management"),
        "oauth_access_tokens": (
            "clerk_backend_api.oauthaccesstokens",
            "OauthAccessTokens",
        ),
    }

    def __init__(
        self,
        bearer_auth: Optional[Union[Optional[str], Callable[[], Optional[str]]]] = None,
        server_idx: Optional[int] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param bearer_auth: The bearer_auth required for authentication
        :param server_idx: The index of the server to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(bearer_auth):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(bearer_auth=bearer_auth())
        else:
            security = models.Security(bearer_auth=bearer_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

    def __getattr__(self, name: str):
        if name in self._sub_sdk_map:
            module_path, class_name = self._sub_sdk_map[name]
            try:
                module = importlib.import_module(module_path)
                klass = getattr(module, class_name)
                instance = klass(self.sdk_configuration)
                setattr(self, name, instance)
                return instance
            except ImportError as e:
                raise AttributeError(
                    f"Failed to import module {module_path} for attribute {name}: {e}"
                ) from e
            except AttributeError as e:
                raise AttributeError(
                    f"Failed to find class {class_name} in module {module_path} for attribute {name}: {e}"
                ) from e

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def __dir__(self):
        default_attrs = list(super().__dir__())
        lazy_attrs = list(self._sub_sdk_map.keys())
        return sorted(list(set(default_attrs + lazy_attrs)))

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None

    # region sdk-class-body
    def authenticate_request(
        self, request: Requestish, options: AuthenticateRequestOptions
    ) -> RequestState:
        """
        Authenticates the session token. Networkless if the options.jwt_key is provided.
        Otherwise, performs a network call to retrieve the JWKS from Clerk's Backend API.

        If the secret_key is not provided, an attempt is made to retrieve it from the bearer_auth token that
        was used to instantiate the SDK. WARNING: this relies on bearerAuth being the only security scheme.
        """

        if options.secret_key is None:
            security = self.sdk_configuration.security
            if security is not None:
                # WARNING: the following assumes bearerAuth is the only security scheme
                if callable(security):
                    options.secret_key = security().bearer_auth
                else:
                    options.secret_key = security.bearer_auth

        return authenticate_request(request, options)

    # endregion sdk-class-body
