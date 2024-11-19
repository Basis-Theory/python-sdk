# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ValidationProblemDetails(UniversalBaseModel):
    errors: typing.Optional[typing.Dict[str, typing.Optional[typing.List[str]]]] = None
    type: typing.Optional[str] = None
    title: typing.Optional[str] = None
    status: typing.Optional[int] = None
    detail: typing.Optional[str] = None
    instance: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow