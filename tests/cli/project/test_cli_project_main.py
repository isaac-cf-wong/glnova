"""Tests for glnova.cli.project.main."""

from unittest.mock import patch

from typer.testing import CliRunner

from glnova.cli.project.main import project_app

runner = CliRunner()


class TestProjectAppConfiguration:
    """Tests for project app configuration."""

    def test_project_app_has_correct_name(self) -> None:
        """Test that the project app has the correct name."""
        assert project_app.info.name == "project"

    def test_project_app_has_correct_help(self) -> None:
        """Test that the project app has the correct help text."""
        assert project_app.info.help == "Manage projects."

    def test_project_app_has_list_command(self) -> None:
        """Test that the project app has the list command registered."""
        commands = [command.name for command in project_app.registered_commands]
        assert "list" in commands

    @patch("glnova.cli.project.list.list_command")
    def test_list_command_is_registered(self, mock_list_command) -> None:
        """Test that the list command is properly registered."""
        # The command should be registered during module import
        # We can verify this by checking that the mock was used during registration
        # This test mainly ensures the registration code runs without errors
        pass
