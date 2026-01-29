"""DS005 주요사항보고서 주요정보 API."""

from opendart_fss.api.base import BaseAPI
from opendart_fss.models.major_event import (
    AssetTransfer,
    AssetTransferListResponse,
    BondWithWarrant,
    BondWithWarrantListResponse,
    BonusIssue,
    BonusIssueListResponse,
    BusinessAcquisition,
    BusinessAcquisitionListResponse,
    BusinessDisposal,
    BusinessDisposalListResponse,
    BusinessSuspension,
    BusinessSuspensionListResponse,
    CapitalChange,
    CapitalChangeListResponse,
    ConvertibleBond,
    ConvertibleBondListResponse,
    CreditorManagementStart,
    CreditorManagementStartListResponse,
    CreditorManagementStop,
    CreditorManagementStopListResponse,
    DefaultOccurrence,
    DefaultOccurrenceListResponse,
    DissolutionReason,
    DissolutionReasonListResponse,
    ExchangeableBond,
    ExchangeableBondListResponse,
    Litigation,
    LitigationListResponse,
    MergerDecision,
    MergerDecisionListResponse,
    MixedCapitalIncrease,
    MixedCapitalIncreaseListResponse,
    OtherCorpStockAcquisition,
    OtherCorpStockAcquisitionListResponse,
    OtherCorpStockDisposal,
    OtherCorpStockDisposalListResponse,
    OverseasDelisting,
    OverseasDelistingDecision,
    OverseasDelistingDecisionListResponse,
    OverseasDelistingListResponse,
    OverseasListing,
    OverseasListingDecision,
    OverseasListingDecisionListResponse,
    OverseasListingListResponse,
    RehabilitationFiling,
    RehabilitationFilingListResponse,
    SplitDecision,
    SplitDecisionListResponse,
    SplitMergerDecision,
    SplitMergerDecisionListResponse,
    StockExchangeDecision,
    StockExchangeDecisionListResponse,
    StockRelatedBondAcquisition,
    StockRelatedBondAcquisitionListResponse,
    StockRelatedBondDisposal,
    StockRelatedBondDisposalListResponse,
    TangibleAssetAcquisition,
    TangibleAssetAcquisitionListResponse,
    TangibleAssetDisposal,
    TangibleAssetDisposalListResponse,
    TreasuryStockAcquisition,
    TreasuryStockAcquisitionListResponse,
    TreasuryStockDisposal,
    TreasuryStockDisposalListResponse,
    TreasuryTrustContract,
    TreasuryTrustContractListResponse,
    TreasuryTrustTermination,
    TreasuryTrustTerminationListResponse,
    WriteOffContingentCapital,
    WriteOffContingentCapitalListResponse,
)


