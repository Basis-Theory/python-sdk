# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unauthorized_error import UnauthorizedError
from ...types.problem_details import ProblemDetails
from ...errors.forbidden_error import ForbiddenError
from ...errors.not_found_error import NotFoundError
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper


class ResultsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.reactors.results.get(
            id="id",
            request_id="requestId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"reactors/{jsonable_encoder(id)}/results/{jsonable_encoder(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
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


class AsyncResultsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, request_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        id : str

        request_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
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
            await client.reactors.results.get(
                id="id",
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"reactors/{jsonable_encoder(id)}/results/{jsonable_encoder(request_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
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
