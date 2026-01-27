"""Unit tests for the base project module."""

from __future__ import annotations

from datetime import date, datetime

import pytest

from glnova.project.base import BaseProject


class TestListProjectsEndpoint:
    """Test cases for the _list_projects_endpoint method."""

    def test_endpoint_authenticated_user_projects(self):
        """Test endpoint for authenticated user's projects."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint()
        assert endpoint == "/projects"
        assert description == "authenticated user's projects"

    def test_endpoint_user_projects_with_user_id(self):
        """Test endpoint for user's projects with user ID."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint(user_id=123)
        assert endpoint == "/users/123/projects"
        assert description == "user's projects"

    def test_endpoint_user_projects_with_username(self):
        """Test endpoint for user's projects with username."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint(user_id="john_doe")
        assert endpoint == "/users/john_doe/projects"
        assert description == "user's projects"

    def test_endpoint_group_projects_with_group_id(self):
        """Test endpoint for group's projects with group ID."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint(group_id=456)
        assert endpoint == "/groups/456/projects"
        assert description == "group's projects"

    def test_endpoint_group_projects_with_group_name(self):
        """Test endpoint for group's projects with group name."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint(group_id="my-group")
        assert endpoint == "/groups/my-group/projects"
        assert description == "group's projects"

    def test_endpoint_group_projects_with_nested_path(self):
        """Test endpoint for group's projects with nested path."""
        base_project = BaseProject()
        endpoint, description = base_project._list_projects_endpoint(group_id="parent/child")
        # cSpell: disable
        assert endpoint == "/groups/parent%2Fchild/projects"
        # cSpell: enable
        assert description == "group's projects"

    def test_endpoint_error_both_user_and_group(self):
        """Test error when both user_id and group_id are provided."""
        base_project = BaseProject()
        with pytest.raises(ValueError, match=r"Either user_id or project_id must be provided, not both."):
            base_project._list_projects_endpoint(user_id=123, group_id=456)


class TestListAuthenticatedUserProjectsParams:
    """Test cases for the _list_authenticated_user_projects_params method."""

    def test_no_params(self):
        """Test with no parameters."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params()
        assert params == {}

    def test_single_param(self):
        """Test with a single parameter."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params(archived=True)
        assert params == {"archived": True}

    def test_multiple_params(self):
        """Test with multiple parameters."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params(
            archived=True,
            simple=True,
            sort="asc",
            search="test",
        )
        assert params == {
            "archived": True,
            "simple": True,
            "sort": "asc",
            "search": "test",
        }

    def test_none_values_excluded(self):
        """Test that None values are excluded from parameters."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params(
            archived=True,
            search=None,
            simple=True,
        )
        assert params == {"archived": True, "simple": True}
        assert "search" not in params

    def test_topic_list_conversion(self):
        """Test topic list conversion to comma-separated string."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params(topic=["python", "django"])
        assert params == {"topic": "python,django"}

    def test_topic_single_value(self):
        """Test single topic value."""
        base_project = BaseProject()
        params = base_project._list_authenticated_user_projects_params(topic=["python"])
        assert params == {"topic": "python"}

    def test_datetime_params(self):
        """Test datetime parameters."""
        base_project = BaseProject()
        test_date = datetime(2023, 1, 1, 12, 0, 0)
        params = base_project._list_authenticated_user_projects_params(last_activity_after=test_date)
        assert params == {"last_activity_after": test_date}

    def test_all_supported_params(self):
        """Test with all supported parameters."""
        base_project = BaseProject()
        test_date = datetime(2023, 1, 1, 12, 0, 0)
        test_date_only = date(2023, 1, 1)
        params = base_project._list_authenticated_user_projects_params(
            archived=True,
            id_after=100,
            id_before=200,
            imported=False,
            include_hidden=True,
            include_pending_delete=False,
            last_activity_after=test_date,
            last_activity_before=test_date,
            membership=True,
            min_access_level=30,
            order_by="name",
            owned=True,
            repository_checksum_failed=False,
            repository_storage="storage_name",
            search_namespaces=True,
            search="test",
            simple=True,
            sort="desc",
            starred=True,
            statistics=True,
            topic_id=1,
            topic=["python"],
            updated_after=test_date,
            updated_before=test_date,
            visibility="private",
            wiki_checksum_failed=False,
            with_custom_attributes=True,
            with_issues_enabled=True,
            with_merge_requests_enabled=True,
            with_programming_language="Python",
            marked_for_deletion_on=test_date_only,
            active=True,
        )
        assert len(params) == 32  # noqa: PLR2004
        assert params["archived"] is True
        assert params["search"] == "test"
        assert params["topic"] == "python"


class TestListUserProjectsParams:
    """Test cases for the _list_user_projects_params method."""

    def test_no_params(self):
        """Test with no parameters."""
        base_project = BaseProject()
        params = base_project._list_user_projects_params()
        assert params == {}

    def test_single_param(self):
        """Test with a single parameter."""
        base_project = BaseProject()
        params = base_project._list_user_projects_params(archived=False)
        assert params == {"archived": False}

    def test_multiple_params(self):
        """Test with multiple parameters."""
        base_project = BaseProject()
        params = base_project._list_user_projects_params(
            archived=False,
            starred=True,
            sort="asc",
        )
        assert params == {
            "archived": False,
            "starred": True,
            "sort": "asc",
        }

    def test_none_values_excluded(self):
        """Test that None values are excluded from parameters."""
        base_project = BaseProject()
        params = base_project._list_user_projects_params(
            archived=True,
            search=None,
        )
        assert params == {"archived": True}
        assert "search" not in params

    def test_user_params_subset(self):
        """Test that user params are a subset of authenticated user params."""
        base_project = BaseProject()
        test_date = datetime(2023, 1, 1)
        params = base_project._list_user_projects_params(
            archived=True,
            id_after=100,
            id_before=200,
            membership=True,
            min_access_level=30,
            order_by="name",
            owned=True,
            search="test",
            simple=True,
            sort="desc",
            starred=True,
            statistics=True,
            updated_after=test_date,
            updated_before=test_date,
            visibility="public",
            with_custom_attributes=True,
            with_issues_enabled=True,
            with_merge_requests_enabled=True,
            with_programming_language="Python",
        )
        assert len(params) == 19  # noqa: PLR2004
        assert "archived" in params
        assert "search" in params
        # These should not be in user params
        assert "topic" not in params
        assert "imported" not in params


class TestListGroupProjectsParams:
    """Test cases for the _list_group_projects_params method."""

    def test_no_params(self):
        """Test with no parameters."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params()
        assert params == {}

    def test_single_param(self):
        """Test with a single parameter."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params(active=True)
        assert params == {"active": True}

    def test_multiple_params(self):
        """Test with multiple parameters."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params(
            active=True,
            archived=False,
            visibility="public",
        )
        assert params == {
            "active": True,
            "archived": False,
            "visibility": "public",
        }

    def test_none_values_excluded(self):
        """Test that None values are excluded from parameters."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params(
            active=True,
            search=None,
        )
        assert params == {"active": True}
        assert "search" not in params

    def test_group_specific_params(self):
        """Test group-specific parameters."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params(
            with_shared=True,
            include_subgroups=True,
            with_security_reports=True,
        )
        assert params == {
            "with_shared": True,
            "include_subgroups": True,
            "with_security_reports": True,
        }

    def test_all_group_params(self):
        """Test with all group-specific parameters."""
        base_project = BaseProject()
        params = base_project._list_group_projects_params(
            active=True,
            archived=False,
            visibility="internal",
            order_by="updated_at",
            sort="desc",
            search="myproject",
            simple=True,
            owned=False,
            starred=False,
            topic="backend",
            with_issues_enabled=True,
            with_merge_requests_enabled=True,
            with_shared=True,
            include_subgroups=True,
            min_access_level=20,
            with_security_reports=True,
        )
        assert len(params) == 16  # noqa: PLR2004
        assert params["with_shared"] is True
        assert params["include_subgroups"] is True


