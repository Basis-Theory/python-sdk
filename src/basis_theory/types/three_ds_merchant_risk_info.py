# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ThreeDsMerchantRiskInfo(UniversalBaseModel):
    delivery_email: typing.Optional[str] = None
    delivery_time_frame: typing.Optional[str] = None
    gift_card_amount: typing.Optional[str] = None
    gift_card_count: typing.Optional[str] = None
    gift_card_currency: typing.Optional[str] = None
    pre_order_purchase: typing.Optional[bool] = None
    pre_order_date: typing.Optional[str] = None
    reordered_purchase: typing.Optional[bool] = None
    shipping_method: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow