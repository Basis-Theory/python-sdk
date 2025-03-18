# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .domain.client import DomainClient
from .session.client import SessionClient
from ...types.apple_pay_method_token import ApplePayMethodToken
from ...core.request_options import RequestOptions
from ...types.apple_pay_tokenize_response import ApplePayTokenizeResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.pydantic_utilities import parse_obj_as
from ...errors.bad_request_error import BadRequestError
from ...types.validation_problem_details import ValidationProblemDetails
from ...errors.unauthorized_error import UnauthorizedError
from ...types.problem_details import ProblemDetails
from ...errors.forbidden_error import ForbiddenError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper
from .domain.client import AsyncDomainClient
from .session.client import AsyncSessionClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ApplePayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.domain = DomainClient(client_wrapper=self._client_wrapper)
        self.session = SessionClient(client_wrapper=self._client_wrapper)

    def tokenize(
        self,
        *,
        apple_payment_method_token: typing.Optional[ApplePayMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplePayTokenizeResponse:
        """
        Parameters
        ----------
        apple_payment_method_token : typing.Optional[ApplePayMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayTokenizeResponse
            Created

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.connections.apple_pay.tokenize()
        """
        _response = self._client_wrapper.httpx_client.request(
            "connections/apple-pay/tokenize",
            method="POST",
            json={
                "apple_payment_method_token": convert_and_respect_annotation_metadata(
                    object_=apple_payment_method_token, annotation=ApplePayMethodToken, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApplePayTokenizeResponse,
                    parse_obj_as(
                        type_=ApplePayTokenizeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncApplePayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.domain = AsyncDomainClient(client_wrapper=self._client_wrapper)
        self.session = AsyncSessionClient(client_wrapper=self._client_wrapper)

    async def tokenize(
        self,
        *,
        apple_payment_method_token: typing.Optional[ApplePayMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplePayTokenizeResponse:
        """
        Parameters
        ----------
        apple_payment_method_token : typing.Optional[ApplePayMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayTokenizeResponse
            Created

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.connections.apple_pay.tokenize()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "connections/apple-pay/tokenize",
            method="POST",
            json={
                "apple_payment_method_token": convert_and_respect_annotation_metadata(
                    object_=apple_payment_method_token, annotation=ApplePayMethodToken, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApplePayTokenizeResponse,
                    parse_obj_as(
                        type_=ApplePayTokenizeResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        ValidationProblemDetails,
                        parse_obj_as(
                            type_=ValidationProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        ProblemDetails,
                        parse_obj_as(
                            type_=ProblemDetails,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
