"""통합 테스트: 엔드포인트 검증."""

import pytest

from opendart_fss.verification import (
    ENDPOINT_CONFIGS,
    EndpointVerifier,
    VerificationStatus,
    generate_report,
)


@pytest.mark.integration
@pytest.mark.asyncio
async def test_verify_single_endpoint(api_key: str) -> None:
    """단일 엔드포인트 검증 테스트."""
    async with EndpointVerifier(api_key=api_key) as verifier:
        result = await verifier.verify_endpoint("DS001-02")  # get_company

    assert result.endpoint_id == "DS001-02"
    assert result.status in (
        VerificationStatus.SUCCESS,
        VerificationStatus.NO_DATA,
    )
    assert result.response_time_ms > 0


@pytest.mark.integration
@pytest.mark.asyncio
async def test_verify_category(api_key: str) -> None:
    """카테고리별 검증 테스트."""
    async with EndpointVerifier(api_key=api_key) as verifier:
        results = await verifier.verify_category("DS001")

    # DS001에는 4개의 엔드포인트가 있음
    assert len(results) == 4

    for result in results:
        assert result.category == "DS001"
        # 모든 결과는 성공, 데이터 없음, 또는 스킵 상태여야 함
        # (rcept_no가 필요한 엔드포인트는 스킵될 수 있음)
        assert result.status in (
            VerificationStatus.SUCCESS,
            VerificationStatus.NO_DATA,
            VerificationStatus.SKIPPED,
        )


@pytest.mark.integration
@pytest.mark.asyncio
async def test_verify_all_endpoints(api_key: str) -> None:
    """모든 엔드포인트 검증 테스트.

    이 테스트는 모든 28개 엔드포인트를 검증합니다.
    Rate limit을 피하기 위해 적응형 rate limiter가 사용됩니다.
    """
    async with EndpointVerifier(api_key=api_key) as verifier:
        results = await verifier.verify_all()

    assert len(results) == len(ENDPOINT_CONFIGS)

    # 최소한 일부는 성공해야 함
    success_count = sum(
        1
        for r in results
        if r.status in (VerificationStatus.SUCCESS, VerificationStatus.NO_DATA)
    )
    assert success_count > 0, "At least some endpoints should succeed"

    # 실패한 엔드포인트 출력
    failed = [r for r in results if r.status == VerificationStatus.FAILED]
    if failed:
        print("\nFailed endpoints:")
        for r in failed:
            print(f"  - {r.endpoint_name}: {r.error_message}")


@pytest.mark.integration
@pytest.mark.asyncio
async def test_generate_report_console(api_key: str) -> None:
    """콘솔 리포트 생성 테스트."""
    async with EndpointVerifier(api_key=api_key) as verifier:
        results = await verifier.verify_category("DS001")

    report = generate_report(results, duration_seconds=1.0, format="console")

    assert "OpenDART API Endpoint Verification Report" in report
    assert "DS001" in report
    assert "disclosure" in report


@pytest.mark.integration
@pytest.mark.asyncio
async def test_generate_report_json(api_key: str) -> None:
    """JSON 리포트 생성 테스트."""
    import json

    async with EndpointVerifier(api_key=api_key) as verifier:
        results = await verifier.verify_category("DS001")

    report = generate_report(results, duration_seconds=1.0, format="json")
    data = json.loads(report)

    assert "timestamp" in data
    assert "summary" in data
    assert "results" in data
    assert len(data["results"]) == 4


@pytest.mark.integration
@pytest.mark.asyncio
async def test_generate_report_markdown(api_key: str) -> None:
    """마크다운 리포트 생성 테스트."""
    async with EndpointVerifier(api_key=api_key) as verifier:
        results = await verifier.verify_category("DS001")

    report = generate_report(results, duration_seconds=1.0, format="markdown")

    assert "# OpenDART API Endpoint Verification Report" in report
    assert "## Summary" in report
    assert "| Status |" in report


@pytest.mark.integration
@pytest.mark.asyncio
async def test_rcept_no_propagation(api_key: str) -> None:
    """rcept_no 전파 테스트.

    disclosure.search에서 얻은 rcept_no가
    download_document와 download_xbrl에 전파되는지 확인합니다.
    """
    async with EndpointVerifier(api_key=api_key) as verifier:
        # 먼저 search를 실행하여 rcept_no를 획득
        search_result = await verifier.verify_endpoint("DS001-01")
        assert search_result.status in (
            VerificationStatus.SUCCESS,
            VerificationStatus.NO_DATA,
        )

        # rcept_no가 있으면 download_document 테스트
        if search_result.status == VerificationStatus.SUCCESS:
            doc_result = await verifier.verify_endpoint("DS001-03")
            # 스킵되지 않아야 함 (rcept_no가 있으므로)
            assert doc_result.status != VerificationStatus.SKIPPED
