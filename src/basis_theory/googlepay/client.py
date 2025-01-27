# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..types.google_payment_method_token import GooglePaymentMethodToken
from ..core.request_options import RequestOptions
from ..types.google_pay_tokenize_response import GooglePayTokenizeResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..types.validation_problem_details import ValidationProblemDetails
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..errors.forbidden_error import ForbiddenError
from ..errors.conflict_error import ConflictError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GooglepayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def tokenize(
        self,
        *,
        google_payment_method_token: typing.Optional[GooglePaymentMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GooglePayTokenizeResponse:
        """
        Parameters
        ----------
        google_payment_method_token : typing.Optional[GooglePaymentMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GooglePayTokenizeResponse
            Created

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.googlepay.tokenize()
        """
        _response = self._client_wrapper.httpx_client.request(
            "connections/google-pay/tokenize",
            method="POST",
            json={
                "google_payment_method_token": convert_and_respect_annotation_metadata(
                    object_=google_payment_method_token, annotation=GooglePaymentMethodToken, direction="write"
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
                    GooglePayTokenizeResponse,
                    parse_obj_as(
                        type_=GooglePayTokenizeResponse,  # type: ignore
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
            if _response.status_code == 409:
                raise ConflictError(
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


class AsyncGooglepayClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def tokenize(
        self,
        *,
        google_payment_method_token: typing.Optional[GooglePaymentMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GooglePayTokenizeResponse:
        """
        Parameters
        ----------
        google_payment_method_token : typing.Optional[GooglePaymentMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GooglePayTokenizeResponse
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
            await client.googlepay.tokenize()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "connections/google-pay/tokenize",
            method="POST",
            json={
                "google_payment_method_token": convert_and_respect_annotation_metadata(
                    object_=google_payment_method_token, annotation=GooglePaymentMethodToken, direction="write"
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
                    GooglePayTokenizeResponse,
                    parse_obj_as(
                        type_=GooglePayTokenizeResponse,  # type: ignore
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
            if _response.status_code == 409:
                raise ConflictError(
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
