"""OpenDART FSS Python SDK.

금융감독원 전자공시시스템 OpenDART API를 위한 Python SDK입니다.

Example:
    ```python
    import asyncio
    from opendart_fss import OpenDartClient

    async def main():
        async with OpenDartClient(api_key="YOUR_API_KEY") as client:
            # 공시 검색
            disclosures = await client.disclosure.search(
                corp_code="00126380",
                bgn_de="20240101",
                end_de="20241231"
            )

            # 기업 개황
            company = await client.disclosure.get_company("00126380")
            print(f"회사명: {company.corp_name}")
            print(f"대표자: {company.ceo_nm}")

            # 재무제표 조회
            financials = await client.financial.get_single_account(
                corp_code="00126380",
                bsns_year="2024",
                reprt_code="11011"  # 사업보고서
            )

            for item in financials:
                print(f"{item.account_nm}: {item.thstrm_amount}")

    asyncio.run(main())
    ```
"""

from opendart_fss.client import OpenDartClient
from opendart_fss.constants import (
    CorpClass,
    DisclosureType,
    FinancialStatementType,
    ReportCode,
    StatusCode,
)
from opendart_fss.exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    OpenDartError,
    RateLimitError,
    ServerError,
    ValidationError,
)

try:
    from opendart_fss._version import __version__
except ImportError:
    __version__ = "0.0.0"  # fallback for editable installs without build
__all__ = [
    # Client
    "OpenDartClient",
    # Constants
    "StatusCode",
    "ReportCode",
    "CorpClass",
    "DisclosureType",
    "FinancialStatementType",
    # Exceptions
    "OpenDartError",
    "APIError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError",
    "NotFoundError",
    "ServerError",
]
