"""pytest 설정."""

import os

import pytest


@pytest.fixture
def api_key() -> str:
    """테스트용 API 키."""
    return os.environ.get("OPENDART_API_KEY", "test_api_key")


@pytest.fixture
def sample_corp_code() -> str:
    """삼성전자 고유번호."""
    return "00126380"
