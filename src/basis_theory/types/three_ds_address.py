# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ThreeDsAddress(UniversalBaseModel):
    line1: typing.Optional[str] = None
    line2: typing.Optional[str] = None
    line3: typing.Optional[str] = None
    postal_code: typing.Optional[str] = None
    city: typing.Optional[str] = None
    state_code: typing.Optional[str] = None
    country_code: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow