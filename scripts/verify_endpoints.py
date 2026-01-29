#!/usr/bin/env python
"""OpenDART API 엔드포인트 검증 CLI.

사용 예시:
    # 콘솔 출력 (기본)
    uv run python scripts/verify_endpoints.py

    # JSON 출력
    uv run python scripts/verify_endpoints.py --format json

    # 마크다운 파일로 저장
    uv run python scripts/verify_endpoints.py --format markdown -o report.md

    # 특정 카테고리만 검증
    uv run python scripts/verify_endpoints.py --category DS001

    # 특정 엔드포인트만 검증
    uv run python scripts/verify_endpoints.py --endpoint DS001-01
"""

import argparse
import asyncio
import sys
import time
from pathlib import Path

# 프로젝트 루트를 path에 추가
sys.path.insert(0, str(Path(__file__).parent.parent))

from opendart_fss.verification import EndpointVerifier, generate_report


async def main() -> int:
    """메인 함수."""
    parser = argparse.ArgumentParser(
        description="OpenDART API 엔드포인트 검증",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["console", "json", "markdown"],
        default="console",
        help="출력 형식 (기본: console)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        help="결과를 파일로 저장",
    )
    parser.add_argument(
        "--category",
        "-c",
        help="특정 카테고리만 검증 (예: DS001, DS002, ...)",
    )
    parser.add_argument(
        "--endpoint",
        "-e",
        help="특정 엔드포인트만 검증 (예: DS001-01)",
    )
    parser.add_argument(
        "--api-key",
        help="OpenDART API 키 (기본: OPENDART_API_KEY 환경변수)",
    )

    args = parser.parse_args()

    print("OpenDART API Endpoint Verification")
    print("-" * 40)

    start_time = time.perf_counter()

    try:
        async with EndpointVerifier(api_key=args.api_key) as verifier:
            if args.endpoint:
                print(f"Verifying endpoint: {args.endpoint}")
                results = [await verifier.verify_endpoint(args.endpoint)]
            elif args.category:
                print(f"Verifying category: {args.category}")
                results = await verifier.verify_category(args.category)
            else:
                print("Verifying all endpoints...")
                results = await verifier.verify_all()

    except ValueError as e:
        print(f"Error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

    duration = time.perf_counter() - start_time

    # 리포트 생성
    report = generate_report(results, duration, format=args.format)

    # 출력 또는 저장
    if args.output:
        args.output.write_text(report, encoding="utf-8")
        print(f"\nReport saved to: {args.output}")

        # 콘솔에도 요약 출력
        if args.format != "console":
            success = sum(1 for r in results if r.status.value == "SUCCESS")
            no_data = sum(1 for r in results if r.status.value == "NO_DATA")
            failed = sum(1 for r in results if r.status.value == "FAILED")
            skipped = sum(1 for r in results if r.status.value == "SKIPPED")
            print(
                f"\nSummary: {success} success, {no_data} no data, "
                f"{failed} failed, {skipped} skipped"
            )
    else:
        print()
        print(report)

    # 실패가 있으면 exit code 1
    failed_count = sum(1 for r in results if r.status.value == "FAILED")
    return 1 if failed_count > 0 else 0


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
