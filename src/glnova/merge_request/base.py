"""Base class for GitLab merge requests."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal


class BaseMergeRequest:
    """Base class for GitLab merge requests."""

    def _list_merge_requests_endpoint(
        self, project_id: int | str | None, group_id: int | str | None
    ) -> tuple[str, str]:
        """Get the API endpoint for listing merge requests.

        If a project_id is provided, the endpoint will list merge requests for that project.
        If a group_id is provided, the endpoint will list merge requests for that group.
        If neither is provided, the endpoint will list all merge requests accessible to the user.

        Args:
            project_id: The project ID or name.
            group_id: The group ID or name.

        Returns:
            A tuple containing the API endpoint and the type of listing ("project", "group", or "user").

        """
        if project_id is not None:
            if isinstance(project_id, str):
                project_id = project_id.replace("/", "%2F")
            return f"/projects/{project_id}/merge_requests", "project"

        if group_id is not None:
            if isinstance(group_id, str):
                group_id = group_id.replace("/", "%2F")
            return f"/groups/{group_id}/merge_requests", "group"

        return "/merge_requests", "user"

    def _list_user_merge_requests_params(  # noqa: PLR0912, PLR0913, PLR0915
        self,
        approved_by_ids: list[int] | Literal["None", "Any"] | None = None,
        approver_ids: list[int] | Literal["None", "Any"] | None = None,
        assignee_id: int | Literal["None", "Any"] | None = None,
        author_id: int | Literal["None", "Any"] | None = None,
        author_username: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        deployed_after: datetime | None = None,
        deployed_before: datetime | None = None,
        environment: str | None = None,
        search_in: list[Literal["title", "description"]] | None = None,
        labels: list[str] | Literal["None", "Any"] | None = None,
        merge_user_id: int | None = None,
        merge_user_username: str | None = None,
        milestone: str | Literal["None", "Any"] | None = None,
        my_reaction_emoji: str | Literal["None", "Any"] | None = None,
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
        state: Literal["all", "opened", "closed", "locked", "merged"] | None = None,
        target_branch: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        view: str | None = None,
        with_labels_details: bool | None = None,
        with_merge_status_recheck: bool | None = None,
        wip: Literal["yes", "no"] | None = None,
    ) -> dict[str, Any]:
        """Return parameters for listing user merge requests.

        Args:
            approved_by_ids: Filter by IDs of users who approved the merge requests.
            approver_ids: Filter by IDs of users who can approve the merge requests.
            assignee_id: Filter by assignee ID.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            deployed_after: Filter by deployment date after this datetime.
            deployed_before: Filter by deployment date before this datetime.
            environment: Filter by environment name.
            search_in: Fields to search in (title, description).
            labels: Filter by labels.
            merge_user_id: Filter by user ID who merged the requests.
            merge_user_username: Filter by username who merged the requests.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            not_match: Exclude certain filters.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            render_html: Whether to render HTML in responses.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term.
            sort: Sort order (asc, desc).
            source_branch: Filter by source branch name.
            state: State of the merge requests.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View type for the response.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.
            wip: Filter by work-in-progress status.

        """
        params: dict[str, Any] = {}

        if approved_by_ids is not None:
            params["approved_by_ids"] = approved_by_ids
        if approver_ids is not None:
            params["approver_ids"] = approver_ids
        if assignee_id is not None:
            params["assignee_id"] = assignee_id
        if author_id is not None:
            params["author_id"] = author_id
        if author_username is not None:
            params["author_username"] = author_username
        if created_after is not None:
            params["created_after"] = created_after.isoformat()
        if created_before is not None:
            params["created_before"] = created_before.isoformat()
        if deployed_after is not None:
            params["deployed_after"] = deployed_after.isoformat()
        if deployed_before is not None:
            params["deployed_before"] = deployed_before.isoformat()
        if environment is not None:
            params["environment"] = environment
        if search_in is not None:
            params["search_in"] = ",".join(search_in)
        if labels is not None:
            params["labels"] = ",".join(labels) if isinstance(labels, list) else labels
        if merge_user_id is not None:
            params["merge_user_id"] = merge_user_id
        if merge_user_username is not None:
            params["merge_user_username"] = merge_user_username
        if milestone is not None:
            params["milestone"] = milestone
        if my_reaction_emoji is not None:
            params["my_reaction_emoji"] = my_reaction_emoji
        if not_match is not None:
            params["not"] = not_match
        if order_by is not None:
            params["order_by"] = order_by
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if render_html is not None:
            params["render_html"] = render_html
        if reviewer_id is not None:
            params["reviewer_id"] = reviewer_id
        if reviewer_username is not None:
            params["reviewer_username"] = reviewer_username
        if scope is not None:
            params["scope"] = scope
        if search is not None:
            params["search"] = search
        if sort is not None:
            params["sort"] = sort
        if source_branch is not None:
            params["source_branch"] = source_branch
        if state is not None:
            params["state"] = state
        if target_branch is not None:
            params["target_branch"] = target_branch
        if updated_after is not None:
            params["updated_after"] = updated_after.isoformat()
        if updated_before is not None:
            params["updated_before"] = updated_before.isoformat()
        if view is not None:
            params["view"] = view
        if with_labels_details is not None:
            params["with_labels_details"] = with_labels_details
        if with_merge_status_recheck is not None:
            params["with_merge_status_recheck"] = with_merge_status_recheck
        if wip is not None:
            params["wip"] = wip

        return params

    def _list_project_merge_requests_params(  # noqa: PLR0912, PLR0913, PLR0915
        self,
        approved_by_ids: list[int] | Literal["None", "Any"] | None = None,
        approver_ids: list[int] | Literal["None", "Any"] | None = None,
        assignee_id: int | Literal["None", "Any"] | None = None,
        author_id: int | Literal["None", "Any"] | None = None,
        author_username: str | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        environment: str | None = None,
        iids: list[int] | None = None,
        labels: list[str] | Literal["None", "Any"] | None = None,
        merge_user_id: int | None = None,
        merge_user_username: str | None = None,
        milestone: str | Literal["None", "Any"] | None = None,
        my_reaction_emoji: str | Literal["None", "Any"] | None = None,
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
        order_by: Literal["created_at", "merged_at", "title", "updated_at"] | None = None,
        page: int = 1,
        per_page: int = 20,
        reviewer_id: int | Literal["None", "Any"] | None = None,
        reviewer_username: str | Literal["None", "Any"] | None = None,
        scope: Literal["created_by_me", "assigned_to_me", "reviews_for_me", "all"] | None = None,
        search: str | None = None,
        sort: Literal["asc", "desc"] | None = None,
        source_branch: str | None = None,
        state: Literal["all", "opened", "closed", "locked", "merged"] | None = None,
        target_branch: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        view: str | None = None,
        wip: Literal["yes", "no"] | None = None,
        with_labels_details: bool | None = None,
        with_merge_status_recheck: bool | None = None,
    ) -> dict[str, Any]:
        """Return parameters for listing project merge requests.

        Args:
            approved_by_ids: Filter by IDs of users who approved the merge requests.
            approver_ids: Filter by IDs of users who can approve the merge requests.
            assignee_id: Filter by assignee ID.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            environment: Filter by environment name.
            iids: Filter by merge request IIDs.
            labels: Filter by labels.
            merge_user_id: Filter by user ID who merged the requests.
            merge_user_username: Filter by username who merged the requests.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            not_match: Exclude certain filters.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term.
            sort: Sort order (asc, desc).
            source_branch: Filter by source branch name.
            state: State of the merge requests.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View type for the response.
            wip: Filter by work-in-progress status.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.

        Returns:
            Parameters dictionary for the API request.

        """
        params: dict[str, Any] = {}

        if approved_by_ids is not None:
            params["approved_by_ids"] = approved_by_ids
        if approver_ids is not None:
            params["approver_ids"] = approver_ids
        if assignee_id is not None:
            params["assignee_id"] = assignee_id
        if author_id is not None:
            params["author_id"] = author_id
        if author_username is not None:
            params["author_username"] = author_username
        if created_after is not None:
            params["created_after"] = created_after.isoformat()
        if created_before is not None:
            params["created_before"] = created_before.isoformat()
        if environment is not None:
            params["environment"] = environment
        if iids is not None:
            params["iids"] = ",".join(str(iid) for iid in iids)
        if labels is not None:
            params["labels"] = ",".join(labels) if isinstance(labels, list) else labels
        if merge_user_id is not None:
            params["merge_user_id"] = merge_user_id
        if merge_user_username is not None:
            params["merge_user_username"] = merge_user_username
        if milestone is not None:
            params["milestone"] = milestone
        if my_reaction_emoji is not None:
            params["my_reaction_emoji"] = my_reaction_emoji
        if not_match is not None:
            params["not"] = not_match
        if order_by is not None:
            params["order_by"] = order_by
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if reviewer_id is not None:
            params["reviewer_id"] = reviewer_id
        if reviewer_username is not None:
            params["reviewer_username"] = reviewer_username
        if scope is not None:
            params["scope"] = scope
        if search is not None:
            params["search"] = search
        if sort is not None:
            params["sort"] = sort
        if source_branch is not None:
            params["source_branch"] = source_branch
        if state is not None:
            params["state"] = state
        if target_branch is not None:
            params["target_branch"] = target_branch
        if updated_after is not None:
            params["updated_after"] = updated_after.isoformat()
        if updated_before is not None:
            params["updated_before"] = updated_before.isoformat()
        if view is not None:
            params["view"] = view
        if wip is not None:
            params["wip"] = wip
        if with_labels_details is not None:
            params["with_labels_details"] = with_labels_details
        if with_merge_status_recheck is not None:
            params["with_merge_status_recheck"] = with_merge_status_recheck

        return params

    def _list_group_merge_requests_params(  # noqa: PLR0912, PLR0913, PLR0915
        self,
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
        order_by: (
            Literal[
                "created_at",
                "label_priority",
                "merged_at",
                "milestone_due",
                "popularity",
                "priority",
                "title",
                "updated_at",
            ]
            | None
        ) = None,
        page: int = 1,
        per_page: int = 20,
        reviewer_id: int | Literal["None", "Any"] | None = None,
        reviewer_username: str | Literal["None", "Any"] | None = None,
        scope: Literal["created_by_me", "assigned_to_me", "reviews_for_me", "all"] | None = None,
        search: str | None = None,
        source_branch: str | None = None,
        source_project_id: int | None = None,
        sort: Literal["asc", "desc"] | None = None,
        state: Literal["all", "opened", "closed", "locked", "merged"] | None = None,
        target_branch: str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        view: str | None = None,
        with_labels_details: bool | None = None,
        with_merge_status_recheck: bool | None = None,
        wip: Literal["yes", "no"] | None = None,
    ) -> dict[str, Any]:
        """Return parameters for listing group merge requests.

        Args:
            approved: Filter by approval status.
            approved_by_ids: Filter by IDs of users who approved the merge requests.
            approved_by_usernames: Filter by usernames of users who approved the merge requests.
            approver_ids: Filter by IDs of users who can approve the merge requests.
            assignee_id: Filter by assignee ID.
            assignee_username: Filter by assignee username.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            deployed_after: Filter by deployment date after this datetime.
            deployed_before: Filter by deployment date before this datetime.
            environment: Filter by environment name.
            search_in: Fields to search in (title, description).
            labels: Filter by labels.
            merge_user_id: Filter by user ID who merged the requests.
            merge_user_username: Filter by username who merged the requests.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            non_archived: Whether to include only non-archived projects.
            not_match: Exclude certain filters.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term.
            source_branch: Filter by source branch name.
            source_project_id: Filter by source project ID.
            sort: Sort order (asc, desc).
            state: State of the merge requests.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View type for the response.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.
            wip: Filter by work-in-progress status.

        Returns:
            Parameters dictionary for the API request.

        """
        params: dict[str, Any] = {}

        if approved is not None:
            params["approved"] = approved
        if approved_by_ids is not None:
            params["approved_by_ids"] = approved_by_ids
        if approved_by_usernames is not None:
            params["approved_by_usernames"] = (
                ",".join(approved_by_usernames) if isinstance(approved_by_usernames, list) else approved_by_usernames
            )
        if approver_ids is not None:
            params["approver_ids"] = approver_ids
        if assignee_id is not None:
            params["assignee_id"] = assignee_id
        if assignee_username is not None:
            params["assignee_username"] = (
                ",".join(assignee_username) if isinstance(assignee_username, list) else assignee_username
            )
        if author_id is not None:
            params["author_id"] = author_id
        if author_username is not None:
            params["author_username"] = author_username
        if created_after is not None:
            params["created_after"] = created_after.isoformat()
        if created_before is not None:
            params["created_before"] = created_before.isoformat()
        if deployed_after is not None:
            params["deployed_after"] = deployed_after.isoformat()
        if deployed_before is not None:
            params["deployed_before"] = deployed_before.isoformat()
        if environment is not None:
            params["environment"] = environment
        if search_in is not None:
            params["in"] = ",".join(search_in)
        if labels is not None:
            params["labels"] = ",".join(labels) if isinstance(labels, list) else labels
        if merge_user_id is not None:
            params["merge_user_id"] = merge_user_id
        if merge_user_username is not None:
            params["merge_user_username"] = merge_user_username
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
        params["page"] = page
        params["per_page"] = per_page
        if reviewer_id is not None:
            params["reviewer_id"] = reviewer_id
        if reviewer_username is not None:
            params["reviewer_username"] = reviewer_username
        if scope is not None:
            params["scope"] = scope
        if search is not None:
            params["search"] = search
        if source_branch is not None:
            params["source_branch"] = source_branch
        if source_project_id is not None:
            params["source_project_id"] = source_project_id
        if sort is not None:
            params["sort"] = sort
        if state is not None:
            params["state"] = state
        if target_branch is not None:
            params["target_branch"] = target_branch
        if updated_after is not None:
            params["updated_after"] = updated_after.isoformat()
        if updated_before is not None:
            params["updated_before"] = updated_before.isoformat()
        if view is not None:
            params["view"] = view
        if with_labels_details is not None:
            params["with_labels_details"] = with_labels_details
        if with_merge_status_recheck is not None:
            params["with_merge_status_recheck"] = with_merge_status_recheck
        if wip is not None:
            params["wip"] = wip

        return params

    def _list_merge_requests_helper(  # noqa: PLR0913
        self,
        project_id: int | str | None,
        group_id: int | str | None,
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
    ) -> tuple[str, dict[str, Any]]:
        """Return parameters for listing merge requests based on the list type.

        Args:
            project_id: The project ID or name.
            group_id: The group ID or name.
            approved: Filter by approval status.
            approved_by_ids: Filter by IDs of users who approved the merge requests.
            approved_by_usernames: Filter by usernames of users who approved the merge requests.
            approver_ids: Filter by IDs of users who can approve the merge requests.
            assignee_id: Filter by assignee ID.
            assignee_username: Filter by assignee username.
            author_id: Filter by author ID.
            author_username: Filter by author username.
            created_after: Filter by creation date after this datetime.
            created_before: Filter by creation date before this datetime.
            deployed_after: Filter by deployment date after this datetime.
            deployed_before: Filter by deployment date before this datetime.
            environment: Filter by environment name.
            iids: Filter by merge request IIDs.
            search_in: Fields to search in (title, description).
            labels: Filter by labels.
            merge_user_id: Filter by user ID who merged the requests.
            merge_user_username: Filter by username who merged the requests.
            milestone: Filter by milestone.
            my_reaction_emoji: Filter by reaction emoji.
            non_archived: Whether to include only non-archived projects.
            not_match: Exclude certain filters.
            order_by: Field to order results by.
            page: Page number for pagination.
            per_page: Number of items per page for pagination.
            render_html: Whether to render HTML in responses.
            reviewer_id: Filter by reviewer ID.
            reviewer_username: Filter by reviewer username.
            scope: Scope of merge requests to return.
            search: Search term.
            sort: Sort order (asc, desc).
            source_branch: Filter by source branch name.
            source_project_id: Filter by source project ID.
            state: State of the merge requests.
            target_branch: Filter by target branch name.
            updated_after: Filter by update date after this datetime.
            updated_before: Filter by update date before this datetime.
            view: View type for the response.
            with_labels_details: Whether to include label details in the response.
            with_merge_status_recheck: Whether to recheck merge status.
            wip: Filter by work-in-progress status.

        Returns:
            A tuple containing the API endpoint and parameters dictionary for the API request.

        """
        endpoint, list_type = self._list_merge_requests_endpoint(
            project_id=project_id,
            group_id=group_id,
        )

        if list_type == "user":
            params = self._list_user_merge_requests_params(
                approved_by_ids=approved_by_ids,
                approver_ids=approver_ids,
                assignee_id=assignee_id,
                author_id=author_id,
                author_username=author_username,
                created_after=created_after,
                created_before=created_before,
                deployed_after=deployed_after,
                deployed_before=deployed_before,
                environment=environment,
                search_in=search_in,
                labels=labels,
                merge_user_id=merge_user_id,
                merge_user_username=merge_user_username,
                milestone=milestone,
                my_reaction_emoji=my_reaction_emoji,
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
                state=state,
                target_branch=target_branch,
                updated_after=updated_after,
                updated_before=updated_before,
                view=view,
                with_labels_details=with_labels_details,
                with_merge_status_recheck=with_merge_status_recheck,
                wip=wip,
            )
        elif list_type == "project":
            params = self._list_project_merge_requests_params(
                approved_by_ids=approved_by_ids,
                approver_ids=approver_ids,
                assignee_id=assignee_id,
                author_id=author_id,
                author_username=author_username,
                created_after=created_after,
                created_before=created_before,
                environment=environment,
                iids=iids,
                labels=labels,
                merge_user_id=merge_user_id,
                merge_user_username=merge_user_username,
                milestone=milestone,
                my_reaction_emoji=my_reaction_emoji,
                not_match=not_match,
                order_by=order_by,
                page=page,
                per_page=per_page,
                reviewer_id=reviewer_id,
                reviewer_username=reviewer_username,
                scope=scope,
                search=search,
                sort=sort,
                source_branch=source_branch,
                state=state,
                target_branch=target_branch,
                updated_after=updated_after,
                updated_before=updated_before,
                view=view,
                wip=wip,
                with_labels_details=with_labels_details,
                with_merge_status_recheck=with_merge_status_recheck,
            )
        else:  # list_type == "group"
            params = self._list_group_merge_requests_params(
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
                reviewer_id=reviewer_id,
                reviewer_username=reviewer_username,
                scope=scope,
                search=search,
                source_branch=source_branch,
                source_project_id=source_project_id,
                sort=sort,
                state=state,
                target_branch=target_branch,
                updated_after=updated_after,
                updated_before=updated_before,
                view=view,
                with_labels_details=with_labels_details,
                with_merge_status_recheck=with_merge_status_recheck,
                wip=wip,
            )
        return endpoint, params
