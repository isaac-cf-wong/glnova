"""Unit tests for glnova.config.manager."""

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from glnova.config.manager import ConfigManager
from glnova.config.model import AccountConfig, Config


class TestConfigManagerInit:
    """Tests for ConfigManager initialization."""

    def test_config_manager_init_with_default_path(self) -> None:
        """Test ConfigManager initialization with default path."""
        with patch("platformdirs.user_config_dir", return_value="/tmp/glnova"):
            manager = ConfigManager()
            assert manager.config_path == Path("/tmp/glnova/config.yaml")

    def test_config_manager_init_with_custom_path_string(self) -> None:
        """Test ConfigManager initialization with custom path as string."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "custom_config.yaml"
            manager = ConfigManager(filename=str(config_file))
            assert manager.config_path == config_file

    def test_config_manager_init_with_custom_path_pathlib(self) -> None:
        """Test ConfigManager initialization with custom path as Path."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "custom_config.yaml"
            manager = ConfigManager(filename=config_file)
            assert manager.config_path == config_file

    def test_config_manager_creates_parent_directory(self) -> None:
        """Test that ConfigManager creates parent directory if it doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "nested" / "dir" / "config.yaml"
            manager = ConfigManager(filename=config_file)
            assert manager.config_path.parent.exists()


class TestConfigManagerConfigProperty:
    """Tests for ConfigManager config property."""

    def test_config_property_returns_empty_config_by_default(self) -> None:
        """Test that config property returns empty Config by default."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            config = manager.config
            assert isinstance(config, Config)
            assert config.accounts == {}
            assert config.default_account is None

    def test_config_property_caches_config(self) -> None:
        """Test that config property caches the configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            config1 = manager.config
            config2 = manager.config
            assert config1 is config2

    def test_config_setter(self) -> None:
        """Test setting the config property."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            new_config = Config()
            manager.config = new_config
            assert manager.config is new_config


class TestConfigManagerGetConfig:
    """Tests for ConfigManager get_config method."""

    def test_get_config_with_existing_account(self) -> None:
        """Test getting an existing account configuration."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            account = AccountConfig(name="test_account", token="test_token")
            manager.config.accounts["test_account"] = account
            manager.config.default_account = "test_account"

            retrieved = manager.get_config("test_account")
            assert retrieved.name == "test_account"
            assert retrieved.token == "test_token"

    def test_get_config_with_none_uses_default(self) -> None:
        """Test that get_config with None uses default account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            account = AccountConfig(name="default_account", token="default_token")
            manager.config.accounts["default_account"] = account
            manager.config.default_account = "default_account"

            retrieved = manager.get_config(None)
            assert retrieved.name == "default_account"

    def test_get_config_with_nonexistent_account_raises_error(self) -> None:
        """Test that getting nonexistent account raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            with pytest.raises(ValueError, match="Account 'nonexistent' does not exist"):
                manager.get_config("nonexistent")

    def test_get_config_loads_config_if_not_loaded(self) -> None:
        """Test that get_config loads config if not already loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            account = AccountConfig(name="test_account", token="test_token")
            manager.config.accounts["test_account"] = account
            manager.config.default_account = "test_account"
            manager.save_config()

            # Create new manager and clear cache
            manager2 = ConfigManager(filename=config_file)
            retrieved = manager2.get_config("test_account")
            assert retrieved.name == "test_account"


