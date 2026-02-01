"""List command for project CLI."""

from __future__ import annotations

from datetime import date, datetime
from typing import Annotated, Literal

import typer


def list_command(  # noqa: PLR0913
    ctx: typer.Context,
    user_id: Annotated[
        str | None,
        typer.Option(
            "--user-id",
            help="Filter projects by user ID or username.",
        ),
    ] = None,
    group_id: Annotated[
        str | None,
        typer.Option(
            "--group-id",
            help="Filter projects by group ID or name.",
        ),
    ] = None,
    archived: Annotated[
        bool | None,
        typer.Option(
            "--archived/--no-archived",
            help="Filter projects by archived status.",
        ),
    ] = None,
    id_after: Annotated[
        int | None,
        typer.Option(
            "--id-after",
            help="Return projects with IDs greater than the specified value.",
        ),
    ] = None,
    id_before: Annotated[
        int | None,
        typer.Option(
            "--id-before",
            help="Return projects with IDs less than the specified value.",
        ),
    ] = None,
    imported: Annotated[
        bool | None,
        typer.Option(
            "--imported/--no-imported",
            help="Filter projects by import status.",
        ),
    ] = None,
    include_hidden: Annotated[
        bool,
        typer.Option(
            "--include-hidden/--no-include-hidden",
            help="Include hidden projects in the results.",
        ),
    ] = False,
    include_pending_delete: Annotated[
        bool,
        typer.Option(
            "--include-pending-delete/--no-include-pending-delete",
            help="Include projects pending deletion in the results.",
        ),
    ] = False,
    last_activity_after: Annotated[
        datetime | None,
        typer.Option(
            "--last-activity-after",
            help="Return projects with last activity after the specified datetime (ISO 8601 format).",
        ),
    ] = None,
    last_activity_before: Annotated[
        datetime | None,
        typer.Option(
            "--last-activity-before",
            help="Return projects with last activity before the specified datetime (ISO 8601 format).",
        ),
    ] = None,
    membership: Annotated[
        bool | None,
        typer.Option(
            "--membership/--no-membership",
            help="Limit results to projects the current user is a member of.",
        ),
    ] = None,
    min_access_level: Annotated[
        Literal[5, 10, 15, 20, 30, 40, 50] | None,
        typer.Option(
            "--min-access-level",
            help="Minimum access level for the current user on the projects.",
        ),
    ] = None,
    order_by: Annotated[
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
        | None,
        typer.Option(
            "--order-by",
            help="Field to order projects by.",
        ),
    ] = None,
    owned: Annotated[
        bool | None,
        typer.Option(
            "--owned/--no-owned",
            help="Limit results to projects owned by the current user.",
        ),
    ] = None,
    repository_checksum_failed: Annotated[
        bool | None,
        typer.Option(
            "--repository-checksum-failed/--no-repository-checksum-failed",
            help="Filter projects by repository checksum status.",
        ),
    ] = None,
    repository_storage: Annotated[
        str | None,
        typer.Option(
            "--repository-storage",
            help="Filter projects by repository storage name.",
        ),
    ] = None,
    search_namespaces: Annotated[
        bool | None,
        typer.Option(
            "--search-namespaces/--no-search-namespaces",
            help="Search within project namespaces.",
        ),
    ] = None,
    search: Annotated[
        str | None,
        typer.Option(
            "--search",
            help="Search term to filter projects by name or description.",
        ),
    ] = None,
    simple: Annotated[
        bool | None,
        typer.Option(
            "--simple/--no-simple",
            help="Return only the ID, name, and path of each project.",
        ),
    ] = None,
    sort: Annotated[
        Literal["asc", "desc"] | None,
        typer.Option(
            "--sort",
            help="Sort order of the projects.",
        ),
    ] = None,
    starred: Annotated[
        bool | None,
        typer.Option(
            "--starred/--no-starred",
            help="Limit results to starred projects.",
        ),
    ] = None,
    statistics: Annotated[
        bool,
        typer.Option(
            "--statistics/--no-statistics",
            help="Include project statistics in the results.",
        ),
    ] = False,
    topic_id: Annotated[
        int | None,
        typer.Option(
            "--topic-id",
            help="Filter projects by topic ID.",
        ),
    ] = None,
    topic: Annotated[
        list[str] | None,
        typer.Option(
            "--topic",
            help="Filter projects by topic name. Repeat --topic for multiple values.",
        ),
    ] = None,
    updated_after: Annotated[
        datetime | None,
        typer.Option(
            "--updated-after",
            help="Return projects updated after the specified datetime (ISO 8601 format).",
        ),
    ] = None,
    updated_before: Annotated[
        datetime | None,
        typer.Option(
            "--updated-before",
            help="Return projects updated before the specified datetime (ISO 8601 format).",
        ),
    ] = None,
    visibility: Annotated[
        Literal["private", "internal", "public"] | None,
        typer.Option(
            "--visibility",
            help="Filter projects by visibility level.",
        ),
    ] = None,
    wiki_checksum_failed: Annotated[
        bool | None,
        typer.Option(
            "--wiki-checksum-failed/--no-wiki-checksum-failed",
            help="Filter projects by wiki checksum status.",
        ),
    ] = None,
    with_custom_attributes: Annotated[
        bool | None,
        typer.Option(
            "--with-custom-attributes/--no-with-custom-attributes",
            help="Include custom attributes in the results.",
        ),
    ] = None,
    with_issues_enabled: Annotated[
        bool | None,
        typer.Option(
            "--with-issues-enabled/--no-with-issues-enabled",
            help="Filter projects by whether issues are enabled.",
        ),
    ] = None,
    with_merge_requests_enabled: Annotated[
        bool | None,
        typer.Option(
            "--with-merge-requests-enabled/--no-with-merge-requests-enabled",
            help="Filter projects by whether merge requests are enabled.",
        ),
    ] = None,
    with_programming_language: Annotated[
        str | None,
        typer.Option(
            "--with-programming-language",
            help="Filter projects by primary programming language.",
        ),
    ] = None,
    marked_for_deletion_on: Annotated[
        str | None,
        typer.Option(
            "--marked-for-deletion-on",
            help="Return projects marked for deletion on the specified date (YYYY-MM-DD format).",
        ),
    ] = None,
    active: Annotated[
        bool | None,
        typer.Option(
            "--active/--no-active",
            help="Filter projects by active status.",
        ),
    ] = None,
    with_shared: Annotated[
        bool | None,
        typer.Option(
            "--with-shared/--no-with-shared",
            help="Include projects shared with groups.",
        ),
    ] = None,
    include_subgroups: Annotated[
        bool | None,
        typer.Option(
            "--include-subgroups/--no-include-subgroups",
            help="Include projects from subgroups when filtering by group ID.",
        ),
    ] = None,
    with_security_reports: Annotated[
        bool | None,
        typer.Option(
            "--with-security-reports/--no-with-security-reports",
            help="Include security reports in the results.",
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
    """List projects.

    Args:
        ctx: Typer context.
        user_id: Filter projects by user ID or username.
        group_id: Filter projects by group ID or name.
        archived: Filter projects by archived status.
        id_after: Return projects with IDs greater than the specified value.
        id_before: Return projects with IDs less than the specified value.
        imported: Filter projects by import status.
        include_hidden: Include hidden projects in the results.
        include_pending_delete: Include projects pending deletion in the results.
        last_activity_after: Return projects with last activity after the specified datetime (ISO 8601 format).
        last_activity_before: Return projects with last activity before the specified datetime (ISO 8601 format).
        membership: Limit results to projects the current user is a member of.
        min_access_level: Minimum access level for the current user on the projects.
        order_by: Field to order projects by.
        owned: Limit results to projects owned by the current user.
        repository_checksum_failed: Filter projects by repository checksum status.
        repository_storage: Filter projects by repository storage name.
        search_namespaces: Search within project namespaces.
        search: Search term to filter projects by name or description.
        simple: Return only the ID, name, and path of each project.
        sort: Sort order of the projects.
        starred: Limit results to starred projects.
        statistics: Include project statistics in the results.
        topic_id: Filter projects by topic ID.
        topic: Filter projects by topic name. Repeat --topic for multiple values.
        updated_after: Return projects updated after the specified datetime (ISO 8601 format).
        updated_before: Return projects updated before the specified datetime (ISO 8601 format).
        visibility: Filter projects by visibility level.
        wiki_checksum_failed: Filter projects by wiki checksum status.
        with_custom_attributes: Include custom attributes in the results.
        with_issues_enabled: Filter projects by whether issues are enabled.
        with_merge_requests_enabled: Filter projects by whether merge requests are enabled.
        with_programming_language: Filter projects by primary programming language.
        marked_for_deletion_on: Return projects marked for deletion on the specified date (YYYY-MM-DD format).
        active: Filter projects by active status.
        with_shared: Include projects shared with groups.
        include_subgroups: Include projects from subgroups when filtering by group ID.
        with_security_reports: Include security reports in the results.
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

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    try:
        with GitLab(token=token, base_url=base_url) as client:
            data, status_code, etag_response = client.project.list_projects(
                user_id=str_to_int_or_none(user_id),
                group_id=str_to_int_or_none(group_id),
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
                marked_for_deletion_on=date.fromisoformat(marked_for_deletion_on) if marked_for_deletion_on else None,
                active=active,
                with_shared=with_shared,
                include_subgroups=include_subgroups,
                with_security_reports=with_security_reports,
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
        logger.error("Error listing projects: %s", e)
        raise typer.Exit(code=1) from e
