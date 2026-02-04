"""List command for issue CLI."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal

import typer


def list_command(  # noqa: PLR0913
    ctx: typer.Context,
    group: Annotated[str | None, typer.Option("--group", help="The group name or ID. ")] = None,
    project: Annotated[
        str | None,
        typer.Option(
            "--project",
            help="The project name or ID.",
        ),
    ] = None,
    assignee_id: Annotated[
        str | None,
        typer.Option(
            "--assignee-id", help="Filter by assignee ID. Use 'None' for unassigned issues and 'Any' for any assignee."
        ),
    ] = None,
    assignee_username: Annotated[
        list[str] | None,
        typer.Option(
            "--assignee-username",
            help="Filter by assignee username(s).",
        ),
    ] = None,
    author_id: Annotated[
        int | None,
        typer.Option(
            "--author-id",
            help="Filter by author ID.",
        ),
    ] = None,
    author_username: Annotated[
        str | None,
        typer.Option(
            "--author-username",
            help="Filter by author username.",
        ),
    ] = None,
    confidential: Annotated[
        bool | None,
        typer.Option(
            "--confidential/--no-confidential",
            help="Filter by confidentiality status.",
        ),
    ] = None,
    created_after: Annotated[
        datetime | None,
        typer.Option(
            "--created-after",
            help="Filter issues created after this date (ISO 8601 format).",
        ),
    ] = None,
    created_before: Annotated[
        datetime | None,
        typer.Option(
            "--created-before",
            help="Filter issues created before this date (ISO 8601 format).",
        ),
    ] = None,
    due_date: Annotated[
        Literal["0", "any", "today", "tomorrow", "overdue", "week", "month", "next_month_and_previous_two_weeks"]
        | None,
        typer.Option(
            "--due-date",
            help="Filter by due date. Options: '0' (no due date), 'any', 'today', 'tomorrow', 'overdue', 'week', 'month', 'next_month_and_previous_two_weeks'.",
        ),
    ] = None,
    epic_id: Annotated[
        str | None,
        typer.Option(
            "--epic-id",
            help="Filter by epic ID. Use 'None' for issues without an epic and 'Any' for any epic.",
        ),
    ] = None,
    health_status: Annotated[
        str | None,
        typer.Option(
            "--health-status",
            help="Filter by health status.",
        ),
    ] = None,
    iids: Annotated[
        list[int] | None,
        typer.Option(
            "--iids",
            help="Filter by issue IIDs.",
        ),
    ] = None,
    search_in: Annotated[
        list[str] | None,
        typer.Option(
            "--search-in",
            help="Specify where to search: 'title', or 'description'.",
        ),
    ] = None,
    issue_type: Annotated[
        Literal["issue", "incident", "test_case", "task"] | None,
        typer.Option(
            "--issue-type",
            help="Filter by issue type.",
        ),
    ] = None,
    iteration_id: Annotated[
        str | None,
        typer.Option(
            "--iteration-id",
            help="Filter by iteration ID. Use 'None' for issues without an iteration and 'Any' for any iteration.",
        ),
    ] = None,
    iteration_title: Annotated[
        str | None,
        typer.Option(
            "--iteration-title",
            help="Filter by iteration title.",
        ),
    ] = None,
    labels: Annotated[
        list[str] | None,
        typer.Option(
            "--labels",
            help="Filter by labels. 'None' for issues without labels, 'Any' for any label.",
        ),
    ] = None,
    milestone_id: Annotated[
        Literal["None", "Any", "Upcoming", "Started"] | None,
        typer.Option(
            "--milestone-id",
            help="Filter by milestone ID. Use 'None' for issues without a milestone, 'Any' for any milestone, 'Upcoming' for upcoming milestones, and 'Started' for started milestones.",
        ),
    ] = None,
    milestone: Annotated[
        str | None,
        typer.Option(
            "--milestone",
            help="Filter by milestone title.",
        ),
    ] = None,
    my_reaction_emoji: Annotated[
        str | None,
        typer.Option(
            "--my-reaction-emoji",
            help="Filter by my reaction emoji. 'None' for no reaction, 'Any' for any reaction.",
        ),
    ] = None,
    non_archived: Annotated[
        bool | None,
        typer.Option(
            "--non-archived/--archived",
            help="Filter by archived status.",
        ),
    ] = None,
    not_match: Annotated[
        Literal[
            "assignee_id",
            "assignee_username",
            "author_id",
            "author_username",
            "iids",
            "iteration_id",
            "iteration_title",
            "labels",
            "milestone",
            "milestone_id",
            "weight",
        ]
        | None,
        typer.Option(
            "--not-match",
            help="Filter by not matching a specific term.",
        ),
    ] = None,
    order_by: Annotated[
        Literal[
            "created_at",
            "due_date",
            "label_priority",
            "milestone_due",
            "popularity",
            "priority",
            "relative_position",
            "title",
            "updated_at",
            "weight",
        ]
        | None,
        typer.Option(
            "--order-by",
            help="Field to order by.",
        ),
    ] = None,
    scope: Annotated[
        Literal["created_by_me", "assigned_to_me", "all"] | None,
        typer.Option(
            "--scope",
            help="Scope of issues to return.",
        ),
    ] = None,
    search: Annotated[
        str | None,
        typer.Option(
            "--search",
            help="Search term.",
        ),
    ] = None,
    sort: Annotated[
        Literal["asc", "desc"] | None,
        typer.Option(
            "--sort",
            help="Sort order.",
        ),
    ] = None,
    state: Annotated[
        Literal["opened", "closed", "all"] | None,
        typer.Option(
            "--state",
            help="State of the issues.",
        ),
    ] = None,
    updated_after: Annotated[
        datetime | None,
        typer.Option(
            "--updated-after",
            help="Filter issues updated after this date (ISO 8601 format).",
        ),
    ] = None,
    updated_before: Annotated[
        datetime | None,
        typer.Option(
            "--updated-before",
            help="Filter issues updated before this date (ISO 8601 format).",
        ),
    ] = None,
    weight: Annotated[
        str | None,
        typer.Option(
            "--weight",
            help="Filter by weight. Use 'None' for issues without weight and 'Any' for any weight.",
        ),
    ] = None,
    with_labels_details: Annotated[
        bool | None,
        typer.Option(
            "--with-labels-details/--no-with-labels-details",
            help="Include label details in the response.",
        ),
    ] = None,
    cursor: Annotated[
        str | None,
        typer.Option(
            "--cursor",
            help="Cursor for pagination.",
        ),
    ] = None,
    page: Annotated[
        int,
        typer.Option(
            "--page",
            help="Page number for pagination.",
        ),
    ] = 1,
    per_page: Annotated[
        int,
        typer.Option(
            "--per-page",
            help="Number of items per page for pagination.",
        ),
    ] = 20,
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
):
    """List issues from GitLab based on provided filters.

    Args:
        ctx: Typer context.
        group: The group name or ID.
        project: The project name or ID.
        assignee_id: Filter by assignee ID. Use 'None' for unassigned issues and 'Any' for any assignee.
        assignee_username: Filter by assignee username(s).
        author_id: Filter by author ID.
        author_username: Filter by author username.
        confidential: Filter by confidentiality status.
        created_after: Filter issues created after this date (ISO 8601 format).
        created_before: Filter issues created before this date (ISO 8601 format).
        due_date: Filter by due date. Options: '0' (no due date), 'any', 'today', 'tomorrow',
            'overdue', 'week', 'month', 'next_month_and_previous_two_weeks'.
        epic_id: Filter by epic ID. Use 'None' for issues without an epic and 'Any' for any epic.
        health_status: Filter by health status.
        iids: Filter by issue IIDs.
        search_in: Specify where to search: 'title', or 'description'.
        issue_type: Filter by issue type.
        iteration_id: Filter by iteration ID. Use 'None' for issues without an iteration and
            'Any' for any iteration.
        iteration_title: Filter by iteration title.
        labels: Filter by labels.
        milestone_id: Filter by milestone ID. Use 'None' for issues without a milestone,
            'Any' for any milestone, 'Upcoming' for upcoming milestones, and 'Started' for started milestones.
        milestone: Filter by milestone title.
        my_reaction_emoji: Filter by my reaction emoji.
        non_archived: Filter by archived status.
        not_match: Filter by not matching a specific term.
        order_by: Field to order by.
        scope: Scope of issues to return.
        search: Search term.
        sort: Sort order.
        state: State of the issues.
        updated_after: Filter issues updated after this date (ISO 8601 format).
        updated_before: Filter issues updated before this date (ISO 8601 format).
        weight: Filter by weight. Use 'None' for issues without weight and 'Any' for any weight.
        with_labels_details: Include label details in the response.
        cursor: Cursor for pagination.
        page: Page number for pagination.
        per_page: Number of items per page for pagination.
        etag: ETag for conditional requests.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    from typing import Any, cast  # noqa: PLC0415

    from glnova.cli.utils.api import execute_api_command  # noqa: PLC0415
    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.cli.utils.convert import str_to_int_or_none, str_to_literal_or_int_or_none  # noqa: PLC0415
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    # Convert the types as needed
    # Assignee ID conversion
    assignee_id_value = str_to_literal_or_int_or_none(assignee_id, ("None", "Any"))
    if isinstance(assignee_id_value, str):
        assignee_id_value = cast(Literal["None", "Any"], assignee_id_value)

    # Epic ID conversion
    epic_id_value = str_to_literal_or_int_or_none(epic_id, ("None", "Any"))
    if isinstance(epic_id_value, str):
        epic_id_value = cast(Literal["None", "Any"], epic_id_value)

    # Iteration ID conversion
    iteration_id_value = str_to_literal_or_int_or_none(iteration_id, ("None", "Any"))
    if isinstance(iteration_id_value, str):
        iteration_id_value = cast(Literal["None", "Any"], iteration_id_value)

    # Weight conversion
    weight_value = str_to_literal_or_int_or_none(weight, ("None", "Any"))
    if isinstance(weight_value, str):
        weight_value = cast(Literal["None", "Any"], weight_value)

    # Search in conversion
    search_in_list = None
    if search_in:
        if not all(item in ["title", "description"] for item in search_in):
            typer.echo(
                "Error: --search-in must be one or more of 'title', 'description'.",
                err=True,
            )
            raise typer.Exit(code=1)
        search_in_list = cast(list[Literal["title", "description"]], list(search_in))

    def api_call() -> tuple[list[dict[str, Any]], dict[str, Any]]:
        with GitLab(token=token, base_url=base_url) as client:
            return client.issue.list_issues(
                group=str_to_int_or_none(group),
                project=str_to_int_or_none(project),
                assignee_id=assignee_id_value,
                assignee_username=assignee_username,
                author_id=author_id,
                author_username=author_username,
                confidential=confidential,
                created_after=created_after,
                created_before=created_before,
                due_date=due_date,
                epic_id=epic_id_value,
                health_status=health_status,
                iids=iids,
                search_in=search_in_list,
                issue_type=issue_type,
                iteration_id=iteration_id_value,
                iteration_title=iteration_title,
                labels=labels,
                milestone_id=milestone_id,
                milestone=milestone,
                my_reaction_emoji=my_reaction_emoji,
                non_archived=non_archived,
                not_match=not_match,
                order_by=order_by,
                scope=scope,
                search=search,
                sort=sort,
                state=state,
                updated_after=updated_after,
                updated_before=updated_before,
                weight=weight_value,
                with_labels_details=with_labels_details,
                cursor=cursor,
                page=page,
                per_page=per_page,
                etag=etag,
            )

    execute_api_command(api_call=api_call, command_name="glnova issue list")
