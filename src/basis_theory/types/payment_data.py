# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .header import Header
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaymentData(UniversalBaseModel):
    data: typing.Optional[str] = None
    signature: typing.Optional[str] = None
    header: typing.Optional[Header] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
