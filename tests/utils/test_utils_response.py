"""Unit tests for response utilities."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from glnova.utils.response import process_async_response_with_last_modified, process_response_with_last_modified


class TestResponseUtils:
    """Test cases for response processing utilities."""

    def test_process_response_with_last_modified_200(self, mocker):
        """Test process_response_with_last_modified with 200 status."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_response.headers = {"Etag": "etag123"}

        result = process_response_with_last_modified(mock_response)

        assert result == ({"key": "value"}, 200, "etag123")
        mock_response.json.assert_called_once()

    def test_process_response_with_last_modified_not_200(self, mocker):
        """Test process_response_with_last_modified with non-200 status."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.headers = {"Etag": "etag123"}

        result = process_response_with_last_modified(mock_response)

        assert result == ({}, 404, "etag123")
        mock_response.json.assert_not_called()

    def test_process_response_with_last_modified_no_etag(self, mocker):
        """Test process_response_with_last_modified without ETag."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}
        mock_response.headers = {}

        result = process_response_with_last_modified(mock_response)

        assert result == ({"key": "value"}, 200, None)

    @pytest.mark.asyncio
    async def test_process_async_response_with_last_modified_200(self, mocker):
        """Test process_async_response_with_last_modified with 200 status."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"key": "value"})
        mock_response.headers = {"Etag": "etag123"}

        result = await process_async_response_with_last_modified(mock_response)

        assert result == ({"key": "value"}, 200, "etag123")
        mock_response.json.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_async_response_with_last_modified_not_200(self, mocker):
        """Test process_async_response_with_last_modified with non-200 status."""
        mock_response = MagicMock()
        mock_response.status = 404
        mock_response.headers = {"Etag": "etag123"}

        result = await process_async_response_with_last_modified(mock_response)

        assert result == ({}, 404, "etag123")
        mock_response.json.assert_not_called()

    @pytest.mark.asyncio
    async def test_process_async_response_with_last_modified_no_etag(self, mocker):
        """Test process_async_response_with_last_modified without ETag."""
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json = AsyncMock(return_value={"key": "value"})
        mock_response.headers = {}

        result = await process_async_response_with_last_modified(mock_response)

        assert result == ({"key": "value"}, 200, None)
