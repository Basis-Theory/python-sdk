# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .three_ds_merchant_risk_info import ThreeDsMerchantRiskInfo
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ThreeDsMerchantInfo(UniversalBaseModel):
    mid: typing.Optional[str] = None
    acquirer_bin: typing.Optional[str] = None
    name: typing.Optional[str] = None
    country_code: typing.Optional[str] = None
    category_code: typing.Optional[str] = None
    risk_info: typing.Optional[ThreeDsMerchantRiskInfo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
