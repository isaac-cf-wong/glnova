"""Tests for glnova.merge_request.base."""

from __future__ import annotations

from datetime import datetime

from glnova.merge_request.base import BaseMergeRequest


class TestBaseMergeRequest:
    """Tests for BaseMergeRequest class."""

    def test_list_merge_requests_endpoint_project_id_int(self) -> None:
        """Test _list_merge_requests_endpoint with integer project_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id=123, group_id=None)
        assert endpoint == "/projects/123/merge_requests"
        assert listing_type == "project"

    def test_list_merge_requests_endpoint_project_id_str(self) -> None:
        """Test _list_merge_requests_endpoint with string project_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id="group/project", group_id=None)
        # cSpell: disable
        assert endpoint == "/projects/group%2Fproject/merge_requests"
        # cSpell: enable
        assert listing_type == "project"

    def test_list_merge_requests_endpoint_group_id_int(self) -> None:
        """Test _list_merge_requests_endpoint with integer group_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id=None, group_id=456)
        assert endpoint == "/groups/456/merge_requests"
        assert listing_type == "group"

    def test_list_merge_requests_endpoint_group_id_str(self) -> None:
        """Test _list_merge_requests_endpoint with string group_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id=None, group_id="my/group")
        # cSpell: disable
        assert endpoint == "/groups/my%2Fgroup/merge_requests"
        # cSpell: enable
        assert listing_type == "group"

    def test_list_merge_requests_endpoint_user(self) -> None:
        """Test _list_merge_requests_endpoint with no project_id or group_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id=None, group_id=None)
        assert endpoint == "/merge_requests"
        assert listing_type == "user"

    def test_list_merge_requests_endpoint_project_takes_precedence(self) -> None:
        """Test that project_id takes precedence over group_id."""
        base_mr = BaseMergeRequest()
        endpoint, listing_type = base_mr._list_merge_requests_endpoint(project_id=123, group_id=456)
        assert endpoint == "/projects/123/merge_requests"
        assert listing_type == "project"

    def test_list_user_merge_requests_params_basic(self) -> None:
        """Test _list_user_merge_requests_params with basic parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(
            assignee_id=123,
            author_username="testuser",
            state="opened",
            scope="assigned_to_me",
            sort="desc",
            order_by="created_at",
            page=2,
            per_page=50,
        )

        expected = {
            "assignee_id": 123,
            "author_username": "testuser",
            "state": "opened",
            "scope": "assigned_to_me",
            "sort": "desc",
            "order_by": "created_at",
            "page": 2,
            "per_page": 50,
        }
        assert params == expected

    def test_list_user_merge_requests_params_with_labels(self) -> None:
        """Test _list_user_merge_requests_params with labels parameter."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(labels=["bug", "feature"])

        assert params["labels"] == "bug,feature"
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_user_merge_requests_params_with_labels_none(self) -> None:
        """Test _list_user_merge_requests_params with labels=None."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(labels="None")

        assert params["labels"] == "None"
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_user_merge_requests_params_with_search_in(self) -> None:
        """Test _list_user_merge_requests_params with search_in parameter."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(search_in=["title", "description"])

        assert params["search_in"] == "title,description"
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_project_merge_requests_params_basic(self) -> None:
        """Test _list_project_merge_requests_params with basic parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_project_merge_requests_params(
            assignee_id=123,
            author_username="testuser",
            state="opened",
            scope="assigned_to_me",
            sort="desc",
            order_by="created_at",
            page=2,
            per_page=50,
        )

        expected = {
            "assignee_id": 123,
            "author_username": "testuser",
            "state": "opened",
            "scope": "assigned_to_me",
            "sort": "desc",
            "order_by": "created_at",
            "page": 2,
            "per_page": 50,
        }
        assert params == expected

    def test_list_project_merge_requests_params_with_iids(self) -> None:
        """Test _list_project_merge_requests_params with iids parameter."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_project_merge_requests_params(iids=[1, 2, 3])

        assert params["iids"] == "1,2,3"
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_group_merge_requests_params_basic(self) -> None:
        """Test _list_group_merge_requests_params with basic parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_group_merge_requests_params(
            assignee_id=123,
            author_username="testuser",
            state="opened",
            scope="assigned_to_me",
            sort="desc",
            order_by="created_at",
            page=2,
            per_page=50,
        )

        expected = {
            "assignee_id": 123,
            "author_username": "testuser",
            "state": "opened",
            "scope": "assigned_to_me",
            "sort": "desc",
            "order_by": "created_at",
            "page": 2,
            "per_page": 50,
        }
        assert params == expected

    def test_list_group_merge_requests_params_with_approved(self) -> None:
        """Test _list_group_merge_requests_params with approved parameter."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_group_merge_requests_params(approved="yes")

        assert params["approved"] == "yes"
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_group_merge_requests_params_with_non_archived(self) -> None:
        """Test _list_group_merge_requests_params with non_archived parameter."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_group_merge_requests_params(non_archived=True)

        assert params["non_archived"] is True
        assert params["page"] == 1
        assert params["per_page"] == 20  # noqa: PLR2004

    def test_list_merge_requests_helper_project(self) -> None:
        """Test _list_merge_requests_helper for project merge requests."""
        base_mr = BaseMergeRequest()
        endpoint, params = base_mr._list_merge_requests_helper(
            project_id=123, group_id=None, assignee_id=456, state="opened"
        )

        assert endpoint == "/projects/123/merge_requests"
        assert params["assignee_id"] == 456  # noqa: PLR2004
        assert params["state"] == "opened"

    def test_list_merge_requests_helper_group(self) -> None:
        """Test _list_merge_requests_helper for group merge requests."""
        base_mr = BaseMergeRequest()
        endpoint, params = base_mr._list_merge_requests_helper(
            project_id=None, group_id=789, assignee_id=456, state="opened"
        )

        assert endpoint == "/groups/789/merge_requests"
        assert params["assignee_id"] == 456  # noqa: PLR2004
        assert params["state"] == "opened"

    def test_list_merge_requests_helper_user(self) -> None:
        """Test _list_merge_requests_helper for user merge requests."""
        base_mr = BaseMergeRequest()
        endpoint, params = base_mr._list_merge_requests_helper(
            project_id=None, group_id=None, assignee_id=456, state="opened"
        )

        assert endpoint == "/merge_requests"
        assert params["assignee_id"] == 456  # noqa: PLR2004
        assert params["state"] == "opened"

    def test_list_user_merge_requests_params_with_all_optional_params(self) -> None:
        """Test _list_user_merge_requests_params with all optional parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(
            approved_by_ids=[1, 2, 3],
            approver_ids=[4, 5],
            author_id=10,
            created_after=datetime(2023, 1, 1),
            created_before=datetime(2023, 12, 31),
            deployed_after=datetime(2023, 6, 1),
            deployed_before=datetime(2023, 6, 30),
            environment="staging",
            merge_user_id=20,
            merge_user_username="merger",
            my_reaction_emoji="thumbs_up",
            not_match="labels",
            render_html=True,
            search="test",
            source_branch="feature",
            target_branch="main",
            updated_after=datetime(2023, 7, 1),
            updated_before=datetime(2023, 7, 31),
            view="simple",
            with_labels_details=True,
            with_merge_status_recheck=True,
            wip="no",
        )

        assert params["approved_by_ids"] == [1, 2, 3]
        assert params["approver_ids"] == [4, 5]
        assert params["author_id"] == 10  # noqa: PLR2004
        assert params["environment"] == "staging"
        assert params["merge_user_id"] == 20  # noqa: PLR2004
        assert params["merge_user_username"] == "merger"
        assert params["my_reaction_emoji"] == "thumbs_up"
        assert params["not"] == "labels"
        assert params["render_html"] is True
        assert params["search"] == "test"
        assert params["source_branch"] == "feature"
        assert params["target_branch"] == "main"
        assert params["view"] == "simple"
        assert params["with_labels_details"] is True
        assert params["with_merge_status_recheck"] is True
        assert params["wip"] == "no"

    def test_list_project_merge_requests_params_with_all_optional_params(self) -> None:
        """Test _list_project_merge_requests_params with all optional parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_project_merge_requests_params(
            approved_by_ids=[1, 2],
            approver_ids=[3, 4],
            author_id=10,
            created_after=datetime(2023, 1, 1),
            created_before=datetime(2023, 12, 31),
            environment="production",
            merge_user_id=20,
            merge_user_username="merger",
            my_reaction_emoji="tada",
            not_match="milestone",
            reviewer_id=30,
            reviewer_username="reviewer1",
            search="bug",
            sort="asc",
            source_branch="develop",
            target_branch="main",
            updated_after=datetime(2023, 7, 1),
            updated_before=datetime(2023, 7, 31),
            view="compact",
            wip="yes",
            with_labels_details=False,
            with_merge_status_recheck=False,
        )

        assert params["approved_by_ids"] == [1, 2]
        assert params["approver_ids"] == [3, 4]
        assert params["author_id"] == 10  # noqa: PLR2004
        assert params["environment"] == "production"
        assert params["merge_user_id"] == 20  # noqa: PLR2004
        assert params["merge_user_username"] == "merger"
        assert params["my_reaction_emoji"] == "tada"
        assert params["not"] == "milestone"
        assert params["reviewer_id"] == 30  # noqa: PLR2004
        assert params["reviewer_username"] == "reviewer1"
        assert params["search"] == "bug"
        assert params["sort"] == "asc"
        assert params["source_branch"] == "develop"
        assert params["target_branch"] == "main"
        assert params["view"] == "compact"
        assert params["wip"] == "yes"
        assert params["with_labels_details"] is False
        assert params["with_merge_status_recheck"] is False

    def test_list_group_merge_requests_params_with_all_optional_params(self) -> None:
        """Test _list_group_merge_requests_params with all optional parameters."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_group_merge_requests_params(
            approved_by_ids=[1, 2],
            approved_by_usernames=["user1", "user2"],
            approver_ids=[3, 4],
            assignee_username=["assignee1"],
            author_id=10,
            created_after=datetime(2023, 1, 1),
            created_before=datetime(2023, 12, 31),
            deployed_after=datetime(2023, 6, 1),
            deployed_before=datetime(2023, 6, 30),
            environment="staging",
            merge_user_id=20,
            merge_user_username="merger",
            my_reaction_emoji="heart",
            not_match="author_id",
            reviewer_id=40,
            reviewer_username="reviewer1",
            search="urgent",
            source_branch="hotfix",
            source_project_id=999,
            target_branch="release",
            updated_after=datetime(2023, 8, 1),
            updated_before=datetime(2023, 8, 31),
            view="detailed",
            with_labels_details=True,
            with_merge_status_recheck=False,
            wip="yes",
        )

        assert params["approved_by_ids"] == [1, 2]
        assert params["approved_by_usernames"] == "user1,user2"
        assert params["approver_ids"] == [3, 4]
        assert params["assignee_username"] == "assignee1"
        assert params["author_id"] == 10  # noqa: PLR2004
        assert params["environment"] == "staging"
        assert params["merge_user_id"] == 20  # noqa: PLR2004
        assert params["merge_user_username"] == "merger"
        assert params["my_reaction_emoji"] == "heart"
        assert params["not"] == "author_id"
        assert params["reviewer_id"] == 40  # noqa: PLR2004
        assert params["reviewer_username"] == "reviewer1"
        assert params["search"] == "urgent"
        assert params["source_branch"] == "hotfix"
        assert params["source_project_id"] == 999  # noqa: PLR2004
        assert params["target_branch"] == "release"
        assert params["view"] == "detailed"
        assert params["with_labels_details"] is True
        assert params["with_merge_status_recheck"] is False
        assert params["wip"] == "yes"

    def test_list_user_merge_requests_params_with_literal_values(self) -> None:
        """Test _list_user_merge_requests_params with Literal values like 'None' and 'Any'."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_user_merge_requests_params(
            approved_by_ids="None",
            assignee_id="Any",
            author_id="None",
            milestone="None",
            my_reaction_emoji="Any",
            reviewer_id="None",
            reviewer_username="Any",
        )

        assert params["approved_by_ids"] == "None"
        assert params["assignee_id"] == "Any"
        assert params["author_id"] == "None"
        assert params["milestone"] == "None"
        assert params["my_reaction_emoji"] == "Any"
        assert params["reviewer_id"] == "None"
        assert params["reviewer_username"] == "Any"

    def test_list_project_merge_requests_params_with_literal_values(self) -> None:
        """Test _list_project_merge_requests_params with Literal values."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_project_merge_requests_params(
            approved_by_ids="Any",
            assignee_id="None",
            author_id="Any",
            labels="None",
            milestone="Any",
            reviewer_id="None",
            reviewer_username="Any",
        )

        assert params["approved_by_ids"] == "Any"
        assert params["assignee_id"] == "None"
        assert params["author_id"] == "Any"
        assert params["labels"] == "None"
        assert params["milestone"] == "Any"
        assert params["reviewer_id"] == "None"
        assert params["reviewer_username"] == "Any"

    def test_list_group_merge_requests_params_with_literal_values(self) -> None:
        """Test _list_group_merge_requests_params with Literal values."""
        base_mr = BaseMergeRequest()
        params = base_mr._list_group_merge_requests_params(
            approved_by_ids="None",
            approved_by_usernames="Any",
            assignee_id="None",
            labels="Any",
            milestone="None",
            my_reaction_emoji="Any",
        )

        assert params["approved_by_ids"] == "None"
        assert params["approved_by_usernames"] == "Any"
        assert params["assignee_id"] == "None"
        assert params["labels"] == "Any"
        assert params["milestone"] == "None"
        assert params["my_reaction_emoji"] == "Any"
