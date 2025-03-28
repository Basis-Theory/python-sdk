# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.bank_verification_response import BankVerificationResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..types.validation_problem_details import ValidationProblemDetails
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..errors.forbidden_error import ForbiddenError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EnrichmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def bank_account_verify(
        self,
        *,
        token_id: str,
        country_code: typing.Optional[str] = OMIT,
        routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankVerificationResponse:
        """
        Parameters
        ----------
        token_id : str

        country_code : typing.Optional[str]

        routing_number : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankVerificationResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.enrichments.bank_account_verify(
            token_id="token_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "enrichments/bank-account-verify",
            method="POST",
            json={
                "token_id": token_id,
                "country_code": country_code,
                "routing_number": routing_number,
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
                    BankVerificationResponse,
                    parse_obj_as(
                        type_=BankVerificationResponse,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEnrichmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def bank_account_verify(
        self,
        *,
        token_id: str,
        country_code: typing.Optional[str] = OMIT,
        routing_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankVerificationResponse:
        """
        Parameters
        ----------
        token_id : str

        country_code : typing.Optional[str]

        routing_number : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankVerificationResponse
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.enrichments.bank_account_verify(
                token_id="token_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "enrichments/bank-account-verify",
            method="POST",
            json={
                "token_id": token_id,
                "country_code": country_code,
                "routing_number": routing_number,
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
                    BankVerificationResponse,
                    parse_obj_as(
                        type_=BankVerificationResponse,  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
