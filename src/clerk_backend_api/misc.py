"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk_backend_api import models, utils
from clerk_backend_api._hooks import HookContext
from clerk_backend_api.types import OptionalNullable, UNSET
from typing import Optional

class Misc(BaseSDK):
    
    
    def get_public_interstitial(
        self, *,
        frontend_api: Optional[str] = None,
        publishable_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ):
        r"""Returns the markup for the interstitial page

        The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's authentication state.
        It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

        :param frontend_api: The Frontend API key of your instance
        :param publishable_key: The publishable key of your instance
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetPublicInterstitialRequest(
            frontend_api=frontend_api,
            publishable_key=publishable_key,
        )
        
        req = self.build_request(
            method="GET",
            path="/public/interstitial",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="*/*",
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="GetPublicInterstitial", oauth2_scopes=[], security_source=None),
            request=req,
            error_status_codes=["400","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "*"):
            return
        if utils.match_response(http_res, ["400","4XX","500","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
    
    async def get_public_interstitial_async(
        self, *,
        frontend_api: Optional[str] = None,
        publishable_key: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ):
        r"""Returns the markup for the interstitial page

        The Clerk interstitial endpoint serves an html page that loads clerk.js in order to check the user's authentication state.
        It is used by Clerk SDKs when the user's authentication state cannot be immediately determined.

        :param frontend_api: The Frontend API key of your instance
        :param publishable_key: The publishable key of your instance
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms
        
        if server_url is not None:
            base_url = server_url
        
        request = models.GetPublicInterstitialRequest(
            frontend_api=frontend_api,
            publishable_key=publishable_key,
        )
        
        req = self.build_request(
            method="GET",
            path="/public/interstitial",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="*/*",
            timeout_ms=timeout_ms,
        )
        
        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, [
                "429",
                "500",
                "502",
                "503",
                "504"
            ])                
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="GetPublicInterstitial", oauth2_scopes=[], security_source=None),
            request=req,
            error_status_codes=["400","4XX","500","5XX"],
            retry_config=retry_config
        )
        
        if utils.match_response(http_res, "200", "*"):
            return
        if utils.match_response(http_res, ["400","4XX","500","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)

    
