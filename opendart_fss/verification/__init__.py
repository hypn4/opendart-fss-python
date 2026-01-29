"""OpenDART API 엔드포인트 검증 모듈.

이 모듈은 OpenDART API의 모든 엔드포인트를 실제 호출하여 검증합니다.

Example:
    ```python
    import asyncio
    from opendart_fss.verification import EndpointVerifier, generate_report

    async def main():
        verifier = EndpointVerifier()
        results = await verifier.verify_all()
        report = generate_report(results, format="console")
        print(report)

    asyncio.run(main())
    ```
"""

from opendart_fss.verification.config import (
    DEFAULT_TEST_DATA,
    ENDPOINT_CONFIGS,
    FALLBACK_CORP_CODES,
    EndpointConfig,
    VerificationResult,
    VerificationStatus,
)
from opendart_fss.verification.rate_limiter import AdaptiveRateLimiter
from opendart_fss.verification.reporter import (
    VerificationReport,
    generate_report,
)
from opendart_fss.verification.runner import EndpointVerifier

__all__ = [
    # Config
    "EndpointConfig",
    "VerificationResult",
    "VerificationStatus",
    "ENDPOINT_CONFIGS",
    "DEFAULT_TEST_DATA",
    "FALLBACK_CORP_CODES",
    # Rate Limiter
    "AdaptiveRateLimiter",
    # Runner
    "EndpointVerifier",
    # Reporter
    "VerificationReport",
    "generate_report",
]
