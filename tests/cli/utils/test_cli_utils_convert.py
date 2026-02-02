"""Unit tests for glnova.cli.utils.convert."""

import pytest

from glnova.cli.utils.convert import (
    list_str_to_list_literal,
    list_str_to_list_literal_or_none,
    list_str_to_literal_or_list_int,
    list_str_to_literal_or_list_int_or_none,
    list_str_to_literal_or_list_str,
    list_str_to_literal_or_list_str_or_none,
    str_to_int,
    str_to_int_or_none,
    str_to_literal_or_int,
    str_to_literal_or_int_or_none,
)


class TestStrToInt:
    """Tests for str_to_int function."""

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


class TestListStrToLiteralOrListInt:
    """Tests for list_str_to_literal_or_list_int function."""

    def test_list_str_to_literal_or_list_int_single_integer(self) -> None:
        """Test list_str_to_literal_or_list_int with single integer string."""
        result = list_str_to_literal_or_list_int(["123"], ("None", "Any"))
        assert result == [123]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_multiple_integers(self) -> None:
        """Test list_str_to_literal_or_list_int with multiple integer strings."""
        result = list_str_to_literal_or_list_int(["123", "456", "789"], ("None", "Any"))
        assert result == [123, 456, 789]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_single_literal(self) -> None:
        """Test list_str_to_literal_or_list_int with single literal string."""
        result = list_str_to_literal_or_list_int(["None"], ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_list_str_to_literal_or_list_int_another_single_literal(self) -> None:
        """Test list_str_to_literal_or_list_int with another single literal string."""
        result = list_str_to_literal_or_list_int(["Any"], ("None", "Any"))
        assert result == "Any"
        assert isinstance(result, str)

    def test_list_str_to_literal_or_list_int_mixed_values(self) -> None:
        """Test list_str_to_literal_or_list_int with mixed integer and literal strings."""
        result = list_str_to_literal_or_list_int(["123", "456"], ("None", "Any"))
        assert result == [123, 456]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_empty_list(self) -> None:
        """Test list_str_to_literal_or_list_int with empty list."""
        result = list_str_to_literal_or_list_int([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_invalid_literal(self) -> None:
        """Test list_str_to_literal_or_list_int with invalid literal."""
        with pytest.raises(ValueError, match="invalid literal for int"):
            _result = list_str_to_literal_or_list_int(["invalid"], ("None", "Any"))

    def test_list_str_to_literal_or_list_int_negative_integers(self) -> None:
        """Test list_str_to_literal_or_list_int with negative integers."""
        result = list_str_to_literal_or_list_int(["-1", "-2", "-3"], ("None", "Any"))
        assert result == [-1, -2, -3]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_zero(self) -> None:
        """Test list_str_to_literal_or_list_int with zero."""
        result = list_str_to_literal_or_list_int(["0"], ("None", "Any"))
        assert result == [0]
        assert isinstance(result, list)


class TestListStrToLiteralOrListIntOrNone:
    """Tests for list_str_to_literal_or_list_int_or_none function."""

    def test_list_str_to_literal_or_list_int_or_none_none_input(self) -> None:
        """Test list_str_to_literal_or_list_int_or_none with None input."""
        result = list_str_to_literal_or_list_int_or_none(None, ("None", "Any"))
        assert result is None

    def test_list_str_to_literal_or_list_int_or_none_valid_list(self) -> None:
        """Test list_str_to_literal_or_list_int_or_none with valid list."""
        result = list_str_to_literal_or_list_int_or_none(["123", "456"], ("None", "Any"))
        assert result == [123, 456]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_int_or_none_single_literal(self) -> None:
        """Test list_str_to_literal_or_list_int_or_none with single literal."""
        result = list_str_to_literal_or_list_int_or_none(["None"], ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_list_str_to_literal_or_list_int_or_none_empty_list(self) -> None:
        """Test list_str_to_literal_or_list_int_or_none with empty list."""
        result = list_str_to_literal_or_list_int_or_none([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)


class TestListStrToLiteralOrListStr:
    """Tests for list_str_to_literal_or_list_str function."""

    def test_list_str_to_literal_or_list_str_single_literal(self) -> None:
        """Test list_str_to_literal_or_list_str with single literal string."""
        result = list_str_to_literal_or_list_str(["None"], ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_list_str_to_literal_or_list_str_multiple_strings(self) -> None:
        """Test list_str_to_literal_or_list_str with multiple strings."""
        result = list_str_to_literal_or_list_str(["hello", "world"], ("None", "Any"))
        assert result == ["hello", "world"]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_str_single_non_literal(self) -> None:
        """Test list_str_to_literal_or_list_str with single non-literal string."""
        result = list_str_to_literal_or_list_str(["hello"], ("None", "Any"))
        assert result == ["hello"]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_str_mixed_values(self) -> None:
        """Test list_str_to_literal_or_list_str with mixed literal and non-literal strings."""
        result = list_str_to_literal_or_list_str(["None", "hello"], ("None", "Any"))
        assert result == ["None", "hello"]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_str_empty_list(self) -> None:
        """Test list_str_to_literal_or_list_str with empty list."""
        result = list_str_to_literal_or_list_str([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_str_case_sensitive(self) -> None:
        """Test list_str_to_literal_or_list_str with case-sensitive literals."""
        result = list_str_to_literal_or_list_str(["none"], ("None", "Any"))
        assert result == ["none"]
        assert isinstance(result, list)


class TestListStrToLiteralOrListStrOrNone:
    """Tests for list_str_to_literal_or_list_str_or_none function."""

    def test_list_str_to_literal_or_list_str_or_none_none_input(self) -> None:
        """Test list_str_to_literal_or_list_str_or_none with None input."""
        result = list_str_to_literal_or_list_str_or_none(None, ("None", "Any"))
        assert result is None

    def test_list_str_to_literal_or_list_str_or_none_valid_list(self) -> None:
        """Test list_str_to_literal_or_list_str_or_none with valid list."""
        result = list_str_to_literal_or_list_str_or_none(["hello", "world"], ("None", "Any"))
        assert result == ["hello", "world"]
        assert isinstance(result, list)

    def test_list_str_to_literal_or_list_str_or_none_single_literal(self) -> None:
        """Test list_str_to_literal_or_list_str_or_none with single literal."""
        result = list_str_to_literal_or_list_str_or_none(["None"], ("None", "Any"))
        assert result == "None"
        assert isinstance(result, str)

    def test_list_str_to_literal_or_list_str_or_none_empty_list(self) -> None:
        """Test list_str_to_literal_or_list_str_or_none with empty list."""
        result = list_str_to_literal_or_list_str_or_none([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)


class TestListStrToListLiteral:
    """Tests for list_str_to_list_literal function."""

    def test_list_str_to_list_literal_valid_literals(self) -> None:
        """Test list_str_to_list_literal with valid literals."""
        result = list_str_to_list_literal(["None", "Any"], ("None", "Any"))
        assert result == ["None", "Any"]
        assert isinstance(result, list)

    def test_list_str_to_list_literal_single_literal(self) -> None:
        """Test list_str_to_list_literal with single literal."""
        result = list_str_to_list_literal(["None"], ("None", "Any"))
        assert result == ["None"]
        assert isinstance(result, list)

    def test_list_str_to_list_literal_empty_list(self) -> None:
        """Test list_str_to_list_literal with empty list."""
        result = list_str_to_list_literal([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)

    def test_list_str_to_list_literal_invalid_literal(self) -> None:
        """Test list_str_to_list_literal with invalid literal."""
        with pytest.raises(ValueError, match="All values must be one of the literals"):
            list_str_to_list_literal(["invalid"], ("None", "Any"))

    def test_list_str_to_list_literal_mixed_valid_invalid(self) -> None:
        """Test list_str_to_list_literal with mixed valid and invalid literals."""
        with pytest.raises(ValueError, match="All values must be one of the literals"):
            list_str_to_list_literal(["None", "invalid"], ("None", "Any"))

    def test_list_str_to_list_literal_case_sensitive(self) -> None:
        """Test list_str_to_list_literal with case-sensitive literals."""
        with pytest.raises(ValueError, match="All values must be one of the literals"):
            list_str_to_list_literal(["none"], ("None", "Any"))


class TestListStrToListLiteralOrNone:
    """Tests for list_str_to_list_literal_or_none function."""

    def test_list_str_to_list_literal_or_none_none_input(self) -> None:
        """Test list_str_to_list_literal_or_none with None input."""
        result = list_str_to_list_literal_or_none(None, ("None", "Any"))
        assert result is None

    def test_list_str_to_list_literal_or_none_valid_list(self) -> None:
        """Test list_str_to_list_literal_or_none with valid list."""
        result = list_str_to_list_literal_or_none(["None", "Any"], ("None", "Any"))
        assert result == ["None", "Any"]
        assert isinstance(result, list)

    def test_list_str_to_list_literal_or_none_invalid_literal(self) -> None:
        """Test list_str_to_list_literal_or_none with invalid literal."""
        with pytest.raises(ValueError, match="All values must be one of the literals"):
            list_str_to_list_literal_or_none(["invalid"], ("None", "Any"))

    def test_list_str_to_list_literal_or_none_empty_list(self) -> None:
        """Test list_str_to_list_literal_or_none with empty list."""
        result = list_str_to_list_literal_or_none([], ("None", "Any"))
        assert result == []
        assert isinstance(result, list)


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
