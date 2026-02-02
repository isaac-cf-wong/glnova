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


def list_str_to_literal_or_list_int(
    values: list[str],
    literal_tuple: tuple[str, ...],
) -> list[int] | str | None:
    """Convert a list of strings to a list of integers or a literal.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of integers if conversion is successful, otherwise the original string if it matches a literal

    """
    if len(values) == 1:
        if values[0] in literal_tuple:
            return values[0]
        else:
            return [int(values[0])]
    return [int(ele) for ele in values]


def list_str_to_literal_or_list_int_or_none(
    values: list[str] | None,
    literal_tuple: tuple[str, ...],
) -> list[int] | str | None:
    """Convert a list of strings to a list of integers, a literal, or None.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of integers if conversion is successful, the original string if it matches a literal, or None if the input is None.

    """
    return values if values is None else list_str_to_literal_or_list_int(values, literal_tuple)


def list_str_to_literal_or_list_str(
    values: list[str],
    literal_tuple: tuple[str, ...],
) -> list[str] | str | None:
    """Convert a list of strings to a list of strings or a literal.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of strings if it does not match a literal, otherwise the original string if it matches a literal.

    """
    if len(values) == 1 and values[0] in literal_tuple:
        return values[0]
    return values


def list_str_to_literal_or_list_str_or_none(
    values: list[str] | None,
    literal_tuple: tuple[str, ...],
) -> list[str] | str | None:
    """Convert a list of strings to a list of strings, a literal, or None.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of strings if it does not match a literal, the original string if it matches a literal, or None if the input is None.

    """
    return values if values is None else list_str_to_literal_or_list_str(values, literal_tuple)


def list_str_to_list_literal(
    values: list[str],
    literal_tuple: tuple[str, ...],
) -> list[str]:
    """Convert a list of strings to a list of literals.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of strings if all values match the literals.

    """
    if not all(ele in literal_tuple for ele in values):
        raise ValueError(f"All values must be one of the literals: {literal_tuple}")
    return values


def list_str_to_list_literal_or_none(
    values: list[str] | None,
    literal_tuple: tuple[str, ...],
) -> list[str] | None:
    """Convert a list of strings to a list of literals or None.

    Args:
        values: The list of strings to convert.
        literal_tuple: A tuple of literal strings to check against.

    Returns:
        A list of strings if all values match the literals, or None if the input is None.

    """
    return values if values is None else list_str_to_list_literal(values, literal_tuple)
