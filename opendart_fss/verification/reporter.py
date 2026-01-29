"""검증 결과 리포트 생성."""

import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from opendart_fss.verification.config import (
    CATEGORY_DESCRIPTIONS,
    VerificationResult,
    VerificationStatus,
)


@dataclass
class VerificationReport:
    """검증 리포트."""

    timestamp: str
    duration_seconds: float
    total_endpoints: int
    success_count: int
    no_data_count: int
    failed_count: int
    skipped_count: int
    results: list[VerificationResult] = field(default_factory=list)

    @property
    def success_rate(self) -> float:
        """성공률 (SUCCESS + NO_DATA)."""
        if self.total_endpoints == 0:
            return 0.0
        return ((self.success_count + self.no_data_count) / self.total_endpoints) * 100

    @classmethod
    def from_results(
        cls,
        results: list[VerificationResult],
        duration_seconds: float,
    ) -> "VerificationReport":
        """검증 결과로부터 리포트 생성.

        Args:
            results: 검증 결과 목록
            duration_seconds: 총 소요 시간 (초)

        Returns:
            검증 리포트
        """
        success_count = sum(
            1 for r in results if r.status == VerificationStatus.SUCCESS
        )
        no_data_count = sum(
            1 for r in results if r.status == VerificationStatus.NO_DATA
        )
        failed_count = sum(1 for r in results if r.status == VerificationStatus.FAILED)
        skipped_count = sum(
            1 for r in results if r.status == VerificationStatus.SKIPPED
        )

        return cls(
            timestamp=datetime.now().isoformat(timespec="seconds"),
            duration_seconds=duration_seconds,
            total_endpoints=len(results),
            success_count=success_count,
            no_data_count=no_data_count,
            failed_count=failed_count,
            skipped_count=skipped_count,
            results=results,
        )


def generate_report(
    results: list[VerificationResult],
    duration_seconds: float,
    format: Literal["console", "json", "markdown"] = "console",
) -> str:
    """검증 결과 리포트 생성.

    Args:
        results: 검증 결과 목록
        duration_seconds: 총 소요 시간 (초)
        format: 출력 형식 (console/json/markdown)

    Returns:
        포맷팅된 리포트 문자열
    """
    report = VerificationReport.from_results(results, duration_seconds)

    if format == "json":
        return _generate_json(report)
    elif format == "markdown":
        return _generate_markdown(report)
    else:
        return _generate_console(report)


def _generate_console(report: VerificationReport) -> str:
    """콘솔 출력 형식 리포트 생성."""
    lines = [
        "=" * 60,
        "OpenDART API Endpoint Verification Report",
        "=" * 60,
        f"Timestamp: {report.timestamp}",
        f"Duration: {report.duration_seconds:.1f}s",
        "",
        "Summary:",
        f"  Total Endpoints: {report.total_endpoints}",
        f"  Successful:      {report.success_count} "
        f"({report.success_count / report.total_endpoints * 100:.1f}%)"
        if report.total_endpoints > 0
        else "  Successful:      0",
        f"  No Data:         {report.no_data_count} "
        f"({report.no_data_count / report.total_endpoints * 100:.1f}%)"
        if report.total_endpoints > 0
        else "  No Data:         0",
        f"  Failed:          {report.failed_count} "
        f"({report.failed_count / report.total_endpoints * 100:.1f}%)"
        if report.total_endpoints > 0
        else "  Failed:          0",
        f"  Skipped:         {report.skipped_count} "
        f"({report.skipped_count / report.total_endpoints * 100:.1f}%)"
        if report.total_endpoints > 0
        else "  Skipped:         0",
        "",
    ]

    # 카테고리별 결과 출력
    current_category = None
    for result in report.results:
        if result.category != current_category:
            current_category = result.category
            desc = CATEGORY_DESCRIPTIONS.get(current_category, "")
            lines.append(f"{current_category} - {desc}:")

        status_icon = _get_status_icon(result.status)
        time_str = (
            f"({result.response_time_ms:.0f}ms)" if result.response_time_ms else ""
        )

        if result.error_message:
            lines.append(f"  [{status_icon}] {result.endpoint_name} {time_str}")
            lines.append(f"       {result.error_message}")
        else:
            lines.append(f"  [{status_icon}] {result.endpoint_name} {time_str}")

    lines.append("")
    lines.append("=" * 60)

    return "\n".join(lines)


