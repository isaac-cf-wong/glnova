"""Tests for glnova.cli.merge_request.list."""

from __future__ import annotations

import json
import re
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
import typer
from typer.testing import CliRunner

from glnova.cli.main import app
from glnova.cli.merge_request.list import list_command


class TestListCommand:
    """Tests for merge request list command."""

    @staticmethod
    def _strip_ansi(text: str) -> str:
        """Remove ANSI escape codes from text."""
        return re.sub(r"\x1b\[[0-9;]*m", "", text)

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a CLI runner for testing."""
        return CliRunner()

    @pytest.fixture
    def mock_config_path(self) -> str:
        """Mock config path for testing."""
        return "/path/to/config"

    @pytest.fixture
    def mock_context(self, mock_config_path: str) -> MagicMock:
        """Create a mock typer context."""
        ctx = MagicMock()
        ctx.obj = {"config_path": mock_config_path}
        return ctx

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_basic_success(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock, capsys
    ) -> None:
        """Test list command with basic parameters succeeds."""
        # Setup mocks
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = (
            [{"id": 1, "title": "Test MR"}],
            {"status_code": 200, "etag": "etag123"},
        )

        # Call the function
        list_command(ctx=mock_context, project_id="123", state="opened")

        # Verify auth was called
        mock_get_auth.assert_called_once_with(
            config_path="/path/to/config", account_name=None, token=None, base_url=None
        )

        # Verify GitLab client was created
        mock_gitlab.assert_called_once_with(token="test_token", base_url="https://gitlab.example.com")

        # Verify list_merge_requests was called with correct params
        mock_client.merge_request.list_merge_requests.assert_called_once()
        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["project_id"] == 123  # Converted to int  # noqa: PLR2004
        assert call_kwargs["group_id"] is None
        assert call_kwargs["state"] == "opened"

        # Verify output
        captured = capsys.readouterr()
        output_data = json.loads(captured.out.strip())
        assert output_data["data"] == [{"id": 1, "title": "Test MR"}]
        assert output_data["metadata"]["status_code"] == 200  # noqa: PLR2004
        assert output_data["metadata"]["etag"] == "etag123"

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_group_id(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with group_id parameter."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(ctx=mock_context, group_id="456", approved="yes")

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["project_id"] is None
        assert call_kwargs["group_id"] == 456  # Converted to int  # noqa: PLR2004
        assert call_kwargs["approved"] == "yes"

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_literal_values(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with literal values like 'None' and 'Any'."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(ctx=mock_context, assignee_id="None", author_id="Any", labels=["None"], milestone="Any")

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["assignee_id"] == "None"
        assert call_kwargs["author_id"] == "Any"
        assert call_kwargs["labels"] == "None"
        assert call_kwargs["milestone"] == "Any"

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_list_parameters(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with list parameters."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(
            ctx=mock_context,
            approved_by_ids=["1", "2", "3"],
            search_in=["title", "description"],
            labels=["bug", "feature"],
        )

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["approved_by_ids"] == [1, 2, 3]  # Converted to list of ints
        assert call_kwargs["search_in"] == ["title", "description"]
        assert call_kwargs["labels"] == ["bug", "feature"]

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_datetime_parameters(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with datetime parameters."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        created_after = datetime(2023, 1, 1)
        updated_before = datetime(2023, 12, 31)

        list_command(ctx=mock_context, created_after=created_after, updated_before=updated_before)

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["created_after"] == created_after
        assert call_kwargs["updated_before"] == updated_before

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_pagination(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with pagination parameters."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(ctx=mock_context, page=5, per_page=50)

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["page"] == 5  # noqa: PLR2004
        assert call_kwargs["per_page"] == 50  # noqa: PLR2004

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_auth_parameters(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with custom auth parameters."""
        mock_get_auth.return_value = ("custom_token", "https://custom.gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(
            ctx=mock_context, account_name="test_account", token="custom_token", base_url="https://custom.gitlab.com"
        )

        mock_get_auth.assert_called_once_with(
            config_path="/path/to/config",
            account_name="test_account",
            token="custom_token",
            base_url="https://custom.gitlab.com",
        )

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_exception_handling(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command handles exceptions properly."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.side_effect = Exception("API Error")

        with pytest.raises(typer.Exit) as exc_info:
            list_command(ctx=mock_context, project_id="123")

        assert exc_info.value.exit_code == 1

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_all_parameters(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with all possible parameters."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(
            ctx=mock_context,
            project_id="123",
            group_id="456",
            approved="yes",
            approved_by_ids=["1", "2"],
            approved_by_usernames=["user1", "user2"],
            approver_ids=["3", "4"],
            assignee_id="5",
            assignee_username=["assignee1"],
            author_id="6",
            author_username="author1",
            created_after=datetime(2023, 1, 1),
            created_before=datetime(2023, 12, 31),
            deployed_after=datetime(2023, 6, 1),
            deployed_before=datetime(2023, 6, 30),
            environment="production",
            iids=[10, 20],
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
            render_html=True,
            reviewer_id="999",
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
            account_name="test_account",
            token="test_token",
            base_url="https://gitlab.example.com",
        )

        # Verify the call was made (detailed parameter checking would be too extensive)
        mock_client.merge_request.list_merge_requests.assert_called_once()
        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]

        # Spot check some key parameters
        assert call_kwargs["project_id"] == 123  # noqa: PLR2004
        assert call_kwargs["group_id"] == 456  # noqa: PLR2004
        assert call_kwargs["approved"] == "yes"
        assert call_kwargs["state"] == "opened"
        assert call_kwargs["page"] == 3  # noqa: PLR2004
        assert call_kwargs["per_page"] == 25  # noqa: PLR2004

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_literal_list_values(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list command with literal values in list parameters."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.merge_request.list_merge_requests.return_value = ([], {"status_code": 200, "etag": None})

        list_command(
            ctx=mock_context,
            approved_by_ids=["None"],
            approved_by_usernames=["Any"],
            approver_ids=["None"],
            reviewer_id="None",
            reviewer_username="Any",
            my_reaction_emoji="None",
        )

        call_kwargs = mock_client.merge_request.list_merge_requests.call_args[1]
        assert call_kwargs["approved_by_ids"] == "None"
        assert call_kwargs["approved_by_usernames"] == "Any"
        assert call_kwargs["approver_ids"] == "None"
        assert call_kwargs["reviewer_id"] == "None"
        assert call_kwargs["reviewer_username"] == "Any"
        assert call_kwargs["my_reaction_emoji"] == "None"

    def test_list_command_help_via_cli(self, runner: CliRunner) -> None:
        """Test that the list command help works via CLI."""
        result = runner.invoke(app, ["merge-request", "list", "--help"])
        assert result.exit_code == 0
        output = self._strip_ansi(result.output)
        assert "--project-id" in output
        assert "--group-id" in output
        assert "--state" in output
        assert "--assignee-id" in output
        assert "--approved" in output
        assert "--labels" in output
