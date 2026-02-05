"""Tests for glnova.cli.user.modify."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest
import typer

from glnova.cli.user.modify import modify_command


class TestModifyCommand:
    """Tests for user modify command."""

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
    def test_modify_command_basic_success(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock, capsys
    ) -> None:
        """Test basic success case for modify_command."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.user.modify_user.return_value = ({"id": 123, "name": "Alice"}, {"status_code": 200, "etag": None})

        modify_command(ctx=mock_context, account_id=123, name="Alice", admin=True)

        mock_get_auth.assert_called_once_with(
            config_path="/path/to/config", account_name=None, token=None, base_url=None
        )
        mock_gitlab.assert_called_once_with(token="test_token", base_url="https://gitlab.example.com")

        call_kwargs = mock_client.user.modify_user.call_args[1]
        assert call_kwargs["account_id"] == 123  # noqa: PLR2004
        assert call_kwargs["name"] == "Alice"
        assert call_kwargs["admin"] is True

        captured = capsys.readouterr()
        output_data = json.loads(captured.out.strip())
        assert output_data["data"] == {"id": 123, "name": "Alice"}
        assert output_data["metadata"]["status_code"] == 200  # noqa: PLR2004

    @patch("glnova.cli.utils.auth.get_auth_params")
    @patch("glnova.client.gitlab.GitLab")
    def test_modify_command_handles_exception(
        self, mock_gitlab: MagicMock, mock_get_auth: MagicMock, mock_context: MagicMock
    ) -> None:
        """Test that modify_command handles exceptions properly."""
        mock_get_auth.return_value = ("test_token", "https://gitlab.example.com")
        mock_client = MagicMock()
        mock_gitlab.return_value.__enter__.return_value = mock_client
        mock_client.user.modify_user.side_effect = Exception("API Error")

        with pytest.raises(typer.Exit) as exc_info:
            modify_command(ctx=mock_context, account_id=123)

        assert exc_info.value.exit_code == 1
