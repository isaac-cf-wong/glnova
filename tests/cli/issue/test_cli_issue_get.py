"""Unit tests for glnova.cli.issue.get."""

import json
from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.issue.get import get_command


class TestGetCommandValidation:
    """Tests for get_command parameter validation."""

    def test_get_command_with_issue_id(self) -> None:
        """Test get_command with issue_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")

            get_command(ctx, issue_id=123)

    def test_get_command_with_project_and_iid(self) -> None:
        """Test get_command with project_id and issue_iid parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")

            get_command(ctx, project_id="myproject", issue_iid=456)

    def test_get_command_missing_required_params(self) -> None:
        """Test get_command with missing required parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with pytest.raises(typer.Exit) as exc_info:
            get_command(ctx)

        assert exc_info.value.exit_code == 1

    def test_get_command_only_project_id(self) -> None:
        """Test get_command with only project_id (missing issue_iid)."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with pytest.raises(typer.Exit) as exc_info:
            get_command(ctx, project_id="myproject")

        assert exc_info.value.exit_code == 1

    def test_get_command_only_issue_iid(self) -> None:
        """Test get_command with only issue_iid (missing project_id)."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with pytest.raises(typer.Exit) as exc_info:
            get_command(ctx, issue_iid=456)

        assert exc_info.value.exit_code == 1

    def test_get_command_conflicting_params(self) -> None:
        """Test get_command with conflicting parameters (both issue_id and project_id)."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with pytest.raises(typer.Exit) as exc_info:
            get_command(ctx, issue_id=123, project_id="myproject")

        assert exc_info.value.exit_code == 1

    def test_get_command_conflicting_params_issue_iid(self) -> None:
        """Test get_command with conflicting parameters (issue_id and issue_iid)."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with pytest.raises(typer.Exit) as exc_info:
            get_command(ctx, issue_id=123, issue_iid=456)

        assert exc_info.value.exit_code == 1


class TestGetCommandAuth:
    """Tests for get_command authentication handling."""

    def test_get_command_calls_get_auth_params(self) -> None:
        """Test that get_command calls get_auth_params correctly."""
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
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")

            get_command(ctx, issue_id=123, account_name=account_name, token=token, base_url=base_url)

            mock_auth.assert_called_once_with(
                config_path="/config/path",
                account_name=account_name,
                token=token,
                base_url=base_url,
            )

    def test_get_command_uses_resolved_auth(self) -> None:
        """Test that get_command uses the resolved auth parameters."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("resolved_token", "https://resolved.gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")

            get_command(ctx, issue_id=123)

            mock_gitlab.assert_called_once_with(
                token="resolved_token",
                base_url="https://resolved.gitlab.com",
            )


class TestGetCommandDataProcessing:
    """Tests for get_command data processing and conversion."""

    def test_get_command_converts_project_id(self) -> None:
        """Test that project_id is properly converted."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("glnova.cli.utils.convert.str_to_int_or_none") as mock_convert,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")
            mock_convert.return_value = 456

            get_command(ctx, project_id="myproject", issue_iid=789)

            mock_convert.assert_called_once_with("myproject")

    def test_get_command_calls_issue_get_issue(self) -> None:
        """Test that get_command calls the correct GitLab API method."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")

            get_command(ctx, issue_id=123, etag="etag456")

            mock_client.issue.get_issue.assert_called_once_with(
                issue_id=123,
                project_id=None,
                issue_iid=None,
                etag="etag456",
            )

    def test_get_command_calls_issue_get_issue_with_project(self) -> None:
        """Test that get_command calls the correct GitLab API method with project."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
            patch("glnova.cli.utils.convert.str_to_int_or_none") as mock_convert,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, "etag123")
            mock_convert.return_value = 456

            get_command(ctx, project_id="myproject", issue_iid=789)

            mock_client.issue.get_issue.assert_called_once_with(
                issue_id=None,
                project_id=456,
                issue_iid=789,
                etag=None,
            )


class TestGetCommandOutput:
    """Tests for get_command output formatting."""

    @patch("builtins.print")
    def test_get_command_outputs_json(self, mock_print: MagicMock) -> None:
        """Test that get_command outputs JSON."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123, "title": "Test Issue"}, 200, "etag123")

            get_command(ctx, issue_id=123)

            # Check that print was called
            mock_print.assert_called_once()

            # Check the output format
            output = mock_print.call_args[0][0]
            parsed = json.loads(output)
            assert "data" in parsed
            assert "metadata" in parsed
            assert parsed["data"] == {"id": 123, "title": "Test Issue"}
            assert parsed["metadata"]["status_code"] == 200  # noqa: PLR2004
            assert parsed["metadata"]["etag"] == "etag123"

    @patch("builtins.print")
    def test_get_command_outputs_with_null_etag(self, mock_print: MagicMock) -> None:
        """Test that get_command handles null etag."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.return_value = ({"id": 123}, 200, None)

            get_command(ctx, issue_id=123)

            output = mock_print.call_args[0][0]
            parsed = json.loads(output)
            assert parsed["metadata"]["etag"] is None


class TestGetCommandErrorHandling:
    """Tests for get_command error handling."""

    def test_get_command_handles_exception(self) -> None:
        """Test that get_command handles exceptions properly."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.get_issue.side_effect = Exception("API Error")

            with pytest.raises(typer.Exit) as exc_info:
                get_command(ctx, issue_id=123)

            assert exc_info.value.exit_code == 1

    def test_get_command_logs_errors(self) -> None:
        """Test that get_command logs errors."""
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
            mock_client.issue.get_issue.side_effect = error

            with pytest.raises(typer.Exit):
                get_command(ctx, issue_id=123)

            mock_logger.error.assert_called_once_with("Error getting issue: %s", error)
