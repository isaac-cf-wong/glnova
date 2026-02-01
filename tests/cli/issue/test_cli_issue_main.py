"""Unit tests for glnova.cli.issue.main."""

from glnova.cli.issue.main import issue_app


class TestIssueAppConfiguration:
    """Tests for issue_app configuration."""

    def test_issue_app_has_correct_name(self) -> None:
        """Test that the issue app has the correct name."""
        assert issue_app.info.name == "issue"

    def test_issue_app_has_help(self) -> None:
        """Test that the issue app has help text."""
        assert "Manage GitLab issues" in issue_app.info.help
