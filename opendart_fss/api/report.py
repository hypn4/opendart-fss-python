"""DS002 정기보고서 주요정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.report import (
    AuditServiceContract,
    AuditServiceContractListResponse,
    AuditorOpinion,
    AuditorOpinionListResponse,
    CommercialPaperBalance,
    CommercialPaperBalanceListResponse,
    ContingentCapitalBalance,
    ContingentCapitalBalanceListResponse,
    CorporateBondBalance,
    CorporateBondBalanceListResponse,
    DebtSecuritiesIssuance,
    DebtSecuritiesIssuanceListResponse,
    DirectorCompensation,
    DirectorCompensationApproval,
    DirectorCompensationApprovalListResponse,
    DirectorCompensationByType,
    DirectorCompensationByTypeListResponse,
    DirectorCompensationListResponse,
    DirectorIndividualCompensation,
    DirectorIndividualCompensationListResponse,
    DividendInfo,
    DividendInfoListResponse,
    Employee,
    EmployeeListResponse,
    Executive,
    ExecutiveListResponse,
    HybridSecuritiesBalance,
    HybridSecuritiesBalanceListResponse,
    IndividualCompensation,
    IndividualCompensationListResponse,
    LargestShareholder,
    LargestShareholderChange,
    LargestShareholderChangeListResponse,
    LargestShareholderListResponse,
    MinorityShareholder,
    MinorityShareholderListResponse,
    NonAuditServiceContract,
    NonAuditServiceContractListResponse,
    OtherCorpInvestment,
    OtherCorpInvestmentListResponse,
    OutsideDirector,
    OutsideDirectorListResponse,
    PrivatePlacementFundUsage,
    PrivatePlacementFundUsageListResponse,
    PublicOfferingFundUsage,
    PublicOfferingFundUsageListResponse,
    ShortTermBondBalance,
    ShortTermBondBalanceListResponse,
    StockChange,
    StockChangeListResponse,
    TotalStockQuantity,
    TotalStockQuantityListResponse,
    TreasuryStock,
    TreasuryStockListResponse,
    UnregisteredExecutiveCompensation,
    UnregisteredExecutiveCompensationListResponse,
)


class ReportAPI(BaseAPI):
    """정기보고서 주요정보 API (DS002)."""

    async def get_stock_changes(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[StockChange]:
        """증자(감자) 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            증자(감자) 현황 목록
        """
        response = await self._get(
            "/api/irdsSttus.json",
            StockChangeListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_dividends(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DividendInfo]:
        """배당에 관한 사항 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            배당 정보 목록
        """
        response = await self._get(
            "/api/alotMatter.json",
            DividendInfoListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_treasury_stock(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[TreasuryStock]:
        """자기주식 취득 및 처분 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            자기주식 현황 목록
        """
        response = await self._get(
            "/api/tesstkAcqsDspsSttus.json",
            TreasuryStockListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_largest_shareholders(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[LargestShareholder]:
        """최대주주 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            최대주주 현황 목록
        """
        response = await self._get(
            "/api/hyslrSttus.json",
            LargestShareholderListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_executives(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[Executive]:
        """임원 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            임원 현황 목록
        """
        response = await self._get(
            "/api/exctvSttus.json",
            ExecutiveListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_employees(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[Employee]:
        """직원 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            직원 현황 목록
        """
        response = await self._get(
            "/api/empSttus.json",
            EmployeeListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_individual_compensation(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[IndividualCompensation]:
        """개인별 보수 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            개인별 보수 현황 목록
        """
        response = await self._get(
            "/api/indvdlByPay.json",
            IndividualCompensationListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_director_compensation(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DirectorCompensation]:
        """이사/감사 보수 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            이사/감사 보수 현황 목록
        """
        response = await self._get(
            "/api/hmvAuditAllSttus.json",
            DirectorCompensationListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_largest_shareholder_changes(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[LargestShareholderChange]:
        """최대주주 변동현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            최대주주 변동현황 목록
        """
        response = await self._get(
            "/api/hyslrChgSttus.json",
            LargestShareholderChangeListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_minority_shareholders(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[MinorityShareholder]:
        """소액주주 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            소액주주 현황 목록
        """
        response = await self._get(
            "/api/mrhlSttus.json",
            MinorityShareholderListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_director_individual_compensation(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DirectorIndividualCompensation]:
        """이사·감사 개인별 보수현황 (5억원 이상) 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            이사·감사 개인별 보수현황 목록
        """
        response = await self._get(
            "/api/hmvAuditIndvdlBySttus.json",
            DirectorIndividualCompensationListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_other_corp_investments(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[OtherCorpInvestment]:
        """타법인 출자현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            타법인 출자현황 목록
        """
        response = await self._get(
            "/api/otrCprInvstmntSttus.json",
            OtherCorpInvestmentListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_total_stock_quantity(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[TotalStockQuantity]:
        """주식의 총수 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            주식의 총수 현황 목록
        """
        response = await self._get(
            "/api/stockTotqySttus.json",
            TotalStockQuantityListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_debt_securities_issuance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DebtSecuritiesIssuance]:
        """채무증권 발행실적 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            채무증권 발행실적 목록
        """
        response = await self._get(
            "/api/detScritsIsuAcmslt.json",
            DebtSecuritiesIssuanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_commercial_paper_balance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[CommercialPaperBalance]:
        """기업어음증권 미상환 잔액 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            기업어음증권 미상환 잔액 목록
        """
        response = await self._get(
            "/api/entrprsBilScritsNrdmpBlce.json",
            CommercialPaperBalanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_short_term_bond_balance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[ShortTermBondBalance]:
        """단기사채 미상환 잔액 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            단기사채 미상환 잔액 목록
        """
        response = await self._get(
            "/api/srtpdPsndbtNrdmpBlce.json",
            ShortTermBondBalanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_corporate_bond_balance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[CorporateBondBalance]:
        """회사채 미상환 잔액 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            회사채 미상환 잔액 목록
        """
        response = await self._get(
            "/api/cprndNrdmpBlce.json",
            CorporateBondBalanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_hybrid_securities_balance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[HybridSecuritiesBalance]:
        """신종자본증권 미상환 잔액 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            신종자본증권 미상환 잔액 목록
        """
        response = await self._get(
            "/api/newCaplScritsNrdmpBlce.json",
            HybridSecuritiesBalanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_contingent_capital_balance(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[ContingentCapitalBalance]:
        """조건부자본증권 미상환 잔액 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            조건부자본증권 미상환 잔액 목록
        """
        response = await self._get(
            "/api/cndlCaplScritsNrdmpBlce.json",
            ContingentCapitalBalanceListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_auditor_opinion(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[AuditorOpinion]:
        """회계감사인의 명칭 및 감사의견 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            회계감사인 정보 목록
        """
        response = await self._get(
            "/api/accnutAdtorNmNdAdtOpinion.json",
            AuditorOpinionListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_audit_service_contract(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[AuditServiceContract]:
        """감사용역 체결현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            감사용역 체결현황 목록
        """
        response = await self._get(
            "/api/adtServcCnclsSttus.json",
            AuditServiceContractListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_non_audit_service_contract(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[NonAuditServiceContract]:
        """회계감사인과의 비감사용역 계약체결 현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            비감사용역 계약체결 현황 목록
        """
        response = await self._get(
            "/api/accnutAdtorNonAdtServcCnclsSttus.json",
            NonAuditServiceContractListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_outside_directors(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[OutsideDirector]:
        """사외이사 및 그 변동현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            사외이사 현황 목록
        """
        response = await self._get(
            "/api/outcmpnyDrctrNdChangeSttus.json",
            OutsideDirectorListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_unregistered_executive_compensation(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[UnregisteredExecutiveCompensation]:
        """미등기임원 보수현황 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            미등기임원 보수현황 목록
        """
        response = await self._get(
            "/api/unrstExctvMendngSttus.json",
            UnregisteredExecutiveCompensationListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_director_compensation_approval(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DirectorCompensationApproval]:
        """이사·감사 보수현황 (주주총회 승인금액) 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            이사·감사 보수현황 목록
        """
        response = await self._get(
            "/api/hmvAuditAllSttus2.json",
            DirectorCompensationApprovalListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_director_compensation_by_type(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[DirectorCompensationByType]:
        """이사·감사 보수현황 (유형별) 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            이사·감사 보수현황 목록
        """
        response = await self._get(
            "/api/hmvAuditAllSttus3.json",
            DirectorCompensationByTypeListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_public_offering_fund_usage(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[PublicOfferingFundUsage]:
        """공모자금의 사용내역 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            공모자금 사용내역 목록
        """
        response = await self._get(
            "/api/pssrpCptalUseDtls.json",
            PublicOfferingFundUsageListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items

    async def get_private_placement_fund_usage(
        self,
        corp_code: str,
        bsns_year: str,
        reprt_code: str,
    ) -> list[PrivatePlacementFundUsage]:
        """사모자금의 사용내역 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bsns_year: 사업연도 (YYYY)
            reprt_code: 보고서 코드 (11011~11014)

        Returns:
            사모자금 사용내역 목록
        """
        response = await self._get(
            "/api/prfdCptalUseDtls.json",
            PrivatePlacementFundUsageListResponse,
            params={
                "corp_code": corp_code,
                "bsns_year": bsns_year,
                "reprt_code": reprt_code,
            },
        )
        return response.items
