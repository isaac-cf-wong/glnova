"""Get command for issue CLI."""

from __future__ import annotations

from typing import Annotated

import typer


def get_command(  # noqa: PLR0913
    ctx: typer.Context,
    issue_id: Annotated[
        int | None,
        typer.Argument(
            help="The ID of the issue to retrieve. Can be used with --project-id.",
        ),
    ] = None,
    project_id: Annotated[
        str | None,
        typer.Option(
            "--project-id",
            help="The project ID or name. Required when using --issue-iid.",
        ),
    ] = None,
    issue_iid: Annotated[
        int | None,
        typer.Option(
            "--issue-iid",
            help="The IID of the issue within the project. Requires --project-id.",
        ),
    ] = None,
    etag: Annotated[
        str | None,
        typer.Option(
            "--etag",
            help="ETag for conditional requests.",
        ),
    ] = None,
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
    """Get a specific GitLab issue by ID or IID.

    You must provide either:
    - --issue-id: Global issue ID
    - --project-id and --issue-iid: Project-specific issue IID

    Args:
        ctx: Typer context.
        issue_id: The global ID of the issue to retrieve.
        project_id: The project ID or name. Required when using --issue-iid.
        issue_iid: The IID of the issue within the project. Requires --project-id.
        etag: ETag for conditional requests.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    import json  # noqa: PLC0415
    import logging  # noqa: PLC0415

    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.cli.utils.convert import str_to_int_or_none  # noqa: PLC0415
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    logger = logging.getLogger("glnova")

    # Validate arguments
    if issue_id is None and (project_id is None or issue_iid is None):
        typer.echo(
            "Error: You must provide either --issue-id or both --project-id and --issue-iid.",
            err=True,
        )
        raise typer.Exit(code=1)

    if issue_id is not None and (project_id is not None or issue_iid is not None):
        typer.echo(
            "Error: --issue-id cannot be used with --project-id or --issue-iid.",
            err=True,
        )
        raise typer.Exit(code=1)

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    try:
        with GitLab(token=token, base_url=base_url) as client:
            data, status_code, etag_response = client.issue.get_issue(
                issue_id=issue_id,
                project_id=str_to_int_or_none(project_id),
                issue_iid=issue_iid,
                etag=etag,
            )

            result = {
                "data": data,
                "metadata": {
                    "status_code": status_code,
                    "etag": etag_response,
                },
            }
            print(json.dumps(result, default=str, indent=2))
    except Exception as e:
        logger.error("Error getting issue: %s", e)
        raise typer.Exit(code=1) from e
