"""Unit tests for the AsyncProject resource."""

from __future__ import annotations

from datetime import date, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from aiohttp import ClientResponse

from glnova.project.async_project import AsyncProject


class MockAsyncProject(AsyncProject):
    """Mock AsyncProject class for testing."""

    def __init__(self):
        """Initialize mock async project."""
        self._get = AsyncMock()


class TestAsyncProjectListProjects:
    """Test cases for the AsyncProject._list_projects method."""

    @pytest.mark.asyncio
    async def test_async_list_authenticated_user_projects(self):
        """Test listing authenticated user's projects asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects(archived=True, search="test")

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/projects"
        assert call_args[1]["params"] == {"archived": True, "search": "test"}
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_user_projects(self):
        """Test listing a user's projects asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects(user_id=789, archived=False)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/users/789/projects"
        assert call_args[1]["params"] == {"archived": False}
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_group_projects(self):
        """Test listing group's projects asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects(group_id="frontend-team", active=True)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/groups/frontend-team/projects"
        assert call_args[1]["params"] == {"active": True}
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_with_etag(self):
        """Test listing projects with ETag asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects(etag="def456")

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[1]["etag"] == "def456"
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_with_kwargs(self):
        """Test listing projects with additional kwargs asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects(archived=True, page=3, per_page=25)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[1]["page"] == 3  # noqa: PLR2004
        assert call_args[1]["per_page"] == 25  # noqa: PLR2004
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_multiple_filters(self):
        """Test listing projects with multiple filters asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        test_date = datetime(2023, 6, 15)
        response = await mock_project._list_projects(
            archived=False,
            visibility="internal",
            order_by="created_at",
            sort="desc",
            search="service",
            last_activity_after=test_date,
            with_merge_requests_enabled=True,
        )

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert params["archived"] is False
        assert params["visibility"] == "internal"
        assert params["order_by"] == "created_at"
        assert params["sort"] == "desc"
        assert params["search"] == "service"
        assert params["last_activity_after"] == test_date
        assert params["with_merge_requests_enabled"] is True
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_no_params(self):
        """Test listing projects with no parameters asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        response = await mock_project._list_projects()

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/projects"
        assert call_args[1]["params"] == {}
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_filters_none_values(self):
        """Test that None values are filtered out asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        _response = await mock_project._list_projects(archived=True, search=None, simple=True)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert "search" not in params
        assert params["archived"] is True
        assert params["simple"] is True

    @pytest.mark.asyncio
    async def test_async_list_projects_all_parameters(self):
        """Test listing projects with all supported parameters asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        test_date = datetime(2023, 3, 1)
        test_date_only = date(2023, 3, 1)

        response = await mock_project._list_projects(
            group_id="backend",
            archived=False,
            id_after=50,
            id_before=250,
            imported=True,
            include_hidden=False,
            include_pending_delete=True,
            last_activity_after=test_date,
            last_activity_before=test_date,
            membership=False,
            min_access_level=10,
            order_by="star_count",
            owned=False,
            repository_checksum_failed=True,
            repository_storage="external",
            search_namespaces=False,
            search="backend",
            simple=False,
            sort="desc",
            starred=False,
            statistics=False,
            topic_id=2,
            topic=["rust", "backend"],
            updated_after=test_date,
            updated_before=test_date,
            visibility="public",
            wiki_checksum_failed=True,
            with_custom_attributes=False,
            with_issues_enabled=False,
            with_merge_requests_enabled=False,
            with_programming_language="Rust",
            marked_for_deletion_on=test_date_only,
            active=False,
            with_shared=True,
            include_subgroups=True,
            with_security_reports=False,
        )

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        assert call_args[0][0] == "/groups/backend/projects"
        assert response == mock_response

    @pytest.mark.asyncio
    async def test_async_list_projects_with_topic_list(self):
        """Test listing projects with topic list asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        _response = await mock_project._list_projects(topic=["python", "asyncio", "web"])

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert params["topic"] == "python,asyncio,web"

    @pytest.mark.asyncio
    async def test_async_list_projects_with_min_access_level(self):
        """Test listing projects with minimum access level asynchronously."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_project._get.return_value = mock_response

        _response = await mock_project._list_projects(min_access_level=40)

        mock_project._get.assert_called_once()
        call_args = mock_project._get.call_args
        params = call_args[1]["params"]
        assert params["min_access_level"] == 40  # noqa: PLR2004


class TestPublicAsyncListProjects:
    """Test cases for the public async list_projects method."""

    @pytest.mark.asyncio
    @patch("glnova.project.async_project.process_async_response_with_last_modified")
    async def test_public_async_list_projects_authenticated(self, mock_process):
        """Test public async list_projects method for authenticated user."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_response.status = 200

        mock_project._list_projects = AsyncMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 1, "name": "async_project1"}], 200, "xyz789")

        result = await mock_project.list_projects(archived=False)

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 1, "name": "async_project1"}], {"status_code": 200, "etag": "xyz789"})

    @pytest.mark.asyncio
    @patch("glnova.project.async_project.process_async_response_with_last_modified")
    async def test_public_async_list_projects_user(self, mock_process):
        """Test public async list_projects method for a user's projects."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_response.status = 200

        mock_project._list_projects = AsyncMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 2, "name": "async_user_project"}], 200, None)

        result = await mock_project.list_projects(user_id=999)

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 2, "name": "async_user_project"}], {"status_code": 200, "etag": None})

    @pytest.mark.asyncio
    @patch("glnova.project.async_project.process_async_response_with_last_modified")
    async def test_public_async_list_projects_group(self, mock_process):
        """Test public async list_projects method for a group's projects."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_response.status = 200

        mock_project._list_projects = AsyncMock(return_value=mock_response)
        mock_process.return_value = ([{"id": 3, "name": "async_group_project"}], 200, None)

        result = await mock_project.list_projects(group_id="devops")

        mock_project._list_projects.assert_called_once()
        assert result == ([{"id": 3, "name": "async_group_project"}], {"status_code": 200, "etag": None})

    @pytest.mark.asyncio
    @patch("glnova.project.async_project.process_async_response_with_last_modified")
    async def test_public_async_list_projects_with_etag(self, mock_process):
        """Test public async list_projects with ETag."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_response.status = 304

        mock_project._list_projects = AsyncMock(return_value=mock_response)
        mock_process.return_value = ([], 304, "cached-etag")

        result = await mock_project.list_projects(etag="cached-etag")

        mock_project._list_projects.assert_called_once()
        # ETag is passed to _get, not _list_projects, so we check the result
        assert result == ([], {"status_code": 304, "etag": "cached-etag"})

    @pytest.mark.asyncio
    @patch("glnova.project.async_project.process_async_response_with_last_modified")
    async def test_public_async_list_projects_with_multiple_parameters(self, mock_process):
        """Test public async list_projects with multiple parameters."""
        mock_project = MockAsyncProject()
        mock_response = MagicMock(spec=ClientResponse)
        mock_response.status = 200

        mock_project._list_projects = AsyncMock(return_value=mock_response)
        mock_process.return_value = ([], 200, None)

        _result = await mock_project.list_projects(
            archived=True, visibility="private", search="database", sort="asc", order_by="name"
        )

        mock_project._list_projects.assert_called_once()
        call_args = mock_project._list_projects.call_args
        assert call_args[1]["archived"] is True
        assert call_args[1]["visibility"] == "private"
        assert call_args[1]["search"] == "database"
        assert call_args[1]["sort"] == "asc"
        assert call_args[1]["order_by"] == "name"
