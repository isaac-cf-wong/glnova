"""Unit tests for glnova.cli.main."""

import logging
from unittest.mock import MagicMock, patch

import typer

from glnova.cli.main import LoggingLevel, main, register_commands, setup_logging


class TestLoggingLevel:
    """Tests for LoggingLevel enum."""

    def test_logging_level_values(self) -> None:
        """Test that LoggingLevel has correct values."""
        assert LoggingLevel.NOTSET == "NOTSET"
        assert LoggingLevel.DEBUG == "DEBUG"
        assert LoggingLevel.INFO == "INFO"
        assert LoggingLevel.WARNING == "WARNING"
        assert LoggingLevel.ERROR == "ERROR"
        assert LoggingLevel.CRITICAL == "CRITICAL"

    def test_logging_level_is_enum(self) -> None:
        """Test that LoggingLevel is a proper enum."""
        assert isinstance(LoggingLevel.INFO, LoggingLevel)
        assert isinstance(LoggingLevel.INFO, str)

    def test_logging_level_all_values(self) -> None:
        """Test that all expected logging levels are present."""
        expected_levels = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        actual_levels = [level.value for level in LoggingLevel]
        assert set(actual_levels) == set(expected_levels)


class TestSetupLogging:
    """Tests for setup_logging function."""

    @patch("rich.logging.RichHandler")
    @patch("rich.console.Console")
    def test_setup_logging_default_level(self, mock_console: MagicMock, mock_rich_handler: MagicMock) -> None:
        """Test setup_logging with default INFO level."""
        mock_console_instance = MagicMock()
        mock_console.return_value = mock_console_instance
        mock_handler_instance = MagicMock()
        mock_rich_handler.return_value = mock_handler_instance

        setup_logging()

        # Check that logger was configured
        logger = logging.getLogger("glnova")
        assert logger.level == logging.INFO

        # Check that RichHandler was created with correct parameters
        mock_rich_handler.assert_called_once()
        call_kwargs = mock_rich_handler.call_args[1]
        assert call_kwargs["console"] == mock_console_instance
        assert call_kwargs["rich_tracebacks"] is True
        assert call_kwargs["show_time"] is True
        assert call_kwargs["show_level"] is True
        assert call_kwargs["markup"] is True
        assert call_kwargs["level"] == "INFO"

        # Check that handler was added to logger
        assert mock_handler_instance in logger.handlers
        assert logger.propagate is False

    @patch("rich.logging.RichHandler")
    @patch("rich.console.Console")
    def test_setup_logging_custom_level(self, mock_console: MagicMock, mock_rich_handler: MagicMock) -> None:
        """Test setup_logging with custom DEBUG level."""
        mock_console_instance = MagicMock()
        mock_console.return_value = mock_console_instance
        mock_handler_instance = MagicMock()
        mock_rich_handler.return_value = mock_handler_instance

        setup_logging(LoggingLevel.DEBUG)

        logger = logging.getLogger("glnova")
        assert logger.level == logging.DEBUG

        # Check RichHandler was created with DEBUG level
        call_kwargs = mock_rich_handler.call_args[1]
        assert call_kwargs["level"] == "DEBUG"

    @patch("rich.logging.RichHandler")
    @patch("rich.console.Console")
    def test_setup_logging_removes_existing_handlers(
        self, mock_console: MagicMock, mock_rich_handler: MagicMock
    ) -> None:
        """Test that setup_logging removes existing handlers."""
        mock_console_instance = MagicMock()
        mock_console.return_value = mock_console_instance
        mock_handler_instance = MagicMock()
        mock_rich_handler.return_value = mock_handler_instance

        logger = logging.getLogger("glnova")
        existing_handler = MagicMock()
        logger.addHandler(existing_handler)

        setup_logging()

        # Check that existing handler was removed
        assert existing_handler not in logger.handlers
        # And new handler was added
        assert mock_handler_instance in logger.handlers


