"""Simplified unit tests for glnova.cli.issue.list."""

from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.issue.list import list_command


class TestListCommandBasic:
    """Basic tests for list_command."""

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_succeeds(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command executes successfully."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx)

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_with_error(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command handles errors."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.side_effect = Exception("API Error")

        with pytest.raises(typer.Exit) as exc_info:
            list_command(ctx)

        assert exc_info.value.exit_code == 1

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("logging.getLogger") as mock_get_logger,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_logger = MagicMock()
            mock_get_logger.return_value = mock_logger
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            error = Exception("API Error")
            mock_client.issue.list_issues.side_effect = error

            with pytest.raises(typer.Exit):
                list_command(ctx)

            mock_logger.error.assert_called_once_with("Error listing issues: %s", error)


class TestListCommandSearchInValidation:
    """Tests for list_command search_in parameter validation."""

    def test_list_command_valid_search_in(self) -> None:
        """Test list_command with valid search_in values."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.list_issues.return_value = ([], 200, None)

            list_command(ctx, search_in=["title", "description"])

    def test_list_command_invalid_search_in(self) -> None:
        """Test list_command with invalid search_in values."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        with (
            patch("glnova.cli.utils.auth.get_auth_params") as mock_auth,
            patch("glnova.client.gitlab.GitLab") as mock_gitlab,
        ):

            mock_auth.return_value = ("token", "https://gitlab.com")
            mock_client = MagicMock()
            mock_gitlab.return_value.__enter__.return_value = mock_client
            mock_client.issue.list_issues.return_value = ([], 200, None)

            with pytest.raises(typer.Exit) as exc_info:
                list_command(ctx, search_in=["invalid"])

            assert exc_info.value.exit_code == 1


class TestListCommandParameterConversions:
    """Tests for list_command parameter type conversions."""

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_assignee_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts assignee_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, assignee_id="None")

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_epic_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts epic_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, epic_id="Any")

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_iteration_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts iteration_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, iteration_id="None")

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_weight(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts weight parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.issue.list_issues.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, weight="Any")
