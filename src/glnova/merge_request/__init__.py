"""Merge request package for glnova."""

from __future__ import annotations

from glnova.merge_request.async_merge_request import AsyncMergeRequest
from glnova.merge_request.merge_request import MergeRequest

__all__ = [
    "AsyncMergeRequest",
    "MergeRequest",
]
