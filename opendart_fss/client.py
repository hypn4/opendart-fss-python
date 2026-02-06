"""OpenDART API 클라이언트."""

import os

import httpx
from dotenv import load_dotenv

from opendart_fss.api.disclosure import DisclosureAPI
from opendart_fss.api.financial import FinancialAPI
from opendart_fss.api.major_event import MajorEventAPI
from opendart_fss.api.registration import RegistrationAPI
from opendart_fss.api.report import ReportAPI
from opendart_fss.api.shareholder import ShareholderAPI

load_dotenv()


class OpenDartClient:
    """OpenDART API 클라이언트.

    Example:
        ```python
        client = OpenDartClient(api_key="YOUR_API_KEY")

        # 공시 검색
        disclosures = await client.disclosure.search(
            corp_code="00126380",
            bgn_de="20240101",
            end_de="20241231"
        )

        # 기업 개황
        company = await client.disclosure.get_company("00126380")
        print(f"회사명: {company.corp_name}")

        # 재무제표 조회
        financials = await client.financial.get_single_account(
            corp_code="00126380",
            bsns_year="2024",
            reprt_code="11011"
        )

        await client.close()  # 또는 contextlib.aclosing() 사용
        ```
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        timeout: float = 30.0,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        """클라이언트 초기화.

        Args:
            api_key: OpenDART API 키. 생략 시 OPENDART_API_KEY 환경변수 사용
            timeout: HTTP 요청 타임아웃 (초)
            http_client: 커스텀 httpx.AsyncClient (선택)

        Raises:
            ValueError: API 키가 제공되지 않고 환경변수도 설정되지 않은 경우
        """
        self.api_key = api_key or os.environ.get("OPENDART_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key is required. "
                "Provide api_key parameter or set OPENDART_API_KEY environment variable."
            )
        self._timeout = timeout
        self._external_client = http_client is not None
        self._http = http_client or httpx.AsyncClient(timeout=timeout)

        # API 모듈 초기화
        self.disclosure = DisclosureAPI(self)
        self.report = ReportAPI(self)
        self.financial = FinancialAPI(self)
        self.shareholder = ShareholderAPI(self)
        self.major_event = MajorEventAPI(self)
        self.registration = RegistrationAPI(self)

    async def aclose(self) -> None:
        """HTTP 클라이언트 종료."""
        if not self._external_client:
            await self._http.aclose()

    close = aclose  # alias
