"""GitLab User resource."""

from __future__ import annotations

from typing import Any, Literal, cast

from requests import Response

from glnova.resource.resource import Resource
from glnova.user.base import BaseUser
from glnova.utils.response import process_response_with_last_modified


class User(BaseUser, Resource):
    """GitLab User resource."""

    def _get_user(
        self,
        account_id: int | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> Response:
        """Get user information.

        Args:
            account_id: The account ID of the user. If None, retrieves the authenticated user.
            etag: The ETag value for conditional requests.
            **kwargs: Additional arguments for the request.

        Returns:
            The response object.
        """
        endpoint, kwargs = self._get_user_helper(account_id=account_id, **kwargs)
        return self._get(endpoint=endpoint, etag=etag, **kwargs)

    def get_user(
        self,
        account_id: int | None = None,
        etag: str | None = None,
        **kwargs: Any,
    ) -> tuple[dict[str, Any], int, str | None]:
        """Get user information.

        Args:
            account_id: The account ID of the user. If None, retrieves the authenticated user.
            etag: The ETag value for conditional requests.
            **kwargs: Additional arguments for the request.

        Returns:
            A tuple containing:
                - A dictionary with user information (empty if 304 Not Modified).
                - The HTTP status code.
                - The Etag value from the response headers (if present).
        """
        response = self._get_user(account_id=account_id, etag=etag, **kwargs)
        data, status_code, etag_value = process_response_with_last_modified(response)
        data = cast(dict[str, Any], data)
        return data, status_code, etag_value

    def _modify_user(  # noqa: PLR0913
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
    ) -> Response:
        """Update the authenticated user's information.

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
            The response object.
        """
        endpoint, payload, kwargs = self._modify_user_helper(
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
            **kwargs,
        )
        return self._put(endpoint=endpoint, json=payload, **kwargs)

    def modify_user(  # noqa: PLR0913
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
    ) -> tuple[dict[str, Any], int, str | None]:
        """Update the authenticated user's information.

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
            A tuple containing:
                - A dictionary with updated user information (empty if 304 Not Modified).
                - The HTTP status code.
                - The ETag value from the response headers (if present).
        """
        response = self._modify_user(
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
            **kwargs,
        )
        data, status_code, etag_value = process_response_with_last_modified(response)
        data = cast(dict[str, Any], data)

        return data, status_code, etag_value

    def _list_users(  # noqa: PLR0913
        self,
        username: str | None = None,
        public_email: str | None = None,
        search: str | None = None,
        active: bool | None = None,
        external: bool | None = None,
        blocked: bool | None = None,
        humans: bool | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
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
        etag: str | None = None,
        **kwargs: Any,
    ) -> Response:
        """List all users.

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
            etag: The Etag value for conditional requests.
            **kwargs: Additional arguments for the request.

        Returns:
            The response object.
        """
        endpoint, params, kwargs = self._list_users_helper(
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
            **kwargs,
        )
        return self._get(endpoint=endpoint, params=params, etag=etag, **kwargs)

    def list_users(  # noqa: PLR0913
        self,
        username: str | None = None,
        public_email: str | None = None,
        search: str | None = None,
        active: bool | None = None,
        external: bool | None = None,
        blocked: bool | None = None,
        humans: bool | None = None,
        created_after: str | None = None,
        created_before: str | None = None,
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
        etag: str | None = None,
        **kwargs: Any,
    ) -> tuple[list[dict[str, Any]], int, str | None]:
        """List all users.

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
            etag: The Etag value for conditional requests.
            **kwargs: Additional arguments for the request.

        Returns:
            A tuple containing:
                - A list of user dictionaries (empty if 304 Not Modified).
                - The HTTP status code.
                - The ETag value from the response headers (if present).
        """
        response = self._list_users(
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
            **kwargs,
        )
        data, status_code, etag_value = process_response_with_last_modified(response)
        if status_code == 304:  # noqa: PLR2004
            data = []
        return cast(list[dict[str, Any]], data), status_code, etag_value
