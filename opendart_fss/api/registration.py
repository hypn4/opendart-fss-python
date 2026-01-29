"""DS006 증권신고서 주요정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.registration import (
    DebtSecurities,
    DebtSecuritiesListResponse,
    DepositaryReceipt,
    DepositaryReceiptListResponse,
    EquitySecurities,
    EquitySecuritiesListResponse,
    MergerRegistration,
    MergerRegistrationListResponse,
    SplitRegistration,
    SplitRegistrationListResponse,
    StockExchangeTransfer,
    StockExchangeTransferListResponse,
)


class RegistrationAPI(BaseAPI):
    """증권신고서 주요정보 API (DS006)."""

    async def get_equity_securities(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[EquitySecurities]:
        """지분증권 발행 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            지분증권 발행 목록
        """
        response = await self._get(
            "/api/estkRs.json",
            EquitySecuritiesListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_debt_securities(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[DebtSecurities]:
        """채무증권 발행 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            채무증권 발행 목록
        """
        response = await self._get(
            "/api/bdRs.json",
            DebtSecuritiesListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_merger_registration(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[MergerRegistration]:
        """합병 신고 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            합병 신고 목록
        """
        response = await self._get(
            "/api/mgRs.json",
            MergerRegistrationListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_split_registration(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[SplitRegistration]:
        """분할 신고 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            분할 신고 목록
        """
        response = await self._get(
            "/api/dvRs.json",
            SplitRegistrationListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_depositary_receipt(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[DepositaryReceipt]:
        """증권예탁증권 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            증권예탁증권 목록
        """
        response = await self._get(
            "/api/stkdpRs.json",
            DepositaryReceiptListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_stock_exchange_transfer(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[StockExchangeTransfer]:
        """주식의 포괄적 교환·이전 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            주식의 포괄적 교환·이전 목록
        """
        response = await self._get(
            "/api/extrRs.json",
            StockExchangeTransferListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items