class MajorEventAPI(BaseAPI):
    """주요사항보고서 주요정보 API (DS005)."""

    async def get_paid_capital_increase(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[CapitalChange]:
        """유상증자 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            유상증자 결정 목록
        """
        response = await self._get(
            "/api/piicDecsn.json",
            CapitalChangeListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_bonus_issue(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[BonusIssue]:
        """무상증자 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            무상증자 결정 목록
        """
        response = await self._get(
            "/api/fricDecsn.json",
            BonusIssueListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_capital_reduction(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[CapitalChange]:
        """감자 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            감자 결정 목록
        """
        response = await self._get(
            "/api/crDecsn.json",
            CapitalChangeListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_convertible_bond(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[ConvertibleBond]:
        """전환사채권 발행결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            전환사채권 발행결정 목록
        """
        response = await self._get(
            "/api/cvbdIsDecsn.json",
            ConvertibleBondListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_merger_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[MergerDecision]:
        """합병 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            합병 결정 목록
        """
        response = await self._get(
            "/api/mgDecsn.json",
            MergerDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_split_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[SplitDecision]:
        """분할 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            분할 결정 목록
        """
        response = await self._get(
            "/api/dvDecsn.json",
            SplitDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_asset_transfer(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[AssetTransfer]:
        """영업양수도 등 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            영업양수도 등 목록
        """
        response = await self._get(
            "/api/astInhtrfEtcPtbkOpt.json",
            AssetTransferListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_default_occurrence(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[DefaultOccurrence]:
        """채무불이행 등 발생 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            채무불이행 등 발생 목록
        """
        response = await self._get(
            "/api/dfOcr.json",
            DefaultOccurrenceListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_business_suspension(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[BusinessSuspension]:
        """영업정지 등 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            영업정지 등 목록
        """
        response = await self._get(
            "/api/suspOprtn.json",
            BusinessSuspensionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_rehabilitation_filing(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[RehabilitationFiling]:
        """회생절차 개시신청 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            회생절차 개시신청 목록
        """
        response = await self._get(
            "/api/rcvrProcdOpnnAppln.json",
            RehabilitationFilingListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_dissolution_reason(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[DissolutionReason]:
        """해산사유 발생 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            해산사유 발생 목록
        """
        response = await self._get(
            "/api/dssltnRsnOccr.json",
            DissolutionReasonListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_mixed_capital_increase(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[MixedCapitalIncrease]:
        """유무상증자 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            유무상증자 결정 목록
        """
        response = await self._get(
            "/api/paidIncsRsnFcIncsRsn.json",
            MixedCapitalIncreaseListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_creditor_management_start(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[CreditorManagementStart]:
        """채권자관리절차 개시신청 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            채권자관리절차 개시신청 목록
        """
        response = await self._get(
            "/api/crdtrMngmntProcdOpnn.json",
            CreditorManagementStartListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_litigation(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[Litigation]:
        """소송 등의 제기 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            소송 등의 제기 목록
        """
        response = await self._get(
            "/api/lgtnOnEtc.json",
            LitigationListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_overseas_listing_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OverseasListingDecision]:
        """해외증권시장 주권등 상장결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            해외증권시장 주권등 상장결정 목록
        """
        response = await self._get(
            "/api/ovrsDcsnLstgDecde.json",
            OverseasListingDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_overseas_delisting_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OverseasDelistingDecision]:
        """해외증권시장 주권등 상장폐지결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            해외증권시장 주권등 상장폐지결정 목록
        """
        response = await self._get(
            "/api/ovrsDelstgDecde.json",
            OverseasDelistingDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_overseas_listing(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OverseasListing]:
        """해외증권시장 주권등 상장 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            해외증권시장 주권등 상장 목록
        """
        response = await self._get(
            "/api/ovrsLstg.json",
            OverseasListingListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_overseas_delisting(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OverseasDelisting]:
        """해외증권시장 주권등 상장폐지 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            해외증권시장 주권등 상장폐지 목록
        """
        response = await self._get(
            "/api/ovrsDeLstg.json",
            OverseasDelistingListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_bond_with_warrant(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[BondWithWarrant]:
        """신주인수권부사채권 발행결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            신주인수권부사채권 발행결정 목록
        """
        response = await self._get(
            "/api/wrtIncsDecde.json",
            BondWithWarrantListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_exchangeable_bond(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[ExchangeableBond]:
        """교환사채권 발행결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            교환사채권 발행결정 목록
        """
        response = await self._get(
            "/api/exchgBndIncsDecde.json",
            ExchangeableBondListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_creditor_management_stop(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[CreditorManagementStop]:
        """채권자관리절차 중단 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            채권자관리절차 중단 목록
        """
        response = await self._get(
            "/api/crdtrMngmntProcdSspnn.json",
            CreditorManagementStopListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_write_off_contingent_capital(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[WriteOffContingentCapital]:
        """상각형 조건부자본증권 발행결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            상각형 조건부자본증권 발행결정 목록
        """
        response = await self._get(
            "/api/amzAmntyDbtSecIncsDecde.json",
            WriteOffContingentCapitalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_treasury_stock_acquisition(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TreasuryStockAcquisition]:
        """자기주식 취득 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            자기주식 취득 결정 목록
        """
        response = await self._get(
            "/api/trsrStckAcqDecde.json",
            TreasuryStockAcquisitionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_treasury_stock_disposal(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TreasuryStockDisposal]:
        """자기주식 처분 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            자기주식 처분 결정 목록
        """
        response = await self._get(
            "/api/trsrStckDspDecde.json",
            TreasuryStockDisposalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_treasury_trust_contract(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TreasuryTrustContract]:
        """자기주식취득 신탁계약 체결 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            자기주식취득 신탁계약 체결 결정 목록
        """
        response = await self._get(
            "/api/trsrStckAcqTrstCntrctCnclsDecde.json",
            TreasuryTrustContractListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_treasury_trust_termination(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TreasuryTrustTermination]:
        """자기주식취득 신탁계약 해지 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            자기주식취득 신탁계약 해지 결정 목록
        """
        response = await self._get(
            "/api/trsrStckAcqTrstCntrctRsltDecde.json",
            TreasuryTrustTerminationListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_business_acquisition(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[BusinessAcquisition]:
        """영업양수 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            영업양수 결정 목록
        """
        response = await self._get(
            "/api/bizAcqDecde.json",
            BusinessAcquisitionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_business_disposal(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[BusinessDisposal]:
        """영업양도 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            영업양도 결정 목록
        """
        response = await self._get(
            "/api/bizDspDecde.json",
            BusinessDisposalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_tangible_asset_acquisition(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TangibleAssetAcquisition]:
        """유형자산 양수 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            유형자산 양수 결정 목록
        """
        response = await self._get(
            "/api/tangblAstAcqDecde.json",
            TangibleAssetAcquisitionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_tangible_asset_disposal(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[TangibleAssetDisposal]:
        """유형자산 양도 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            유형자산 양도 결정 목록
        """
        response = await self._get(
            "/api/tangblAstDspDecde.json",
            TangibleAssetDisposalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_other_corp_stock_acquisition(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OtherCorpStockAcquisition]:
        """타법인 주식 및 출자증권 양수 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            타법인 주식 및 출자증권 양수 결정 목록
        """
        response = await self._get(
            "/api/otherCorpStckAcqDecde.json",
            OtherCorpStockAcquisitionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_other_corp_stock_disposal(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[OtherCorpStockDisposal]:
        """타법인 주식 및 출자증권 양도 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            타법인 주식 및 출자증권 양도 결정 목록
        """
        response = await self._get(
            "/api/otherCorpStckDspDecde.json",
            OtherCorpStockDisposalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_stock_related_bond_acquisition(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[StockRelatedBondAcquisition]:
        """주권 관련 사채권 양수 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            주권 관련 사채권 양수 결정 목록
        """
        response = await self._get(
            "/api/stckRltdBndAcqDecde.json",
            StockRelatedBondAcquisitionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_stock_related_bond_disposal(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[StockRelatedBondDisposal]:
        """주권 관련 사채권 양도 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            주권 관련 사채권 양도 결정 목록
        """
        response = await self._get(
            "/api/stckRltdBndDspDecde.json",
            StockRelatedBondDisposalListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_split_merger_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[SplitMergerDecision]:
        """분할합병 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            분할합병 결정 목록
        """
        response = await self._get(
            "/api/spltMergerDecde.json",
            SplitMergerDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items

    async def get_stock_exchange_decision(
        self,
        corp_code: str,
        bgn_de: str | None = None,
        end_de: str | None = None,
    ) -> list[StockExchangeDecision]:
        """주식의 포괄적 교환·이전 결정 조회.

        Args:
            corp_code: 고유번호 (8자리)
            bgn_de: 시작일 (YYYYMMDD)
            end_de: 종료일 (YYYYMMDD)

        Returns:
            주식의 포괄적 교환·이전 결정 목록
        """
        response = await self._get(
            "/api/stckExchngTransDecde.json",
            StockExchangeDecisionListResponse,
            params={
                "corp_code": corp_code,
                "bgn_de": bgn_de,
                "end_de": end_de,
            },
        )
        return response.items
