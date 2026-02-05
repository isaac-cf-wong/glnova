"""Base class for GitLab User resource."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal


class BaseUser:
    """Base class for GitLab User resource."""

    def _get_user_endpoint(self, account_id: int | None) -> str:
        """Determine the user endpoint based on user id.

        If account_id is None, returns the endpoint for the authenticated user.

        Args:
            account_id: The account ID of the user. If None, retrieves the authenticated user.

        Returns:
            The API endpoint for the user.

        """
        return "/user" if account_id is None else f"/users/{account_id}"

    def _get_user_helper(self, account_id: int | None = None, **kwargs: Any) -> tuple[str, dict[str, Any]]:
        """Get user information.

        Args:
            account_id: The account ID of the user. If None, retrieves the authenticated user.
            **kwargs: Additional arguments for the request.

        Returns:
            A tuple containing the endpoint and the request arguments.
                - The API endpoint for the user.
                - A dictionary of request arguments.

        """
        endpoint = self._get_user_endpoint(account_id=account_id)

        return endpoint, kwargs

    def _modify_user_endpoint(self, account_id: int) -> str:
        """Get the endpoint for modifying an existing user.

        Args:
            account_id: The account ID of the user.

        Returns:
            The API endpoint for modifying an existing user.

        """
        return f"/users/{account_id}"

    def _modify_user_helper(  # noqa: PLR0912, PLR0913, PLR0915
        self,
        account_id: int,
        admin: bool | None = None,
        auditor: bool | None = None,
        avatar: str | None = None,
        bio: str | None = None,
        can_create_group: bool | None = None,
        color_scheme_id: int | None = None,
        commit_email: str | None = None,
        email: str | None = None,
        extern_uid: str | None = None,
        external: bool | None = None,
        extra_shared_runners_minutes_limit: int | None = None,
        group_id_for_saml: int | None = None,
        linkedin: str | None = None,
        location: str | None = None,
        name: str | None = None,
        note: str | None = None,
        organization: str | None = None,
        password: str | None = None,
        private_profile: bool | None = None,
        projects_limit: int | None = None,
        pronouns: str | None = None,
        provider: str | None = None,
        public_email: str | None = None,
        shared_runners_minutes_limit: int | None = None,
        skip_reconfirmation: bool | None = None,
        theme_id: int | None = None,
        twitter: str | None = None,
        discord: str | None = None,
        github: str | None = None,
        username: str | None = None,
        view_diffs_file_by_file: bool | None = None,
        website_url: str | None = None,
        **kwargs: Any,
    ) -> tuple[str, dict[str, Any], dict[str, Any]]:
        """Get the endpoint and arguments for modifying an existing user.

        Admin-only.

        Args:
            account_id: The account ID of the user.
            admin: Whether the user is an admin.
            auditor: Whether the user is an auditor.
            avatar: The avatar URL of the user.
            bio: The bio of the user.
            can_create_group: Whether the user can create groups.
            color_scheme_id: The color scheme ID of the user.
            commit_email: The commit email of the user.
            email: The email of the user.
            extern_uid: The external UID of the user.
            external: Whether the user is external.
            extra_shared_runners_minutes_limit: The extra shared runners minutes limit.
            group_id_for_saml: The group ID for SAML.
            linkedin: The LinkedIn profile of the user.
            location: The location of the user.
            name: The name of the user.
            note: The note for the user.
            organization: The organization of the user.
            password: The password of the user.
            private_profile: Whether the profile is private.
            projects_limit: The projects limit of the user.
            pronouns: The pronouns of the user.
            provider: The provider of the user.
            public_email: The public email of the user.
            shared_runners_minutes_limit: The shared runners minutes limit.
            skip_reconfirmation: Whether to skip reconfirmation.
            theme_id: The theme ID of the user.
            twitter: The Twitter handle of the user.
            discord: The Discord handle of the user.
            github: The GitHub username of the user.
            username: The username of the user.
            view_diffs_file_by_file: Whether to view diffs file by file.
            website_url: The website URL of the user.
            **kwargs: Additional arguments for the request.

        Returns:
            A tuple containing the endpoint and the request arguments.
                - The API endpoint for updating the authenticated user.
                - A dictionary representing the JSON payload.
                - A dictionary of request arguments.

        """
        endpoint = self._modify_user_endpoint(account_id=account_id)

        payload = {}
        if admin is not None:
            payload["admin"] = admin
        if auditor is not None:
            payload["auditor"] = auditor
        if avatar is not None:
            payload["avatar"] = avatar
        if bio is not None:
            payload["bio"] = bio
        if can_create_group is not None:
            payload["can_create_group"] = can_create_group
        if color_scheme_id is not None:
            payload["color_scheme_id"] = color_scheme_id
        if commit_email is not None:
            payload["commit_email"] = commit_email
        if email is not None:
            payload["email"] = email
        if extern_uid is not None:
            payload["extern_uid"] = extern_uid
        if external is not None:
            payload["external"] = external
        if extra_shared_runners_minutes_limit is not None:
            payload["extra_shared_runners_minutes_limit"] = extra_shared_runners_minutes_limit
        if group_id_for_saml is not None:
            payload["group_id_for_saml"] = group_id_for_saml
        if linkedin is not None:
            payload["linkedin"] = linkedin
        if location is not None:
            payload["location"] = location
        if name is not None:
            payload["name"] = name
        if note is not None:
            payload["note"] = note
        if organization is not None:
            payload["organization"] = organization
        if password is not None:
            payload["password"] = password
        if private_profile is not None:
            payload["private_profile"] = private_profile
        if projects_limit is not None:
            payload["projects_limit"] = projects_limit
        if pronouns is not None:
            payload["pronouns"] = pronouns
        if provider is not None:
            payload["provider"] = provider
        if public_email is not None:
            payload["public_email"] = public_email
        if shared_runners_minutes_limit is not None:
            payload["shared_runners_minutes_limit"] = shared_runners_minutes_limit
        if skip_reconfirmation is not None:
            payload["skip_reconfirmation"] = skip_reconfirmation
        if theme_id is not None:
            payload["theme_id"] = theme_id
        if twitter is not None:
            payload["twitter"] = twitter
        if discord is not None:
            payload["discord"] = discord
        if github is not None:
            payload["github"] = github
        if username is not None:
            payload["username"] = username
        if view_diffs_file_by_file is not None:
            payload["view_diffs_file_by_file"] = view_diffs_file_by_file
        if website_url is not None:
            payload["website_url"] = website_url

        return endpoint, payload, kwargs

    def _list_users_endpoint(self) -> str:
        """Get the endpoint for listing all users.

        Returns:
            The API endpoint for listing all users.

        """
        return "/users"

    def _list_users_helper(  # noqa: PLR0912, PLR0913, PLR0915
        self,
        username: str | None = None,
        public_email: str | None = None,
        search: str | None = None,
        active: bool | None = None,
        external: bool | None = None,
        blocked: bool | None = None,
        humans: bool | None = None,
        created_after: datetime | None = None,
        created_before: datetime | None = None,
        exclude_active: bool | None = None,
        exclude_external: bool | None = None,
        exclude_humans: bool | None = None,
        exclude_internal: bool | None = None,
        without_project_bots: bool | None = None,
        saml_provider_id: int | None = None,
        extern_uid: str | None = None,
        provider: str | None = None,
        two_factor: Literal["enabled", "disabled"] | None = None,
        without_projects: bool | None = None,
        admins: bool | None = None,
        auditors: bool | None = None,
        skip_ldap: bool | None = None,
        page: int = 1,
        per_page: int = 20,
        order_by: str = "id",
        sort="asc",
        **kwargs: Any,
    ) -> tuple[str, dict[str, Any], dict[str, Any]]:
        """Get the endpoint and arguments for listing all users.

        Args:
            username: Filter by username.
            public_email: Filter by public email.
            search: Search term.
            active: Filter by active status.
            external: Filter by external status.
            blocked: Filter by blocked status.
            humans: Filter by human users.
            created_after: Filter by creation date after this date.
            created_before: Filter by creation date before this date.
            exclude_active: Exclude active users.
            exclude_external: Exclude external users.
            exclude_humans: Exclude human users.
            exclude_internal: Exclude internal users.
            without_project_bots: Exclude project bots.
            saml_provider_id: Filter by SAML provider ID.
            extern_uid: Filter by external UID. (Admin only)
            provider: Filter by provider. (Admin only)
            two_factor: Filter by two-factor authentication status. (Admin only)
            without_projects: Exclude users with projects. (Admin only)
            admins: Filter by admin users. (Admin only)
            auditors: Filter by auditor users. (Admin only)
            skip_ldap: Skip LDAP users. (Admin only)
            page: The page number for pagination.
            per_page: The number of users per page.
            order_by: The field to order by.
            sort: The sort order, either 'asc' or 'desc'.
            **kwargs: Additional arguments for the request.

        Returns:
            A tuple containing the endpoint and the request arguments.
                - The API endpoint for listing all users.
                - A dictionary of query parameters.
                - A dictionary of request arguments.

        """
        endpoint = self._list_users_endpoint()

        params = {}
        if username is not None:
            params["username"] = username
        if public_email is not None:
            params["public_email"] = public_email
        if search is not None:
            params["search"] = search
        if active is not None:
            params["active"] = active
        if external is not None:
            params["external"] = external
        if blocked is not None:
            params["blocked"] = blocked
        if humans is not None:
            params["humans"] = humans
        if created_after is not None:
            params["created_after"] = created_after
        if created_before is not None:
            params["created_before"] = created_before
        if exclude_active is not None:
            params["exclude_active"] = exclude_active
        if exclude_external is not None:
            params["exclude_external"] = exclude_external
        if exclude_humans is not None:
            params["exclude_humans"] = exclude_humans
        if exclude_internal is not None:
            params["exclude_internal"] = exclude_internal
        if without_project_bots is not None:
            params["without_project_bots"] = without_project_bots
        if saml_provider_id is not None:
            params["saml_provider_id"] = saml_provider_id
        if extern_uid is not None:
            params["extern_uid"] = extern_uid
        if provider is not None:
            params["provider"] = provider
        if two_factor is not None:
            params["two_factor"] = two_factor
        if without_projects is not None:
            params["without_projects"] = without_projects
        if admins is not None:
            params["admins"] = admins
        if auditors is not None:
            params["auditors"] = auditors
        if skip_ldap is not None:
            params["skip_ldap"] = skip_ldap
        params["page"] = page
        params["per_page"] = per_page
        params["order_by"] = order_by
        params["sort"] = sort

        return endpoint, params, kwargs
