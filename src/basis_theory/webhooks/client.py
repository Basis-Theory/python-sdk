# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .events.client import EventsClient
from .signing_key.client import SigningKeyClient
from ..core.request_options import RequestOptions
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.webhook_response import WebhookResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unauthorized_error import UnauthorizedError
from ..types.problem_details import ProblemDetails
from ..errors.forbidden_error import ForbiddenError
from ..errors.bad_request_error import BadRequestError
from ..types.validation_problem_details import ValidationProblemDetails
from ..errors.not_found_error import NotFoundError
from ..errors.conflict_error import ConflictError
from ..types.webhook_list_response import WebhookListResponse
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..core.client_wrapper import AsyncClientWrapper
from .events.client import AsyncEventsClient
from .signing_key.client import AsyncSigningKeyClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.events = EventsClient(client_wrapper=self._client_wrapper)
        self.signing_key = SigningKeyClient(client_wrapper=self._client_wrapper)

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Simple endpoint that can be utilized to verify the application is running

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.ping()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ping",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookResponse:
        """
        Returns the webhook

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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

    def update(
        self,
        id: str,
        *,
        name: str,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookResponse:
        """
        Update a new webhook

        Parameters
        ----------
        id : str

        name : str
            The name of the webhook

        url : str
            The URL to which the webhook will send events

        events : typing.Sequence[str]
            An array of event types that the webhook will listen for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update(
            id="id",
            name="webhook-update",
            url="http://www.example.com",
            events=["token:created"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "events": events,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a new webhook

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookListResponse:
        """
        Returns the configured webhooks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookListResponse,
                    parse_obj_as(
                        type_=WebhookListResponse,  # type: ignore
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

    def create(
        self,
        *,
        name: str,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookResponse:
        """
        Create a new webhook

        Parameters
        ----------
        name : str
            The name of the webhook

        url : str
            The URL to which the webhook will send events

        events : typing.Sequence[str]
            An array of event types that the webhook will listen for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create(
            name="webhook-create",
            url="http://www.example.com",
            events=["token:created"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "events": events,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        self.signing_key = AsyncSigningKeyClient(client_wrapper=self._client_wrapper)

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Simple endpoint that can be utilized to verify the application is running

        Parameters
        ----------
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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.ping()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ping",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookResponse:
        """
        Returns the webhook

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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

    async def update(
        self,
        id: str,
        *,
        name: str,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookResponse:
        """
        Update a new webhook

        Parameters
        ----------
        id : str

        name : str
            The name of the webhook

        url : str
            The URL to which the webhook will send events

        events : typing.Sequence[str]
            An array of event types that the webhook will listen for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.update(
                id="id",
                name="webhook-update",
                url="http://www.example.com",
                events=["token:created"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "events": events,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a new webhook

        Parameters
        ----------
        id : str

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookListResponse:
        """
        Returns the configured webhooks

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListResponse
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookListResponse,
                    parse_obj_as(
                        type_=WebhookListResponse,  # type: ignore
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

    async def create(
        self,
        *,
        name: str,
        url: str,
        events: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookResponse:
        """
        Create a new webhook

        Parameters
        ----------
        name : str
            The name of the webhook

        url : str
            The URL to which the webhook will send events

        events : typing.Sequence[str]
            An array of event types that the webhook will listen for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookResponse
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory

        client = AsyncBasisTheory(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.webhooks.create(
                name="webhook-create",
                url="http://www.example.com",
                events=["token:created"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "events": events,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebhookResponse,
                    parse_obj_as(
                        type_=WebhookResponse,  # type: ignore
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
