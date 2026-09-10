"""Shared pytest fixtures for the Digna SDK test suite."""

from __future__ import annotations

import pytest

from digna_sdk import DignaClient

BASE_URL = "http://digna.test"


@pytest.fixture
def client() -> DignaClient:
    return DignaClient(base_url=BASE_URL, token="test-token")
