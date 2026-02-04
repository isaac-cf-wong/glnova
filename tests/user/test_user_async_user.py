"""Unit tests for the async user resource."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from glnova.user.async_user import AsyncUser


class TestAsyncUser:
    """Test cases for the AsyncUser class."""

    @pytest.mark.asyncio
    async def test_get_user_authenticated(self, mocker):
        """Test get_user for authenticated user."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"id": 1, "name": "test"})
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=({"id": 1, "name": "test"}, 200, "etag123"),
        )

        result = await user.get_user()

        assert result == ({"id": 1, "name": "test"}, {"status_code": 200, "etag": "etag123"})
        user._get.assert_called_once_with(endpoint="/user", etag=None)

    @pytest.mark.asyncio
    async def test_get_user_with_id(self, mocker):
        """Test get_user with account_id."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"id": 123, "name": "test"})
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=({"id": 123, "name": "test"}, 200, "etag123"),
        )

        result = await user.get_user(account_id=123)

        assert result == ({"id": 123, "name": "test"}, {"status_code": 200, "etag": "etag123"})
        user._get.assert_called_once_with(endpoint="/users/123", etag=None)

    @pytest.mark.asyncio
    async def test_get_user_with_etag(self, mocker):
        """Test get_user with etag."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 304
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=({}, 304, "etag123"),
        )

        result = await user.get_user(account_id=123, etag="old_etag")

        assert result == ({}, {"status_code": 304, "etag": "etag123"})
        user._get.assert_called_once_with(endpoint="/users/123", etag="old_etag")

    @pytest.mark.asyncio
    async def test_modify_user(self, mocker):
        """Test modify_user."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"id": 123, "name": "updated"})
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_put", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=({"id": 123, "name": "updated"}, 200, "etag123"),
        )

        result = await user.modify_user(account_id=123, name="updated")

        assert result == ({"id": 123, "name": "updated"}, {"status_code": 200, "etag": "etag123"})
        user._put.assert_called_once_with(
            endpoint="/users/123",
            json={"name": "updated"},
        )

    @pytest.mark.asyncio
    async def test_list_users_defaults(self, mocker):
        """Test list_users with default parameters."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=[{"id": 1}, {"id": 2}])
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=(["user1", "user2"], 200, "etag123"),
        )

        result = await user.list_users()

        assert result == (["user1", "user2"], {"status_code": 200, "etag": "etag123"})
        user._get.assert_called_once_with(
            endpoint="/users", params={"page": 1, "per_page": 20, "order_by": "id", "sort": "asc"}, etag=None
        )

    @pytest.mark.asyncio
    async def test_list_users_with_filters(self, mocker):
        """Test list_users with filters."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value=[{"id": 1}])
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=(["user1"], 200, "etag123"),
        )

        result = await user.list_users(username="testuser", active=True, page=2, per_page=10)

        assert result == (["user1"], {"status_code": 200, "etag": "etag123"})
        user._get.assert_called_once_with(
            endpoint="/users",
            params={"username": "testuser", "active": True, "page": 2, "per_page": 10, "order_by": "id", "sort": "asc"},
            etag=None,
        )

    @pytest.mark.asyncio
    async def test_list_users_304(self, mocker):
        """Test list_users with 304 response."""
        mock_client = MagicMock()
        user = AsyncUser(client=mock_client)

        mock_response = MagicMock()
        mock_response.status = 304
        mock_response.headers = {"ETag": "etag123"}

        mocker.patch.object(user, "_get", new_callable=AsyncMock, return_value=mock_response)
        mocker.patch(
            "glnova.user.async_user.process_async_response_with_last_modified",
            new_callable=AsyncMock,
            return_value=({"some": "data"}, 304, "etag123"),
        )

        result = await user.list_users()

        assert result == ([], {"status_code": 304, "etag": "etag123"})  # Special handling for 304 in list_users
