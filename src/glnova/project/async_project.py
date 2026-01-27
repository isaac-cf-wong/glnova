"""Asynchronous GitLab Project resource."""

from __future__ import annotations

from datetime import date, datetime
from typing import Any, Literal, cast

from aiohttp import ClientResponse

from glnova.project.base import BaseProject
from glnova.resource.async_resource import AsyncResource
from glnova.utils.response import process_async_response_with_last_modified


class AsyncProject(AsyncResource, BaseProject):
    """Asynchronous GitLab Project resource."""

    async def _list_projects(  # noqa: PLR0913
        self,
        user_id: int | str | None = None,
        group_id: int | str | None = None,
        archived: bool | None = None,
        id_after: int | None = None,
        id_before: int | None = None,
        imported: bool | None = None,
        include_hidden: bool | None = None,
        include_pending_delete: bool | None = None,
        last_activity_after: datetime | None = None,
        last_activity_before: datetime | None = None,
        membership: bool | None = None,
        min_access_level: Literal[5, 10, 15, 20, 30, 40, 50] | None = None,
        order_by: (
            Literal[
                "id",
                "name",
                "path",
                "created_at",
                "updated_at",
                "star_count",
                "last_activity_at",
                "similarity",
                "repository_size",
                "storage_size",
                "packages_size",
                "wiki_size",
            ]
            | None
        ) = None,
        owned: bool | None = None,
        repository_checksum_failed: bool | None = None,
        repository_storage: str | None = None,
        search_namespaces: bool | None = None,
        search: str | None = None,
        simple: bool | None = None,
        sort: Literal["asc", "desc"] | None = None,
        starred: bool | None = None,
        statistics: bool | None = None,
        topic_id: int | None = None,
        topic: list[str] | str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        visibility: Literal["private", "internal", "public"] | None = None,
        wiki_checksum_failed: bool | None = None,
        with_custom_attributes: bool | None = None,
        with_issues_enabled: bool | None = None,
        with_merge_requests_enabled: bool | None = None,
        with_programming_language: str | None = None,
        marked_for_deletion_on: date | None = None,
        active: bool | None = None,
        with_shared: bool | None = None,
        include_subgroups: bool | None = None,
        with_security_reports: bool | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> ClientResponse:
        """List projects with various filtering options.

        Args:
            user_id: The user ID or username. Defaults to None.
            group_id: The group ID or group name. Defaults to None.
            archived: Limit by archived status. Defaults to None.
            id_after: Limit by ID after. Defaults to None.
            id_before: Limit by ID before. Defaults to None.
            imported: Limit by imported status. Defaults to None.
            include_hidden: Include hidden projects. Defaults to None.
            include_pending_delete: Include pending delete projects. Defaults to None.
            last_activity_after: Limit by last activity after. Defaults to None.
            last_activity_before: Limit by last activity before. Defaults to None.
            membership: Limit by membership status. Defaults to None.
            min_access_level: Minimum access level. Defaults to None.
            order_by: Order by field. Defaults to None.
            owned: Limit by owned status. Defaults to None.
            repository_checksum_failed: Limit by repository checksum failed status. Defaults to None.
            repository_storage: Repository storage name. Defaults to None.
            search_namespaces: Search in namespaces. Defaults to None.
            search: Search term. Defaults to None.
            simple: Simple response format. Defaults to None.
            sort: Sort order. Defaults to None.
            starred: Limit by starred status. Defaults to None.
            statistics: Include statistics. Defaults to None.
            topic_id: Limit by topic ID. Defaults to None.
            topic: Limit by topics. Defaults to None.
            updated_after: Limit by updated after. Defaults to None.
            updated_before: Limit by updated before. Defaults to None.
            visibility: Limit by visibility level. Defaults to None.
            wiki_checksum_failed: Limit by wiki checksum failed status. Defaults to None.
            with_custom_attributes: Include custom attributes. Defaults to None.
            with_issues_enabled: Include projects with issues enabled. Defaults to None.
            with_merge_requests_enabled: Include projects with merge requests enabled. Defaults to None.
            with_programming_language: Limit by programming language. Defaults to None.
            marked_for_deletion_on: Limit by marked for deletion date. Defaults to None.
            active: Limit by active status. Defaults to None.
            with_shared: Include shared projects (for group projects). Defaults to None.
            include_subgroups: Include subgroup projects (for group projects). Defaults to None.
            with_security_reports: Include security reports (for group projects). Defaults to None.
            etag: ETag for caching. Defaults to None.
            **kwargs: Additional keyword arguments.

        Returns:
            A ClientResponse object containing the server's response to the HTTP request.

        """
        endpoint, params = self._list_projects_helper(
            user_id=user_id,
            group_id=group_id,
            archived=archived,
            id_after=id_after,
            id_before=id_before,
            imported=imported,
            include_hidden=include_hidden,
            include_pending_delete=include_pending_delete,
            last_activity_after=last_activity_after,
            last_activity_before=last_activity_before,
            membership=membership,
            min_access_level=min_access_level,
            order_by=order_by,
            owned=owned,
            repository_checksum_failed=repository_checksum_failed,
            repository_storage=repository_storage,
            search_namespaces=search_namespaces,
            search=search,
            simple=simple,
            sort=sort,
            starred=starred,
            statistics=statistics,
            topic_id=topic_id,
            topic=topic,
            updated_after=updated_after,
            updated_before=updated_before,
            visibility=visibility,
            wiki_checksum_failed=wiki_checksum_failed,
            with_custom_attributes=with_custom_attributes,
            with_issues_enabled=with_issues_enabled,
            with_merge_requests_enabled=with_merge_requests_enabled,
            with_programming_language=with_programming_language,
            marked_for_deletion_on=marked_for_deletion_on,
            active=active,
            with_shared=with_shared,
            include_subgroups=include_subgroups,
            with_security_reports=with_security_reports,
        )
        return await self._get(endpoint, params=params, etag=etag, **kwargs)

    async def list_projects(  # noqa: PLR0913
        self,
        user_id: int | str | None = None,
        group_id: int | str | None = None,
        archived: bool | None = None,
        id_after: int | None = None,
        id_before: int | None = None,
        imported: bool | None = None,
        include_hidden: bool | None = None,
        include_pending_delete: bool | None = None,
        last_activity_after: datetime | None = None,
        last_activity_before: datetime | None = None,
        membership: bool | None = None,
        min_access_level: Literal[5, 10, 15, 20, 30, 40, 50] | None = None,
        order_by: (
            Literal[
                "id",
                "name",
                "path",
                "created_at",
                "updated_at",
                "star_count",
                "last_activity_at",
                "similarity",
                "repository_size",
                "storage_size",
                "packages_size",
                "wiki_size",
            ]
            | None
        ) = None,
        owned: bool | None = None,
        repository_checksum_failed: bool | None = None,
        repository_storage: str | None = None,
        search_namespaces: bool | None = None,
        search: str | None = None,
        simple: bool | None = None,
        sort: Literal["asc", "desc"] | None = None,
        starred: bool | None = None,
        statistics: bool | None = None,
        topic_id: int | None = None,
        topic: list[str] | str | None = None,
        updated_after: datetime | None = None,
        updated_before: datetime | None = None,
        visibility: Literal["private", "internal", "public"] | None = None,
        wiki_checksum_failed: bool | None = None,
        with_custom_attributes: bool | None = None,
        with_issues_enabled: bool | None = None,
        with_merge_requests_enabled: bool | None = None,
        with_programming_language: str | None = None,
        marked_for_deletion_on: date | None = None,
        active: bool | None = None,
        with_shared: bool | None = None,
        include_subgroups: bool | None = None,
        with_security_reports: bool | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> tuple[list[dict[str, Any]], int, str | None]:
        """List projects with various filtering options.

        Args:
            user_id: The user ID or username. Defaults to None.
            group_id: The group ID or group name. Defaults to None.
            archived: Limit by archived status. Defaults to None.
            id_after: Limit by ID after. Defaults to None.
            id_before: Limit by ID before. Defaults to None.
            imported: Limit by imported status. Defaults to None.
            include_hidden: Include hidden projects. Defaults to None.
            include_pending_delete: Include pending delete projects. Defaults to None.
            last_activity_after: Limit by last activity after. Defaults to None.
            last_activity_before: Limit by last activity before. Defaults to None.
            membership: Limit by membership status. Defaults to None.
            min_access_level: Minimum access level. Defaults to None.
            order_by: Order by field. Defaults to None.
            owned: Limit by owned status. Defaults to None.
            repository_checksum_failed: Limit by repository checksum failed status. Defaults to None.
            repository_storage: Repository storage name. Defaults to None.
            search_namespaces: Search in namespaces. Defaults to None.
            search: Search term. Defaults to None.
            simple: Simple response format. Defaults to None.
            sort: Sort order. Defaults to None.
            starred: Limit by starred status. Defaults to None.
            statistics: Include statistics. Defaults to None.
            topic_id: Limit by topic ID. Defaults to None.
            topic: Limit by topics. Defaults to None.
            updated_after: Limit by updated after. Defaults to None.
            updated_before: Limit by updated before. Defaults to None.
            visibility: Limit by visibility level. Defaults to None.
            wiki_checksum_failed: Limit by wiki checksum failed status. Defaults to None.
            with_custom_attributes: Include custom attributes. Defaults to None.
            with_issues_enabled: Include projects with issues enabled. Defaults to None.
            with_merge_requests_enabled: Include projects with merge requests enabled. Defaults to None.
            with_programming_language: Limit by programming language. Defaults to None.
            marked_for_deletion_on: Limit by marked for deletion date. Defaults to None.
            active: Limit by active status. Defaults to None.
            with_shared: Include shared projects (for group projects). Defaults to None.
            include_subgroups: Include subgroup projects (for group projects). Defaults to None.
            with_security_reports: Include security reports (for group projects). Defaults to None.
            etag: ETag for caching. Defaults to None.
            **kwargs: Additional keyword arguments.

        Returns:
            A tuple containing:

                - A list of dictionaries representing the projects.
                - The HTTP status code of the response.
                - The ETag of the response, if available.

        """
        response = await self._list_projects(
            user_id=user_id,
            group_id=group_id,
            archived=archived,
            id_after=id_after,
            id_before=id_before,
            imported=imported,
            include_hidden=include_hidden,
            include_pending_delete=include_pending_delete,
            last_activity_after=last_activity_after,
            last_activity_before=last_activity_before,
            membership=membership,
            min_access_level=min_access_level,
            order_by=order_by,
            owned=owned,
            repository_checksum_failed=repository_checksum_failed,
            repository_storage=repository_storage,
            search_namespaces=search_namespaces,
            search=search,
            simple=simple,
            sort=sort,
            starred=starred,
            statistics=statistics,
            topic_id=topic_id,
            topic=topic,
            updated_after=updated_after,
            updated_before=updated_before,
            visibility=visibility,
            wiki_checksum_failed=wiki_checksum_failed,
            with_custom_attributes=with_custom_attributes,
            with_issues_enabled=with_issues_enabled,
            with_merge_requests_enabled=with_merge_requests_enabled,
            with_programming_language=with_programming_language,
            marked_for_deletion_on=marked_for_deletion_on,
            active=active,
            with_shared=with_shared,
            include_subgroups=include_subgroups,
            with_security_reports=with_security_reports,
        )
        data, status_code, etag = await process_async_response_with_last_modified(response)
        return cast(list[dict[str, Any]], data), status_code, etag
