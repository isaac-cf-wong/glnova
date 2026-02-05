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
    from glnova.cli.user.get import get_command  # noqa: PLC0415

    user_app.command(name="get", help="Get user information.")(get_command)


register_commands()
