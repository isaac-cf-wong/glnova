"""Simplified unit tests for glnova.cli.project.list."""

from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.project.list import list_command


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
        mock_client.project.list_projects.return_value = ([], 200, None)

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
        mock_client.project.list_projects.side_effect = Exception("API Error")

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
            mock_client.project.list_projects.side_effect = error

            with pytest.raises(typer.Exit):
                list_command(ctx)

            mock_logger.exception.assert_called_once_with("Error listing projects: %s", error)


class TestListCommandParameterConversions:
    """Tests for list_command parameter type conversions."""

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_user_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts user_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.project.list_projects.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, user_id="123")

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_group_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts group_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.project.list_projects.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, group_id="456")

    @patch("glnova.client.gitlab.GitLab")
    @patch("glnova.cli.utils.auth.get_auth_params")
    def test_list_command_converts_topic_id(self, mock_get_auth: MagicMock, mock_gitlab: MagicMock) -> None:
        """Test list_command converts topic_id parameter."""
        ctx = MagicMock()
        ctx.obj = {"config_path": None}

        mock_get_auth.return_value = ("token", "https://gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.project.list_projects.return_value = ([], 200, None)

        with patch("builtins.print"):
            list_command(ctx, topic_id=789)
