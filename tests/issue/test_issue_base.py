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

    def test_edit_issue_helper_with_params(self):
        """Test _edit_issue_helper with various parameters."""
        base_issue = BaseIssue()
        endpoint, payload = base_issue._edit_issue_helper(
            project_id="test",
            issue_iid=1,
            title="New Title",
            description="New Description",
            labels=["bug", "urgent"],
            add_labels=["feature"],
            remove_labels=["old"],
            state_event="close",
            assignee_ids=[123, 456],
            confidential=True,
            weight=5,
        )
        assert endpoint == "/projects/test/issues/1"
        expected_payload = {
            "title": "New Title",
            "description": "New Description",
            "labels": "bug,urgent",
            "add_labels": "feature",
            "remove_labels": "old",
            "state_event": "close",
            "assignee_ids": [123, 456],
            "confidential": True,
            "weight": 5,
        }
        assert payload == expected_payload