class TestConfigManagerAddAccount:
    """Tests for ConfigManager add_account method."""

    def test_add_account_basic(self) -> None:
        """Test adding a basic account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("new_account", "new_token")
            assert "new_account" in manager.config.accounts
            assert manager.config.accounts["new_account"].token == "new_token"

    def test_add_account_with_custom_base_url(self) -> None:
        """Test adding an account with custom base_url."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account(
                "gitlab_custom",
                "token123",
                base_url="https://gitlab.example.com",
            )
            account = manager.config.accounts["gitlab_custom"]
            assert account.base_url == "https://gitlab.example.com"

    def test_add_account_first_account_becomes_default(self) -> None:
        """Test that first added account becomes default."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("first_account", "token1")
            assert manager.config.default_account == "first_account"

    def test_add_account_second_account_not_default_unless_specified(self) -> None:
        """Test that second added account is not default unless specified."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("first_account", "token1")
            manager.add_account("second_account", "token2")
            assert manager.config.default_account == "first_account"

    def test_add_account_with_is_default_true(self) -> None:
        """Test adding account with is_default=True."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("first_account", "token1")
            manager.add_account("second_account", "token2", is_default=True)
            assert manager.config.default_account == "second_account"

    def test_add_account_duplicate_name_raises_error(self) -> None:
        """Test that adding duplicate account name raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("existing_account", "token1")
            with pytest.raises(ValueError, match="Account 'existing_account' already exists"):
                manager.add_account("existing_account", "token2")

    def test_add_account_loads_config_if_not_loaded(self) -> None:
        """Test that add_account loads config if not already loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("account1", "token1")
            manager.save_config()

            manager2 = ConfigManager(filename=config_file)
            manager2.add_account("account2", "token2")
            assert "account1" in manager2.config.accounts
            assert "account2" in manager2.config.accounts


class TestConfigManagerUpdateAccount:
    """Tests for ConfigManager update_account method."""

    def test_update_account_token(self) -> None:
        """Test updating account token."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "old_token")
            manager.update_account("test_account", token="new_token")
            assert manager.config.accounts["test_account"].token == "new_token"

    def test_update_account_base_url(self) -> None:
        """Test updating account base_url."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token")
            manager.update_account(
                "test_account",
                base_url="https://new.gitlab.com",
            )
            assert manager.config.accounts["test_account"].base_url == "https://new.gitlab.com"

    def test_update_account_set_as_default(self) -> None:
        """Test updating account to be default."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("account1", "token1")
            manager.add_account("account2", "token2")
            manager.update_account("account2", is_default=True)
            assert manager.config.default_account == "account2"

    def test_update_account_remove_as_default(self) -> None:
        """Test removing account from being default."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token", is_default=True)
            manager.update_account("test_account", is_default=False)
            assert manager.config.default_account is None

    def test_update_account_nonexistent_raises_error(self) -> None:
        """Test updating nonexistent account raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            with pytest.raises(ValueError, match="Account 'nonexistent' does not exist"):
                manager.update_account("nonexistent", token="new_token")

    def test_update_account_multiple_fields(self) -> None:
        """Test updating multiple fields at once."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "old_token")
            manager.update_account(
                "test_account",
                token="new_token",
                base_url="https://gitlab.new.com",
            )
            account = manager.config.accounts["test_account"]
            assert account.token == "new_token"
            assert account.base_url == "https://gitlab.new.com"

    def test_update_account_loads_config_if_not_loaded(self) -> None:
        """Test that update_account loads config if not already loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token1")
            manager.save_config()

            manager2 = ConfigManager(filename=config_file)
            manager2.update_account("test_account", token="token2")
            assert manager2.config.accounts["test_account"].token == "token2"

    def test_update_account_warning_when_removing_non_default(self, caplog) -> None:
        """Test warning when trying to remove as default for non-default account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("account1", "token1")
            manager.add_account("account2", "token2")
            manager.update_account("account2", is_default=False)
            assert "is not the default account" in caplog.text


class TestConfigManagerDeleteAccount:
    """Tests for ConfigManager delete_account method."""

    def test_delete_account_basic(self) -> None:
        """Test deleting an account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token")
            manager.delete_account("test_account")
            assert "test_account" not in manager.config.accounts

    def test_delete_default_account_clears_default(self) -> None:
        """Test that deleting default account clears default_account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token", is_default=True)
            manager.delete_account("test_account")
            assert manager.config.default_account is None

    def test_delete_nondefault_account_keeps_default(self) -> None:
        """Test that deleting non-default account keeps default unchanged."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("default_account", "token1")
            manager.add_account("other_account", "token2")
            manager.delete_account("other_account")
            assert manager.config.default_account == "default_account"

    def test_delete_nonexistent_account_raises_error(self) -> None:
        """Test that deleting nonexistent account raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            with pytest.raises(ValueError, match="Account 'nonexistent' does not exist"):
                manager.delete_account("nonexistent")

    def test_delete_account_loads_config_if_not_loaded(self) -> None:
        """Test that delete_account loads config if not already loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token")
            manager.save_config()

            manager2 = ConfigManager(filename=config_file)
            manager2.delete_account("test_account")
            assert "test_account" not in manager2.config.accounts


