"""Get command for user CLI."""

from __future__ import annotations

from typing import Annotated

import typer


def get_command(  # noqa: PLR0913
    ctx: typer.Context,
    account_id: Annotated[int | None, typer.Option("--account-id", help="Account ID of the user.")] = None,
    etag: Annotated[str | None, typer.Option("--etag", help="ETag for caching.")] = None,
    account_name: Annotated[
        str | None,
        typer.Option(
            "--account-name",
            help="Name of the account to use for authentication.",
        ),
    ] = None,
    token: Annotated[
        str | None,
        typer.Option(
            "--token",
            help="Token for authentication. If not provided, the token from the specified account will be used.",
        ),
    ] = None,
    base_url: Annotated[
        str | None,
        typer.Option(
            "--base-url",
            help="Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.",
        ),
    ] = None,
) -> None:
    """Get user information.

    Args:
        ctx: Typer context.
        account_id: Account ID of the user.
        etag: ETag for caching.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    from typing import Any  # noqa: PLC0415

    from glnova.cli.utils.api import execute_api_command  # noqa: PLC0415
    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    def api_call() -> tuple[dict[str, Any], dict[str, Any]]:
        """Implement the API call to get user information.

        Returns:
            A tuple containing the user data and response metadata.

        """
        with GitLab(token=token, base_url=base_url) as client:
            return client.user.get_user(
                account_id=account_id,
                etag=etag,
            )

    execute_api_command(api_call=api_call, command_name="glnova user get")
