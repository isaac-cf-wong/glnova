"""Edit command for issue CLI."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal

import typer


def edit_command(  # noqa: PLR0913
    ctx: typer.Context,
    project_id: Annotated[
        str,
        typer.Argument(
            help="The project ID or name where the issue belongs.",
        ),
    ],
    issue_iid: Annotated[
        int,
        typer.Argument(
            help="The IID of the issue to edit.",
        ),
    ],
    title: Annotated[
        str | None,
        typer.Option(
            "--title",
            help="New title for the issue.",
        ),
    ] = None,
    description: Annotated[
        str | None,
        typer.Option(
            "--description",
            help="New description for the issue.",
        ),
    ] = None,
    assignee_ids: Annotated[
        list[int] | None,
        typer.Option(
            "--assignee-ids",
            help="Assignee IDs to assign to the issue. Repeat --assignee-ids for multiple values.",
        ),
    ] = None,
    labels: Annotated[
        list[str] | None,
        typer.Option(
            "--labels",
            help="Labels to set on the issue. Repeat --labels for multiple values.",
        ),
    ] = None,
    add_labels: Annotated[
        list[str] | None,
        typer.Option(
            "--add-labels",
            help="Labels to add to the issue. Repeat --add-labels for multiple values.",
        ),
    ] = None,
    remove_labels: Annotated[
        list[str] | None,
        typer.Option(
            "--remove-labels",
            help="Labels to remove from the issue. Repeat --remove-labels for multiple values.",
        ),
    ] = None,
    milestone_id: Annotated[
        int | None,
        typer.Option(
            "--milestone-id",
            help="Milestone ID to assign to the issue.",
        ),
    ] = None,
    state_event: Annotated[
        Literal["close", "reopen"] | None,
        typer.Option(
            "--state-event",
            help="State event to apply to the issue.",
        ),
    ] = None,
    confidential: Annotated[
        bool | None,
        typer.Option(
            "--confidential/--public",
            help="Set the issue as confidential or public.",
        ),
    ] = None,
    due_date: Annotated[
        str | None,
        typer.Option(
            "--due-date",
            help="Due date for the issue (YYYY-MM-DD format).",
        ),
    ] = None,
    weight: Annotated[
        int | None,
        typer.Option(
            "--weight",
            help="Weight to assign to the issue.",
        ),
    ] = None,
    epic_id: Annotated[
        int | None,
        typer.Option(
            "--epic-id",
            help="Epic ID to assign to the issue.",
        ),
    ] = None,
    epic_iid: Annotated[
        int | None,
        typer.Option(
            "--epic-iid",
            help="Epic IID to assign to the issue.",
        ),
    ] = None,
    issue_type: Annotated[
        Literal["issue", "incident", "test_case", "task"] | None,
        typer.Option(
            "--issue-type",
            help="Type of the issue.",
        ),
    ] = None,
    discussion_locked: Annotated[
        bool | None,
        typer.Option(
            "--lock-discussion/--unlock-discussion",
            help="Lock or unlock discussions on the issue.",
        ),
    ] = None,
    updated_at: Annotated[
        datetime | None,
        typer.Option(
            "--updated-at",
            help="Updated timestamp for the issue (ISO 8601 format).",
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
    """Edit a GitLab issue.

    Args:
        ctx: Typer context.
        project_id: The project ID or name where the issue belongs.
        issue_iid: The IID of the issue to edit.
        title: New title for the issue.
        description: New description for the issue.
        assignee_ids: Assignee IDs to assign to the issue.
        labels: Labels to set on the issue.
        add_labels: Labels to add to the issue.
        remove_labels: Labels to remove from the issue.
        milestone_id: Milestone ID to assign to the issue.
        state_event: State event to apply to the issue.
        confidential: Set the issue as confidential or public.
        due_date: Due date for the issue.
        weight: Weight to assign to the issue.
        epic_id: Epic ID to assign to the issue.
        epic_iid: Epic IID to assign to the issue.
        issue_type: Type of the issue.
        discussion_locked: Lock or unlock discussions on the issue.
        updated_at: Updated timestamp for the issue.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    from typing import Any  # noqa: PLC0415

    from glnova.cli.utils.api import execute_api_command  # noqa: PLC0415
    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.cli.utils.convert import str_to_int  # noqa: PLC0415
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    def api_call() -> tuple[dict[str, Any], dict[str, Any]]:
        with GitLab(token=token, base_url=base_url) as client:
            return client.issue.edit_issue(
                project_id=str_to_int(project_id),
                issue_iid=issue_iid,
                title=title,
                description=description,
                assignee_ids=assignee_ids,
                labels=labels,
                add_labels=add_labels,
                remove_labels=remove_labels,
                milestone_id=milestone_id,
                state_event=state_event,
                confidential=confidential,
                due_date=due_date,
                weight=weight,
                epic_id=epic_id,
                epic_iid=epic_iid,
                issue_type=issue_type,
                discussion_locked=discussion_locked,
                updated_at=updated_at,
            )

    execute_api_command(api_call=api_call, command_name="glnova issue edit")
