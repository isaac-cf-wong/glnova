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
    from glnova.cli.issue.edit import edit_command  # noqa: PLC0415
    from glnova.cli.issue.get import get_command  # noqa: PLC0415
    from glnova.cli.issue.list import list_command  # noqa: PLC0415

    issue_app.command(name="edit", help="Edit a GitLab issue.")(edit_command)
    issue_app.command(name="get", help="Get a specific GitLab issue.")(get_command)
    issue_app.command(name="list", help="List GitLab issues.")(list_command)


register_commands()
