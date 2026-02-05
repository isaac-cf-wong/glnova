"""User CLI commands for glnova."""

from __future__ import annotations

import typer

user_app = typer.Typer(
    name="user",
    help="Manage users.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register user subcommands."""


register_commands()
