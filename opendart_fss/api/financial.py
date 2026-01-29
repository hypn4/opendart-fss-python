"""DS003 정기보고서 재무정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.financial import (
    FinancialAccount,
    FinancialAccountListResponse,
    FinancialIndicator,
    FinancialIndicatorListResponse,
    XbrlTaxonomy,
    XbrlTaxonomyListResponse,
)


class FinancialAPI(BaseAPI):
    """정기보고서 재무정보 API (DS003)."""

    async def get_single_account(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
        fs_div: str = "CFS",
    ) -> list[FinancialAccount]:
        """단일회사 주요계정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)
            fs_div: 개별/연결 구분 (CFS/OFS)

        Returns:
            주요계정 목록
        """
        response = await self._get(
            "/api/fnlttSinglAcnt.json",
            FinancialAccountListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "fs_div": fs_div,
            },
        )
        return response.items

    async def get_multi_account(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
        fs_div: str = "CFS",
    ) -> list[FinancialAccount]:
        """다중회사 주요계정 조회.

        Args:
            corp_code: 고유번호 (쉼표로 구분, 최대 100개)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)
            fs_div: 개별/연결 구분 (CFS/OFS)

        Returns:
            주요계정 목록
        """
        response = await self._get(
            "/api/fnlttMultiAcnt.json",
            FinancialAccountListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "fs_div": fs_div,
            },
        )
        return response.items

    async def get_full_statements(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
        fs_div: str = "CFS",
    ) -> list[FinancialAccount]:
        """단일회사 전체 재무제표 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)
            fs_div: 개별/연결 구분 (CFS/OFS)

        Returns:
            전체 재무제표 계정 목록
        """
        response = await self._get(
            "/api/fnlttSinglAcntAll.json",
            FinancialAccountListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "fs_div": fs_div,
            },
        )
        return response.items

    async def download_xbrl(
        self,
        rcept_no: str,
        reprt_code: str,
    ) -> bytes:
        """XBRL 원본파일 다운로드.

        Args:
            rcept_no: 접수번호 (14자리)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            ZIP 파일 바이트
        """
        return await self._download(
            "/api/fnlttXbrl.xml",
            params={
                "rcept_no": rcept_no,
                "reprt_code": reprt_code,
            },
        )

    async def get_xbrl_taxonomy(
        self,
        sj_div: str,
    ) -> list[XbrlTaxonomy]:
        """XBRL 택사노미 조회.

        Args:
            sj_div: 재무제표구분 (BS/IS/CIS/CF/SCE)

        Returns:
            택사노미 목록
        """
        response = await self._get(
            "/api/xbrlTaxonomy.json",
            XbrlTaxonomyListResponse,
            params={"sj_div": sj_div},
        )
        return response.items

    async def get_indicators(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
        idx_cl_code: str | None = None,
    ) -> list[FinancialIndicator]:
        """다중회사 재무지표 조회.

        Args:
            corp_code: 고유번호 (쉼표로 구분, 최대 100개)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)
            idx_cl_code: 지표분류코드 (선택)

        Returns:
            재무지표 목록
        """
        response = await self._get(
            "/api/fnlttCmpnyIndx.json",
            FinancialIndicatorListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "idx_cl_code": idx_cl_code,
            },
        )
        return response.items

    async def get_single_indicators(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
        idx_cl_code: str,
    ) -> list[FinancialIndicator]:
        """단일회사 주요 재무지표 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY, 2023년 3분기 이후)
            reprt_code: 보고서 코드 (11011~11014)
            idx_cl_code: 지표분류코드 (M210000~M240000)

        Returns:
            재무지표 목록
        """
        response = await self._get(
            "/api/fnlttSinglIndx.json",
            FinancialIndicatorListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
                "idx_cl_code": idx_cl_code,
            },
        )
        return response.items
