# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import BasisTheoryEnvironment
import os
import httpx
from .core.api_error import ApiError
from .core.client_wrapper import SyncClientWrapper
from .applications.client import ApplicationsClient
from .application_keys.client import ApplicationKeysClient
from .application_templates.client import ApplicationTemplatesClient
from .tokens.client import TokensClient
from .logs.client import LogsClient
from .permissions.client import PermissionsClient
from .proxies.client import ProxiesClient
from .reactorformulas.client import ReactorformulasClient
from .reactors.client import ReactorsClient
from .roles.client import RolesClient
from .sessions.client import SessionsClient
from .threeds.client import ThreedsClient
from .webhooks.client import WebhooksClient
from .tenants.client import TenantsClient
from .core.client_wrapper import AsyncClientWrapper
from .applications.client import AsyncApplicationsClient
from .application_keys.client import AsyncApplicationKeysClient
from .application_templates.client import AsyncApplicationTemplatesClient
from .tokens.client import AsyncTokensClient
from .logs.client import AsyncLogsClient
from .permissions.client import AsyncPermissionsClient
from .proxies.client import AsyncProxiesClient
from .reactorformulas.client import AsyncReactorformulasClient
from .reactors.client import AsyncReactorsClient
from .roles.client import AsyncRolesClient
from .sessions.client import AsyncSessionsClient
from .threeds.client import AsyncThreedsClient
from .webhooks.client import AsyncWebhooksClient
from .tenants.client import AsyncTenantsClient


class BasisTheory:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : BasisTheoryEnvironment
        The environment to use for requests from the client. from .environment import BasisTheoryEnvironment



        Defaults to BasisTheoryEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from basis_theory import BasisTheory

    client = BasisTheory(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: BasisTheoryEnvironment = BasisTheoryEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("BT-API-KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(body="The client must be instantiated be either passing in api_key or setting BT-API-KEY")
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.applications = ApplicationsClient(client_wrapper=self._client_wrapper)
        self.application_keys = ApplicationKeysClient(client_wrapper=self._client_wrapper)
        self.application_templates = ApplicationTemplatesClient(client_wrapper=self._client_wrapper)
        self.tokens = TokensClient(client_wrapper=self._client_wrapper)
        self.logs = LogsClient(client_wrapper=self._client_wrapper)
        self.permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        self.proxies = ProxiesClient(client_wrapper=self._client_wrapper)
        self.reactorformulas = ReactorformulasClient(client_wrapper=self._client_wrapper)
        self.reactors = ReactorsClient(client_wrapper=self._client_wrapper)
        self.roles = RolesClient(client_wrapper=self._client_wrapper)
        self.sessions = SessionsClient(client_wrapper=self._client_wrapper)
        self.threeds = ThreedsClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        self.tenants = TenantsClient(client_wrapper=self._client_wrapper)


class AsyncBasisTheory:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : BasisTheoryEnvironment
        The environment to use for requests from the client. from .environment import BasisTheoryEnvironment



        Defaults to BasisTheoryEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from basis_theory import AsyncBasisTheory

    client = AsyncBasisTheory(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: BasisTheoryEnvironment = BasisTheoryEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("BT-API-KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(body="The client must be instantiated be either passing in api_key or setting BT-API-KEY")
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.applications = AsyncApplicationsClient(client_wrapper=self._client_wrapper)
        self.application_keys = AsyncApplicationKeysClient(client_wrapper=self._client_wrapper)
        self.application_templates = AsyncApplicationTemplatesClient(client_wrapper=self._client_wrapper)
        self.tokens = AsyncTokensClient(client_wrapper=self._client_wrapper)
        self.logs = AsyncLogsClient(client_wrapper=self._client_wrapper)
        self.permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        self.proxies = AsyncProxiesClient(client_wrapper=self._client_wrapper)
        self.reactorformulas = AsyncReactorformulasClient(client_wrapper=self._client_wrapper)
        self.reactors = AsyncReactorsClient(client_wrapper=self._client_wrapper)
        self.roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        self.sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        self.threeds = AsyncThreedsClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        self.tenants = AsyncTenantsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: BasisTheoryEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
