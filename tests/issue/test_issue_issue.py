"""Unit tests for the issue resource."""

from unittest.mock import MagicMock

from glnova.issue.issue import Issue


class TestIssue:
    """Test cases for the Issue class."""

    def test_list_issues_minimal(self, mocker):
        """Test list_issues with minimal parameters."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "title": "Test Issue"}]

        mocker.patch.object(issue, "_list_issues", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=([{"id": 1, "title": "Test Issue"}], 200, "etag123"),
        )

        result = issue.list_issues()

        assert result == ([{"id": 1, "title": "Test Issue"}], 200, "etag123")
        issue._list_issues.assert_called_once_with(
            group=None,
            project=None,
            assignee_id=None,
            assignee_username=None,
            author_id=None,
            author_username=None,
            confidential=None,
            created_after=None,
            created_before=None,
            due_date=None,
            epic_id=None,
            health_status=None,
            iids=None,
            search_in=None,
            issue_type=None,
            iteration_id=None,
            iteration_title=None,
            labels=None,
            milestone_id=None,
            milestone=None,
            my_reaction_emoji=None,
            non_archived=None,
            not_match=None,
            order_by=None,
            scope=None,
            search=None,
            sort=None,
            state=None,
            updated_after=None,
            updated_before=None,
            weight=None,
            with_labels_details=None,
            cursor=None,
            page=1,
            per_page=20,
            etag=None,
        )

    def test_list_issues_with_params(self, mocker):
        """Test list_issues with various parameters."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 2, "title": "Filtered Issue"}]

        mocker.patch.object(issue, "_list_issues", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=([{"id": 2, "title": "Filtered Issue"}], 200, "etag456"),
        )

        result = issue.list_issues(
            project="test/project",
            state="opened",
            labels=["bug"],
            page=2,
            per_page=10,
            etag="old_etag",
        )

        assert result == ([{"id": 2, "title": "Filtered Issue"}], 200, "etag456")
        issue._list_issues.assert_called_once_with(
            group=None,
            project="test/project",
            assignee_id=None,
            assignee_username=None,
            author_id=None,
            author_username=None,
            confidential=None,
            created_after=None,
            created_before=None,
            due_date=None,
            epic_id=None,
            health_status=None,
            iids=None,
            search_in=None,
            issue_type=None,
            iteration_id=None,
            iteration_title=None,
            labels=["bug"],
            milestone_id=None,
            milestone=None,
            my_reaction_emoji=None,
            non_archived=None,
            not_match=None,
            order_by=None,
            scope=None,
            search=None,
            sort=None,
            state="opened",
            updated_after=None,
            updated_before=None,
            weight=None,
            with_labels_details=None,
            cursor=None,
            page=2,
            per_page=10,
            etag="old_etag",
        )

    def test_get_issue_by_id(self, mocker):
        """Test get_issue with issue_id."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 123, "title": "Test Issue"}

        mocker.patch.object(issue, "_get_issue", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=({"id": 123, "title": "Test Issue"}, 200, "etag789"),
        )

        result = issue.get_issue(issue_id=123)

        assert result == ({"id": 123, "title": "Test Issue"}, 200, "etag789")
        issue._get_issue.assert_called_once_with(issue_id=123, project_id=None, issue_iid=None, etag=None)

    def test_get_issue_by_project_iid(self, mocker):
        """Test get_issue with project_id and issue_iid."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 456, "iid": 10, "title": "Project Issue"}

        mocker.patch.object(issue, "_get_issue", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=({"id": 456, "iid": 10, "title": "Project Issue"}, 200, "etag101"),
        )

        result = issue.get_issue(project_id="test/project", issue_iid=10, etag="old_etag")

        assert result == ({"id": 456, "iid": 10, "title": "Project Issue"}, 200, "etag101")
        issue._get_issue.assert_called_once_with(
            issue_id=None, project_id="test/project", issue_iid=10, etag="old_etag"
        )

    def test_edit_issue_minimal(self, mocker):
        """Test edit_issue with minimal parameters."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 789, "title": "Updated Issue"}

        mocker.patch.object(issue, "_edit_issue", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=({"id": 789, "title": "Updated Issue"}, 200, "etag202"),
        )

        result = issue.edit_issue(project_id="test/project", issue_iid=5)

        assert result == ({"id": 789, "title": "Updated Issue"}, 200, "etag202")
        issue._edit_issue.assert_called_once_with(
            project_id="test/project",
            issue_iid=5,
            add_labels=None,
            assignee_ids=None,
            confidential=None,
            description=None,
            discussion_locked=None,
            due_date=None,
            epic_id=None,
            epic_iid=None,
            issue_type=None,
            labels=None,
            milestone_id=None,
            remove_labels=None,
            state_event=None,
            title=None,
            updated_at=None,
            weight=None,
        )

    def test_edit_issue_with_params(self, mocker):
        """Test edit_issue with various parameters."""
        mock_client = MagicMock()
        issue = Issue(client=mock_client)

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 101, "title": "Fully Updated Issue"}

        mocker.patch.object(issue, "_edit_issue", return_value=mock_response)
        mocker.patch(
            "glnova.issue.issue.process_response_with_last_modified",
            return_value=({"id": 101, "title": "Fully Updated Issue"}, 200, "etag303"),
        )

        result = issue.edit_issue(
            project_id=123,
            issue_iid=7,
            title="New Title",
            description="New Description",
            labels=["urgent", "bug"],
            add_labels=["feature"],
            remove_labels=["old"],
            state_event="close",
            assignee_ids=[456, 789],
            confidential=True,
            weight=3,
        )

        assert result == ({"id": 101, "title": "Fully Updated Issue"}, 200, "etag303")
        issue._edit_issue.assert_called_once_with(
            project_id=123,
            issue_iid=7,
            add_labels=["feature"],
            assignee_ids=[456, 789],
            confidential=True,
            description="New Description",
            discussion_locked=None,
            due_date=None,
            epic_id=None,
            epic_iid=None,
            issue_type=None,
            labels=["urgent", "bug"],
            milestone_id=None,
            remove_labels=["old"],
            state_event="close",
            title="New Title",
            updated_at=None,
            weight=3,
        )
