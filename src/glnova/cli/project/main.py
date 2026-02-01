"""Project CLI commands for glnova."""

from __future__ import annotations

import typer

project_app = typer.Typer(
    name="project",
    help="Manage projects.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register issue subcommands."""


register_commands()
