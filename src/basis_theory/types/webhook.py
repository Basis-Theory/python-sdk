# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .webhook_status import WebhookStatus
import typing
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Webhook(UniversalBaseModel):
    id: str
    tenant_id: str
    status: WebhookStatus
    name: str
    url: str
    notify_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address to use for management notification events. Ie: webhook disabled
    """

    events: typing.List[str]
    created_by: str
    created_at: dt.datetime
    modified_by: typing.Optional[str] = None
    modified_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
