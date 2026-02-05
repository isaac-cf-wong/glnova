"""Modify user information."""

from __future__ import annotations

from typing import Annotated

import typer


def modify_command(  # noqa: PLR0913
    ctx: typer.Context,
    account_id: Annotated[int, typer.Option("--account-id", help="Account ID of the user.")],
    admin: Annotated[bool | None, typer.Option("--admin/--no-admin", help="Set user as admin or not.")] = None,
    auditor: Annotated[bool | None, typer.Option("--auditor/--no-auditor", help="Set user as auditor or not.")] = None,
    avatar: Annotated[str | None, typer.Option("--avatar", help="URL of the user's avatar.")] = None,
    bio: Annotated[str | None, typer.Option("--bio", help="Biography of the user.")] = None,
    can_create_group: Annotated[
        bool | None,
        typer.Option("--can-create-group/--cannot-create-group", help="Set whether the user can create groups."),
    ] = None,
    color_scheme_id: Annotated[
        int | None,
        typer.Option("--color-scheme-id", help="ID of the color scheme to set for the user."),
    ] = None,
    commit_email: Annotated[
        str | None,
        typer.Option("--commit-email", help="Commit email address of the user."),
    ] = None,
    email: Annotated[
        str | None,
        typer.Option("--email", help="Email address of the user."),
    ] = None,
    extern_uid: Annotated[
        str | None,
        typer.Option("--extern-uid", help="External UID of the user."),
    ] = None,
    external: Annotated[
        bool | None,
        typer.Option("--external/--internal", help="Set whether the user is external."),
    ] = None,
    extra_shared_runners_minutes_limit: Annotated[
        int | None,
        typer.Option(
            "--extra-shared-runners-minutes-limit",
            help="Set extra shared runners minutes limit for the user.",
        ),
    ] = None,
    group_id_for_saml: Annotated[
        str | None,
        typer.Option("--group-id-for-saml", help="Group ID for SAML authentication."),
    ] = None,
    linkedin: Annotated[
        str | None,
        typer.Option("--linkedin", help="LinkedIn profile URL of the user."),
    ] = None,
    location: Annotated[
        str | None,
        typer.Option("--location", help="Location of the user."),
    ] = None,
    name: Annotated[
        str | None,
        typer.Option("--name", help="Full name of the user."),
    ] = None,
    note: Annotated[
        str | None,
        typer.Option("--note", help="Admin note for the user."),
    ] = None,
    organization: Annotated[
        str | None,
        typer.Option("--organization", help="Organization of the user."),
    ] = None,
    password: Annotated[
        str | None,
        typer.Option("--password", help="Password for the user."),
    ] = None,
    private_profile: Annotated[
        bool | None,
        typer.Option("--private-profile/--public-profile", help="Set whether the user's profile is private."),
    ] = None,
    projects_limit: Annotated[
        int | None,
        typer.Option("--projects-limit", help="Set the maximum number of projects for the user."),
    ] = None,
    pronouns: Annotated[
        str | None,
        typer.Option("--pronouns", help="Pronouns of the user."),
    ] = None,
    provider: Annotated[
        str | None,
        typer.Option("--provider", help="External provider of the user."),
    ] = None,
    public_email: Annotated[
        str | None,
        typer.Option("--public-email", help="Public email address of the user."),
    ] = None,
    shared_runners_minutes_limit: Annotated[
        int | None,
        typer.Option(
            "--shared-runners-minutes-limit",
            help="Set shared runners minutes limit for the user.",
        ),
    ] = None,
    skip_reconfirmation: Annotated[
        bool | None,
        typer.Option(
            "--skip-reconfirmation/--no-skip-reconfirmation",
            help="Skip email reconfirmation for the user when changing email.",
        ),
    ] = None,
    theme_id: Annotated[
        int | None,
        typer.Option("--theme-id", help="ID of the theme to set for the user."),
    ] = None,
    twitter: Annotated[
        str | None,
        typer.Option("--twitter", help="Twitter profile URL of the user."),
    ] = None,
    discord: Annotated[
        str | None,
        typer.Option("--discord", help="Discord handle of the user."),
    ] = None,
    github: Annotated[
        str | None,
        typer.Option("--github", help="GitHub profile URL of the user."),
    ] = None,
    username: Annotated[
        str | None,
        typer.Option("--username", help="Username of the user."),
    ] = None,
    view_diffs_file_by_file: Annotated[
        bool | None,
        typer.Option(
            "--view-diffs-file-by-file/--view-diffs-inline",
            help="Set whether to view diffs file by file.",
        ),
    ] = None,
    website_url: Annotated[
        str | None,
        typer.Option("--website-url", help="Website URL of the user."),
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
    """Modify user information.

    Args:
        ctx: Typer context.
        account_id: Account ID of the user.
        admin: Set user as admin or not.
        auditor: Set user as auditor or not.
        avatar: URL of the user's avatar.
        bio: Biography of the user.
        can_create_group: Set whether the user can create groups.
        color_scheme_id: ID of the color scheme to set for the user.
        commit_email: Commit email address of the user.
        email: Email address of the user.
        extern_uid: External UID of the user.
        external: Set whether the user is external.
        extra_shared_runners_minutes_limit: Set extra shared runners minutes limit for the user.
        group_id_for_saml: Group ID for SAML authentication.
        linkedin: LinkedIn profile URL of the user.
        location: Location of the user.
        name: Full name of the user.
        note: Admin note for the user.
        organization: Organization of the user.
        password: Password for the user.
        private_profile: Set whether the user's profile is private.
        projects_limit: Set the maximum number of projects for the user.
        pronouns: Pronouns of the user.
        provider: External provider of the user.
        public_email: Public email address of the user.
        shared_runners_minutes_limit: Set shared runners minutes limit for the user.
        skip_reconfirmation: Skip email reconfirmation for the user when changing email.
        theme_id: ID of the theme to set for the user.
        twitter: Twitter profile URL of the user.
        discord: Discord handle of the user.
        github: GitHub profile URL of the user.
        username: Username of the user.
        view_diffs_file_by_file: Set whether to view diffs file by file.
        website_url: Website URL of the user.
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

    def api_call() -> tuple[dict[str, Any], dict[str, Any]]:
        """Implement the API call to modify user information.

        Returns:
            A tuple containing the user data and response metadata.

        """
        with GitLab(token=token, base_url=base_url) as client:
            return client.user.modify_user(
                account_id=account_id,
                admin=admin,
                auditor=auditor,
                avatar=avatar,
                bio=bio,
                can_create_group=can_create_group,
                color_scheme_id=color_scheme_id,
                commit_email=commit_email,
                email=email,
                extern_uid=extern_uid,
                external=external,
                extra_shared_runners_minutes_limit=extra_shared_runners_minutes_limit,
                group_id_for_saml=group_id_for_saml,
                linkedin=linkedin,
                location=location,
                name=name,
                note=note,
                organization=organization,
                password=password,
                private_profile=private_profile,
                projects_limit=projects_limit,
                pronouns=pronouns,
                provider=provider,
                public_email=public_email,
                shared_runners_minutes_limit=shared_runners_minutes_limit,
                skip_reconfirmation=skip_reconfirmation,
                theme_id=theme_id,
                twitter=twitter,
                discord=discord,
                github=github,
                username=username,
                view_diffs_file_by_file=view_diffs_file_by_file,
                website_url=website_url,
            )

    execute_api_command(api_call=api_call, command_name="glnova user modify")
