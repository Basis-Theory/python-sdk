# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...types.tenant_invitation_status import TenantInvitationStatus
from ...core.request_options import RequestOptions
from ...core.pagination import SyncPager
from ...types.tenant_invitation_response import TenantInvitationResponse
from ...types.tenant_invitation_response_paginated_list import TenantInvitationResponsePaginatedList
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unauthorized_error import UnauthorizedError
from ...types.problem_details import ProblemDetails
from ...errors.forbidden_error import ForbiddenError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...errors.bad_request_error import BadRequestError
from ...types.validation_problem_details import ValidationProblemDetails
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.not_found_error import NotFoundError
from ...core.client_wrapper import AsyncClientWrapper
from ...core.pagination import AsyncPager

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InvitationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        status: typing.Optional[TenantInvitationStatus] = None,
        page: typing.Optional[int] = None,
        start: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[TenantInvitationResponse]:
        """
        Parameters
        ----------
        status : typing.Optional[TenantInvitationStatus]

        page : typing.Optional[int]

        start : typing.Optional[str]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[TenantInvitationResponse]
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        response = client.tenants.invitations.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        page = page if page is not None else 1
        _response = self._client_wrapper.httpx_client.request(
            "tenants/self/invitations",
            method="GET",
            params={
                "status": status,
                "page": page,
                "start": start,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    TenantInvitationResponsePaginatedList,
                    parse_obj_as(
                        type_=TenantInvitationResponsePaginatedList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.list(
                    status=status,
                    page=page + 1,
                    start=start,
                    size=size,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
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

    def create(
        self,
        *,
        email: str,
        role: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        email : str

        role : typing.Optional[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
            Created

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.tenants.invitations.create(
            email="email",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "tenants/self/invitations",
            method="POST",
            json={
                "email": email,
                "role": role,
            },
            headers={
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    def resend(
        self,
        invitation_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        invitation_id : str

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.tenants.invitations.resend(
            invitation_id="invitationId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}/resend",
            method="POST",
            headers={
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    def get(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        invitation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.tenants.invitations.get(
            invitation_id="invitationId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    def delete(self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        invitation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.tenants.invitations.delete(
            invitation_id="invitationId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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


class AsyncInvitationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        status: typing.Optional[TenantInvitationStatus] = None,
        page: typing.Optional[int] = None,
        start: typing.Optional[str] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[TenantInvitationResponse]:
        """
        Parameters
        ----------
        status : typing.Optional[TenantInvitationStatus]

        page : typing.Optional[int]

        start : typing.Optional[str]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[TenantInvitationResponse]
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
            response = await client.tenants.invitations.list()
            async for item in response:
                yield item
            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        page = page if page is not None else 1
        _response = await self._client_wrapper.httpx_client.request(
            "tenants/self/invitations",
            method="GET",
            params={
                "status": status,
                "page": page,
                "start": start,
                "size": size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    TenantInvitationResponsePaginatedList,
                    parse_obj_as(
                        type_=TenantInvitationResponsePaginatedList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _has_next = True
                _get_next = lambda: self.list(
                    status=status,
                    page=page + 1,
                    start=start,
                    size=size,
                    request_options=request_options,
                )
                _items = _parsed_response.data
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
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

    async def create(
        self,
        *,
        email: str,
        role: typing.Optional[str] = OMIT,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        email : str

        role : typing.Optional[str]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
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
            await client.tenants.invitations.create(
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tenants/self/invitations",
            method="POST",
            json={
                "email": email,
                "role": role,
            },
            headers={
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    async def resend(
        self,
        invitation_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        invitation_id : str

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
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
            await client.tenants.invitations.resend(
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}/resend",
            method="POST",
            headers={
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    async def get(
        self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TenantInvitationResponse:
        """
        Parameters
        ----------
        invitation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TenantInvitationResponse
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
            await client.tenants.invitations.get(
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TenantInvitationResponse,
                    parse_obj_as(
                        type_=TenantInvitationResponse,  # type: ignore
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

    async def delete(self, invitation_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        invitation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.tenants.invitations.delete(
                invitation_id="invitationId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tenants/self/invitations/{jsonable_encoder(invitation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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