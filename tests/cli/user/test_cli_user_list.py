"""Tests for glnova.cli.user.list."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.user.list import list_command


class TestListCommand:
    """Tests for user list command."""

    @pytest.fixture
    def mock_config_path(self) -> str:
        """Fixture for mock config path."""
        return "/path/to/config"

    @pytest.fixture
    def mock_context(self, mock_config_path: str) -> MagicMock:
        """Fixture for mock typer context."""
        ctx = MagicMock()
        ctx.obj = {"config_path": mock_config_path}
        return ctx

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_basic_success(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock, capsys
    ) -> None:
        """Test basic success case for list_command."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.user.list_users.return_value = (
            [{"id": 1, "username": "alice"}],
            {"status_code": 200, "etag": "etag123"},
        )

        list_command(ctx=mock_context, username="alice", page=2)

        mock_get_auth.assert_called_once_with(
            config_path="/path/to/config", account_name=None, token=None, base_url=None
        )
        mock_gitlab.assert_called_once_with(token="test_token", base_url="https://gitlab.example.com")

        call_kwargs = mock_client.user.list_users.call_args[1]
        assert call_kwargs["username"] == "alice"
        assert call_kwargs["page"] == 2  # noqa: PLR2004

        captured = capsys.readouterr()
        output_data = json.loads(captured.out.strip())
        assert output_data["data"] == [{"id": 1, "username": "alice"}]
        assert output_data["metadata"]["status_code"] == 200  # noqa: PLR2004
        assert output_data["metadata"]["etag"] == "etag123"

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_list_command_with_auth_parameters(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test list_command with explicit auth parameters."""
        mock_get_auth.return_value = ("custom_token", "https://custom.gitlab.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.user.list_users.return_value = ([], {"status_code": 200, "etag": None})

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
    def test_list_command_handles_exception(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test that list_command handles exceptions properly."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.user.list_users.side_effect = Exception("API Error")

        with pytest.raises(typer.Exit) as exc_info:
            list_command(ctx=mock_context)

        assert exc_info.value.exit_code == 1
