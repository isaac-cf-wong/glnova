"""Merge Request CLI commands for glnova."""

from __future__ import annotations

import typer

merge_request_app = typer.Typer(
    name="merge-request",
    help="Manage GitLab merge requests.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register merge request subcommands."""


register_commands()
