# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...types.three_ds_device_info import ThreeDsDeviceInfo
from ...core.request_options import RequestOptions
from ...types.create_three_ds_session_response import CreateThreeDsSessionResponse
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.pydantic_utilities import parse_obj_as
from ...errors.bad_request_error import BadRequestError
from ...types.validation_problem_details import ValidationProblemDetails
from ...errors.unauthorized_error import UnauthorizedError
from ...types.problem_details import ProblemDetails
from ...errors.forbidden_error import ForbiddenError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.three_ds_requestor_info import ThreeDsRequestorInfo
from ...types.three_ds_purchase_info import ThreeDsPurchaseInfo
from ...types.three_ds_merchant_info import ThreeDsMerchantInfo
from ...types.three_ds_cardholder_info import ThreeDsCardholderInfo
from ...types.three_ds_message_extension import ThreeDsMessageExtension
from ...types.three_ds_authentication import ThreeDsAuthentication
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.not_found_error import NotFoundError
from ...types.three_ds_session import ThreeDsSession
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        pan: typing.Optional[str] = OMIT,
        token_id: typing.Optional[str] = OMIT,
        token_intent_id: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        device: typing.Optional[str] = OMIT,
        web_challenge_mode: typing.Optional[str] = OMIT,
        device_info: typing.Optional[ThreeDsDeviceInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateThreeDsSessionResponse:
        """
        Parameters
        ----------
        pan : typing.Optional[str]

        token_id : typing.Optional[str]

        token_intent_id : typing.Optional[str]

        type : typing.Optional[str]

        device : typing.Optional[str]

        web_challenge_mode : typing.Optional[str]

        device_info : typing.Optional[ThreeDsDeviceInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateThreeDsSessionResponse
            Created

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.threeds.sessions.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "3ds/sessions",
            method="POST",
            json={
                "pan": pan,
                "token_id": token_id,
                "token_intent_id": token_intent_id,
                "type": type,
                "device": device,
                "web_challenge_mode": web_challenge_mode,
                "device_info": convert_and_respect_annotation_metadata(
                    object_=device_info, annotation=ThreeDsDeviceInfo, direction="write"
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
                    CreateThreeDsSessionResponse,
                    parse_obj_as(
                        type_=CreateThreeDsSessionResponse,  # type: ignore
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

    def authenticate(
        self,
        session_id: str,
        *,
        authentication_category: str,
        authentication_type: str,
        requestor_info: ThreeDsRequestorInfo,
        challenge_preference: typing.Optional[str] = OMIT,
        request_decoupled_challenge: typing.Optional[bool] = OMIT,
        decoupled_challenge_max_time: typing.Optional[int] = OMIT,
        purchase_info: typing.Optional[ThreeDsPurchaseInfo] = OMIT,
        merchant_info: typing.Optional[ThreeDsMerchantInfo] = OMIT,
        cardholder_info: typing.Optional[ThreeDsCardholderInfo] = OMIT,
        broadcast_info: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        message_extensions: typing.Optional[typing.Sequence[ThreeDsMessageExtension]] = OMIT,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreeDsAuthentication:
        """
        Parameters
        ----------
        session_id : str

        authentication_category : str

        authentication_type : str

        requestor_info : ThreeDsRequestorInfo

        challenge_preference : typing.Optional[str]

        request_decoupled_challenge : typing.Optional[bool]

        decoupled_challenge_max_time : typing.Optional[int]

        purchase_info : typing.Optional[ThreeDsPurchaseInfo]

        merchant_info : typing.Optional[ThreeDsMerchantInfo]

        cardholder_info : typing.Optional[ThreeDsCardholderInfo]

        broadcast_info : typing.Optional[typing.Optional[typing.Any]]

        message_extensions : typing.Optional[typing.Sequence[ThreeDsMessageExtension]]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsAuthentication
            Success

        Examples
        --------
        from basis_theory import BasisTheory, ThreeDsRequestorInfo

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.threeds.sessions.authenticate(
            session_id="sessionId",
            authentication_category="authentication_category",
            authentication_type="authentication_type",
            requestor_info=ThreeDsRequestorInfo(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(session_id)}/authenticate",
            method="POST",
            json={
                "authentication_category": authentication_category,
                "authentication_type": authentication_type,
                "challenge_preference": challenge_preference,
                "request_decoupled_challenge": request_decoupled_challenge,
                "decoupled_challenge_max_time": decoupled_challenge_max_time,
                "purchase_info": convert_and_respect_annotation_metadata(
                    object_=purchase_info, annotation=ThreeDsPurchaseInfo, direction="write"
                ),
                "merchant_info": convert_and_respect_annotation_metadata(
                    object_=merchant_info, annotation=ThreeDsMerchantInfo, direction="write"
                ),
                "requestor_info": convert_and_respect_annotation_metadata(
                    object_=requestor_info, annotation=ThreeDsRequestorInfo, direction="write"
                ),
                "cardholder_info": convert_and_respect_annotation_metadata(
                    object_=cardholder_info, annotation=ThreeDsCardholderInfo, direction="write"
                ),
                "broadcast_info": broadcast_info,
                "message_extensions": convert_and_respect_annotation_metadata(
                    object_=message_extensions, annotation=typing.Sequence[ThreeDsMessageExtension], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsAuthentication,
                    parse_obj_as(
                        type_=ThreeDsAuthentication,  # type: ignore
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

    def get_challenge_result(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreeDsAuthentication:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsAuthentication
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.threeds.sessions.get_challenge_result(
            session_id="sessionId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(session_id)}/challenge-result",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsAuthentication,
                    parse_obj_as(
                        type_=ThreeDsAuthentication,  # type: ignore
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ThreeDsSession:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsSession
            Success

        Examples
        --------
        from basis_theory import BasisTheory

        client = BasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )
        client.threeds.sessions.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsSession,
                    parse_obj_as(
                        type_=ThreeDsSession,  # type: ignore
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


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        pan: typing.Optional[str] = OMIT,
        token_id: typing.Optional[str] = OMIT,
        token_intent_id: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        device: typing.Optional[str] = OMIT,
        web_challenge_mode: typing.Optional[str] = OMIT,
        device_info: typing.Optional[ThreeDsDeviceInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateThreeDsSessionResponse:
        """
        Parameters
        ----------
        pan : typing.Optional[str]

        token_id : typing.Optional[str]

        token_intent_id : typing.Optional[str]

        type : typing.Optional[str]

        device : typing.Optional[str]

        web_challenge_mode : typing.Optional[str]

        device_info : typing.Optional[ThreeDsDeviceInfo]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateThreeDsSessionResponse
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
            await client.threeds.sessions.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "3ds/sessions",
            method="POST",
            json={
                "pan": pan,
                "token_id": token_id,
                "token_intent_id": token_intent_id,
                "type": type,
                "device": device,
                "web_challenge_mode": web_challenge_mode,
                "device_info": convert_and_respect_annotation_metadata(
                    object_=device_info, annotation=ThreeDsDeviceInfo, direction="write"
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
                    CreateThreeDsSessionResponse,
                    parse_obj_as(
                        type_=CreateThreeDsSessionResponse,  # type: ignore
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

    async def authenticate(
        self,
        session_id: str,
        *,
        authentication_category: str,
        authentication_type: str,
        requestor_info: ThreeDsRequestorInfo,
        challenge_preference: typing.Optional[str] = OMIT,
        request_decoupled_challenge: typing.Optional[bool] = OMIT,
        decoupled_challenge_max_time: typing.Optional[int] = OMIT,
        purchase_info: typing.Optional[ThreeDsPurchaseInfo] = OMIT,
        merchant_info: typing.Optional[ThreeDsMerchantInfo] = OMIT,
        cardholder_info: typing.Optional[ThreeDsCardholderInfo] = OMIT,
        broadcast_info: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        message_extensions: typing.Optional[typing.Sequence[ThreeDsMessageExtension]] = OMIT,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreeDsAuthentication:
        """
        Parameters
        ----------
        session_id : str

        authentication_category : str

        authentication_type : str

        requestor_info : ThreeDsRequestorInfo

        challenge_preference : typing.Optional[str]

        request_decoupled_challenge : typing.Optional[bool]

        decoupled_challenge_max_time : typing.Optional[int]

        purchase_info : typing.Optional[ThreeDsPurchaseInfo]

        merchant_info : typing.Optional[ThreeDsMerchantInfo]

        cardholder_info : typing.Optional[ThreeDsCardholderInfo]

        broadcast_info : typing.Optional[typing.Optional[typing.Any]]

        message_extensions : typing.Optional[typing.Sequence[ThreeDsMessageExtension]]

        idempotency_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsAuthentication
            Success

        Examples
        --------
        import asyncio

        from basis_theory import AsyncBasisTheory, ThreeDsRequestorInfo

        client = AsyncBasisTheory(
            correlation_id="YOUR_CORRELATION_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.threeds.sessions.authenticate(
                session_id="sessionId",
                authentication_category="authentication_category",
                authentication_type="authentication_type",
                requestor_info=ThreeDsRequestorInfo(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(session_id)}/authenticate",
            method="POST",
            json={
                "authentication_category": authentication_category,
                "authentication_type": authentication_type,
                "challenge_preference": challenge_preference,
                "request_decoupled_challenge": request_decoupled_challenge,
                "decoupled_challenge_max_time": decoupled_challenge_max_time,
                "purchase_info": convert_and_respect_annotation_metadata(
                    object_=purchase_info, annotation=ThreeDsPurchaseInfo, direction="write"
                ),
                "merchant_info": convert_and_respect_annotation_metadata(
                    object_=merchant_info, annotation=ThreeDsMerchantInfo, direction="write"
                ),
                "requestor_info": convert_and_respect_annotation_metadata(
                    object_=requestor_info, annotation=ThreeDsRequestorInfo, direction="write"
                ),
                "cardholder_info": convert_and_respect_annotation_metadata(
                    object_=cardholder_info, annotation=ThreeDsCardholderInfo, direction="write"
                ),
                "broadcast_info": broadcast_info,
                "message_extensions": convert_and_respect_annotation_metadata(
                    object_=message_extensions, annotation=typing.Sequence[ThreeDsMessageExtension], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "BT-IDEMPOTENCY-KEY": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsAuthentication,
                    parse_obj_as(
                        type_=ThreeDsAuthentication,  # type: ignore
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

    async def get_challenge_result(
        self, session_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreeDsAuthentication:
        """
        Parameters
        ----------
        session_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsAuthentication
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
            await client.threeds.sessions.get_challenge_result(
                session_id="sessionId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(session_id)}/challenge-result",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsAuthentication,
                    parse_obj_as(
                        type_=ThreeDsAuthentication,  # type: ignore
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

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ThreeDsSession:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreeDsSession
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
            await client.threeds.sessions.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"3ds/sessions/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ThreeDsSession,
                    parse_obj_as(
                        type_=ThreeDsSession,  # type: ignore
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
