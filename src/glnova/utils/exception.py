"""Custom exception classes."""

from __future__ import annotations


class InvalidLiteralListError(ValueError):
    """Exception raised when a value is not in the allowed literal list."""

    def __init__(self, literal_tuple: tuple[str, ...]) -> None:
        """Initialize the InvalidLiteralListError.

        Args:
            literal_tuple: A tuple of allowed literal strings.

        """
        super().__init__(f"All values must be one of the literals: {literal_tuple}")
