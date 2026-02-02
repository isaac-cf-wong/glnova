"""Tests for glnova.cli.merge_request.main."""

from __future__ import annotations

import re

import pytest
from typer.testing import CliRunner

from glnova.cli.merge_request.main import merge_request_app


class TestMergeRequestMain:
    """Tests for merge request CLI main app."""

    @staticmethod
    def _strip_ansi(text: str) -> str:
        """Remove ANSI escape codes from text."""
        return re.sub(r"\x1b\[[0-9;]*m", "", text)

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a CLI runner for testing."""
        return CliRunner()

    def test_merge_request_app_exists(self) -> None:
        """Test that the merge request app exists."""
        assert merge_request_app is not None
        assert merge_request_app.info.name == "merge-request"
        assert merge_request_app.info.help == "Manage GitLab merge requests."

    def test_merge_request_app_has_list_command(self, runner: CliRunner) -> None:
        """Test that the merge request app has a list command."""
        result = runner.invoke(merge_request_app, ["--help"])
        assert result.exit_code == 0
        output = self._strip_ansi(result.output)
        assert "list" in output
        assert "List GitLab merge requests." in output

    def test_merge_request_app_list_command_help(self, runner: CliRunner) -> None:
        """Test that the list command help works."""
        result = runner.invoke(merge_request_app, ["list", "--help"])
        assert result.exit_code == 0
        output = self._strip_ansi(result.output)
        assert "--project-id" in output
        assert "--group-id" in output
        assert "--state" in output
        assert "--assignee-id" in output
