"""Unit tests for the base issue class."""

import pytest

from glnova.issue.base import BaseIssue


class TestBaseIssue:
    """Test cases for the BaseIssue class."""

    def test_list_issues_endpoint_project_str(self):
        """Test _list_issues_endpoint with project as string."""
        base_issue = BaseIssue()
        endpoint, endpoint_type = base_issue._list_issues_endpoint(project="group/project")
        # cSpell:disable
        assert endpoint == "/projects/group%2Fproject/issues"
        # cSpell:enable
        assert endpoint_type == "project issues"

    def test_list_issues_endpoint_project_int(self):
        """Test _list_issues_endpoint with project as int."""
        base_issue = BaseIssue()
        endpoint, endpoint_type = base_issue._list_issues_endpoint(project=123)
        assert endpoint == "/projects/123/issues"
        assert endpoint_type == "project issues"

    def test_list_issues_endpoint_group_str(self):
        """Test _list_issues_endpoint with group as string."""
        base_issue = BaseIssue()
        endpoint, endpoint_type = base_issue._list_issues_endpoint(group="group/subgroup")
        # cSpell:disable
        assert endpoint == "/groups/group%2Fsubgroup/issues"
        # cSpell:enable
        assert endpoint_type == "group issues"

    def test_list_issues_endpoint_group_int(self):
        """Test _list_issues_endpoint with group as int."""
        base_issue = BaseIssue()
        endpoint, endpoint_type = base_issue._list_issues_endpoint(group=456)
        assert endpoint == "/groups/456/issues"
        assert endpoint_type == "group issues"

    def test_list_issues_endpoint_none(self):
        """Test _list_issues_endpoint with no group or project."""
        base_issue = BaseIssue()
        endpoint, endpoint_type = base_issue._list_issues_endpoint()
        assert endpoint == "/issues"
        assert endpoint_type == "authenticated user issues"

    def test_list_issues_helper_minimal(self):
        """Test _list_issues_helper with minimal parameters."""
        base_issue = BaseIssue()
        endpoint, params, kwargs = base_issue._list_issues_helper()
        assert endpoint == "/issues"
        assert params == {"page": 1, "per_page": 20}
        assert kwargs == {}

    def test_list_issues_helper_with_project(self):
        """Test _list_issues_helper with project."""
        base_issue = BaseIssue()
        endpoint, params, kwargs = base_issue._list_issues_helper(project="test/project")
        # cSpell:disable
        assert endpoint == "/projects/test%2Fproject/issues"
        # cSpell:enable
        assert params == {"page": 1, "per_page": 20}
        assert kwargs == {}

    def test_list_issues_helper_with_group(self):
        """Test _list_issues_helper with group."""
        base_issue = BaseIssue()
        endpoint, params, kwargs = base_issue._list_issues_helper(group="test/group")
        # cSpell:disable
        assert endpoint == "/groups/test%2Fgroup/issues"
        # cSpell:enable
        assert params == {"page": 1, "per_page": 20}
        assert kwargs == {}

    def test_list_issues_helper_with_params(self):
        """Test _list_issues_helper with various parameters."""
        base_issue = BaseIssue()
        endpoint, params, kwargs = base_issue._list_issues_helper(
            state="opened",
            labels=["bug", "feature"],
            assignee_username=["user1"],
            page=2,
            per_page=10,
        )
        assert endpoint == "/issues"
        expected_params = {
            "state": "opened",
            "labels": "bug,feature",
            "assignee_username": ["user1"],
            "page": 2,
            "per_page": 10,
        }
        assert params == expected_params
        assert kwargs == {}

    def test_list_issues_helper_cursor_project(self):
        """Test _list_issues_helper with cursor for project issues."""
        base_issue = BaseIssue()
        endpoint, params, _kwargs = base_issue._list_issues_helper(project="test", cursor="abc123")
        assert endpoint == "/projects/test/issues"
        assert params["cursor"] == "abc123"

    def test_list_issues_helper_cursor_non_project(self, caplog):
        """Test _list_issues_helper with cursor for non-project issues logs warning."""
        base_issue = BaseIssue()
        endpoint, params, _kwargs = base_issue._list_issues_helper(cursor="abc123")
        assert endpoint == "/issues"
        assert "cursor" not in params
        assert "Cursor pagination is only supported for project issues endpoints." in caplog.text

    def test_get_issue_endpoint_issue_id(self):
        """Test _get_issue_endpoint with issue_id."""
        base_issue = BaseIssue()
        endpoint = base_issue._get_issue_endpoint(issue_id=123)
        assert endpoint == "/issues/123"

    def test_get_issue_endpoint_project_str(self):
        """Test _get_issue_endpoint with project as string."""
        base_issue = BaseIssue()
        endpoint = base_issue._get_issue_endpoint(project_id="group/project", issue_iid=456)
        # cSpell:disable
        assert endpoint == "/projects/group%2Fproject/issues/456"
        # cSpell:enable

    def test_get_issue_endpoint_project_int(self):
        """Test _get_issue_endpoint with project as int."""
        base_issue = BaseIssue()
        endpoint = base_issue._get_issue_endpoint(project_id=789, issue_iid=101)
        assert endpoint == "/projects/789/issues/101"

    def test_get_issue_endpoint_invalid(self):
        """Test _get_issue_endpoint with invalid parameters."""
        base_issue = BaseIssue()
        with pytest.raises(ValueError, match=r"Either issue_id or both project_id and issue_iid must be provided."):
            base_issue._get_issue_endpoint()

    def test_get_issue_helper(self):
        """Test _get_issue_helper."""
        base_issue = BaseIssue()
        endpoint, params = base_issue._get_issue_helper(issue_id=123, extra="value")
        assert endpoint == "/issues/123"
        assert params == {"extra": "value"}

    def test_edit_issue_endpoint_str(self):
        """Test _edit_issue_endpoint with project as string."""
        base_issue = BaseIssue()
        endpoint = base_issue._edit_issue_endpoint(project_id="group/project", issue_iid=456)
        # cSpell:disable
        assert endpoint == "/projects/group%2Fproject/issues/456"
        # cSpell:enable

    def test_edit_issue_endpoint_int(self):
        """Test _edit_issue_endpoint with project as int."""
        base_issue = BaseIssue()
        endpoint = base_issue._edit_issue_endpoint(project_id=789, issue_iid=101)
        assert endpoint == "/projects/789/issues/101"

    def test_edit_issue_helper_minimal(self):
        """Test _edit_issue_helper with minimal parameters."""
        base_issue = BaseIssue()
        endpoint, payload = base_issue._edit_issue_helper(project_id="test", issue_iid=1)
        assert endpoint == "/projects/test/issues/1"
        assert payload == {}

    def test_list_issues_helper_full_params(self):
        """Test _list_issues_helper with all parameters to cover missing lines."""
        base_issue = BaseIssue()
        endpoint, params, kwargs = base_issue._list_issues_helper(
            assignee_id=123,
            assignee_username=["user1"],
            author_id=456,
            author_username="author1",
            confidential=True,
            created_after="2023-01-01",
            created_before="2023-12-31",
            due_date="today",
            epic_id=789,
            health_status="on_track",
            iids=[1, 2, 3],
            search_in=["title"],
            issue_type="issue",
            iteration_id=101,
            iteration_title="Sprint 1",
            labels=["bug"],
            milestone_id="Upcoming",
            milestone="v1.0",
            my_reaction_emoji="thumbs_up",
            non_archived=True,
            not_match="assignee_id",
            order_by="created_at",
            scope="assigned_to_me",
            search="query",
            sort="desc",
            state="opened",
            updated_after="2023-06-01",
            updated_before="2023-06-30",
            weight=5,
            with_labels_details=True,
            page=1,
            per_page=20,
        )
        assert endpoint == "/issues"
        expected_params = {
            "assignee_id": 123,
            "assignee_username": ["user1"],
            "author_id": 456,
            "author_username": "author1",
            "confidential": True,
            "created_after": "2023-01-01",
            "created_before": "2023-12-31",
            "due_date": "today",
            "epic_id": 789,
            "health_status": "on_track",
            "iids": [1, 2, 3],
            "in": ["title"],
            "issue_type": "issue",
            "iteration_id": 101,
            "iteration_title": "Sprint 1",
            "labels": "bug",
            "milestone_id": "Upcoming",
            "milestone": "v1.0",
            "my_reaction_emoji": "thumbs_up",
            "non_archived": True,
            "not": "assignee_id",
            "order_by": "created_at",
            "scope": "assigned_to_me",
            "search": "query",
            "sort": "desc",
            "state": "opened",
            "updated_after": "2023-06-01",
            "updated_before": "2023-06-30",
            "weight": 5,
            "with_labels_details": True,
            "page": 1,
            "per_page": 20,
        }
        assert params == expected_params
        assert kwargs == {}

    def test_edit_issue_helper_full_params(self):
        """Test _edit_issue_helper with all parameters to cover missing lines."""
        base_issue = BaseIssue()
        endpoint, payload = base_issue._edit_issue_helper(
            project_id="test",
            issue_iid=1,
            add_labels=["feature"],
            assignee_ids=[123],
            confidential=True,
            description="Desc",
            discussion_locked=True,
            due_date="2023-12-31",
            epic_id=456,
            epic_iid=789,
            issue_type="issue",
            labels=["bug"],
            milestone_id=101,
            remove_labels=["old"],
            state_event="close",
            title="Title",
            updated_at="2023-01-01T00:00:00Z",
            weight=5,
        )
        assert endpoint == "/projects/test/issues/1"
        expected_payload = {
            "add_labels": "feature",
            "assignee_ids": [123],
            "confidential": True,
            "description": "Desc",
            "discussion_locked": True,
            "due_date": "2023-12-31",
            "epic_id": 456,
            "epic_iid": 789,
            "issue_type": "issue",
            "labels": "bug",
            "milestone_id": 101,
            "remove_labels": "old",
            "state_event": "close",
            "title": "Title",
            "updated_at": "2023-01-01T00:00:00Z",
            "weight": 5,
        }
        assert payload == expected_payload
