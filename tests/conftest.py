"""Configuration and fixtures for pytest."""

from __future__ import annotations

import logging

import pytest


@pytest.fixture(autouse=True)
def cleanup_logging_handlers() -> None:
    """Clean up logging state after each test to prevent test pollution.

    This ensures that handlers and settings from setup_logging() calls
    in one test don't interfere with caplog in subsequent tests.
    """
    yield

    # After test: completely reset the logger
    logger = logging.getLogger("glnova")
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    logger.setLevel(logging.NOTSET)
    logger.propagate = True


@pytest.fixture
def some_name() -> str:
    """Provide a sample name for testing.

    Returns:
        A string name.

    """
    return "developer"