class TestConfigManagerLoadConfig:
    """Tests for ConfigManager load_config method."""

    def test_load_config_from_file(self) -> None:
        """Test loading configuration from file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            # Create initial config
            manager1 = ConfigManager(filename=config_file)
            manager1.add_account("test_account", "test_token")
            manager1.save_config()

            # Load in new manager
            manager2 = ConfigManager(filename=config_file)
            manager2.load_config()
            assert "test_account" in manager2.config.accounts
            assert manager2.config.accounts["test_account"].token == "test_token"

    def test_load_config_nonexistent_file_returns_empty_config(self) -> None:
        """Test that loading nonexistent file returns empty config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "nonexistent.yaml"
            manager = ConfigManager(filename=config_file)
            manager.load_config()
            assert manager.config.accounts == {}
            assert manager.config.default_account is None

    def test_load_config_custom_filename(self) -> None:
        """Test loading config with custom filename parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file1 = Path(tmpdir) / "config1.yaml"
            config_file2 = Path(tmpdir) / "config2.yaml"

            # Create config in file1
            manager1 = ConfigManager(filename=config_file1)
            manager1.add_account("account1", "token1")
            manager1.save_config()

            # Load from file1 into manager with file2 path
            manager2 = ConfigManager(filename=config_file2)
            manager2.load_config(filename=config_file1)
            assert "account1" in manager2.config.accounts

    def test_load_config_invalid_yaml_raises_error(self) -> None:
        """Test that loading invalid YAML raises error."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            config_file.write_text("invalid: yaml: content: [", encoding="utf-8")
            manager = ConfigManager(filename=config_file)
            with pytest.raises(Exception, match="mapping values are not allowed here"):  # YAML parsing error
                manager.load_config()


class TestConfigManagerSaveConfig:
    """Tests for ConfigManager save_config method."""

    def test_save_config_to_file(self) -> None:
        """Test saving configuration to file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "test_token")
            manager.save_config()
            assert config_file.exists()

            # Verify file contents
            with config_file.open("r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            assert "accounts" in data
            assert "test_account" in data["accounts"]

    def test_save_config_custom_filename(self) -> None:
        """Test saving config with custom filename parameter."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file1 = Path(tmpdir) / "config1.yaml"
            config_file2 = Path(tmpdir) / "config2.yaml"

            manager = ConfigManager(filename=config_file1)
            manager.add_account("test_account", "test_token")
            manager.save_config(filename=config_file2)

            assert config_file2.exists()
            assert not config_file1.exists()

    def test_save_and_load_roundtrip(self) -> None:
        """Test that saving and loading preserves data."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"

            # Save
            manager1 = ConfigManager(filename=config_file)
            manager1.add_account("account1", "token1", base_url="https://gitlab.com")
            manager1.add_account("account2", "token2")
            manager1.config.default_account = "account1"
            manager1.save_config()

            # Load
            manager2 = ConfigManager(filename=config_file)
            manager2.load_config()

            # Verify
            assert len(manager2.config.accounts) == 2  # noqa: PLR2004
            assert manager2.config.accounts["account1"].token == "token1"
            assert manager2.config.accounts["account2"].token == "token2"
            assert manager2.config.default_account == "account1"


class TestConfigManagerHasDefaultAccount:
    """Tests for ConfigManager has_default_account method."""

    def test_has_default_account_true(self) -> None:
        """Test has_default_account returns True when default is set."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token", is_default=True)
            assert manager.has_default_account() is True

    def test_has_default_account_false(self) -> None:
        """Test has_default_account returns False when no default is set."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            assert manager.has_default_account() is False

    def test_has_default_account_false_after_deletion(self) -> None:
        """Test has_default_account returns False after deleting default account."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token", is_default=True)
            manager.delete_account("test_account")
            assert manager.has_default_account() is False

    def test_has_default_account_loads_config_if_not_loaded(self) -> None:
        """Test that has_default_account loads config if not already loaded."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)
            manager.add_account("test_account", "token", is_default=True)
            manager.save_config()

            manager2 = ConfigManager(filename=config_file)
            assert manager2.has_default_account() is True


class TestConfigManagerIntegration:
    """Integration tests for ConfigManager."""

    def test_full_workflow(self) -> None:
        """Test full workflow of managing accounts."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.yaml"
            manager = ConfigManager(filename=config_file)

            # Add accounts
            manager.add_account("gitlab_com", "token1", is_default=True)
            manager.add_account("gitlab_local", "token2", base_url="https://gitlab.local")

            # Verify
            assert manager.has_default_account()
            assert manager.get_config("gitlab_com").base_url == "https://gitlab.com"

            # Update account
            manager.update_account("gitlab_local", token="new_token2")
            assert manager.get_config("gitlab_local").token == "new_token2"

            # Save and reload
            manager.save_config()

            manager2 = ConfigManager(filename=config_file)
            manager2.load_config()

            # Verify after reload
            assert len(manager2.config.accounts) == 2  # noqa: PLR2004
            assert manager2.has_default_account()
            assert manager2.get_config("gitlab_local").token == "new_token2"

            # Delete and verify
            manager2.delete_account("gitlab_local")
            assert len(manager2.config.accounts) == 1
            assert manager2.config.default_account == "gitlab_com"

    def test_multiple_config_files(self) -> None:
        """Test managing multiple config files independently."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file1 = Path(tmpdir) / "config1.yaml"
            config_file2 = Path(tmpdir) / "config2.yaml"

            manager1 = ConfigManager(filename=config_file1)
            manager1.add_account("account1", "token1")
            manager1.save_config()

            manager2 = ConfigManager(filename=config_file2)
            manager2.add_account("account2", "token2")
            manager2.save_config()

            # Verify independence
            manager1_reload = ConfigManager(filename=config_file1)
            manager1_reload.load_config()
            assert "account1" in manager1_reload.config.accounts
            assert "account2" not in manager1_reload.config.accounts
