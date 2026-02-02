"""Project CLI commands for glnova."""

from __future__ import annotations

import typer

project_app = typer.Typer(
    name="project",
    help="Manage projects.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register project subcommands."""
    from glnova.cli.project.list import list_command  # noqa: PLC0415

    project_app.command(name="list", help="List projects.")(list_command)


register_commands()
