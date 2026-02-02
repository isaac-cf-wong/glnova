"""Tests for glnova.merge_request.base."""

from __future__ import annotations

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
