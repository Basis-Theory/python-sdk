# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .proxy_transform import ProxyTransform
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Proxy(UniversalBaseModel):
    id: typing.Optional[str] = None
    key: typing.Optional[str] = None
    tenant_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    destination_url: typing.Optional[str] = None
    request_reactor_id: typing.Optional[str] = None
    response_reactor_id: typing.Optional[str] = None
    require_auth: typing.Optional[bool] = None
    request_transform: typing.Optional[ProxyTransform] = None
    response_transform: typing.Optional[ProxyTransform] = None
    application_id: typing.Optional[str] = None
    configuration: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    proxy_host: typing.Optional[str] = None
    timeout: typing.Optional[int] = None
    created_by: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    modified_by: typing.Optional[str] = None
    modified_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
