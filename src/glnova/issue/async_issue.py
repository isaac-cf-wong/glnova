"""Asynchronous GitLab Issue resource."""

from __future__ import annotations

from typing import Any, Literal, cast

from aiohttp import ClientResponse

from glnova.issue.base import BaseIssue
from glnova.resource.async_resource import AsyncResource
from glnova.utils.response import process_async_response_with_last_modified


class Issue(BaseIssue, AsyncResource):
    """GitLab Issue resource."""

    async def _list_issues(  # noqa: PLR0913
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
        etag: str | None = None,
        **kwargs: Any,
    ) -> ClientResponse:
        """List issues with optional filters.

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
            etag: ETag for caching.
            **kwargs: Additional keyword arguments.

        Returns:
            A ClientResponse object.
        """
        endpoint, params, kwargs = self._list_issues_helper(
            group=group,
            project=project,
            assignee_id=assignee_id,
            assignee_username=assignee_username,
            author_id=author_id,
            author_username=author_username,
            confidential=confidential,
            created_after=created_after,
            created_before=created_before,
            due_date=due_date,
            epic_id=epic_id,
            health_status=health_status,
            iids=iids,
            search_in=search_in,
            issue_type=issue_type,
            iteration_id=iteration_id,
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
            weight=weight,
            with_labels_details=with_labels_details,
            cursor=cursor,
            page=page,
            per_page=per_page,
            **kwargs,
        )
        return await self._get(endpoint=endpoint, params=params, etag=etag, **kwargs)

    async def list_issues(  # noqa: PLR0913
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
        etag: str | None = None,
        **kwargs: Any,
    ) -> tuple[list[dict[str, Any]], int, str | None]:
        """List issues with optional filters.

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
            etag: ETag for caching.
            **kwargs: Additional keyword arguments.

        Returns:
            A tuple containing a list of issues, the status code, and the ETag value.
        """
        response = await self._list_issues(
            group=group,
            project=project,
            assignee_id=assignee_id,
            assignee_username=assignee_username,
            author_id=author_id,
            author_username=author_username,
            confidential=confidential,
            created_after=created_after,
            created_before=created_before,
            due_date=due_date,
            epic_id=epic_id,
            health_status=health_status,
            iids=iids,
            search_in=search_in,
            issue_type=issue_type,
            iteration_id=iteration_id,
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
            weight=weight,
            with_labels_details=with_labels_details,
            cursor=cursor,
            page=page,
            per_page=per_page,
            etag=etag,
            **kwargs,
        )
        data, status_code, etag_value = await process_async_response_with_last_modified(response)
        return cast(list[dict[str, Any]], data), status_code, etag_value
