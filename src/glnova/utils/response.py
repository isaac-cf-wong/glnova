from __future__ import annotations

from typing import Any

from aiohttp import ClientResponse
from requests import Response


def process_response_with_last_modified(
    response: Response,
) -> tuple[dict[str, Any] | list[dict[str, Any]], int, str | None]:
    """Process an HTTP response and extract data, status, and ETag.

    Args:
        response: The HTTP response object.

    Returns:
        A tuple containing the response data, status code, and ETag.
    """
    status_code = response.status_code
    etag = response.headers.get("Etag", None)
    data = response.json() if status_code == 200 else {}  # noqa: PLR2004
    return data, status_code, etag


async def process_async_response_with_last_modified(
    response: ClientResponse,
) -> tuple[dict[str, Any] | list[dict[str, Any]], int, str | None]:
    """Process an asynchronous HTTP response and extract data, status, and Etag.

    Args:
        response: The asynchronous HTTP response object.

    Returns:
        A tuple containing the response data, status code, and Etag.
    """
    status_code = response.status
    etag = response.headers.get("Etag", None)
    data = await response.json() if status_code == 200 else {}  # noqa: PLR2004
    return data, status_code, etag
