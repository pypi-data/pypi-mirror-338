# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["InputItemsResource", "AsyncInputItemsResource"]


class InputItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InputItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hanzoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return InputItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InputItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hanzoai/python-sdk#with_streaming_response
        """
        return InputItemsResourceWithStreamingResponse(self)

    def list(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get input items for a response.

        Follows the OpenAI Responses API spec:
        https://platform.openai.com/docs/api-reference/responses/input-items

        ```bash
        curl -X GET http://localhost:4000/v1/responses/resp_abc123/input_items     -H "Authorization: Bearer sk-1234"
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return self._get(
            f"/v1/responses/{response_id}/input_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncInputItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInputItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hanzoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInputItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInputItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hanzoai/python-sdk#with_streaming_response
        """
        return AsyncInputItemsResourceWithStreamingResponse(self)

    async def list(
        self,
        response_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Get input items for a response.

        Follows the OpenAI Responses API spec:
        https://platform.openai.com/docs/api-reference/responses/input-items

        ```bash
        curl -X GET http://localhost:4000/v1/responses/resp_abc123/input_items     -H "Authorization: Bearer sk-1234"
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not response_id:
            raise ValueError(f"Expected a non-empty value for `response_id` but received {response_id!r}")
        return await self._get(
            f"/v1/responses/{response_id}/input_items",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class InputItemsResourceWithRawResponse:
    def __init__(self, input_items: InputItemsResource) -> None:
        self._input_items = input_items

        self.list = to_raw_response_wrapper(
            input_items.list,
        )


class AsyncInputItemsResourceWithRawResponse:
    def __init__(self, input_items: AsyncInputItemsResource) -> None:
        self._input_items = input_items

        self.list = async_to_raw_response_wrapper(
            input_items.list,
        )


class InputItemsResourceWithStreamingResponse:
    def __init__(self, input_items: InputItemsResource) -> None:
        self._input_items = input_items

        self.list = to_streamed_response_wrapper(
            input_items.list,
        )


class AsyncInputItemsResourceWithStreamingResponse:
    def __init__(self, input_items: AsyncInputItemsResource) -> None:
        self._input_items = input_items

        self.list = async_to_streamed_response_wrapper(
            input_items.list,
        )
