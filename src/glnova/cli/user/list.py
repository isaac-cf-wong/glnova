"""List command for user CLI."""

from __future__ import annotations

from datetime import datetime
from typing import Annotated, Literal

import typer


def list_command(  # noqa: PLR0913
    ctx: typer.Context,
    username: Annotated[
        str | None,
        typer.Option("--username", help="Username of the user."),
    ] = None,
    public_email: Annotated[
        str | None,
        typer.Option("--public-email", help="Public email of the user."),
    ] = None,
    search: Annotated[
        str | None,
        typer.Option("--search", help="Search term for user attributes."),
    ] = None,
    active: Annotated[
        bool | None,
        typer.Option(
            "--active/--no-active",
            help="Filter by active status. Use --active to filter active users, --no-active for inactive users.",
        ),
    ] = None,
    external: Annotated[
        bool | None,
        typer.Option(
            "--external/--no-external",
            help="Filter by external status. Use --external to filter external users, --no-external for internal users.",
        ),
    ] = None,
    blocked: Annotated[
        bool | None,
        typer.Option(
            "--blocked/--no-blocked",
            help="Filter by blocked status. Use --blocked to filter blocked users, --no-blocked for unblocked users.",
        ),
    ] = None,
    humans: Annotated[
        bool | None,
        typer.Option(
            "--humans/--no-humans",
            help="Filter by human status. Use --humans to filter human users, --no-humans for bots and other non-human accounts.",
        ),
    ] = None,
    created_after: Annotated[
        datetime | None,
        typer.Option(
            "--created-after",
            help="Filter users created after this datetime (YYYY-MM-DDTHH:MM:SS).",
        ),
    ] = None,
    created_before: Annotated[
        datetime | None,
        typer.Option(
            "--created-before",
            help="Filter users created before this datetime (YYYY-MM-DDTHH:MM:SS).",
        ),
    ] = None,
    exclude_active: Annotated[
        bool | None,
        typer.Option(
            "--exclude-active/--no-exclude-active",
            help="Exclude users based on active status. Use --exclude-active to exclude active users, --no-exclude-active to exclude inactive users.",
        ),
    ] = None,
    exclude_external: Annotated[
        bool | None,
        typer.Option(
            "--exclude-external/--no-exclude-external",
            help="Exclude users based on external status. Use --exclude-external to exclude external users, --no-exclude-external to exclude internal users.",
        ),
    ] = None,
    exclude_humans: Annotated[
        bool | None,
        typer.Option(
            "--exclude-humans/--no-exclude-humans",
            help="Exclude users based on human status. Use --exclude-humans to exclude human users, --no-exclude-humans to exclude bots and other non-human accounts.",
        ),
    ] = None,
    exclude_internal: Annotated[
        bool | None,
        typer.Option(
            "--exclude-internal/--no-exclude-internal",
            help="Exclude users based on internal status. Use --exclude-internal to exclude internal users, --no-exclude-internal to exclude external users.",
        ),
    ] = None,
    without_project_bots: Annotated[
        bool | None,
        typer.Option(
            "--without-project-bots/--with-project-bots",
            help="Exclude or include project bot users. By default, project bots are included.",
            show_default=True,
        ),
    ] = None,
    saml_provider_id: Annotated[
        int | None,
        typer.Option(
            "--saml-provider-id",
            help="Filter users by SAML provider ID. Only users associated with the specified SAML provider will be included.",
        ),
    ] = None,
    extern_uid: Annotated[
        str | None,
        typer.Option(
            "--extern-uid",
            help="Filter users by external UID. Only users with the specified external UID will be included.",
        ),
    ] = None,
    provider: Annotated[
        str | None,
        typer.Option(
            "--provider",
            help="Filter users by authentication provider. Only users authenticated via the specified provider will be included.",
        ),
    ] = None,
    two_factor: Annotated[
        Literal["enabled", "disabled"] | None,
        typer.Option(
            "--two-factor",
            help="Filter users based on two-factor authentication status. Use 'enabled' to include only users with 2FA enabled, 'disabled' for those without 2FA.",
        ),
    ] = None,
    without_projects: Annotated[
        bool | None,
        typer.Option(
            "--without-projects/--with-projects",
            help="Filter users based on project membership. Use --without-projects to include only users without any project memberships, --with-projects to include only users with project memberships.",
        ),
    ] = None,
    admins: Annotated[
        bool | None,
        typer.Option(
            "--admins/--no-admins",
            help="Filter by admin status. Use --admins to filter admin users, --no-admins for non-admin users.",
        ),
    ] = None,
    auditors: Annotated[
        bool | None,
        typer.Option(
            "--auditors/--no-auditors",
            help="Filter by auditor status. Use --auditors to filter auditor users, --no-auditors for non-auditor users.",
        ),
    ] = None,
    skip_ldap: Annotated[
        bool | None,
        typer.Option(
            "--skip-ldap/--no-skip-ldap",
            help="Filter users based on LDAP status. Use --skip-ldap to include only users that do not use LDAP for authentication, --no-skip-ldap to include only users that use LDAP.",
        ),
    ] = None,
    page: Annotated[
        int,
        typer.Option(
            "--page",
            help="Page number for pagination. Defaults to 1.",
        ),
    ] = 1,
    per_page: Annotated[
        int,
        typer.Option(
            "--per-page",
            help="Number of users per page for pagination. Defaults to 20.",
        ),
    ] = 20,
    order_by: Annotated[
        str,
        typer.Option(
            "--order-by",
            help="Attribute to order users by. Defaults to 'id'.",
        ),
    ] = "id",
    sort: Annotated[
        Literal["asc", "desc"],
        typer.Option(
            "--sort",
            help="Sort order for users. Can be 'asc' or 'desc'. Defaults to 'asc'.",
        ),
    ] = "asc",
    etag: Annotated[
        str | None,
        typer.Option(
            "--etag",
            help="ETag for caching.",
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
    """List users with various filtering options.

    Args:
        ctx: Typer context.
        username: Username of the user.
        public_email: Public email of the user.
        search: Search term for user attributes.
        active: Filter by active status.
        external: Filter by external status.
        blocked: Filter by blocked status.
        humans: Filter by human status.
        created_after: Filter users created after this datetime.
        created_before: Filter users created before this datetime.
        exclude_active: Exclude users based on active status.
        exclude_external: Exclude users based on external status.
        exclude_humans: Exclude users based on human status.
        exclude_internal: Exclude users based on internal status.
        without_project_bots: Exclude or include project bot users.
        saml_provider_id: Filter users by SAML provider ID.
        extern_uid: Filter users by external UID.
        provider: Filter users by authentication provider.
        two_factor: Filter users based on two-factor authentication status.
        without_projects: Filter users based on project membership.
        admins: Filter by admin status.
        auditors: Filter by auditor status.
        skip_ldap: Filter users based on LDAP status.
        page: Page number for pagination.
        per_page: Number of users per page for pagination.
        order_by: Attribute to order users by.
        sort: Sort order for users.
        etag: ETag for caching.
        account_name: Name of the account to use for authentication.
        token: Token for authentication. If not provided, the token from the specified account will be used.
        base_url: Base URL of the GitLab platform. If not provided, the base URL from the specified account will be used.

    """
    from typing import Any  # noqa: PLC0415

    from glnova.cli.utils.api import execute_api_command  # noqa: PLC0415
    from glnova.cli.utils.auth import get_auth_params  # noqa: PLC0415
    from glnova.client.gitlab import GitLab  # noqa: PLC0415

    token, base_url = get_auth_params(
        config_path=ctx.obj["config_path"],
        account_name=account_name,
        token=token,
        base_url=base_url,
    )

    def api_call() -> tuple[list[dict[str, Any]], dict[str, Any]]:
        """Implement the API call to list users."""
        with GitLab(base_url=base_url, token=token) as client:
            return client.user.list_users(
                username=username,
                public_email=public_email,
                search=search,
                active=active,
                external=external,
                blocked=blocked,
                humans=humans,
                created_after=created_after,
                created_before=created_before,
                exclude_active=exclude_active,
                exclude_external=exclude_external,
                exclude_humans=exclude_humans,
                exclude_internal=exclude_internal,
                without_project_bots=without_project_bots,
                saml_provider_id=saml_provider_id,
                extern_uid=extern_uid,
                provider=provider,
                two_factor=two_factor,
                without_projects=without_projects,
                admins=admins,
                auditors=auditors,
                skip_ldap=skip_ldap,
                page=page,
                per_page=per_page,
                order_by=order_by,
                sort=sort,
                etag=etag,
            )

    execute_api_command(api_call=api_call, command_name="glnova user list")
