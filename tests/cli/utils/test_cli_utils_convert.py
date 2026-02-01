"""Unit tests for glnova.cli.utils.convert."""

import pytest

from glnova.cli.utils.convert import str_to_int, str_to_literal_or_int


class TestStrToInt:
    """Tests for str_to_int function."""

    def test_str_to_int_none_input(self) -> None:
        """Test str_to_int with None input."""
        result = str_to_int(None)
        assert result is None

    def test_str_to_int_valid_positive_integer(self) -> None:
        """Test str_to_int with valid positive integer string."""
        result = str_to_int("123")
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_valid_negative_integer(self) -> None:
        """Test str_to_int with valid negative integer string."""
        result = str_to_int("-456")
        assert result == -456  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_zero(self) -> None:
        """Test str_to_int with zero string."""
        result = str_to_int("0")
        assert result == 0
        assert isinstance(result, int)

    def test_str_to_int_large_integer(self) -> None:
        """Test str_to_int with large integer string."""
        result = str_to_int("999999999999999999999")
        assert result == 999999999999999999999  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_invalid_integer_string(self) -> None:
        """Test str_to_int with invalid integer string."""
        result = str_to_int("abc")
        assert result == "abc"
        assert isinstance(result, str)

    def test_str_to_int_float_string(self) -> None:
        """Test str_to_int with float string."""
        result = str_to_int("123.45")
        assert result == "123.45"
        assert isinstance(result, str)

    def test_str_to_int_empty_string(self) -> None:
        """Test str_to_int with empty string."""
        result = str_to_int("")
        assert result == ""
        assert isinstance(result, str)

    def test_str_to_int_whitespace_string(self) -> None:
        """Test str_to_int with whitespace string."""
        result = str_to_int("  ")
        assert result == "  "
        assert isinstance(result, str)

    def test_str_to_int_integer_with_leading_zeros(self) -> None:
        """Test str_to_int with integer string with leading zeros."""
        result = str_to_int("007")
        assert result == 7  # noqa: PLR2004
        assert isinstance(result, int)


class TestStrToLiteralOrInt:
    """Tests for str_to_literal_or_int function."""

    def test_str_to_literal_or_int_none_input(self) -> None:
        """Test str_to_literal_or_int with None input."""
        result = str_to_literal_or_int(None, ("None", "Any"))
        assert result is None

    def test_str_to_literal_or_int_valid_integer(self) -> None:
        """Test str_to_literal_or_int with valid integer string."""
        result = str_to_literal_or_int("123", ("None", "Any"))
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_valid_negative_integer(self) -> None:
        """Test str_to_literal_or_int with valid negative integer string."""
        result = str_to_literal_or_int("-456", ("None", "Any"))
        assert result == -456  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_valid_literal(self) -> None:
        """Test str_to_literal_or_int with valid literal string."""
        result = str_to_literal_or_int("None", ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_another_valid_literal(self) -> None:
        """Test str_to_literal_or_int with another valid literal string."""
        result = str_to_literal_or_int("Any", ("None", "Any"))
        assert result == "Any"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_invalid_string(self) -> None:
        """Test str_to_literal_or_int with invalid string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int("invalid", ("None", "Any"))

    def test_str_to_literal_or_int_empty_string(self) -> None:
        """Test str_to_literal_or_int with empty string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int("", ("None", "Any"))

    def test_str_to_literal_or_int_float_string(self) -> None:
        """Test str_to_literal_or_int with float string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int("123.45", ("None", "Any"))

    def test_str_to_literal_or_int_case_sensitive_literal(self) -> None:
        """Test str_to_literal_or_int with case-sensitive literal."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int("none", ("None", "Any"))

    def test_str_to_literal_or_int_empty_literal_tuple(self) -> None:
        """Test str_to_literal_or_int with empty literal tuple."""
        result = str_to_literal_or_int("123", ())
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_invalid_with_empty_tuple(self) -> None:
        """Test str_to_literal_or_int with invalid string and empty literal tuple."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int("abc", ())

    def test_str_to_literal_or_int_zero_as_integer(self) -> None:
        """Test str_to_literal_or_int with zero as integer."""
        result = str_to_literal_or_int("0", ("None", "Any"))
        assert result == 0
        assert isinstance(result, int)

    def test_str_to_literal_or_int_large_integer(self) -> None:
        """Test str_to_literal_or_int with large integer."""
        result = str_to_literal_or_int("999999999999999999999", ("None", "Any"))
        assert result == 999999999999999999999  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_multiple_literals(self) -> None:
        """Test str_to_literal_or_int with multiple literals."""
        literals = ("None", "Any", "All", "Unassigned")
        result = str_to_literal_or_int("All", literals)
        assert result == "All"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_whitespace_literal(self) -> None:
        """Test str_to_literal_or_int with whitespace in literal."""
        literals = ("None", "Any ", " All")
        result = str_to_literal_or_int("Any ", literals)
        assert result == "Any "
        assert isinstance(result, str)

    def test_str_to_literal_or_int_integer_with_leading_zeros(self) -> None:
        """Test str_to_literal_or_int with integer string with leading zeros."""
        result = str_to_literal_or_int("007", ("None", "Any"))
        assert result == 7  # noqa: PLR2004
        assert isinstance(result, int)


class TestStrToLiteralOrIntEdgeCases:
    """Edge case tests for str_to_literal_or_int function."""

    def test_str_to_literal_or_int_mixed_case_literals(self) -> None:
        """Test str_to_literal_or_int with mixed case literals."""
        literals = ("none", "NONE", "None")
        result = str_to_literal_or_int("none", literals)
        assert result == "none"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_special_characters(self) -> None:
        """Test str_to_literal_or_int with special characters in literals."""
        literals = ("@none", "#any", "$all")
        result = str_to_literal_or_int("@none", literals)
        assert result == "@none"
        assert isinstance(result, str)
