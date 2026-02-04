"""List command for merge request CLI."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal

import typer


def list_command(  # noqa: PLR0913
    ctx: typer.Context,
    project_id: Annotated[
        str | None, typer.Option("--project-id", help="The project ID or name to filter merge requests.")
    ] = None,
    group_id: Annotated[
        str | None, typer.Option("--group-id", help="The group ID or name to filter merge requests.")
    ] = None,
    approved: Annotated[
        Literal["yes", "no"] | None, typer.Option("--approved", help="Filter merge requests by approval status.")
    ] = None,
    approved_by_ids: Annotated[
        list[str] | None, typer.Option("--approved-by-ids", help="Filter merge requests by approved by user IDs.")
    ] = None,
    approved_by_usernames: Annotated[
        list[str] | None,
        typer.Option("--approved-by-usernames", help="Filter merge requests by approved by usernames."),
    ] = None,
    approver_ids: Annotated[
        list[str] | None, typer.Option("--approver-ids", help="Filter merge requests by approver IDs.")
    ] = None,
    assignee_id: Annotated[
        str | None, typer.Option("--assignee-id", help="Filter merge requests by assignee ID.")
    ] = None,
    assignee_username: Annotated[
        list[str] | None, typer.Option("--assignee-username", help="Filter merge requests by assignee usernames.")
    ] = None,
    author_id: Annotated[str | None, typer.Option("--author-id", help="Filter merge requests by author ID.")] = None,
    author_username: Annotated[
        str | None, typer.Option("--author-username", help="Filter merge requests by author username.")
    ] = None,
    created_after: Annotated[
        datetime | None, typer.Option("--created-after", help="Filter merge requests created after this date.")
    ] = None,
    created_before: Annotated[
        datetime | None, typer.Option("--created-before", help="Filter merge requests created before this date.")
    ] = None,
    deployed_after: Annotated[
        datetime | None, typer.Option("--deployed-after", help="Filter merge requests deployed after this date.")
    ] = None,
    deployed_before: Annotated[
        datetime | None, typer.Option("--deployed-before", help="Filter merge requests deployed before this date.")
    ] = None,
    environment: Annotated[
        str | None, typer.Option("--environment", help="Filter merge requests by environment.")
    ] = None,
    iids: Annotated[list[int] | None, typer.Option("--iids", help="Filter merge requests by internal IDs.")] = None,
    search_in: Annotated[
        list[str] | None, typer.Option("--search-in", help="Filter merge requests by search fields.")
    ] = None,
    labels: Annotated[list[str] | None, typer.Option("--labels", help="Filter merge requests by labels.")] = None,
    merge_user_id: Annotated[
        int | None, typer.Option("--merge-user-id", help="Filter merge requests by merge user ID.")
    ] = None,
    merge_user_username: Annotated[
        str | None, typer.Option("--merge-user-username", help="Filter merge requests by merge user username.")
    ] = None,
    milestone: Annotated[str | None, typer.Option("--milestone", help="Filter merge requests by milestone.")] = None,
    my_reaction_emoji: Annotated[
        str | None, typer.Option("--my-reaction-emoji", help="Filter merge requests by my reaction emoji.")
    ] = None,
    non_archived: Annotated[
        bool | None, typer.Option("--non-archived", help="Filter merge requests by non-archived status.")
    ] = None,
    not_match: Annotated[
        Literal[
            "labels",
            "milestone",
            "author_id",
            "author_username",
            "assignee_id",
            "assignee_username",
            "reviewer_id",
            "reviewer_username",
            "my_reaction_emoji",
        ]
        | None,
        typer.Option(
            "--not-match",
            help="Filter merge requests that do not match the specified criteria.",
        ),
    ] = None,
    order_by: Annotated[
        Literal["created_at", "title", "merged_at", "updated_at"] | None,
        typer.Option("--order-by", help="Order merge requests by the specified field."),
    ] = None,
    page: Annotated[int, typer.Option("--page", help="Page number for pagination.")] = 1,
    per_page: Annotated[int, typer.Option("--per-page", help="Number of items per page for pagination.")] = 20,
    render_html: Annotated[
        bool | None, typer.Option("--render-html/--no-render-html", help="Render merge requests as HTML.")
    ] = None,
    reviewer_id: Annotated[
        str | None, typer.Option("--reviewer-id", help="Filter merge requests by reviewer ID.")
    ] = None,
    reviewer_username: Annotated[
        str | None, typer.Option("--reviewer-username", help="Filter merge requests by reviewer username.")
    ] = None,
    scope: Annotated[
        Literal["created_by_me", "assigned_to_me", "reviews_for_me", "all"] | None,
        typer.Option("--scope", help="Filter merge requests by scope."),
    ] = None,
    search: Annotated[str | None, typer.Option("--search", help="Search merge requests.")] = None,
    sort: Annotated[Literal["asc", "desc"] | None, typer.Option("--sort", help="Sort merge requests.")] = None,
    source_branch: Annotated[
        str | None, typer.Option("--source-branch", help="Filter merge requests by source branch.")
    ] = None,
    source_project_id: Annotated[
        int | None, typer.Option("--source-project-id", help="Filter merge requests by source project ID.")
    ] = None,
    state: Annotated[
        Literal["all", "opened", "closed", "locked", "merged"] | None,
        typer.Option("--state", help="Filter merge requests by state."),
    ] = None,
    target_branch: Annotated[
        str | None, typer.Option("--target-branch", help="Filter merge requests by target branch.")
    ] = None,
    updated_after: Annotated[
        datetime | None, typer.Option("--updated-after", help="Filter merge requests updated after this date.")
    ] = None,
    updated_before: Annotated[
        datetime | None, typer.Option("--updated-before", help="Filter merge requests updated before this date.")
    ] = None,
    view: Annotated[str | None, typer.Option("--view", help="View option for merge requests.")] = None,
    with_labels_details: Annotated[
        bool | None,
        typer.Option("--with-labels-details/--no-with-labels-details", help="Include label details in the response."),
    ] = None,
    with_merge_status_recheck: Annotated[
        bool | None,
        typer.Option("--with-merge-status-recheck/--no-with-merge-status-recheck", help="Recheck merge status."),
    ] = None,
    wip: Annotated[
        Literal["yes", "no"] | None, typer.Option("--wip", help="Filter merge requests by work-in-progress status.")
    ] = None,
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
    """List GitLab merge requests.

    Args:
        ctx: Typer context.
        project_id: The project ID or name to filter merge requests.
        group_id: The group ID or name to filter merge requests.
        approved: Filter merge requests by approval status.
        approved_by_ids: Filter merge requests by approved by user IDs.
        approved_by_usernames: Filter merge requests by approved by usernames.
        approver_ids: Filter merge requests by approver IDs.
        assignee_id: Filter merge requests by assignee ID.
        assignee_username: Filter merge requests by assignee usernames.
        author_id: Filter merge requests by author ID.
        author_username: Filter merge requests by author username.
        created_after: Filter merge requests created after this date.
        created_before: Filter merge requests created before this date.
        deployed_after: Filter merge requests deployed after this date.
        deployed_before: Filter merge requests deployed before this date.
        environment: Filter merge requests by environment.
        iids: Filter merge requests by internal IDs.
        search_in: Filter merge requests by search fields.
        labels: Filter merge requests by labels.
        merge_user_id: Filter merge requests by merge user ID.
        merge_user_username: Filter merge requests by merge user username.
        milestone: Filter merge requests by milestone.
        my_reaction_emoji: Filter merge requests by my reaction emoji.
        non_archived: Filter merge requests by non-archived status.
        not_match: Filter merge requests that do not match the specified criteria.
        order_by: Order merge requests by the specified field.
        page: Page number for pagination.
        per_page: Number of items per page for pagination.
        render_html: Render merge requests as HTML.
        reviewer_id: Filter merge requests by reviewer ID.
        reviewer_username: Filter merge requests by reviewer username.
        scope: Filter merge requests by scope.
        search: Search merge requests.
        sort: Sort merge requests.
        source_branch: Filter merge requests by source branch.
        source_project_id: Filter merge requests by source project ID.
        state: Filter merge requests by state.
        target_branch: Filter merge requests by target branch.
        updated_after: Filter merge requests updated after this date.
        updated_before: Filter merge requests updated before this date.
        view: View option for merge requests.
        with_labels_details: Include label details in the response.
        with_merge_status_recheck: Recheck merge status.
        wip: Filter merge requests by work-in-progress status.
        etag: ETag for caching.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    from typing import Any, cast  # noqa: PLC0415

    from glnova.cli.utils.api import execute_api_command  # noqa: PLC0415
    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.cli.utils.convert import (  # noqa: PLC0415
        list_str_to_list_literal_or_none,
        list_str_to_literal_or_list_int_or_none,
        list_str_to_literal_or_list_str_or_none,
        str_to_int_or_none,
        str_to_literal_or_int_or_none,
    )
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    # Convert the types as needed
    # Project ID
    project_id_value = str_to_int_or_none(project_id)

    # Group ID
    group_id_value = str_to_int_or_none(group_id)

    # Approved by IDs
    approved_by_ids_value = list_str_to_literal_or_list_int_or_none(approved_by_ids, ("None", "Any"))
    if isinstance(approved_by_ids_value, str):
        approved_by_ids_value = cast(Literal["None", "Any"], approved_by_ids_value)

    # Approved by usernames
    approved_by_usernames_value = list_str_to_literal_or_list_str_or_none(approved_by_usernames, ("None", "Any"))
    if isinstance(approved_by_usernames_value, str):
        approved_by_usernames_value = cast(Literal["None", "Any"], approved_by_usernames_value)

    # Approver IDs
    approver_ids_value = list_str_to_literal_or_list_int_or_none(approver_ids, ("None", "Any"))
    if isinstance(approver_ids_value, str):
        approver_ids_value = cast(Literal["None", "Any"], approver_ids_value)

    # Assignee ID
    assignee_id_value = str_to_literal_or_int_or_none(assignee_id, ("None", "Any"))
    if isinstance(assignee_id_value, str):
        assignee_id_value = cast(Literal["None", "Any"], assignee_id_value)

    # Author ID
    author_id_value = str_to_literal_or_int_or_none(author_id, ("None", "Any"))
    if isinstance(author_id_value, str):
        author_id_value = cast(Literal["None", "Any"], author_id_value)

    # Search in
    search_in_value = cast(
        list[Literal["title", "description"]] | None,
        list_str_to_list_literal_or_none(search_in, ("title", "description")),
    )

    # Labels
    labels_value = list_str_to_literal_or_list_str_or_none(labels, ("None", "Any"))
    if isinstance(labels_value, str):
        labels_value = cast(Literal["None", "Any"], labels_value)

    # Milestone
    milestone_value = milestone
    if milestone_value in ("None", "Any"):
        milestone_value = cast(Literal["None", "Any"], milestone_value)

    # My reaction emoji
    my_reaction_emoji_value = my_reaction_emoji
    if my_reaction_emoji_value in ("None", "Any"):
        my_reaction_emoji_value = cast(Literal["None", "Any"], my_reaction_emoji_value)

    # Reviewer ID
    reviewer_id_value = str_to_literal_or_int_or_none(reviewer_id, ("None", "Any"))
    if isinstance(reviewer_id_value, str):
        reviewer_id_value = cast(Literal["None", "Any"], reviewer_id_value)

    # Reviewer username
    reviewer_username_value = reviewer_username
    if reviewer_username_value in ("None", "Any"):
        reviewer_username_value = cast(Literal["None", "Any"], reviewer_username_value)

    def api_call() -> tuple[list[dict[str, Any]], dict[str, Any]]:
        with GitLab(token=token, base_url=base_url) as client:
            return client.merge_request.list_merge_requests(
                project_id=project_id_value,
                group_id=group_id_value,
                approved=approved,
                approved_by_ids=approved_by_ids_value,
                approved_by_usernames=approved_by_usernames_value,
                approver_ids=approver_ids_value,
                assignee_id=assignee_id_value,
                assignee_username=assignee_username,
                author_id=author_id_value,
                author_username=author_username,
                created_after=created_after,
                created_before=created_before,
                deployed_after=deployed_after,
                deployed_before=deployed_before,
                environment=environment,
                iids=iids,
                search_in=search_in_value,
                labels=labels_value,
                merge_user_id=merge_user_id,
                merge_user_username=merge_user_username,
                milestone=milestone_value,
                my_reaction_emoji=my_reaction_emoji_value,
                non_archived=non_archived,
                not_match=not_match,
                order_by=order_by,
                page=page,
                per_page=per_page,
                render_html=render_html,
                reviewer_id=reviewer_id_value,
                reviewer_username=reviewer_username_value,
                scope=scope,
                search=search,
                sort=sort,
                source_branch=source_branch,
                source_project_id=source_project_id,
                state=state,
                target_branch=target_branch,
                updated_after=updated_after,
                updated_before=updated_before,
                view=view,
                with_labels_details=with_labels_details,
                with_merge_status_recheck=with_merge_status_recheck,
                wip=wip,
                etag=etag,
            )

    execute_api_command(api_call=api_call, command_name="glnova merge-request list")
