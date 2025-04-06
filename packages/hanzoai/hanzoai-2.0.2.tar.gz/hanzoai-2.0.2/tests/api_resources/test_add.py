# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hanzoai import Hanzo, AsyncHanzo
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdd:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_add_allowed_ip(self, client: Hanzo) -> None:
        add = client.add.add_allowed_ip(
            ip="ip",
        )
        assert_matches_type(object, add, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_allowed_ip(self, client: Hanzo) -> None:
        response = client.add.with_raw_response.add_allowed_ip(
            ip="ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add = response.parse()
        assert_matches_type(object, add, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_allowed_ip(self, client: Hanzo) -> None:
        with client.add.with_streaming_response.add_allowed_ip(
            ip="ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add = response.parse()
            assert_matches_type(object, add, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAdd:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_allowed_ip(self, async_client: AsyncHanzo) -> None:
        add = await async_client.add.add_allowed_ip(
            ip="ip",
        )
        assert_matches_type(object, add, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_allowed_ip(self, async_client: AsyncHanzo) -> None:
        response = await async_client.add.with_raw_response.add_allowed_ip(
            ip="ip",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        add = await response.parse()
        assert_matches_type(object, add, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_allowed_ip(self, async_client: AsyncHanzo) -> None:
        async with async_client.add.with_streaming_response.add_allowed_ip(
            ip="ip",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            add = await response.parse()
            assert_matches_type(object, add, path=["response"])

        assert cast(Any, response.is_closed) is True
