"""Unit tests for the synchronous GitLab client."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from glnova.client.gitlab import GitLab


class TestGitLab:
    """Test cases for the GitLab class."""

    def test_init_with_token(self):
        """Test initialization with a token."""
        client = GitLab(token="test_token", base_url="https://gitlab.com")
        assert client.token == "test_token"
        assert client.base_url == "https://gitlab.com"
        assert client.headers == {"Authorization": "Bearer test_token"}
        assert client.session is None

    def test_init_without_token(self):
        """Test initialization without a token."""
        client = GitLab(token=None, base_url="https://gitlab.com")
        assert client.token is None
        assert client.base_url == "https://gitlab.com"
        assert client.headers == {}
        assert client.session is None

    def test_str_representation(self):
        """Test string representation."""
        client = GitLab(token=None, base_url="https://gitlab.com")
        assert str(client) == "<GitLab base_url=https://gitlab.com>"

    def test_enter_context_manager(self):
        """Test entering the context manager."""
        client = GitLab(token=None, base_url="https://gitlab.com")
        with client as c:
            assert c is client
            assert isinstance(client.session, requests.Session)

    def test_exit_context_manager(self):
        """Test exiting the context manager."""
        client = GitLab(token=None, base_url="https://gitlab.com")
        with patch("requests.Session") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            with client:
                pass
            mock_session.close.assert_called_once()

    @patch("requests.Session")
    def test_request_success(self, mock_session_class):
        """Test successful _request."""
        mock_session = MagicMock()
        mock_session_class.return_value = mock_session
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_session.request.return_value = mock_response

        client = GitLab(token="test_token", base_url="https://gitlab.com")
        with client:
            response = client._request("GET", "repos/octocat/Hello-World", etag="test-etag")

        assert response == mock_response
        mock_session.request.assert_called_once_with(
            "GET",
            "https://gitlab.com/api/v4/repos/octocat/Hello-World",
            headers={"Authorization": "Bearer test_token", "If-None-Match": "test-etag"},
            timeout=30,
        )

    def test_request_without_session(self):
        """Test _request without entering context manager."""
        client = GitLab(token=None, base_url="https://gitlab.com")
        with pytest.raises(RuntimeError, match="GitLab must be used as a context manager"):
            client._request("GET", "repos/octocat/Hello-World")
