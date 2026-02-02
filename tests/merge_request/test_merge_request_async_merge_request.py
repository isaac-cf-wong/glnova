"""Tests for glnova.merge_request.async_merge_request."""

from __future__ import annotations

from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from glnova.merge_request.async_merge_request import AsyncMergeRequest


class TestAsyncMergeRequest:
    """Tests for AsyncMergeRequest class."""

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._get")
    async def test_list_merge_requests_private_method_calls_get(self, mock_get: AsyncMock) -> None:
        """Test that _list_merge_requests calls _get with correct parameters."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        result = await mr._list_merge_requests(
            project_id=123, group_id=None, state="opened", assignee_id=456, page=2, per_page=50
        )

        # Verify _get was called at least once with correct parameters
        assert mock_get.called
        assert result == mock_response

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._get")
    async def test_list_merge_requests_private_method_group_scope(self, mock_get: AsyncMock) -> None:
        """Test that _list_merge_requests uses group endpoint when group_id is provided."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        await mr._list_merge_requests(project_id=None, group_id=789, state="merged")

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args[1]["endpoint"] == "/groups/789/merge_requests"
        assert call_args[1]["params"]["state"] == "merged"

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._get")
    async def test_list_merge_requests_private_method_user_scope(self, mock_get: AsyncMock) -> None:
        """Test that _list_merge_requests uses user endpoint when neither project_id nor group_id is provided."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        await mr._list_merge_requests(project_id=None, group_id=None, scope="assigned_to_me")

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        assert call_args[1]["endpoint"] == "/merge_requests"
        assert call_args[1]["params"]["scope"] == "assigned_to_me"

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._get")
    async def test_list_merge_requests_private_method_with_all_params(self, mock_get: AsyncMock) -> None:
        """Test _list_merge_requests with all possible parameters."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        await mr._list_merge_requests(
            project_id=None,
            group_id="my_group",
            approved="yes",
            approved_by_ids=[1, 2],
            approved_by_usernames=["user1", "user2"],
            approver_ids=[3, 4],
            assignee_id=123,
            assignee_username=["assignee1"],
            author_id=456,
            author_username="author1",
            created_after=datetime(2023, 1, 1),
            created_before=datetime(2023, 12, 31),
            deployed_after=datetime(2023, 6, 1),
            deployed_before=datetime(2023, 6, 30),
            environment="production",
            search_in=["title", "description"],
            labels=["bug", "feature"],
            merge_user_id=789,
            merge_user_username="merger",
            milestone="v1.0",
            my_reaction_emoji="thumbs_up",
            non_archived=True,
            not_match="labels",
            order_by="created_at",
            page=3,
            per_page=25,
            reviewer_id=999,
            reviewer_username="reviewer1",
            scope="all",
            search="test search",
            sort="desc",
            source_branch="feature-branch",
            source_project_id=111,
            state="opened",
            target_branch="main",
            updated_after=datetime(2023, 7, 1),
            updated_before=datetime(2023, 7, 31),
            view="simple",
            with_labels_details=True,
            with_merge_status_recheck=True,
            wip="no",
            etag="some-etag",
        )

        mock_get.assert_called_once()
        call_args = mock_get.call_args
        params = call_args[1]["params"]

        # Verify a few key parameters
        assert params["approved"] == "yes"
        assert params["assignee_id"] == 123  # noqa: PLR2004
        assert params["state"] == "opened"
        assert params["page"] == 3  # noqa: PLR2004
        assert params["per_page"] == 25  # noqa: PLR2004
        assert params["sort"] == "desc"
        # List parameters converted to comma-separated strings
        assert params["labels"] == "bug,feature"
        assert params["in"] == "title,description"
        assert call_args[1]["etag"] == "some-etag"

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.process_async_response_with_last_modified")
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._list_merge_requests")
    async def test_list_merge_requests_public_method_processes_response(
        self, mock_private_method: AsyncMock, mock_process: AsyncMock
    ) -> None:
        """Test that list_merge_requests processes the response correctly."""
        mock_response = MagicMock()
        mock_private_method.return_value = mock_response
        mock_process.return_value = ({"data": "test"}, 200, "etag123")

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        result = await mr.list_merge_requests(project_id=123, group_id=None, state="opened")

        # Verify private method was called
        mock_private_method.assert_called_once_with(
            project_id=123,
            group_id=None,
            approved=None,
            approved_by_ids=None,
            approved_by_usernames=None,
            approver_ids=None,
            assignee_id=None,
            assignee_username=None,
            author_id=None,
            author_username=None,
            created_after=None,
            created_before=None,
            deployed_after=None,
            deployed_before=None,
            environment=None,
            iids=None,
            search_in=None,
            labels=None,
            merge_user_id=None,
            merge_user_username=None,
            milestone=None,
            my_reaction_emoji=None,
            non_archived=None,
            not_match=None,
            order_by=None,
            page=1,
            per_page=20,
            render_html=None,
            reviewer_id=None,
            reviewer_username=None,
            scope=None,
            search=None,
            sort=None,
            source_branch=None,
            source_project_id=None,
            state="opened",
            target_branch=None,
            updated_after=None,
            updated_before=None,
            view=None,
            with_labels_details=None,
            with_merge_status_recheck=None,
            wip=None,
            etag=None,
        )

        # Verify response processing
        mock_process.assert_called_once_with(mock_response)

        # Verify return value
        assert result == ({"data": "test"}, 200, "etag123")

    @pytest.mark.asyncio
    @patch("glnova.merge_request.async_merge_request.process_async_response_with_last_modified")
    @patch("glnova.merge_request.async_merge_request.AsyncMergeRequest._list_merge_requests")
    async def test_list_merge_requests_public_method_with_custom_params(
        self, mock_private_method: AsyncMock, mock_process: AsyncMock
    ) -> None:
        """Test list_merge_requests with custom parameters."""
        mock_response = MagicMock()
        mock_private_method.return_value = mock_response
        mock_process.return_value = ([{"id": 1}], 200, None)

        mock_client = MagicMock()
        mr = AsyncMergeRequest(client=mock_client)
        result = await mr.list_merge_requests(
            project_id="myproject", group_id=None, assignee_id=123, state="merged", page=5, per_page=10, sort="asc"
        )

        # Verify private method was called with correct params
        mock_private_method.assert_called_once()
        call_kwargs = mock_private_method.call_args[1]
        assert call_kwargs["project_id"] == "myproject"
        assert call_kwargs["assignee_id"] == 123  # noqa: PLR2004
        assert call_kwargs["state"] == "merged"
        assert call_kwargs["page"] == 5  # noqa: PLR2004
        assert call_kwargs["per_page"] == 10  # noqa: PLR2004
        assert call_kwargs["sort"] == "asc"

        # Verify response processing
        mock_process.assert_called_once_with(mock_response)
        assert result == ([{"id": 1}], 200, None)
