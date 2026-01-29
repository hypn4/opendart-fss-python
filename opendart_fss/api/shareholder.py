"""DS004 지분공시 종합정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.shareholder import (
    ExecutiveStock,
    ExecutiveStockListResponse,
    MajorStock,
    MajorStockListResponse,
)


class ShareholderAPI(BaseAPI):
    """지분공시 종합정보 API (DS004)."""

    async def get_major_stock(
        self,
        corp_code: str,
    ) -> list[MajorStock]:
        """대량보유 상황보고 조회.

        Args:
            corp_code: 고유번호 (8자리)

        Returns:
            대량보유 상황보고 목록
        """
        response = await self._get(
            "/api/majorstock.json",
            MajorStockListResponse,
            params={"corp_code": corp_code},
        )
        return response.items

    async def get_executive_stock(
        self,
        corp_code: str,
    ) -> list[ExecutiveStock]:
        """임원/주요주주 소유보고 조회.

        Args:
            corp_code: 고유번호 (8자리)

        Returns:
            임원/주요주주 소유보고 목록
        """
        response = await self._get(
            "/api/elestock.json",
            ExecutiveStockListResponse,
            params={"corp_code": corp_code},
        )
        return response.items
