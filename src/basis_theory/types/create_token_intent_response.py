# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .card_details import CardDetails
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CreateTokenIntentResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None
    tenant_id: typing.Optional[str] = None
    fingerprint: typing.Optional[str] = None
    created_by: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    card: typing.Optional[CardDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
