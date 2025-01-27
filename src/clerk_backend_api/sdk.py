"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from clerk_backend_api import models, utils
from clerk_backend_api._hooks import SDKHooks
from clerk_backend_api.actortokens import ActorTokens
from clerk_backend_api.allowlistblocklist import AllowlistBlocklist
from clerk_backend_api.allowlistidentifiers import AllowlistIdentifiers
from clerk_backend_api.betafeatures import BetaFeatures
from clerk_backend_api.blocklistidentifiers_sdk import BlocklistIdentifiersSDK
from clerk_backend_api.clerk_redirecturls import ClerkRedirectUrls
from clerk_backend_api.clients import Clients
from clerk_backend_api.domains_sdk import DomainsSDK
from clerk_backend_api.emailaddresses import EmailAddresses
from clerk_backend_api.emailandsmstemplates import EmailAndSmsTemplates
from clerk_backend_api.emailsmstemplates import EmailSMSTemplates
from clerk_backend_api.instance_settings_sdk import InstanceSettingsSDK
from clerk_backend_api.invitations import Invitations
from clerk_backend_api.jwks_sdk import JwksSDK
from clerk_backend_api.jwttemplates import JwtTemplates
from clerk_backend_api.miscellaneous import Miscellaneous
from clerk_backend_api.oauthapplications_sdk import OauthApplicationsSDK
from clerk_backend_api.organizationdomain_sdk import OrganizationDomainSDK
from clerk_backend_api.organizationdomains_sdk import OrganizationDomainsSDK
from clerk_backend_api.organizationinvitations_sdk import OrganizationInvitationsSDK
from clerk_backend_api.organizationmemberships_sdk import OrganizationMembershipsSDK
from clerk_backend_api.organizations_sdk import OrganizationsSDK
from clerk_backend_api.phonenumbers import PhoneNumbers
from clerk_backend_api.proxychecks import ProxyChecks
from clerk_backend_api.redirecturls import RedirectURLs
from clerk_backend_api.samlconnections_sdk import SamlConnectionsSDK
from clerk_backend_api.sessions import Sessions
from clerk_backend_api.signintokens import SignInTokens
from clerk_backend_api.signups import SignUps
from clerk_backend_api.templates import Templates
from clerk_backend_api.testingtokens import TestingTokens
from clerk_backend_api.types import OptionalNullable, UNSET
from clerk_backend_api.users import Users
from clerk_backend_api.waitlist_entries_sdk import WaitlistEntriesSDK
from clerk_backend_api.webhooks import Webhooks
import httpx
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref

# region imports
from .jwks_helpers import AuthenticateRequestOptions, RequestState, authenticate_request
# endregion imports


