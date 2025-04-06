# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options

__all__ = ["CancelResource", "AsyncCancelResource"]


class CancelResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CancelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hanzoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CancelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CancelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hanzoai/python-sdk#with_streaming_response
        """
        return CancelResourceWithStreamingResponse(self)

    def create(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancel a fine-tuning job.

        This is the equivalent of POST
        https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel

        Supported Query Params:

        - `custom_llm_provider`: Name of the LLM provider
        - `fine_tuning_job_id`: The ID of the fine-tuning job to cancel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return self._post(
            f"/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCancelResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCancelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hanzoai/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCancelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCancelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hanzoai/python-sdk#with_streaming_response
        """
        return AsyncCancelResourceWithStreamingResponse(self)

    async def create(
        self,
        fine_tuning_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Cancel a fine-tuning job.

        This is the equivalent of POST
        https://api.openai.com/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel

        Supported Query Params:

        - `custom_llm_provider`: Name of the LLM provider
        - `fine_tuning_job_id`: The ID of the fine-tuning job to cancel.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not fine_tuning_job_id:
            raise ValueError(f"Expected a non-empty value for `fine_tuning_job_id` but received {fine_tuning_job_id!r}")
        return await self._post(
            f"/v1/fine_tuning/jobs/{fine_tuning_job_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CancelResourceWithRawResponse:
    def __init__(self, cancel: CancelResource) -> None:
        self._cancel = cancel

        self.create = to_raw_response_wrapper(
            cancel.create,
        )


class AsyncCancelResourceWithRawResponse:
    def __init__(self, cancel: AsyncCancelResource) -> None:
        self._cancel = cancel

        self.create = async_to_raw_response_wrapper(
            cancel.create,
        )


class CancelResourceWithStreamingResponse:
    def __init__(self, cancel: CancelResource) -> None:
        self._cancel = cancel

        self.create = to_streamed_response_wrapper(
            cancel.create,
        )


class AsyncCancelResourceWithStreamingResponse:
    def __init__(self, cancel: AsyncCancelResource) -> None:
        self._cancel = cancel

        self.create = async_to_streamed_response_wrapper(
            cancel.create,
        )
