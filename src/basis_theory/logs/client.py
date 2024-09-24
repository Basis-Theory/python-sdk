# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
import datetime as dt
from ..core.request_options import RequestOptions
from ..core.pagination import SyncPager
from ..types.log import Log
from ..core.datetime_utils import serialize_datetime
from ..types.log_paginated_list import LogPaginatedList
from ..core.pydantic_utilities import parse_obj_as
from ..errors.bad_request_error import BadRequestError
from ..types.validation_problem_details import ValidationProblemDetails
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..errors.forbidden_error import ForbiddenError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.log_entity_type import LogEntityType
from ..core.client_wrapper import AsyncClientWrapper
from ..core.pagination import AsyncPager


class LogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        entity_type: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        start: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Log]:
        """
        Parameters
        ----------
        entity_type : typing.Optional[str]

        entity_id : typing.Optional[str]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        page : typing.Optional[int]

        start : typing.Optional[str]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Log]
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        response = client.logs.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        page = page if page is not None else 1
        _response = self._client_wrapper.httpx_client.request(
            "logs",
            method="GET",
            params={
                "entity_type": entity_type,
                "entity_id": entity_id,
                "start_date": serialize_datetime(start_date) if start_date is not None else None,
                "end_date": serialize_datetime(end_date) if end_date is not None else None,
                "page": page,
                "start": start,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    LogPaginatedList,
                    parse_obj_as(
                        type_=LogPaginatedList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.list(
                    entity_type=entity_type,
                    entity_id=entity_id,
                    start_date=start_date,
                    end_date=end_date,
                    page=page + 1,
                    start=start,
                    size=size,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
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

    def get_entity_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LogEntityType]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LogEntityType]
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.logs.get_entity_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "logs/entity-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LogEntityType],
                    parse_obj_as(
                        type_=typing.List[LogEntityType],  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        entity_type: typing.Optional[str] = None,
        entity_id: typing.Optional[str] = None,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        page: typing.Optional[int] = None,
        start: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Log]:
        """
        Parameters
        ----------
        entity_type : typing.Optional[str]

        entity_id : typing.Optional[str]

        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        page : typing.Optional[int]

        start : typing.Optional[str]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Log]
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            response = await client.logs.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        page = page if page is not None else 1
        _response = await self._client_wrapper.httpx_client.request(
            "logs",
            method="GET",
            params={
                "entity_type": entity_type,
                "entity_id": entity_id,
                "start_date": serialize_datetime(start_date) if start_date is not None else None,
                "end_date": serialize_datetime(end_date) if end_date is not None else None,
                "page": page,
                "start": start,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    LogPaginatedList,
                    parse_obj_as(
                        type_=LogPaginatedList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.list(
                    entity_type=entity_type,
                    entity_id=entity_id,
                    start_date=start_date,
                    end_date=end_date,
                    page=page + 1,
                    start=start,
                    size=size,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
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

    async def get_entity_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LogEntityType]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LogEntityType]
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.logs.get_entity_types()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "logs/entity-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LogEntityType],
                    parse_obj_as(
                        type_=typing.List[LogEntityType],  # type: ignore
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