class Clerk(BaseSDK):
    r"""Clerk Backend API: The Clerk REST Backend API, meant to be accessed by backend
    servers.

    ### Versions

    When the API changes in a way that isn't compatible with older versions, a new version is released.
    Each version is identified by its release date, e.g. `2021-02-05`. For more information, please see [Clerk API Versions](https://clerk.com/docs/backend-requests/versioning/overview).


    Please see https://clerk.com/docs for more information.
    https://clerk.com/docs
    """

    miscellaneous: Miscellaneous
    r"""Various endpoints that do not belong in any particular category."""
    jwks: JwksSDK
    clients: Clients
    r"""The Client object tracks sessions, as well as the state of any sign in and sign up attempts, for a given device.
    https://clerk.com/docs/reference/clerkjs/client
    """
    email_addresses: EmailAddresses
    phone_numbers: PhoneNumbers
    sessions: Sessions
    r"""The Session object is an abstraction over an HTTP session.
    It models the period of information exchange between a user and the server.
    Sessions are created when a user successfully goes through the sign in or sign up flows.
    https://clerk.com/docs/reference/clerkjs/session
    """
    email_sms_templates: EmailSMSTemplates
    email_and_sms_templates: EmailAndSmsTemplates
    templates: Templates
    users: Users
    r"""The user object represents a user that has successfully signed up to your application.
    https://clerk.com/docs/reference/clerkjs/user
    """
    invitations: Invitations
    r"""Invitations allow you to invite someone to sign up to your application, via email.
    https://clerk.com/docs/authentication/invitations
    """
    organization_invitations: OrganizationInvitationsSDK
    allowlist_blocklist: AllowlistBlocklist
    allowlist_identifiers: AllowlistIdentifiers
    blocklist_identifiers: BlocklistIdentifiersSDK
    beta_features: BetaFeatures
    actor_tokens: ActorTokens
    domains: DomainsSDK
    r"""Domains represent each instance's URLs and DNS setup."""
    instance_settings: InstanceSettingsSDK
    webhooks: Webhooks
    r"""You can configure webhooks to be notified about various events that happen on your instance.
    https://clerk.com/docs/integration/webhooks
    """
    jwt_templates: JwtTemplates
    organizations: OrganizationsSDK
    r"""Organizations are used to group members under a common entity and provide shared access to resources.
    https://clerk.com/docs/organizations/overview
    """
    organization_memberships: OrganizationMembershipsSDK
    organization_domains: OrganizationDomainsSDK
    organization_domain: OrganizationDomainSDK
    proxy_checks: ProxyChecks
    redirect_ur_ls: RedirectURLs
    redirect_urls: ClerkRedirectUrls
    sign_in_tokens: SignInTokens
    sign_ups: SignUps
    oauth_applications: OauthApplicationsSDK
    saml_connections: SamlConnectionsSDK
    testing_tokens: TestingTokens
    waitlist_entries: WaitlistEntriesSDK

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
        if client is None:
            client = httpx.Client()

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        if async_client is None:
            async_client = httpx.AsyncClient()

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
                async_client=async_client,
                security=security,
                server_url=server_url,
                server_idx=server_idx,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, self.sdk_configuration.client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.async_client,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.miscellaneous = Miscellaneous(self.sdk_configuration)
        self.jwks = JwksSDK(self.sdk_configuration)
        self.clients = Clients(self.sdk_configuration)
        self.email_addresses = EmailAddresses(self.sdk_configuration)
        self.phone_numbers = PhoneNumbers(self.sdk_configuration)
        self.sessions = Sessions(self.sdk_configuration)
        self.email_sms_templates = EmailSMSTemplates(self.sdk_configuration)
        self.email_and_sms_templates = EmailAndSmsTemplates(self.sdk_configuration)
        self.templates = Templates(self.sdk_configuration)
        self.users = Users(self.sdk_configuration)
        self.invitations = Invitations(self.sdk_configuration)
        self.organization_invitations = OrganizationInvitationsSDK(
            self.sdk_configuration
        )
        self.allowlist_blocklist = AllowlistBlocklist(self.sdk_configuration)
        self.allowlist_identifiers = AllowlistIdentifiers(self.sdk_configuration)
        self.blocklist_identifiers = BlocklistIdentifiersSDK(self.sdk_configuration)
        self.beta_features = BetaFeatures(self.sdk_configuration)
        self.actor_tokens = ActorTokens(self.sdk_configuration)
        self.domains = DomainsSDK(self.sdk_configuration)
        self.instance_settings = InstanceSettingsSDK(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
        self.jwt_templates = JwtTemplates(self.sdk_configuration)
        self.organizations = OrganizationsSDK(self.sdk_configuration)
        self.organization_memberships = OrganizationMembershipsSDK(
            self.sdk_configuration
        )
        self.organization_domains = OrganizationDomainsSDK(self.sdk_configuration)
        self.organization_domain = OrganizationDomainSDK(self.sdk_configuration)
        self.proxy_checks = ProxyChecks(self.sdk_configuration)
        self.redirect_ur_ls = RedirectURLs(self.sdk_configuration)
        self.redirect_urls = ClerkRedirectUrls(self.sdk_configuration)
        self.sign_in_tokens = SignInTokens(self.sdk_configuration)
        self.sign_ups = SignUps(self.sdk_configuration)
        self.oauth_applications = OauthApplicationsSDK(self.sdk_configuration)
        self.saml_connections = SamlConnectionsSDK(self.sdk_configuration)
        self.testing_tokens = TestingTokens(self.sdk_configuration)
        self.waitlist_entries = WaitlistEntriesSDK(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.client is not None:
            self.sdk_configuration.client.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.sdk_configuration.async_client is not None:
            await self.sdk_configuration.async_client.aclose()

    # region sdk-class-body
    def authenticate_request(self, request: httpx.Request, options: AuthenticateRequestOptions) -> RequestState:
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
