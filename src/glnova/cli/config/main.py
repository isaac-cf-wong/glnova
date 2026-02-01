"""Configuration CLI commands for glnova."""

from __future__ import annotations

import typer

config_app = typer.Typer(
    name="config",
    help="Manage gitlab configuration.",
    rich_markup_mode="rich",
)


def register_commands() -> None:
    """Register config subcommands."""


register_commands()
