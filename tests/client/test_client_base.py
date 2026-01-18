"""Unit tests for the base client."""

from glnova.client.base import Client


class TestClient:
    """Test cases for the Client class."""

    def test_init_with_token(self):
        """Test initialization with a token."""
        client = Client(token="test_token", base_url="https://gitlab.com")
        assert client.token == "test_token"
        assert client.base_url == "https://gitlab.com"
        assert client.headers == {"Authorization": "Bearer test_token"}

    def test_init_without_token(self):
        """Test initialization without a token."""
        client = Client(token=None, base_url="https://gitlab.com")
        assert client.token is None
        assert client.base_url == "https://gitlab.com"
        assert client.headers == {}

    def test_init_custom_base_url(self):
        """Test initialization with a custom base URL."""
        client = Client(token="test_token", base_url="https://custom.gitlab.com/")
        assert client.base_url == "https://custom.gitlab.com"
        assert client.headers == {"Authorization": "Bearer test_token"}

    def test_str_representation(self):
        """Test string representation."""
        client = Client(token=None, base_url="https://gitlab.com")
        assert str(client) == "<Client base_url=https://gitlab.com>"

    def test_api_url_gitlab_com(self):
        """Test api_url for gitlab.com."""
        client = Client(token=None, base_url="https://gitlab.com")
        assert client.api_url == "https://gitlab.com/api/v4"

    def test_api_url_custom(self):
        """Test api_url for custom base URL."""
        client = Client(token=None, base_url="https://custom.gitlab.com")
        assert client.api_url == "https://custom.gitlab.com/api/v4"

    def test_build_url_simple(self):
        """Test _build_url with a simple endpoint."""
        client = Client(token=None, base_url="https://gitlab.com")
        url = client._build_url("repos/octocat/Hello-World")
        assert url == "https://gitlab.com/api/v4/repos/octocat/Hello-World"

    def test_build_url_with_leading_slash(self):
        """Test _build_url with endpoint starting with slash."""
        client = Client(token=None, base_url="https://gitlab.com")
        url = client._build_url("/repos/octocat/Hello-World")
        assert url == "https://gitlab.com/api/v4/repos/octocat/Hello-World"

    def test_build_url_custom_base(self):
        """Test _build_url with custom base URL."""
        client = Client(token=None, base_url="https://custom.gitlab.com")
        url = client._build_url("repos/octocat/Hello-World")
        assert url == "https://custom.gitlab.com/api/v4/repos/octocat/Hello-World"

    def test_get_conditional_request_headers(self):
        """Test _get_conditional_request_headers method."""
        client = Client(token=None, base_url="https://gitlab.com")
        headers = client._get_conditional_request_headers(etag="test-etag")
        assert headers == {"If-None-Match": "test-etag"}

    def test_get_conditional_request_headers_none(self):
        """Test _get_conditional_request_headers with None values."""
        client = Client(token=None, base_url="https://gitlab.com")
        headers = client._get_conditional_request_headers()
        assert headers == {}