def _generate_json(report: VerificationReport) -> str:
    """JSON 형식 리포트 생성."""
    data = {
        "timestamp": report.timestamp,
        "duration_seconds": report.duration_seconds,
        "summary": {
            "total": report.total_endpoints,
            "success": report.success_count,
            "no_data": report.no_data_count,
            "failed": report.failed_count,
            "skipped": report.skipped_count,
            "success_rate": report.success_rate,
        },
        "results": [
            {
                "id": r.endpoint_id,
                "name": r.endpoint_name,
                "category": r.category,
                "status": r.status.value,
                "response_time_ms": r.response_time_ms,
                "error_message": r.error_message,
                "response_data": r.response_data,
            }
            for r in report.results
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def _generate_markdown(report: VerificationReport) -> str:
    """마크다운 형식 리포트 생성."""
    lines = [
        "# OpenDART API Endpoint Verification Report",
        "",
        f"- **Timestamp:** {report.timestamp}",
        f"- **Duration:** {report.duration_seconds:.1f}s",
        "",
        "## Summary",
        "",
        "| Metric | Count | Percentage |",
        "|--------|-------|------------|",
    ]

    if report.total_endpoints > 0:
        lines.extend(
            [
                f"| Total | {report.total_endpoints} | 100% |",
                f"| Success | {report.success_count} | "
                f"{report.success_count / report.total_endpoints * 100:.1f}% |",
                f"| No Data | {report.no_data_count} | "
                f"{report.no_data_count / report.total_endpoints * 100:.1f}% |",
                f"| Failed | {report.failed_count} | "
                f"{report.failed_count / report.total_endpoints * 100:.1f}% |",
                f"| Skipped | {report.skipped_count} | "
                f"{report.skipped_count / report.total_endpoints * 100:.1f}% |",
            ]
        )
    else:
        lines.append("| Total | 0 | 0% |")

    lines.extend(["", "## Details", ""])

    # 카테고리별 결과
    current_category = None
    for result in report.results:
        if result.category != current_category:
            current_category = result.category
            desc = CATEGORY_DESCRIPTIONS.get(current_category, "")
            lines.extend(["", f"### {current_category} - {desc}", ""])
            lines.append("| Status | Endpoint | Time (ms) | Notes |")
            lines.append("|--------|----------|-----------|-------|")

        status_badge = _get_status_badge(result.status)
        time_str = f"{result.response_time_ms:.0f}" if result.response_time_ms else "-"
        notes = result.error_message or "-"

        lines.append(
            f"| {status_badge} | {result.endpoint_name} | {time_str} | {notes} |"
        )

    return "\n".join(lines)


def _get_status_icon(status: VerificationStatus) -> str:
    """상태에 따른 아이콘 반환."""
    icons = {
        VerificationStatus.SUCCESS: "OK",
        VerificationStatus.NO_DATA: "NO_DATA",
        VerificationStatus.FAILED: "FAIL",
        VerificationStatus.SKIPPED: "SKIP",
    }
    return icons.get(status, "?")


def _get_status_badge(status: VerificationStatus) -> str:
    """상태에 따른 마크다운 배지 반환."""
    badges = {
        VerificationStatus.SUCCESS: "SUCCESS",
        VerificationStatus.NO_DATA: "NO_DATA",
        VerificationStatus.FAILED: "FAILED",
        VerificationStatus.SKIPPED: "SKIPPED",
    }
    return badges.get(status, "UNKNOWN")
