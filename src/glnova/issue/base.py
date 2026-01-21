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
    ) -> tuple[str, dict[str, Any]]:
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

        Returns:
            tuple: A tuple containing the endpoint, and parameters dictionary.
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
            params["labels"] = ",".join(labels) if isinstance(labels, list) else labels
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

        return endpoint, params

    def _get_issue_endpoint(
        self,
        issue_id: int | None = None,
        project_id: int | str | None = None,
        issue_iid: int | None = None,
    ) -> str:
        """Construct the endpoint for getting a specific issue.

        Args:
            issue_id: The global issue ID (Administrator only).
            project_id: The project name or ID.
            issue_iid: The issue IID within the project.

        Returns:
            str: The constructed endpoint.
        """
        if issue_id is not None:
            return f"/issues/{issue_id}"
        if project_id is not None and issue_iid is not None:
            if isinstance(project_id, str):
                project_id = project_id.replace("/", "%2F")
            return f"/projects/{project_id}/issues/{issue_iid}"
        raise ValueError("Either issue_id or both project_id and issue_iid must be provided.")

    def _get_issue_helper(
        self,
        issue_id: int | None = None,
        project_id: int | str | None = None,
        issue_iid: int | None = None,
    ) -> str:
        """Helper method to construct endpoint and parameters for getting a specific issue.

        Args:
            issue_id: The global issue ID (Administrator only).
            project_id: The project name or ID.
            issue_iid: The issue IID within the project.

        Returns:
            The constructed endpoint.
        """
        endpoint = self._get_issue_endpoint(
            issue_id=issue_id,
            project_id=project_id,
            issue_iid=issue_iid,
        )

        return endpoint

    def _edit_issue_endpoint(
        self,
        project_id: int | str,
        issue_iid: int,
    ) -> str:
        """Construct the endpoint for editing a specific issue.

        Args:
            project_id: The project name or ID.
            issue_iid: The issue IID within the project.

        Returns:
            str: The constructed endpoint.
        """
        if isinstance(project_id, str):
            project_id = project_id.replace("/", "%2F")

        return f"/projects/{project_id}/issues/{issue_iid}"

    def _edit_issue_helper(  # noqa: PLR0912, PLR0913
        self,
        project_id: int | str,
        issue_iid: int,
        add_labels: list[str] | None = None,
        assignee_ids: list[int] | None = None,
        confidential: bool | None = None,
        description: str | None = None,
        discussion_locked: bool | None = None,
        due_date: str | None = None,
        epic_id: int | None = None,
        epic_iid: int | None = None,
        issue_type: Literal["issue", "incident", "test_case", "task"] | None = None,
        labels: list[str] | None = None,
        milestone_id: int | None = None,
        remove_labels: list[str] | None = None,
        state_event: Literal["close", "reopen"] | None = None,
        title: str | None = None,
        updated_at: str | None = None,
        weight: int | None = None,
    ) -> tuple[str, dict[str, Any]]:
        """Helper method to construct endpoint and parameters for editing a specific issue.

        Args:
            project_id: The project name or ID.
            issue_iid: The issue IID within the project.
            add_labels: Labels to add.
            assignee_ids: Assignee IDs.
            confidential: Set confidentiality.
            description: Issue description.
            discussion_locked: Lock or unlock discussion.
            due_date: Due date.
            epic_id: Epic ID.
            epic_iid: Epic IID.
            issue_type: Issue type.
            labels: Labels to set.
            milestone_id: Milestone ID.
            remove_labels: Labels to remove.
            state_event: State event.
            title: Issue title.
            updated_at: Updated at timestamp.
            weight: Issue weight.

        Returns:
            tuple: A tuple containing the endpoint and parameters dictionary.
        """
        endpoint = self._edit_issue_endpoint(
            project_id=project_id,
            issue_iid=issue_iid,
        )

        payload = {}
        if add_labels is not None:
            payload["add_labels"] = ",".join(add_labels)
        if assignee_ids is not None:
            payload["assignee_ids"] = assignee_ids
        if confidential is not None:
            payload["confidential"] = confidential
        if description is not None:
            payload["description"] = description
        if discussion_locked is not None:
            payload["discussion_locked"] = discussion_locked
        if due_date is not None:
            payload["due_date"] = due_date
        if epic_id is not None:
            payload["epic_id"] = epic_id
        if epic_iid is not None:
            payload["epic_iid"] = epic_iid
        if issue_type is not None:
            payload["issue_type"] = issue_type
        if labels is not None:
            payload["labels"] = ",".join(labels)
        if milestone_id is not None:
            payload["milestone_id"] = milestone_id
        if remove_labels is not None:
            payload["remove_labels"] = ",".join(remove_labels)
        if state_event is not None:
            payload["state_event"] = state_event
        if title is not None:
            payload["title"] = title
        if updated_at is not None:
            payload["updated_at"] = updated_at
        if weight is not None:
            payload["weight"] = weight

        return endpoint, payload
