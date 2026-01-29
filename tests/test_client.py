"""클라이언트 테스트."""

import pytest

from opendart_fss import OpenDartClient
from opendart_fss.api.disclosure import DisclosureAPI
from opendart_fss.api.financial import FinancialAPI
from opendart_fss.api.major_event import MajorEventAPI
from opendart_fss.api.registration import RegistrationAPI
from opendart_fss.api.report import ReportAPI
from opendart_fss.api.shareholder import ShareholderAPI


class TestOpenDartClient:
    """OpenDartClient 테스트."""

    def test_client_initialization(self, api_key: str) -> None:
        """클라이언트 초기화 테스트."""
        client = OpenDartClient(api_key=api_key)

        assert client.api_key == api_key
        assert isinstance(client.disclosure, DisclosureAPI)
        assert isinstance(client.report, ReportAPI)
        assert isinstance(client.financial, FinancialAPI)
        assert isinstance(client.shareholder, ShareholderAPI)
        assert isinstance(client.major_event, MajorEventAPI)
        assert isinstance(client.registration, RegistrationAPI)

    @pytest.mark.asyncio
    async def test_client_context_manager(self, api_key: str) -> None:
        """컨텍스트 매니저 테스트."""
        async with OpenDartClient(api_key=api_key) as client:
            assert client.api_key == api_key
            assert not client._http.is_closed

        # 컨텍스트 종료 후 HTTP 클라이언트가 닫혀야 함
        assert client._http.is_closed

    @pytest.mark.asyncio
    async def test_client_close(self, api_key: str) -> None:
        """클라이언트 종료 테스트."""
        client = OpenDartClient(api_key=api_key)
        assert not client._http.is_closed

        await client.close()
        assert client._http.is_closed
