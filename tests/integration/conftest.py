"""통합 테스트 fixtures."""

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """pytest 설정."""
    config.addinivalue_line(
        "markers",
        "integration: mark test as integration test (requires API key)",
    )


@pytest.fixture(scope="session")
def api_key() -> str:
    """실제 API 키.

    환경변수 OPENDART_API_KEY가 설정되어 있어야 합니다.
    """
    key = os.environ.get("OPENDART_API_KEY")
    if not key:
        pytest.skip("OPENDART_API_KEY environment variable not set")
    return key


@pytest.fixture
def test_data() -> dict[str, str]:
    """테스트 데이터."""
    return {
        "corp_code": "00126380",  # 삼성전자
        "bsns_year": "2023",
        "reprt_code": "11011",  # 사업보고서
        "bgn_de": "20230101",
        "end_de": "20231231",
        "fs_div": "CFS",
        "sj_div": "BS",
    }
