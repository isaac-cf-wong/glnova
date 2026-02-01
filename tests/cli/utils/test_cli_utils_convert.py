"""Unit tests for glnova.cli.utils.convert."""

import pytest

from glnova.cli.utils.convert import str_to_int_or_none, str_to_literal_or_int_or_none


class TestStrToIntOrNone:
    """Tests for str_to_int_or_none function."""

    def test_str_to_int_or_none_none_input(self) -> None:
        """Test str_to_int_or_none with None input."""
        result = str_to_int_or_none(None)
        assert result is None

    def test_str_to_int_or_none_valid_positive_integer(self) -> None:
        """Test str_to_int_or_none with valid positive integer string."""
        result = str_to_int_or_none("123")
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_or_none_valid_negative_integer(self) -> None:
        """Test str_to_int_or_none with valid negative integer string."""
        result = str_to_int_or_none("-456")
        assert result == -456  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_or_none_zero(self) -> None:
        """Test str_to_int_or_none with zero string."""
        result = str_to_int_or_none("0")
        assert result == 0
        assert isinstance(result, int)

    def test_str_to_int_or_none_large_integer(self) -> None:
        """Test str_to_int_or_none with large integer string."""
        result = str_to_int_or_none("999999999999999999999")
        assert result == 999999999999999999999  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_int_or_none_invalid_integer_string(self) -> None:
        """Test str_to_int_or_none with invalid integer string."""
        result = str_to_int_or_none("abc")
        assert result == "abc"
        assert isinstance(result, str)

    def test_str_to_int_or_none_float_string(self) -> None:
        """Test str_to_int_or_none with float string."""
        result = str_to_int_or_none("123.45")
        assert result == "123.45"
        assert isinstance(result, str)

    def test_str_to_int_or_none_empty_string(self) -> None:
        """Test str_to_int_or_none with empty string."""
        result = str_to_int_or_none("")
        assert result == ""
        assert isinstance(result, str)

    def test_str_to_int_or_none_whitespace_string(self) -> None:
        """Test str_to_int_or_none with whitespace string."""
        result = str_to_int_or_none("  ")
        assert result == "  "
        assert isinstance(result, str)

    def test_str_to_int_or_none_integer_with_leading_zeros(self) -> None:
        """Test str_to_int_or_none with integer string with leading zeros."""
        result = str_to_int_or_none("007")
        assert result == 7  # noqa: PLR2004
        assert isinstance(result, int)


class TestStrToLiteralOrIntOrNone:
    """Tests for str_to_literal_or_int_or_none function."""

    def test_str_to_literal_or_int_or_none_none_input(self) -> None:
        """Test str_to_literal_or_int_or_none with None input."""
        result = str_to_literal_or_int_or_none(None, ("None", "Any"))
        assert result is None

    def test_str_to_literal_or_int_or_none_valid_integer(self) -> None:
        """Test str_to_literal_or_int_or_none with valid integer string."""
        result = str_to_literal_or_int_or_none("123", ("None", "Any"))
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_or_none_valid_negative_integer(self) -> None:
        """Test str_to_literal_or_int_or_none with valid negative integer string."""
        result = str_to_literal_or_int_or_none("-456", ("None", "Any"))
        assert result == -456  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_or_none_valid_literal(self) -> None:
        """Test str_to_literal_or_int_or_none with valid literal string."""
        result = str_to_literal_or_int_or_none("None", ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_or_none_another_valid_literal(self) -> None:
        """Test str_to_literal_or_int_or_none with another valid literal string."""
        result = str_to_literal_or_int_or_none("Any", ("None", "Any"))
        assert result == "Any"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_or_none_invalid_string(self) -> None:
        """Test str_to_literal_or_int_or_none with invalid string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int_or_none("invalid", ("None", "Any"))

    def test_str_to_literal_or_int_or_none_empty_string(self) -> None:
        """Test str_to_literal_or_int_or_none with empty string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int_or_none("", ("None", "Any"))

    def test_str_to_literal_or_int_or_none_float_string(self) -> None:
        """Test str_to_literal_or_int_or_none with float string."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int_or_none("123.45", ("None", "Any"))

    def test_str_to_literal_or_int_or_none_case_sensitive_literal(self) -> None:
        """Test str_to_literal_or_int_or_none with case-sensitive literal."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int_or_none("none", ("None", "Any"))

    def test_str_to_literal_or_int_or_none_empty_literal_tuple(self) -> None:
        """Test str_to_literal_or_int_or_none with empty literal tuple."""
        result = str_to_literal_or_int_or_none("123", ())
        assert result == 123  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_or_none_invalid_with_empty_tuple(self) -> None:
        """Test str_to_literal_or_int_or_none with invalid string and empty literal tuple."""
        with pytest.raises(ValueError, match="Value must be an integer or one of the literals"):
            str_to_literal_or_int_or_none("abc", ())

    def test_str_to_literal_or_int_or_none_zero_as_integer(self) -> None:
        """Test str_to_literal_or_int_or_none with zero as integer."""
        result = str_to_literal_or_int_or_none("0", ("None", "Any"))
        assert result == 0
        assert isinstance(result, int)

    def test_str_to_literal_or_int_or_none_large_integer(self) -> None:
        """Test str_to_literal_or_int_or_none with large integer."""
        result = str_to_literal_or_int_or_none("999999999999999999999", ("None", "Any"))
        assert result == 999999999999999999999  # noqa: PLR2004
        assert isinstance(result, int)

    def test_str_to_literal_or_int_or_none_multiple_literals(self) -> None:
        """Test str_to_literal_or_int_or_none with multiple literals."""
        literals = ("None", "Any", "All", "Unassigned")
        result = str_to_literal_or_int_or_none("All", literals)
        assert result == "All"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_or_none_whitespace_literal(self) -> None:
        """Test str_to_literal_or_int_or_none with whitespace in literal."""
        literals = ("None", "Any ", " All")
        result = str_to_literal_or_int_or_none("Any ", literals)
        assert result == "Any "
        assert isinstance(result, str)

    def test_str_to_literal_or_int_or_none_integer_with_leading_zeros(self) -> None:
        """Test str_to_literal_or_int_or_none with integer string with leading zeros."""
        result = str_to_literal_or_int_or_none("007", ("None", "Any"))
        assert result == 7  # noqa: PLR2004
        assert isinstance(result, int)


class TestStrToLiteralOrIntOrNoneEdgeCases:
    """Edge case tests for str_to_literal_or_int_or_none function."""

    def test_str_to_literal_or_int_or_none_mixed_case_literals(self) -> None:
        """Test str_to_literal_or_int_or_none with mixed case literals."""
        literals = ("none", "NONE", "None")
        result = str_to_literal_or_int_or_none("none", literals)
        assert result == "none"
        assert isinstance(result, str)

    def test_str_to_literal_or_int_or_none_special_characters(self) -> None:
        """Test str_to_literal_or_int_or_none with special characters in literals."""
        literals = ("@none", "#any", "$all")
        result = str_to_literal_or_int_or_none("@none", literals)
        assert result == "@none"
        assert isinstance(result, str)
