"""Tests for glnova.cli.project.main."""

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
