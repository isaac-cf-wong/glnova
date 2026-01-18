"""Unit tests for the base user."""

from glnova.user.base import BaseUser


class TestBaseUser:
    """Test cases for the BaseUser class."""

    def test_get_user_endpoint_none(self):
        """Test _get_user_endpoint with None account_id."""
        base = BaseUser()
        assert base._get_user_endpoint(None) == "/user"

    def test_get_user_endpoint_with_id(self):
        """Test _get_user_endpoint with account_id."""
        base = BaseUser()
        assert base._get_user_endpoint(123) == "/users/123"

    def test_get_user_helper_none(self):
        """Test _get_user_helper with None account_id."""
        base = BaseUser()
        endpoint, kwargs = base._get_user_helper(None, key="value")
        assert endpoint == "/user"
        assert kwargs == {"key": "value"}

    def test_get_user_helper_with_id(self):
        """Test _get_user_helper with account_id."""
        base = BaseUser()
        endpoint, kwargs = base._get_user_helper(123, key="value")
        assert endpoint == "/users/123"
        assert kwargs == {"key": "value"}

    def test_modify_user_endpoint(self):
        """Test _modify_user_endpoint."""
        base = BaseUser()
        assert base._modify_user_endpoint(123) == "/users/123"

    def test_modify_user_helper(self):
        """Test _modify_user_helper with some parameters."""
        base = BaseUser()
        endpoint, payload, kwargs = base._modify_user_helper(
            123, name="Test User", email="test@example.com", extra="value"
        )
        assert endpoint == "/users/123"
        expected_payload = {"name": "Test User", "email": "test@example.com"}
        assert payload == expected_payload
        assert kwargs == {"extra": "value"}

    def test_modify_user_helper_none_values(self):
        """Test _modify_user_helper with None values (should not include in payload)."""
        base = BaseUser()
        endpoint, payload, kwargs = base._modify_user_helper(123, name=None, email="test@example.com")
        assert endpoint == "/users/123"
        expected_payload = {"email": "test@example.com"}
        assert payload == expected_payload
        assert kwargs == {}

    def test_list_users_endpoint(self):
        """Test _list_users_endpoint."""
        base = BaseUser()
        assert base._list_users_endpoint() == "/users"

    def test_list_users_helper_defaults(self):
        """Test _list_users_helper with default parameters."""
        base = BaseUser()
        endpoint, params, kwargs = base._list_users_helper()
        assert endpoint == "/users"
        expected_params = {"page": 1, "per_page": 20, "order_by": "id", "sort": "asc"}
        assert params == expected_params
        assert kwargs == {}

    def test_list_users_helper_with_filters(self):
        """Test _list_users_helper with some filters."""
        base = BaseUser()
        endpoint, params, kwargs = base._list_users_helper(
            username="testuser", active=True, page=2, per_page=10, extra="value"
        )
        assert endpoint == "/users"
        expected_params = {
            "username": "testuser",
            "active": True,
            "page": 2,
            "per_page": 10,
            "order_by": "id",
            "sort": "asc",
        }
        assert params == expected_params
        assert kwargs == {"extra": "value"}

    def test_list_users_helper_exclude_filters(self):
        """Test _list_users_helper with exclude filters."""
        base = BaseUser()
        endpoint, params, kwargs = base._list_users_helper(
            exclude_active=True, exclude_external=False, without_project_bots=True
        )
        assert endpoint == "/users"
        expected_params = {
            "exclude_active": True,
            "exclude_external": False,
            "without_project_bots": True,
            "page": 1,
            "per_page": 20,
            "order_by": "id",
            "sort": "asc",
        }
        assert params == expected_params
        assert kwargs == {}
