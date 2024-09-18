# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ThreeDsAcsRenderingType(UniversalBaseModel):
    acs_interface: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="acsInterface")] = None
    acs_ui_template: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="acsUiTemplate")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
