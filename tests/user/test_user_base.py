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

    def test_modify_user_helper_all_params(self):
        """Test _modify_user_helper with all parameters set."""
        base = BaseUser()
        endpoint, payload, kwargs = base._modify_user_helper(
            123,
            admin=True,
            auditor=False,
            avatar="http://example.com/avatar.jpg",
            bio="Test bio",
            can_create_group=True,
            color_scheme_id=1,
            commit_email="commit@example.com",
            email="test@example.com",
            extern_uid="ext123",
            external=False,
            extra_shared_runners_minutes_limit=100,
            group_id_for_saml=456,
            linkedin="linkedin.com/in/test",
            location="Test City",
            name="Test User",
            note="Test note",
            organization="Test Org",
            password="password123",  # pragma: allowlist secret
            private_profile=True,
            projects_limit=10,
            pronouns="they/them",
            provider="ldap",
            public_email="public@example.com",
            shared_runners_minutes_limit=50,
            skip_reconfirmation=True,
            theme_id=2,
            twitter="testuser",
            discord="test#1234",
            github="testuser",
            username="testuser",
            view_diffs_file_by_file=True,
            website_url="http://example.com",
            extra="value",
        )
        assert endpoint == "/users/123"
        expected_payload = {
            "admin": True,
            "auditor": False,
            "avatar": "http://example.com/avatar.jpg",
            "bio": "Test bio",
            "can_create_group": True,
            "color_scheme_id": 1,
            "commit_email": "commit@example.com",
            "email": "test@example.com",
            "extern_uid": "ext123",
            "external": False,
            "extra_shared_runners_minutes_limit": 100,
            "group_id_for_saml": 456,
            "linkedin": "linkedin.com/in/test",
            "location": "Test City",
            "name": "Test User",
            "note": "Test note",
            "organization": "Test Org",
            "password": "password123",  # pragma: allowlist secret
            "private_profile": True,
            "projects_limit": 10,
            "pronouns": "they/them",
            "provider": "ldap",
            "public_email": "public@example.com",
            "shared_runners_minutes_limit": 50,
            "skip_reconfirmation": True,
            "theme_id": 2,
            "twitter": "testuser",
            "discord": "test#1234",
            "github": "testuser",
            "username": "testuser",
            "view_diffs_file_by_file": True,
            "website_url": "http://example.com",
        }
        assert payload == expected_payload
        assert kwargs == {"extra": "value"}

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

    def test_list_users_helper_all_filters(self):
        """Test _list_users_helper with all filters set."""
        base = BaseUser()
        endpoint, params, kwargs = base._list_users_helper(
            username="testuser",
            public_email="public@example.com",
            search="search term",
            active=True,
            external=False,
            blocked=True,
            humans=True,
            created_after="2023-01-01",
            created_before="2023-12-31",
            exclude_active=False,
            exclude_external=True,
            exclude_humans=False,
            exclude_internal=True,
            without_project_bots=True,
            saml_provider_id=789,
            extern_uid="ext123",
            provider="ldap",
            two_factor="enabled",
            without_projects=True,
            admins=True,
            auditors=False,
            skip_ldap=True,
            page=2,
            per_page=10,
            order_by="name",
            sort="desc",
            extra="value",
        )
        assert endpoint == "/users"
        expected_params = {
            "username": "testuser",
            "public_email": "public@example.com",
            "search": "search term",
            "active": True,
            "external": False,
            "blocked": True,
            "humans": True,
            "created_after": "2023-01-01",
            "created_before": "2023-12-31",
            "exclude_active": False,
            "exclude_external": True,
            "exclude_humans": False,
            "exclude_internal": True,
            "without_project_bots": True,
            "saml_provider_id": 789,
            "extern_uid": "ext123",
            "provider": "ldap",
            "two_factor": "enabled",
            "without_projects": True,
            "admins": True,
            "auditors": False,
            "skip_ldap": True,
            "page": 2,
            "per_page": 10,
            "order_by": "name",
            "sort": "desc",
        }
        assert params == expected_params
        assert kwargs == {"extra": "value"}
