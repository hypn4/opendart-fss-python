"""DS001 공시정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.disclosure import (
    Company,
    CompanyResponse,
    Disclosure,
    DisclosureListResponse,
)


class DisclosureAPI(BaseAPI):
    """공시정보 API (DS001)."""

    async def search(
        self,
        *,
        corp_code: str | None = None,
        bgn_de: str | None = None,
        end_de: str | None = None,
        last_reprt_at: str | None = None,
        pblntf_ty: str | None = None,
        pblntf_detail_ty: str | None = None,
        corp_cls: str | None = None,
        sort: str | None = None,
        sort_mth: str | None = None,
        page_no: int | None = None,
        page_count: int | None = None,
    ) -> list[Disclosure]:
        """공시검색.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)
            last_reprt_at: 최종보고서만 검색여부 (Y/N)
            pblntf_ty: 공시유형 (A~J)
            pblntf_detail_ty: 공시상세유형
            corp_cls: 법인구분 (Y/K/N/E)
            sort: 정렬 기준 (date/crp/rpt)
            sort_mth: 정렬 방법 (asc/desc)
            page_no: 페이지 번호
            page_count: 페이지당 건수 (최대 100)

        Returns:
            공시 목록
        """
        response = await self._get(
            "/api/list.json",
            DisclosureListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
                "last_reprt_at": last_reprt_at,
                "pblntf_ty": pblntf_ty,
                "pblntf_detail_ty": pblntf_detail_ty,
                "corp_cls": corp_cls,
                "sort": sort,
                "sort_mth": sort_mth,
                "page_no": page_no,
                "page_count": page_count,
            },
        )
        return response.items

    async def get_company(self, corp_code: str) -> Company:
        """기업개황 조회.

        Args:
            corp_code: 고유번호 (8자리)

        Returns:
            기업 개황 정보
        """
        response = await self._get(
            "/api/company.json",
            CompanyResponse,
            params={"corp_code": corp_code},
        )
        return response.to_company()

    async def download_document(self, rcept_no: str) -> bytes:
        """공시서류 원본 다운로드.

        Args:
            rcept_no: 접수번호 (14자리)

        Returns:
            ZIP 파일 바이트
        """
        return await self._download(
            "/api/document.xml",
            params={"rcept_no": rcept_no},
        )

    async def download_corp_codes(self) -> bytes:
        """고유번호 전체 다운로드.

        Returns:
            ZIP 파일 바이트 (CORPCODE.xml 포함)
        """
        return await self._download("/api/corpCode.xml")
