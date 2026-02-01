"""Issue CLI commands for glnova."""

from __future__ import annotations

import typer

issue_app = typer.Typer(
    name="issue",
    help="Manage GitLab issues.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register issue subcommands."""


register_commands()
