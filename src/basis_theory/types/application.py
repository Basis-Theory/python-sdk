# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .application_key import ApplicationKey
import datetime as dt
from .access_rule import AccessRule
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Application(UniversalBaseModel):
    id: typing.Optional[str] = None
    tenant_id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    key: typing.Optional[str] = None
    keys: typing.Optional[typing.List[ApplicationKey]] = None
    type: typing.Optional[str] = None
    created_by: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    modified_by: typing.Optional[str] = None
    modified_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    permissions: typing.Optional[typing.List[str]] = None
    rules: typing.Optional[typing.List[AccessRule]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow