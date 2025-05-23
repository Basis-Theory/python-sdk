# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CreateThreeDsSessionResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    type: typing.Optional[str] = None
    card_brand: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="cardBrand")] = None
    additional_card_brands: typing.Optional[typing.List[str]] = None
    method_url: typing.Optional[str] = None
    method_notification_url: typing.Optional[str] = None
    directory_server_id: typing.Optional[str] = None
    recommended_version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
