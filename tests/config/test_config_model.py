"""Unit tests for glnova.config.model."""

import pytest
from pydantic import ValidationError

from glnova.config.model import AccountConfig, Config


class TestAccountConfig:
    """Tests for AccountConfig model."""

    def test_account_config_creation_with_defaults(self) -> None:
        """Test creating an AccountConfig with default base_url."""
        account = AccountConfig(name="test_account", token="test_token")
        assert account.name == "test_account"
        assert account.token == "test_token"
        assert account.base_url == "https://gitlab.com"

    def test_account_config_creation_with_custom_base_url(self) -> None:
        """Test creating an AccountConfig with custom base_url."""
        account = AccountConfig(
            name="custom_account",
            token="custom_token",
            base_url="https://gitlab.example.com",
        )
        assert account.name == "custom_account"
        assert account.token == "custom_token"
        assert account.base_url == "https://gitlab.example.com"

    def test_account_config_strips_trailing_slash(self) -> None:
        """Test that base_url trailing slash is stripped."""
        account = AccountConfig(
            name="test_account",
            token="test_token",
            base_url="https://gitlab.com/",
        )
        assert account.base_url == "https://gitlab.com"

    def test_account_config_strips_multiple_trailing_slashes(self) -> None:
        """Test that multiple trailing slashes are stripped."""
        account = AccountConfig(
            name="test_account",
            token="test_token",
            base_url="https://gitlab.com///",
        )
        assert account.base_url == "https://gitlab.com"

    def test_account_config_base_url_http_protocol(self) -> None:
        """Test that base_url accepts http protocol."""
        account = AccountConfig(
            name="test_account",
            token="test_token",
            base_url="http://gitlab.local",
        )
        assert account.base_url == "http://gitlab.local"

    def test_account_config_invalid_base_url_no_protocol(self) -> None:
        """Test that base_url without protocol raises ValueError."""
        with pytest.raises(ValidationError) as exc_info:
            AccountConfig(
                name="test_account",
                token="test_token",
                base_url="gitlab.com",
            )
        assert "base_url must start with http:// or https://" in str(exc_info.value)

    def test_account_config_invalid_base_url_ftp_protocol(self) -> None:
        """Test that base_url with invalid protocol raises ValueError."""
        with pytest.raises(ValidationError) as exc_info:
            AccountConfig(
                name="test_account",
                token="test_token",
                base_url="ftp://gitlab.com",
            )
        assert "base_url must start with http:// or https://" in str(exc_info.value)

    def test_account_config_missing_name(self) -> None:
        """Test that missing name raises ValidationError."""
        with pytest.raises(ValidationError):
            AccountConfig(token="test_token")

    def test_account_config_missing_token(self) -> None:
        """Test that missing token raises ValidationError."""
        with pytest.raises(ValidationError):
            AccountConfig(name="test_account")

    def test_account_config_repr(self) -> None:
        """Test the string representation of AccountConfig."""
        account = AccountConfig(
            name="my_account",
            token="secret_token",
            base_url="https://gitlab.example.com",
        )
        repr_str = repr(account)
        assert "AccountConfig" in repr_str
        assert "my_account" in repr_str
        # Verify the actual base_url field instead of checking substring
        assert account.base_url == "https://gitlab.example.com"
        # Token should not be exposed in repr
        assert "secret_token" not in repr_str

    def test_account_config_equality(self) -> None:
        """Test that two AccountConfigs with same values are equal."""
        account1 = AccountConfig(
            name="test_account",
            token="test_token",
            base_url="https://gitlab.com",
        )
        account2 = AccountConfig(
            name="test_account",
            token="test_token",
            base_url="https://gitlab.com",
        )
        assert account1 == account2

    def test_account_config_inequality(self) -> None:
        """Test that two AccountConfigs with different values are not equal."""
        account1 = AccountConfig(
            name="test_account1",
            token="test_token",
            base_url="https://gitlab.com",
        )
        account2 = AccountConfig(
            name="test_account2",
            token="test_token",
            base_url="https://gitlab.com",
        )
        assert account1 != account2


class TestConfig:
    """Tests for Config model."""

    def test_config_creation_empty(self) -> None:
        """Test creating an empty Config."""
        config = Config()
        assert config.accounts == {}
        assert config.default_account is None

    def test_config_with_single_account(self) -> None:
        """Test creating a Config with a single account."""
        account = AccountConfig(name="test_account", token="test_token")
        config = Config(accounts={"test_account": account})
        assert "test_account" in config.accounts
        assert config.accounts["test_account"] == account

    def test_config_with_multiple_accounts(self) -> None:
        """Test creating a Config with multiple accounts."""
        account1 = AccountConfig(name="account1", token="token1")
        account2 = AccountConfig(name="account2", token="token2")
        config = Config(
            accounts={"account1": account1, "account2": account2},
            default_account="account1",
        )
        assert len(config.accounts) == 2  # noqa: PLR2004
        assert config.accounts["account1"] == account1
        assert config.accounts["account2"] == account2
        assert config.default_account == "account1"

    def test_config_default_account_none(self) -> None:
        """Test that default_account can be None."""
        account = AccountConfig(name="test_account", token="test_token")
        config = Config(accounts={"test_account": account}, default_account=None)
        assert config.default_account is None

    def test_config_model_dump(self) -> None:
        """Test that Config can be converted to dict."""
        account = AccountConfig(name="test_account", token="test_token")
        config = Config(accounts={"test_account": account}, default_account="test_account")
        dumped = config.model_dump()
        assert isinstance(dumped, dict)
        assert "accounts" in dumped
        assert "default_account" in dumped
        assert dumped["default_account"] == "test_account"

    def test_config_model_validate_from_dict(self) -> None:
        """Test creating Config from dict."""
        config_dict = {
            "accounts": {
                "test": {
                    "name": "test",
                    "token": "token123",
                    "base_url": "https://gitlab.com",
                }
            },
            "default_account": "test",
        }
        config = Config(**config_dict)
        assert "test" in config.accounts
        assert config.accounts["test"].name == "test"
        assert config.default_account == "test"

    def test_config_accounts_field_default_factory(self) -> None:
        """Test that accounts field uses default_factory."""
        config1 = Config()
        config2 = Config()
        assert config1.accounts is not config2.accounts


class TestAccountConfigValidation:
    """Tests for AccountConfig field validation."""

    def test_valid_https_url_variations(self) -> None:
        """Test various valid HTTPS URLs."""
        urls = [
            "https://gitlab.com",
            "https://gitlab.example.com",
            "https://gitlab.example.co.uk",
            "https://localhost:8080",
            "https://192.168.1.1",
        ]
        for url in urls:
            account = AccountConfig(
                name="test",
                token="token",
                base_url=url,
            )
            assert account.base_url == url.rstrip("/")

    def test_valid_http_url_variations(self) -> None:
        """Test various valid HTTP URLs."""
        urls = [
            "http://gitlab.local",
            "http://localhost:3000",
            "http://192.168.1.1:8080",
        ]
        for url in urls:
            account = AccountConfig(
                name="test",
                token="token",
                base_url=url,
            )
            assert account.base_url == url.rstrip("/")

    def test_invalid_url_protocols(self) -> None:
        """Test various invalid URL protocols."""
        invalid_urls = [
            "gitlab.com",
            "ftp://gitlab.com",
            "file://gitlab.com",
            "git://gitlab.com",
        ]
        for url in invalid_urls:
            with pytest.raises(ValidationError) as exc_info:
                AccountConfig(
                    name="test",
                    token="token",
                    base_url=url,
                )
            assert "base_url must start with http:// or https://" in str(exc_info.value)
