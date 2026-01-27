"""Unit tests for the Project resource."""

from __future__ import annotations

from datetime import date, datetime
from unittest.mock import MagicMock, patch

from requests import Response

from glnova.project.project import Project


class MockProject(Project):
    """Mock Project class for testing."""

    def __init__(self):
        """Initialize mock project."""
        self._get = MagicMock()


class TestProjectListProjects:
    """Test cases for the Project._list_projects method."""

    def test_list_authenticated_user_projects(self):
        """Test listing authenticated user's projects."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects(archived=True, search="test")

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/projects"
        assert call_args[1]["params"] == {"archived": True, "search": "test"}
        assert response == mock_response

    def test_list_user_projects(self):
        """Test listing a user's projects."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects(user_id=123, archived=False)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/users/123/projects"
        assert call_args[1]["params"] == {"archived": False}
        assert response == mock_response

    def test_list_group_projects(self):
        """Test listing group's projects."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects(group_id="backend-team", active=True)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/groups/backend-team/projects"
        assert call_args[1]["params"] == {"active": True}
        assert response == mock_response

    def test_list_projects_with_etag(self):
        """Test listing projects with ETag."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects(etag="abc123")

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[1]["etag"] == "abc123"
        assert response == mock_response

    def test_list_projects_with_kwargs(self):
        """Test listing projects with additional kwargs."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects(archived=True, page=2, per_page=50)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[1]["page"] == 2  # noqa: PLR2004
        assert call_args[1]["per_page"] == 50  # noqa: PLR2004
        assert response == mock_response

    def test_list_projects_multiple_filters(self):
        """Test listing projects with multiple filters."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        test_date = datetime(2023, 1, 1)
        response = mock_project._list_projects(
            archived=False,
            visibility="public",
            order_by="updated_at",
            sort="desc",
            search="api",
            last_activity_after=test_date,
            with_issues_enabled=True,
        )

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert params["archived"] is False
        assert params["visibility"] == "public"
        assert params["order_by"] == "updated_at"
        assert params["sort"] == "desc"
        assert params["search"] == "api"
        assert params["last_activity_after"] == test_date
        assert params["with_issues_enabled"] is True
        assert response == mock_response

    def test_list_projects_no_params(self):
        """Test listing projects with no parameters."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        response = mock_project._list_projects()

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/projects"
        assert call_args[1]["params"] == {}
        assert response == mock_response

    def test_list_projects_filters_none_values(self):
        """Test that None values are filtered out."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        _response = mock_project._list_projects(archived=True, search=None, simple=True)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert "search" not in params
        assert params["archived"] is True
        assert params["simple"] is True

    def test_list_projects_all_parameters(self):
        """Test listing projects with all supported parameters."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_project._get.return_value = mock_response

        test_date = datetime(2023, 1, 1)
        test_date_only = date(2023, 1, 1)

        response = mock_project._list_projects(
            user_id=None,
            group_id=None,
            archived=True,
            id_after=100,
            id_before=500,
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
            repository_storage="storage",
            search_namespaces=True,
            search="project",
            simple=True,
            sort="asc",
            starred=True,
            statistics=True,
            topic_id=1,
            topic=["python", "django"],
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
            with_shared=False,
            include_subgroups=False,
            with_security_reports=True,
        )

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/projects"
        assert response == mock_response


class TestPublicListProjects:
    """Test cases for the public list_projects method."""

    @patch("glnova.project.project.process_response_with_last_modified")
    def test_public_list_projects_authenticated(self, mock_process):
        """Test public list_projects method for authenticated user."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "name": "project1"}]
        mock_response.headers = {"etag": "abc123"}

        mock_project._list_projects = MagicMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 1, "name": "project1"}], 200, "abc123")

        result = mock_project.list_projects(archived=True)

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 1, "name": "project1"}], 200, "abc123")

    @patch("glnova.project.project.process_response_with_last_modified")
    def test_public_list_projects_user(self, mock_process):
        """Test public list_projects method for a user's projects."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 2, "name": "user_project"}]
        mock_response.headers = {}

        mock_project._list_projects = MagicMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 2, "name": "user_project"}], 200, None)

        result = mock_project.list_projects(user_id=456)

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 2, "name": "user_project"}], 200, None)

    @patch("glnova.project.project.process_response_with_last_modified")
    def test_public_list_projects_group(self, mock_process):
        """Test public list_projects method for a group's projects."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 3, "name": "group_project"}]
        mock_response.headers = {}

        mock_project._list_projects = MagicMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 3, "name": "group_project"}], 200, None)

        result = mock_project.list_projects(group_id="team")

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 3, "name": "group_project"}], 200, None)

    @patch("glnova.project.project.process_response_with_last_modified")
    def test_public_list_projects_with_multiple_parameters(self, mock_process):
        """Test public list_projects with multiple filtering parameters."""
        mock_project = MockProject()
        mock_response = MagicMock(spec=Response)
        mock_response.status_code = 200

        mock_project._list_projects = MagicMock(return_value=mock_response)
        mock_process.return_value = ([], 200, None)

        _result = mock_project.list_projects(archived=False, visibility="public", search="api", sort="asc")

        mock_project._list_projects.assert_called_once()
        call_args = mock_project._list_projects.call_args
        assert call_args[1]["archived"] is False
        assert call_args[1]["visibility"] == "public"
        assert call_args[1]["search"] == "api"
        assert call_args[1]["sort"] == "asc"
