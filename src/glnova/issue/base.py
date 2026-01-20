from __future__ import annotations

import logging
from typing import Any, Literal

logger = logging.getLogger("glnova")


class BaseIssue:
    """Base class for GitLab Issue resource."""

    def _list_issues_endpoint(
        self, group: str | int | None = None, project: str | int | None = None
    ) -> tuple[str, str]:
        """Construct the endpoint for listing issues.

        If a project is specified, the endpoint will be for that project.
        If a group is specified (and no project), the endpoint will be for that group.
        If neither is specified, the endpoint will be for all issues.

        Args:
            group: The group name or ID.
            project: The project name or ID.

        Returns:
            str: The constructed endpoint.
        """
        if project is not None:
            if isinstance(project, str):
                project = project.replace("/", "%2F")
            return f"/projects/{project}/issues", "project issues"
        elif group is not None:
            if isinstance(group, str):
                group = group.replace("/", "%2F")
            return f"/groups/{group}/issues", "group issues"
        else:
            return "/issues", "authenticated user issues"

    def _list_issues_helper(  # noqa: PLR0912, PLR0913, PLR0915
        self,
        group: str | int | None = None,
        project: str | int | None = None,
        assignee_id: int | Literal["None", "Any"] | None = None,
        assignee_username: list[str] | None = None,
        author_id: int | None = None,
        author_username: str | None = None,
        confidential: bool | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
        due_date: (
            Literal["0", "any", "today", "tomorrow", "overdue", "week", "month", "next_month_and_previous_two_weeks"]
            | None
        ) = None,
        epic_id: int | Literal["None", "Any"] | None = None,
        health_status: str | None = None,
        iids: list[int] | None = None,
        search_in: list[Literal["title", "description"]] | None = None,
        issue_type: Literal["issue", "incident", "test_case", "task"] | None = None,
        iteration_id: int | Literal["None", "Any"] | None = None,
        iteration_title: str | None = None,
        labels: list[str] | Literal["None", "Any"] | None = None,
        milestone_id: Literal["None", "Any", "Upcoming", "Started"] | None = None,
        milestone: str | None = None,
        my_reaction_emoji: str | Literal["None", "Any"] | None = None,
        non_archived: bool | None = None,
        not_match: (
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
            | None
        ) = None,
        order_by: (
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
            | None
        ) = None,
        scope: Literal["created_by_me", "assigned_to_me", "all"] | None = None,
        search: str | None = None,
        sort: Literal["asc", "desc"] | None = None,
        state: Literal["opened", "closed", "all"] | None = None,
        updated_after: str | None = None,
        updated_before: str | None = None,
        weight: int | Literal["None", "Any"] | None = None,
        with_labels_details: bool | None = None,
        cursor: str | None = None,
        page: int = 1,
        per_page: int = 20,
        **kwargs: Any,
    ) -> tuple[str, dict[str, Any], dict[str, Any]]:
        """Helper method to construct endpoint and parameters for listing issues.

        Args:
            group: The group name or ID.
            project: The project name or ID.
            assignee_id: Filter by assignee ID.
            assignee_username: Filter by assignee username.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            confidential: Filter by confidentiality.
            created_after: Filter by creation date after this date.
            created_before: Filter by creation date before this date.
            due_date: Filter by due date.
            epic_id: Filter by epic ID.
            health_status: Filter by health status.
            iids: Filter by issue IIDs.
            search_in: Fields to search in.
            issue_type: Filter by issue type.
            iteration_id: Filter by iteration ID.
            iteration_title: Filter by iteration title.
            labels: Filter by labels.
            milestone_id: Filter by milestone ID.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            non_archived: Filter by non-archived issues.
            not_match: Fields to exclude from the match.
            order_by: Field to order by.
            scope: Scope of issues.
            search: Search term.
            sort: Sort order.
            state: State of the issues.
            updated_after: Filter by update date after this date.
            updated_before: Filter by update date before this date.
            weight: Filter by weight.
            with_labels_details: Include label details.
            cursor: Cursor for pagination (only for project issues).
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            **kwargs: Additional keyword arguments.

        Returns:
            tuple: A tuple containing the endpoint, parameters dictionary, and additional kwargs.
        """
        endpoint, endpoint_type = self._list_issues_endpoint(group=group, project=project)

        params = {}
        if assignee_id is not None:
            params["assignee_id"] = assignee_id
        if assignee_username is not None:
            params["assignee_username"] = assignee_username
        if author_id is not None:
            params["author_id"] = author_id
        if author_username is not None:
            params["author_username"] = author_username
        if confidential is not None:
            params["confidential"] = confidential
        if created_after is not None:
            params["created_after"] = created_after
        if created_before is not None:
            params["created_before"] = created_before
        if due_date is not None:
            params["due_date"] = due_date
        if epic_id is not None:
            params["epic_id"] = epic_id
        if health_status is not None:
            params["health_status"] = health_status
        if iids is not None:
            params["iids"] = iids
        if search_in is not None:
            params["in"] = search_in
        if issue_type is not None:
            params["issue_type"] = issue_type
        if iteration_id is not None:
            params["iteration_id"] = iteration_id
        if iteration_title is not None:
            params["iteration_title"] = iteration_title
        if labels is not None:
            params["labels"] = ",".join(labels)
        if milestone_id is not None:
            params["milestone_id"] = milestone_id
        if milestone is not None:
            params["milestone"] = milestone
        if my_reaction_emoji is not None:
            params["my_reaction_emoji"] = my_reaction_emoji
        if non_archived is not None:
            params["non_archived"] = non_archived
        if not_match is not None:
            params["not"] = not_match
        if order_by is not None:
            params["order_by"] = order_by
        if scope is not None:
            params["scope"] = scope
        if search is not None:
            params["search"] = search
        if sort is not None:
            params["sort"] = sort
        if state is not None:
            params["state"] = state
        if updated_after is not None:
            params["updated_after"] = updated_after
        if updated_before is not None:
            params["updated_before"] = updated_before
        if weight is not None:
            params["weight"] = weight
        if with_labels_details is not None:
            params["with_labels_details"] = with_labels_details
        if cursor is not None:
            if endpoint_type == "project issues":
                params["cursor"] = cursor
            else:
                logger.warning("Cursor pagination is only supported for project issues endpoints.")
        params["page"] = page
        params["per_page"] = per_page

        return endpoint, params, kwargs
