# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .three_ds_device_info import ThreeDsDeviceInfo
from .three_ds_version import ThreeDsVersion
from .three_ds_method import ThreeDsMethod
from .three_ds_authentication import ThreeDsAuthentication
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ThreeDsSession(UniversalBaseModel):
    id: typing.Optional[str] = None
    tenant_id: typing.Optional[str] = None
    pan_token_id: typing.Optional[str] = None
    card_brand: typing.Optional[str] = None
    expiration_date: typing.Optional[dt.datetime] = None
    created_date: typing.Optional[dt.datetime] = None
    created_by: typing.Optional[str] = None
    modified_date: typing.Optional[dt.datetime] = None
    modified_by: typing.Optional[str] = None
    device: typing.Optional[str] = None
    device_info: typing.Optional[ThreeDsDeviceInfo] = None
    version: typing.Optional[ThreeDsVersion] = None
    method: typing.Optional[ThreeDsMethod] = None
    authentication: typing.Optional[ThreeDsAuthentication] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
