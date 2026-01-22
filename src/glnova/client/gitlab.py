"""GitLab API client implementation."""

from __future__ import annotations

from typing import Any

import requests
from requests import Response

from glnova.client.base import Client
from glnova.issue.issue import Issue
from glnova.user.user import User


class GitLab(Client):
    """Synchronous GitLab API client."""

    def __init__(self, token: str | None = None, base_url: str = "https://gitlab.com") -> None:
        """Initialize the GitLab client.

        Args:
            token: The API token for authentication.
            base_url: The base URL of the GitLab instance.

        """
        super().__init__(token=token, base_url=base_url)
        self.session: requests.Session | None = None

        # Initialize resource handlers
        self.issue = Issue(client=self)
        self.user = User(client=self)

    def __str__(self) -> str:
        """Return a string representation of the GitLab client.

        Returns:
            str: String representation.

        """
        return f"<GitLab base_url={self.base_url}>"

    def __enter__(self) -> GitLab:
        """Enter the context manager.

        Returns:
            The GitLab client instance.

        """
        if self.session is not None:
            raise RuntimeError("GitLab session already open; do not re-enter context manager.")
        self.session = requests.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the context manager.

        Args:
            exc_type: The exception type.
            exc_val: The exception value.
            exc_tb: The traceback.

        """
        if self.session:
            self.session.close()
            self.session = None

    def _request(
        self,
        method: str,
        endpoint: str,
        etag: str | None = None,
        headers: dict | None = None,
        timeout: int = 30,
        **kwargs: Any,
    ) -> Response:
        """Make an HTTP request to the GitLab API.

        Args:
            method: The HTTP method (GET, POST, etc.).
            endpoint: The API endpoint.
            etag: The ETag value for conditional requests.
            headers: Additional headers for the request.
            timeout: Timeout for the request in seconds.
            **kwargs: Additional arguments for the request.

        Returns:
            The HTTP response.

        """
        if self.session is None:
            raise RuntimeError(
                "GitLab must be used as a context manager. "
                + "Use 'with GitLab(...) as client:' to ensure proper resource cleanup."
            )
        url = self._build_url(endpoint=endpoint)
        conditional_headers = self._get_conditional_request_headers(etag=etag)
        request_headers = {**self.headers, **conditional_headers, **(headers or {})}
        response = self.session.request(method, url, headers=request_headers, timeout=timeout, **kwargs)
        try:
            response.raise_for_status()
        except Exception:
            response.close()
            raise

        return response
