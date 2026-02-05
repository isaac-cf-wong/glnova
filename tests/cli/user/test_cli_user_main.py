"""Unit tests for glnova.cli.user.main."""

from glnova.cli.user.main import user_app


class TestUserAppConfiguration:
    """Tests for user_app configuration."""

    def test_user_app_has_correct_name(self) -> None:
        """Test that the user app has the correct name."""
        assert user_app.info.name == "user"

    def test_user_app_has_help(self) -> None:
        """Test that the user app has help text."""
        assert "Manage users" in user_app.info.help
