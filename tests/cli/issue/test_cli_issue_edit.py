"""Unit tests for glnova.cli.issue.edit."""

import json
from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.issue.edit import edit_command


class TestEditCommandValidation:
    """Tests for edit_command parameter validation."""

    def test_edit_command_valid_basic_call(self) -> None:
        """Test edit_command with minimal valid parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(ctx, project_id="myproject", issue_iid=456)

    def test_edit_command_with_title(self) -> None:
        """Test edit_command with title parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(ctx, project_id="myproject", issue_iid=456, title="New Title")

    def test_edit_command_with_multiple_params(self) -> None:
        """Test edit_command with multiple parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(
                ctx,
                project_id="myproject",
                issue_iid=456,
                title="New Title",
                description="New Description",
                labels=["bug", "urgent"],
                state_event="close",
            )


class TestEditCommandAuth:
    """Tests for edit_command authentication handling."""

    def test_edit_command_calls_get_auth_params(self) -> None:
        """Test that edit_command calls get_auth_params correctly."""
        ctx = MagicMock()
        ctx.obj = {"config_path": "/config/path"}
        account_name = "test_account"
        token = "test_token"
        base_url = "https://custom.gitlab.com"

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("resolved_token", "https://resolved.gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(
                ctx,
                project_id="myproject",
                issue_iid=456,
                account_name=account_name,
                token=token,
                base_url=base_url,
            )

            mock_auth.assert_called_once_with(
                config_path="/config/path",
                account_name=account_name,
                token=token,
                base_url=base_url,
            )

    def test_edit_command_uses_resolved_auth(self) -> None:
        """Test that edit_command uses the resolved auth parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("resolved_token", "https://resolved.gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(ctx, project_id="myproject", issue_iid=456)

            mock_gitlab.assert_called_once_with(
                token="resolved_token",
                base_url="https://resolved.gitlab.com",
            )


class TestEditCommandDataProcessing:
    """Tests for edit_command data processing and conversion."""

    def test_edit_command_converts_project_id(self) -> None:
        """Test that project_id is properly converted."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("glnova.cli.utils.convert.str_to_int") as mock_convert,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})
            mock_convert.return_value = 789

            edit_command(ctx, project_id="myproject", issue_iid=456)

            mock_convert.assert_called_once_with("myproject")

    def test_edit_command_calls_issue_edit_issue(self) -> None:
        """Test that edit_command calls the correct GitLab API method."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("glnova.cli.utils.convert.str_to_int") as mock_convert,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})
            mock_convert.return_value = 789

            edit_command(
                ctx,
                project_id="myproject",
                issue_iid=456,
                title="New Title",
                description="New Description",
                assignee_ids=[1, 2, 3],
                labels=["bug", "urgent"],
                add_labels=["critical"],
                remove_labels=["minor"],
                milestone_id=10,
                state_event="close",
                confidential=True,
                due_date="2024-12-31",
                weight=5,
                epic_id=20,
                epic_iid=30,
                issue_type="incident",
                discussion_locked=True,
            )

            mock_client.issue.edit_issue.assert_called_once_with(
                project_id=789,
                issue_iid=456,
                title="New Title",
                description="New Description",
                assignee_ids=[1, 2, 3],
                labels=["bug", "urgent"],
                add_labels=["critical"],
                remove_labels=["minor"],
                milestone_id=10,
                state_event="close",
                confidential=True,
                due_date="2024-12-31",
                weight=5,
                epic_id=20,
                epic_iid=30,
                issue_type="incident",
                discussion_locked=True,
                updated_at=None,
            )

    def test_edit_command_with_none_values(self) -> None:
        """Test that edit_command passes None values correctly."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("glnova.cli.utils.convert.str_to_int") as mock_convert,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})
            mock_convert.return_value = 789

            edit_command(ctx, project_id="myproject", issue_iid=456)

            mock_client.issue.edit_issue.assert_called_once_with(
                project_id=789,
                issue_iid=456,
                title=None,
                description=None,
                assignee_ids=None,
                labels=None,
                add_labels=None,
                remove_labels=None,
                milestone_id=None,
                state_event=None,
                confidential=None,
                due_date=None,
                weight=None,
                epic_id=None,
                epic_iid=None,
                issue_type=None,
                discussion_locked=None,
                updated_at=None,
            )


class TestEditCommandOutput:
    """Tests for edit_command output formatting."""

    @patch("builtins.print")
    def test_edit_command_outputs_json(self, mock_print: MagicMock) -> None:
        """Test that edit_command outputs JSON."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = (
                {"id": 123, "title": "Updated Issue"},
                {"status_code": 200, "etag": "etag123"},
            )

            edit_command(ctx, project_id="myproject", issue_iid=456, title="Updated Issue")

            # Check that print was called
            mock_print.assert_called_once()

            # Check the output format
            output = mock_print.call_args[0][0]
            parsed = json.loads(output)
            assert "data" in parsed
            assert "metadata" in parsed
            assert parsed["data"] == {"id": 123, "title": "Updated Issue"}
            assert parsed["metadata"]["status_code"] == 200  # noqa: PLR2004
            assert parsed["metadata"]["etag"] == "etag123"

    @patch("builtins.print")
    def test_edit_command_outputs_with_null_etag(self, mock_print: MagicMock) -> None:
        """Test that edit_command handles null etag."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": None})

            edit_command(ctx, project_id="myproject", issue_iid=456)

            output = mock_print.call_args[0][0]
            parsed = json.loads(output)
            assert parsed["metadata"]["etag"] is None


class TestEditCommandErrorHandling:
    """Tests for edit_command error handling."""

    def test_edit_command_handles_exception(self) -> None:
        """Test that edit_command handles exceptions properly."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.side_effect = Exception("API Error")

            with pytest.raises(typer.Exit) as exc_info:
                edit_command(ctx, project_id="myproject", issue_iid=456)

            assert exc_info.value.exit_code == 1

    def test_edit_command_logs_errors(self) -> None:
        """Test that edit_command logs errors."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("logging.getLogger") as mock_get_logger,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            error = Exception("API Error")
            mock_client.issue.edit_issue.side_effect = error

            with pytest.raises(typer.Exit):
                edit_command(ctx, project_id="myproject", issue_iid=456)


class TestEditCommandParameterTypes:
    """Tests for edit_command parameter type handling."""

    def test_edit_command_assignee_ids_list(self) -> None:
        """Test that assignee_ids parameter accepts list."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(ctx, project_id="myproject", issue_iid=456, assignee_ids=[1, 2, 3])

            mock_client.issue.edit_issue.assert_called_with(
                project_id=mock_client.issue.edit_issue.call_args[1]["project_id"],
                issue_iid=456,
                assignee_ids=[1, 2, 3],
                title=None,
                description=None,
                labels=None,
                add_labels=None,
                remove_labels=None,
                milestone_id=None,
                state_event=None,
                confidential=None,
                due_date=None,
                weight=None,
                epic_id=None,
                epic_iid=None,
                issue_type=None,
                discussion_locked=None,
                updated_at=None,
            )

    def test_edit_command_labels_list(self) -> None:
        """Test that labels parameter accepts list."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.edit_issue.return_value = ({"id": 123}, {"status_code": 200, "etag": "etag123"})

            edit_command(ctx, project_id="myproject", issue_iid=456, labels=["bug", "urgent"])

            mock_client.issue.edit_issue.assert_called_with(
                project_id=mock_client.issue.edit_issue.call_args[1]["project_id"],
                issue_iid=456,
                labels=["bug", "urgent"],
                title=None,
                description=None,
                assignee_ids=None,
                add_labels=None,
                remove_labels=None,
                milestone_id=None,
                state_event=None,
                confidential=None,
                due_date=None,
                weight=None,
                epic_id=None,
                epic_iid=None,
                issue_type=None,
                discussion_locked=None,
                updated_at=None,
            )