class TestListProjectsHelper:
    """Test cases for the _list_projects_helper method."""

    def test_authenticated_user_projects_helper(self):
        """Test helper for authenticated user's projects."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(archived=True, search="test")
        assert endpoint == "/projects"
        assert params == {"archived": True, "search": "test"}

    def test_user_projects_helper(self):
        """Test helper for user's projects."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(user_id=123, archived=False, search="myproject")
        assert endpoint == "/users/123/projects"
        assert params == {"archived": False, "search": "myproject"}

    def test_group_projects_helper(self):
        """Test helper for group's projects."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(group_id="my-group", active=True, with_shared=True)
        assert endpoint == "/groups/my-group/projects"
        assert params == {"active": True, "with_shared": True}

    def test_helper_with_topic_conversion_authenticated(self):
        """Test topic string to list conversion in authenticated endpoint."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(topic="python")
        assert endpoint == "/projects"
        assert params == {"topic": "python"}

    def test_helper_with_topic_list_authenticated(self):
        """Test topic list handling in authenticated endpoint."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(topic=["python", "django"])
        assert endpoint == "/projects"
        assert params == {"topic": "python,django"}

    def test_helper_with_topic_string_group(self):
        """Test topic string handling in group endpoint."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(group_id=1, topic="python")
        assert endpoint == "/groups/1/projects"
        assert params == {"topic": "python"}

    def test_helper_with_topic_list_group(self):
        """Test that only first topic is used in group endpoint."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(group_id=1, topic=["python", "django"])
        assert endpoint == "/groups/1/projects"
        assert params == {"topic": "python"}

    def test_helper_endpoint_only_specific_params(self):
        """Test that endpoint-specific params are used correctly."""
        base_project = BaseProject()
        # User endpoint should not include 'with_shared' or 'include_subgroups'
        endpoint, params = base_project._list_projects_helper(user_id=123, with_shared=True, include_subgroups=True)
        assert endpoint == "/users/123/projects"
        assert "with_shared" not in params
        assert "include_subgroups" not in params

    def test_helper_authenticated_endpoint_has_membership(self):
        """Test that authenticated endpoint includes membership param."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(membership=True)
        assert endpoint == "/projects"
        assert params == {"membership": True}

    def test_helper_user_endpoint_has_membership(self):
        """Test that user endpoint includes membership param."""
        base_project = BaseProject()
        endpoint, params = base_project._list_projects_helper(user_id=123, membership=False)
        assert endpoint == "/users/123/projects"
        assert params == {"membership": False}
