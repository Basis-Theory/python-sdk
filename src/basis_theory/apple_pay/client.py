# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .domain.client import DomainClient
from .session.client import SessionClient
from ..types.apple_pay_method_token import ApplePayMethodToken
from ..core.request_options import RequestOptions
from ..types.apple_pay_create_response import ApplePayCreateResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..types.validation_problem_details import ValidationProblemDetails
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..errors.forbidden_error import ForbiddenError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.apple_pay_token import ApplePayToken
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..core.client_wrapper import AsyncClientWrapper
from .domain.client import AsyncDomainClient
from .session.client import AsyncSessionClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ApplePayClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.domain = DomainClient(client_wrapper=self._client_wrapper)
        self.session = SessionClient(client_wrapper=self._client_wrapper)

    def create(
        self,
        *,
        expires_at: typing.Optional[str] = OMIT,
        apple_payment_data: typing.Optional[ApplePayMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplePayCreateResponse:
        """
        Parameters
        ----------
        expires_at : typing.Optional[str]

        apple_payment_data : typing.Optional[ApplePayMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayCreateResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.apple_pay.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "apple-pay",
            method="POST",
            json={
                "expires_at": expires_at,
                "apple_payment_data": convert_and_respect_annotation_metadata(
                    object_=apple_payment_data, annotation=ApplePayMethodToken, direction="write"
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
                    ApplePayCreateResponse,
                    parse_obj_as(
                        type_=ApplePayCreateResponse,  # type: ignore
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApplePayToken:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayToken
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.apple_pay.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apple-pay/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApplePayToken,
                    parse_obj_as(
                        type_=ApplePayToken,  # type: ignore
                        object_=_response.json(),
                    ),
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
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def unlink(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.apple_pay.unlink(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apple-pay/{jsonable_encoder(id)}/unlink",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
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

    async def create(
        self,
        *,
        expires_at: typing.Optional[str] = OMIT,
        apple_payment_data: typing.Optional[ApplePayMethodToken] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplePayCreateResponse:
        """
        Parameters
        ----------
        expires_at : typing.Optional[str]

        apple_payment_data : typing.Optional[ApplePayMethodToken]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayCreateResponse
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
            await client.apple_pay.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apple-pay",
            method="POST",
            json={
                "expires_at": expires_at,
                "apple_payment_data": convert_and_respect_annotation_metadata(
                    object_=apple_payment_data, annotation=ApplePayMethodToken, direction="write"
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
                    ApplePayCreateResponse,
                    parse_obj_as(
                        type_=ApplePayCreateResponse,  # type: ignore
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

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApplePayToken:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplePayToken
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
            await client.apple_pay.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apple-pay/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ApplePayToken,
                    parse_obj_as(
                        type_=ApplePayToken,  # type: ignore
                        object_=_response.json(),
                    ),
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
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def unlink(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
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
            await client.apple_pay.unlink(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apple-pay/{jsonable_encoder(id)}/unlink",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,  # type: ignore
                        object_=_response.json(),
                    ),
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
