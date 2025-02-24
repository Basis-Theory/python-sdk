# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .reactor_formula_configuration import ReactorFormulaConfiguration
from .reactor_formula_request_parameter import ReactorFormulaRequestParameter
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class UpdateReactorFormulaRequest(UniversalBaseModel):
    type: str
    name: str
    description: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    code: typing.Optional[str] = None
    configuration: typing.Optional[typing.List[ReactorFormulaConfiguration]] = None
    request_parameters: typing.Optional[typing.List[ReactorFormulaRequestParameter]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
