"""GitLab Asynchronous Merge Request resource."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal, cast

from aiohttp import ClientResponse

from glnova.merge_request.base import BaseMergeRequest
from glnova.resource.async_resource import AsyncResource
from glnova.utils.response import process_async_response_with_last_modified


class AsyncMergeRequest(BaseMergeRequest, AsyncResource):
    """GitLab Asynchronous Merge Request resource class."""

    async def _list_merge_requests(  # noqa: PLR0913
        self,
        project_id: int | str | None = None,
        group_id: int | str | None = None,
        approved: Literal["yes", "no"] | None = None,
        approved_by_ids: list[int] | Literal["None", "Any"] | None = None,
        approved_by_usernames: list[str] | Literal["None", "Any"] | None = None,
        approver_ids: list[int] | Literal["None", "Any"] | None = None,
        assignee_id: int | Literal["None", "Any"] | None = None,
        assignee_username: list[str] | None = None,
        author_id: int | Literal["None", "Any"] | None = None,
        author_username: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        deployed_after: datetime | None = None,
        deployed_before: datetime | None = None,
        environment: str | None = None,
        iids: list[int] | None = None,
        search_in: list[Literal["title", "description"]] | None = None,
        labels: list[str] | Literal["None", "Any"] | None = None,
        merge_user_id: int | None = None,
        merge_user_username: str | None = None,
        milestone: str | Literal["None", "Any"] | None = None,
        my_reaction_emoji: str | Literal["None", "Any"] | None = None,
        non_archived: bool | None = None,
        not_match: (
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
            | None
        ) = None,
        order_by: Literal["created_at", "title", "merged_at", "updated_at"] | None = None,
        page: int = 1,
        per_page: int = 20,
        render_html: bool | None = None,
        reviewer_id: int | Literal["None", "Any"] | None = None,
        reviewer_username: str | Literal["None", "Any"] | None = None,
        scope: Literal["created_by_me", "assigned_to_me", "reviews_for_me", "all"] | None = None,
        search: str | None = None,
        sort: Literal["asc", "desc"] | None = None,
        source_branch: str | None = None,
        source_project_id: int | None = None,
        state: Literal["all", "opened", "closed", "locked", "merged"] | None = None,
        target_branch: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        view: str | None = None,
        with_labels_details: bool | None = None,
        with_merge_status_recheck: bool | None = None,
        wip: Literal["yes", "no"] | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> ClientResponse:
        """List merge requests with various filtering options.

        Args:
            project_id: The project ID or name to filter merge requests.
            group_id: The group ID or name to filter merge requests.
            approved: Filter by approval status.
            approved_by_ids: Filter by approver IDs.
            approved_by_usernames: Filter by approver usernames.
            approver_ids: Filter by approver IDs.
            assignee_id: Filter by assignee ID.
            assignee_username: Filter by assignee usernames.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            deployed_after: Filter by deployment date after this datetime.
            deployed_before: Filter by deployment date before this datetime.
            environment: Filter by environment name.
            iids: Filter by list of merge request IIDs.
            search_in: Fields to search in (title, description).
            labels: Filter by labels.
            merge_user_id: Filter by user who merged the MR.
            merge_user_username: Filter by username of the user who merged the MR.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            non_archived: Whether to include non-archived MRs only.
            not_match: Exclude MRs matching certain criteria.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page.
            render_html: Whether to render HTML in descriptions.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term to filter merge requests.
            sort: Sort order (asc or desc).
            source_branch: Filter by source branch name.
            source_project_id: Filter by source project ID.
            state: State of the merge requests to filter by.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View mode for the response.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.
            wip: Filter by work-in-progress status.
            etag: ETag for conditional requests.
            **kwargs: Additional arguments.

        Returns:
            A ClientResponse object from the API request.

        """
        endpoint, params = self._list_merge_requests_helper(
            project_id=project_id,
            group_id=group_id,
            approved=approved,
            approved_by_ids=approved_by_ids,
            approved_by_usernames=approved_by_usernames,
            approver_ids=approver_ids,
            assignee_id=assignee_id,
            assignee_username=assignee_username,
            author_id=author_id,
            author_username=author_username,
            created_after=created_after,
            created_before=created_before,
            deployed_after=deployed_after,
            deployed_before=deployed_before,
            environment=environment,
            iids=iids,
            search_in=search_in,
            labels=labels,
            merge_user_id=merge_user_id,
            merge_user_username=merge_user_username,
            milestone=milestone,
            my_reaction_emoji=my_reaction_emoji,
            non_archived=non_archived,
            not_match=not_match,
            order_by=order_by,
            page=page,
            per_page=per_page,
            render_html=render_html,
            reviewer_id=reviewer_id,
            reviewer_username=reviewer_username,
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
        )

        return await self._get(endpoint=endpoint, params=params, etag=etag, **kwargs)

    async def list_merge_requests(  # noqa: PLR0913
        self,
        project_id: int | str | None = None,
        group_id: int | str | None = None,
        approved: Literal["yes", "no"] | None = None,
        approved_by_ids: list[int] | Literal["None", "Any"] | None = None,
        approved_by_usernames: list[str] | Literal["None", "Any"] | None = None,
        approver_ids: list[int] | Literal["None", "Any"] | None = None,
        assignee_id: int | Literal["None", "Any"] | None = None,
        assignee_username: list[str] | None = None,
        author_id: int | Literal["None", "Any"] | None = None,
        author_username: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        deployed_after: datetime | None = None,
        deployed_before: datetime | None = None,
        environment: str | None = None,
        iids: list[int] | None = None,
        search_in: list[Literal["title", "description"]] | None = None,
        labels: list[str] | Literal["None", "Any"] | None = None,
        merge_user_id: int | None = None,
        merge_user_username: str | None = None,
        milestone: str | Literal["None", "Any"] | None = None,
        my_reaction_emoji: str | Literal["None", "Any"] | None = None,
        non_archived: bool | None = None,
        not_match: (
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
            | None
        ) = None,
        order_by: Literal["created_at", "title", "merged_at", "updated_at"] | None = None,
        page: int = 1,
        per_page: int = 20,
        render_html: bool | None = None,
        reviewer_id: int | Literal["None", "Any"] | None = None,
        reviewer_username: str | Literal["None", "Any"] | None = None,
        scope: Literal["created_by_me", "assigned_to_me", "reviews_for_me", "all"] | None = None,
        search: str | None = None,
        sort: Literal["asc", "desc"] | None = None,
        source_branch: str | None = None,
        source_project_id: int | None = None,
        state: Literal["all", "opened", "closed", "locked", "merged"] | None = None,
        target_branch: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        view: str | None = None,
        with_labels_details: bool | None = None,
        with_merge_status_recheck: bool | None = None,
        wip: Literal["yes", "no"] | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> tuple[list[dict[str, Any]], dict[str, Any]]:
        """List merge requests with various filtering options.

        Args:
            project_id: The project ID or name to filter merge requests.
            group_id: The group ID or name to filter merge requests.
            approved: Filter by approval status.
            approved_by_ids: Filter by approver IDs.
            approved_by_usernames: Filter by approver usernames.
            approver_ids: Filter by approver IDs.
            assignee_id: Filter by assignee ID.
            assignee_username: Filter by assignee usernames.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            deployed_after: Filter by deployment date after this datetime.
            deployed_before: Filter by deployment date before this datetime.
            environment: Filter by environment name.
            iids: Filter by list of merge request IIDs.
            search_in: Fields to search in (title, description).
            labels: Filter by labels.
            merge_user_id: Filter by user who merged the MR.
            merge_user_username: Filter by username of the user who merged the MR.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            non_archived: Whether to include non-archived MRs only.
            not_match: Exclude MRs matching certain criteria.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page.
            render_html: Whether to render HTML in descriptions.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term to filter merge requests.
            sort: Sort order (asc or desc).
            source_branch: Filter by source branch name.
            source_project_id: Filter by source project ID.
            state: State of the merge requests to filter by.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View mode for the response.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.
            wip: Filter by work-in-progress status.
            etag: ETag for conditional requests.
            **kwargs: Additional arguments.

        Returns:
            A tuple containing a list of merge requests and a dictionary with the status code and the ETag value.

        """
        response = await self._list_merge_requests(
            project_id=project_id,
            group_id=group_id,
            approved=approved,
            approved_by_ids=approved_by_ids,
            approved_by_usernames=approved_by_usernames,
            approver_ids=approver_ids,
            assignee_id=assignee_id,
            assignee_username=assignee_username,
            author_id=author_id,
            author_username=author_username,
            created_after=created_after,
            created_before=created_before,
            deployed_after=deployed_after,
            deployed_before=deployed_before,
            environment=environment,
            iids=iids,
            search_in=search_in,
            labels=labels,
            merge_user_id=merge_user_id,
            merge_user_username=merge_user_username,
            milestone=milestone,
            my_reaction_emoji=my_reaction_emoji,
            non_archived=non_archived,
            not_match=not_match,
            order_by=order_by,
            page=page,
            per_page=per_page,
            render_html=render_html,
            reviewer_id=reviewer_id,
            reviewer_username=reviewer_username,
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
            **kwargs,
        )
        data, status_code, etag_value = await process_async_response_with_last_modified(response)
        return cast(list[dict[str, Any]], data), {"status_code": status_code, "etag": etag_value}
