# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hanzoai import Hanzo, AsyncHanzo
from tests.utils import assert_matches_type
from hanzoai.types.config import (
    PassThroughEndpointResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPassThroughEndpoint:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Hanzo) -> None:
        pass_through_endpoint = client.config.pass_through_endpoint.create(
            headers={},
            path="path",
            target="target",
        )
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Hanzo) -> None:
        response = client.config.pass_through_endpoint.with_raw_response.create(
            headers={},
            path="path",
            target="target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = response.parse()
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Hanzo) -> None:
        with client.config.pass_through_endpoint.with_streaming_response.create(
            headers={},
            path="path",
            target="target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = response.parse()
            assert_matches_type(object, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Hanzo) -> None:
        pass_through_endpoint = client.config.pass_through_endpoint.update(
            "endpoint_id",
        )
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Hanzo) -> None:
        response = client.config.pass_through_endpoint.with_raw_response.update(
            "endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = response.parse()
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Hanzo) -> None:
        with client.config.pass_through_endpoint.with_streaming_response.update(
            "endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = response.parse()
            assert_matches_type(object, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Hanzo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            client.config.pass_through_endpoint.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Hanzo) -> None:
        pass_through_endpoint = client.config.pass_through_endpoint.list()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Hanzo) -> None:
        pass_through_endpoint = client.config.pass_through_endpoint.list(
            endpoint_id="endpoint_id",
        )
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Hanzo) -> None:
        response = client.config.pass_through_endpoint.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = response.parse()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Hanzo) -> None:
        with client.config.pass_through_endpoint.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = response.parse()
            assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Hanzo) -> None:
        pass_through_endpoint = client.config.pass_through_endpoint.delete(
            endpoint_id="endpoint_id",
        )
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Hanzo) -> None:
        response = client.config.pass_through_endpoint.with_raw_response.delete(
            endpoint_id="endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = response.parse()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Hanzo) -> None:
        with client.config.pass_through_endpoint.with_streaming_response.delete(
            endpoint_id="endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = response.parse()
            assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPassThroughEndpoint:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncHanzo) -> None:
        pass_through_endpoint = await async_client.config.pass_through_endpoint.create(
            headers={},
            path="path",
            target="target",
        )
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHanzo) -> None:
        response = await async_client.config.pass_through_endpoint.with_raw_response.create(
            headers={},
            path="path",
            target="target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = await response.parse()
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHanzo) -> None:
        async with async_client.config.pass_through_endpoint.with_streaming_response.create(
            headers={},
            path="path",
            target="target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = await response.parse()
            assert_matches_type(object, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncHanzo) -> None:
        pass_through_endpoint = await async_client.config.pass_through_endpoint.update(
            "endpoint_id",
        )
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHanzo) -> None:
        response = await async_client.config.pass_through_endpoint.with_raw_response.update(
            "endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = await response.parse()
        assert_matches_type(object, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHanzo) -> None:
        async with async_client.config.pass_through_endpoint.with_streaming_response.update(
            "endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = await response.parse()
            assert_matches_type(object, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHanzo) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `endpoint_id` but received ''"):
            await async_client.config.pass_through_endpoint.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncHanzo) -> None:
        pass_through_endpoint = await async_client.config.pass_through_endpoint.list()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHanzo) -> None:
        pass_through_endpoint = await async_client.config.pass_through_endpoint.list(
            endpoint_id="endpoint_id",
        )
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHanzo) -> None:
        response = await async_client.config.pass_through_endpoint.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = await response.parse()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHanzo) -> None:
        async with async_client.config.pass_through_endpoint.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = await response.parse()
            assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncHanzo) -> None:
        pass_through_endpoint = await async_client.config.pass_through_endpoint.delete(
            endpoint_id="endpoint_id",
        )
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHanzo) -> None:
        response = await async_client.config.pass_through_endpoint.with_raw_response.delete(
            endpoint_id="endpoint_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pass_through_endpoint = await response.parse()
        assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHanzo) -> None:
        async with async_client.config.pass_through_endpoint.with_streaming_response.delete(
            endpoint_id="endpoint_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pass_through_endpoint = await response.parse()
            assert_matches_type(PassThroughEndpointResponse, pass_through_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True
