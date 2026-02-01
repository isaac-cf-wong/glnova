"""Utility functions for converting data types."""

from __future__ import annotations


def str_to_int(value: str) -> int | str:
    """Convert a string to an integer if possible.

    Args:
        value: The string to convert.

    Returns:
        The integer value if conversion is successful, otherwise the original string.

    """
    try:
        return int(value)
    except ValueError:
        return value


def str_to_int_or_none(value: str | None) -> str | int | None:
    """Convert a string to an integer if possible.

    Args:
        value: The string to convert.

    Returns:
        The integer value if conversion is successful, otherwise the original string or None.

    """
    if value is None:
        return value
    return str_to_int(value)


def str_to_literal_or_int(
    value: str,
    literal_tuple: tuple[str, ...],
) -> str | int:
    """Convert a string to an integer or a literal.

    Args:
        value: The string to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        The integer value if conversion is successful, otherwise the original string if it matches a literal.

    """
    try:
        return int(value)
    except ValueError as e:
        if value in literal_tuple:
            return value
        else:
            raise ValueError(f"Value must be an integer or one of the literals: {literal_tuple}") from e


def str_to_literal_or_int_or_none(
    value: str | None,
    literal_tuple: tuple[str, ...],
) -> str | int | None:
    """Convert a string to an integer, 'None', or 'Any' literal.

    Args:
        value: The string to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        The integer value if conversion is successful, the original string if it matches a literal, or None if the input is None.

    """
    if value is None:
        return value
    return str_to_literal_or_int(value, literal_tuple)