class TestMainCallback:
    """Tests for main callback function."""

    @patch("glnova.cli.main.setup_logging")
    @patch("os.getenv")
    def test_main_with_config_path(self, mock_getenv: MagicMock, mock_setup_logging: MagicMock) -> None:
        """Test main callback with explicit config path."""
        ctx = MagicMock(spec=typer.Context)
        config_path = "/custom/config.yaml"

        main(ctx, config_path=config_path, verbose=LoggingLevel.DEBUG)

        # Check that ctx.obj was set correctly
        assert ctx.obj == {"config_path": config_path}

        # Check that setup_logging was called with correct level
        mock_setup_logging.assert_called_once_with(LoggingLevel.DEBUG)

        # Check that os.getenv was not called
        mock_getenv.assert_not_called()

    @patch("glnova.cli.main.setup_logging")
    @patch("os.getenv")
    def test_main_with_env_var(self, mock_getenv: MagicMock, mock_setup_logging: MagicMock) -> None:
        """Test main callback using environment variable."""
        ctx = MagicMock(spec=typer.Context)
        env_config_path = "/env/config.yaml"
        mock_getenv.return_value = env_config_path

        main(ctx, config_path=None, verbose=LoggingLevel.INFO)

        # Check that ctx.obj was set to env var value
        assert ctx.obj == {"config_path": env_config_path}

        # Check that os.getenv was called with correct key
        mock_getenv.assert_called_once_with("GLNOVA_CONFIG_PATH")

        # Check that setup_logging was called with default level
        mock_setup_logging.assert_called_once_with(LoggingLevel.INFO)

    @patch("glnova.cli.main.setup_logging")
    @patch("os.getenv")
    def test_main_without_config(self, mock_getenv: MagicMock, mock_setup_logging: MagicMock) -> None:
        """Test main callback without config (env var returns None)."""
        ctx = MagicMock(spec=typer.Context)
        mock_getenv.return_value = None

        main(ctx, config_path=None, verbose=LoggingLevel.WARNING)

        # Check that ctx.obj was set to None
        assert ctx.obj == {"config_path": None}

        # Check that setup_logging was called
        mock_setup_logging.assert_called_once_with(LoggingLevel.WARNING)

    @patch("glnova.cli.main.setup_logging")
    @patch("os.getenv")
    def test_main_config_path_precedence(self, mock_getenv: MagicMock, mock_setup_logging: MagicMock) -> None:
        """Test that explicit config_path takes precedence over env var."""
        ctx = MagicMock(spec=typer.Context)
        explicit_path = "/explicit/config.yaml"
        env_path = "/env/config.yaml"
        mock_getenv.return_value = env_path

        main(ctx, config_path=explicit_path, verbose=LoggingLevel.ERROR)

        # Check that explicit path was used
        assert ctx.obj == {"config_path": explicit_path}

        # Check that os.getenv was not called
        mock_getenv.assert_not_called()


class TestRegisterCommands:
    """Tests for register_commands function."""

    @patch("glnova.cli.main.app")
    @patch("glnova.cli.issue.main.issue_app")
    def test_register_commands(self, mock_issue_app: MagicMock, mock_app: MagicMock) -> None:
        """Test that register_commands adds the issue_app to main app."""
        register_commands()

        # Check that add_typer was called with issue_app
        mock_app.add_typer.assert_called_once_with(mock_issue_app)

    @patch("glnova.cli.main.app")
    @patch("glnova.cli.issue.main.issue_app")
    def test_register_commands_imports_issue_app(self, mock_issue_app: MagicMock, mock_app: MagicMock) -> None:
        """Test that register_commands imports the issue_app module."""
        # Clear any cached imports
        import sys  # noqa: PLC0415

        modules_to_clear = [k for k in sys.modules if k.startswith("glnova.cli.issue")]
        for module in modules_to_clear:
            del sys.modules[module]

        with patch.dict("sys.modules", {"glnova.cli.issue.main": MagicMock()}):
            register_commands()

        # The import should have been attempted
        # This is tested implicitly by the fact that the function runs without ImportError


class TestMainAppConfiguration:
    """Tests for main app configuration."""

    def test_app_has_correct_name(self) -> None:
        """Test that the main app has the correct name."""
        from glnova.cli.main import app  # noqa: PLC0415

        assert app.info.name == "glnova"

    def test_app_has_help(self) -> None:
        """Test that the app has help text."""
        from glnova.cli.main import app  # noqa: PLC0415

        assert "Main CLI for glnova" in app.info.help
