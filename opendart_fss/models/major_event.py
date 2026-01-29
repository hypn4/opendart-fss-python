"""DS005 주요사항보고서 주요정보 모델."""

import msgspec


class CapitalChange(msgspec.Struct, kw_only=True):
    """유상증자/감자 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nstk_ostk_cnt: str | None = None  # 신주의수 보통주식
    nstk_estk_cnt: str | None = None  # 신주의수 기타주식
    fv_ps: str | None = None  # 1주당 액면가액
    bfic_tisstk_ostk: str | None = None  # 증자전 보통주 발행주식총수
    bfic_tisstk_estk: str | None = None  # 증자전 기타주식 발행주식총수
    fdpp_fclt: str | None = None  # 자금조달목적 시설자금
    fdpp_bsninh: str | None = None  # 자금조달목적 사업운영
    fdpp_op: str | None = None  # 자금조달목적 운영자금
    fdpp_dtrp: str | None = None  # 자금조달목적 채무상환
    fdpp_ocsa: str | None = None  # 자금조달목적 기타자금
    fdpp_etc: str | None = None  # 자금조달목적 기타


class CapitalChangeListResponse(msgspec.Struct, kw_only=True):
    """유상증자/감자 결정 응답."""

    status: str
    message: str
    items: list[CapitalChange] = msgspec.field(default_factory=list, name="list")


class BonusIssue(msgspec.Struct, kw_only=True):
    """무상증자 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nstk_ostk_cnt: str | None = None  # 신주의수 보통주식
    nstk_estk_cnt: str | None = None  # 신주의수 기타주식
    fv_ps: str | None = None  # 1주당 액면가액
    bfic_tisstk_ostk: str | None = None  # 증자전 보통주 발행주식총수
    bfic_tisstk_estk: str | None = None  # 증자전 기타주식 발행주식총수
    nstk_asstd: str | None = None  # 신주배정기준일
    nstk_ascnt_ps_ostk: str | None = None  # 1주당 신주배정주식수(보통주식)
    nstk_ascnt_ps_estk: str | None = None  # 1주당 신주배정주식수(기타주식)
    nstk_dividrk: str | None = None  # 신주의 배당기산일
    nstk_dlprd: str | None = None  # 신주권교부예정일
    nstk_lstprd: str | None = None  # 신주의 상장예정일
    bddd: str | None = None  # 이사회결의일
    od_a_at_t: str | None = None  # 사외이사참석여부
    od_a_at_b: str | None = None  # 사외이사참석(참석)
    od_a_at_c: str | None = None  # 사외이사참석(불참)
    adt_a_atn: str | None = None  # 감사위원 참석여부


class BonusIssueListResponse(msgspec.Struct, kw_only=True):
    """무상증자 결정 응답."""

    status: str
    message: str
    items: list[BonusIssue] = msgspec.field(default_factory=list, name="list")


class ConvertibleBond(msgspec.Struct, kw_only=True):
    """전환사채권 발행결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bd_tm: str | None = None  # 사채의종류(회차)
    bd_knd: str | None = None  # 사채의종류(종류)
    bd_fta: str | None = None  # 사채의권면총액
    atcsc: str | None = None  # 자금조달목적
    ovis_fta: str | None = None  # 해외발행(권면총액)
    ovis_fxrt: str | None = None  # 해외발행(환율)
    ovis_fta_crn: str | None = None  # 해외발행(원화환산금액)
    fdpp_fclt: str | None = None  # 자금조달목적 시설자금
    fdpp_bsninh: str | None = None  # 자금조달목적 영업양수자금
    fdpp_op: str | None = None  # 자금조달목적 운영자금
    fdpp_dtrp: str | None = None  # 자금조달목적 채무상환자금
    fdpp_ocsa: str | None = None  # 자금조달목적 타법인증권취득자금
    fdpp_etc: str | None = None  # 자금조달목적 기타자금
    bd_intr_ex: str | None = None  # 사채이율 표면이자율
    bd_intr_sf: str | None = None  # 사채이율 만기이자율
    bd_mtd: str | None = None  # 사채만기일
    bd_repay: str | None = None  # 상환방법
    bd_tm_nstkqy: str | None = None  # 전환주식수
    bd_tm_act_pr: str | None = None  # 전환비율


class ConvertibleBondListResponse(msgspec.Struct, kw_only=True):
    """전환사채권 발행결정 응답."""

    status: str
    message: str
    items: list[ConvertibleBond] = msgspec.field(default_factory=list, name="list")


class MergerDecision(msgspec.Struct, kw_only=True):
    """합병 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    mgcpn: str | None = None  # 합병상대회사
    mg_prc: str | None = None  # 합병가액
    mg_rt: str | None = None  # 합병비율
    mgsc: str | None = None  # 합병방식
    mg_pp: str | None = None  # 합병목적
    mg_nsp: str | None = None  # 합병후신설회사
    mg_bdddr: str | None = None  # 이사회결의일
    mg_ctrcdd: str | None = None  # 계약체결일
    mg_shddsr: str | None = None  # 주주총회예정일
    mg_cdd: str | None = None  # 합병기일


class MergerDecisionListResponse(msgspec.Struct, kw_only=True):
    """합병 결정 응답."""

    status: str
    message: str
    items: list[MergerDecision] = msgspec.field(default_factory=list, name="list")


class SplitDecision(msgspec.Struct, kw_only=True):
    """분할 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    dv_mthn: str | None = None  # 분할방법
    dv_nspcpn: str | None = None  # 분할신설회사
    dv_rt: str | None = None  # 분할비율
    dv_pp: str | None = None  # 분할목적
    dv_bdddr: str | None = None  # 이사회결의일
    dv_shddsr: str | None = None  # 주주총회예정일
    dv_cdd: str | None = None  # 분할기일


class SplitDecisionListResponse(msgspec.Struct, kw_only=True):
    """분할 결정 응답."""

    status: str
    message: str
    items: list[SplitDecision] = msgspec.field(default_factory=list, name="list")


class AssetTransfer(msgspec.Struct, kw_only=True):
    """자산양수도(기타), 풋백옵션."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    rp_rsn: str | None = None  # 보고사유
    ast_inhtrf_prc: str | None = None  # 자산양수도가액


class AssetTransferListResponse(msgspec.Struct, kw_only=True):
    """자산양수도 응답."""

    status: str
    message: str
    items: list[AssetTransfer] = msgspec.field(default_factory=list, name="list")


class DefaultOccurrence(msgspec.Struct, kw_only=True):
    """부도발생."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    df_cn: str | None = None  # 부도내용
    df_amt: str | None = None  # 부도금액
    df_bnk: str | None = None  # 부도발생은행
    dfd: str | None = None  # 최종부도일자
    df_rs: str | None = None  # 부도사유 및 경위


class DefaultOccurrenceListResponse(msgspec.Struct, kw_only=True):
    """부도발생 응답."""

    status: str
    message: str
    items: list[DefaultOccurrence] = msgspec.field(default_factory=list, name="list")


class BusinessSuspension(msgspec.Struct, kw_only=True):
    """영업정지."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsnsp_rm: str | None = None  # 영업정지분야
    bsnsp_amt: str | None = None  # 영업정지금액
    rsl: str | None = None  # 최근매출총액
    bsnsp_cn: str | None = None  # 영업정지내용
    bsnsp_rs: str | None = None  # 영업정지사유
    bsnspd: str | None = None  # 영업정지일자
    bddd: str | None = None  # 이사회결의일


class BusinessSuspensionListResponse(msgspec.Struct, kw_only=True):
    """영업정지 응답."""

    status: str
    message: str
    items: list[BusinessSuspension] = msgspec.field(default_factory=list, name="list")


class RehabilitationFiling(msgspec.Struct, kw_only=True):
    """회생절차 개시신청."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    apcnt: str | None = None  # 신청인
    cpct: str | None = None  # 관할법원
    rq_rs: str | None = None  # 신청사유
    rqd: str | None = None  # 신청일자
    ft_ctp_sc: str | None = None  # 향후대책 및 일정


class RehabilitationFilingListResponse(msgspec.Struct, kw_only=True):
    """회생절차 개시신청 응답."""

    status: str
    message: str
    items: list[RehabilitationFiling] = msgspec.field(default_factory=list, name="list")


class DissolutionReason(msgspec.Struct, kw_only=True):
    """해산사유 발생."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ds_rs: str | None = None  # 해산사유
    ds_rsd: str | None = None  # 해산사유발생일
    od_a_at_t: str | None = None  # 사외이사참석
    od_a_at_b: str | None = None  # 사외이사불참
    adt_a_atn: str | None = None  # 감사참석여부


class DissolutionReasonListResponse(msgspec.Struct, kw_only=True):
    """해산사유 발생 응답."""

    status: str
    message: str
    items: list[DissolutionReason] = msgspec.field(default_factory=list, name="list")


class MixedCapitalIncrease(msgspec.Struct, kw_only=True):
    """유무상증자 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    nstk_ostk_cnt: str | None = None  # 신주의수 보통주식
    nstk_estk_cnt: str | None = None  # 신주의수 기타주식
    fv_ps: str | None = None  # 1주당 액면가액
    bfic_tisstk_ostk: str | None = None  # 증자전 보통주 발행주식총수
    bfic_tisstk_estk: str | None = None  # 증자전 기타주식 발행주식총수
    bddd: str | None = None  # 이사회결의일


class MixedCapitalIncreaseListResponse(msgspec.Struct, kw_only=True):
    """유무상증자 결정 응답."""

    status: str
    message: str
    items: list[MixedCapitalIncrease] = msgspec.field(default_factory=list, name="list")


class CreditorManagementStart(msgspec.Struct, kw_only=True):
    """채권자 관리절차 개시신청."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    apcnt: str | None = None  # 신청인
    cpct: str | None = None  # 관할법원
    rq_rs: str | None = None  # 신청사유
    rqd: str | None = None  # 신청일자


class CreditorManagementStartListResponse(msgspec.Struct, kw_only=True):
    """채권자 관리절차 개시신청 응답."""

    status: str
    message: str
    items: list[CreditorManagementStart] = msgspec.field(
        default_factory=list, name="list"
    )


class Litigation(msgspec.Struct, kw_only=True):
    """소송 등의 제기."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    lgtn_cn: str | None = None  # 소송내용
    lgtn_amt: str | None = None  # 소송금액
    lgtn_crt: str | None = None  # 소송법원
    lgtn_pl: str | None = None  # 원고
    lgtn_df: str | None = None  # 피고
    lgtn_d: str | None = None  # 소송제기일


class LitigationListResponse(msgspec.Struct, kw_only=True):
    """소송 등의 제기 응답."""

    status: str
    message: str
    items: list[Litigation] = msgspec.field(default_factory=list, name="list")


class OverseasListingDecision(msgspec.Struct, kw_only=True):
    """해외상장 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ovrs_lstg_mktnm: str | None = None  # 상장시장
    ovrs_lstg_pp: str | None = None  # 상장목적
    ovrs_lstg_stk_knd: str | None = None  # 상장증권종류
    ovrs_lstg_stk_cnt: str | None = None  # 상장증권수량
    bddd: str | None = None  # 이사회결의일


class OverseasListingDecisionListResponse(msgspec.Struct, kw_only=True):
    """해외상장 결정 응답."""

    status: str
    message: str
    items: list[OverseasListingDecision] = msgspec.field(
        default_factory=list, name="list"
    )


class OverseasDelistingDecision(msgspec.Struct, kw_only=True):
    """해외상장폐지 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ovrs_lstg_mktnm: str | None = None  # 상장폐지시장
    ovrs_dlstg_rs: str | None = None  # 상장폐지사유
    ovrs_dlstg_stk_knd: str | None = None  # 상장폐지증권종류
    ovrs_dlstg_stk_cnt: str | None = None  # 상장폐지증권수량
    bddd: str | None = None  # 이사회결의일


class OverseasDelistingDecisionListResponse(msgspec.Struct, kw_only=True):
    """해외상장폐지 결정 응답."""

    status: str
    message: str
    items: list[OverseasDelistingDecision] = msgspec.field(
        default_factory=list, name="list"
    )


class OverseasListing(msgspec.Struct, kw_only=True):
    """해외상장."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ovrs_lstg_mktnm: str | None = None  # 상장시장
    ovrs_lstg_stk_knd: str | None = None  # 상장증권종류
    ovrs_lstg_stk_cnt: str | None = None  # 상장증권수량
    ovrs_lstgd: str | None = None  # 상장일자


class OverseasListingListResponse(msgspec.Struct, kw_only=True):
    """해외상장 응답."""

    status: str
    message: str
    items: list[OverseasListing] = msgspec.field(default_factory=list, name="list")


class OverseasDelisting(msgspec.Struct, kw_only=True):
    """해외상장폐지."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ovrs_lstg_mktnm: str | None = None  # 상장폐지시장
    ovrs_dlstg_rs: str | None = None  # 상장폐지사유
    ovrs_dlstg_stk_knd: str | None = None  # 상장폐지증권종류
    ovrs_dlstg_stk_cnt: str | None = None  # 상장폐지증권수량
    ovrs_dlstgd: str | None = None  # 상장폐지일자


class OverseasDelistingListResponse(msgspec.Struct, kw_only=True):
    """해외상장폐지 응답."""

    status: str
    message: str
    items: list[OverseasDelisting] = msgspec.field(default_factory=list, name="list")


class BondWithWarrant(msgspec.Struct, kw_only=True):
    """신주인수권부사채권 발행결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bd_tm: str | None = None  # 사채의종류(회차)
    bd_knd: str | None = None  # 사채의종류(종류)
    bd_fta: str | None = None  # 사채의권면총액
    bd_intr_sf: str | None = None  # 표면이자율
    bd_intr_ex: str | None = None  # 만기이자율
    bd_mtd: str | None = None  # 사채만기일
    bddd: str | None = None  # 이사회결의일


class BondWithWarrantListResponse(msgspec.Struct, kw_only=True):
    """신주인수권부사채권 발행결정 응답."""

    status: str
    message: str
    items: list[BondWithWarrant] = msgspec.field(default_factory=list, name="list")


class ExchangeableBond(msgspec.Struct, kw_only=True):
    """교환사채권 발행결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bd_tm: str | None = None  # 사채의종류(회차)
    bd_knd: str | None = None  # 사채의종류(종류)
    bd_fta: str | None = None  # 사채의권면총액
    bd_intr_sf: str | None = None  # 표면이자율
    bd_intr_ex: str | None = None  # 만기이자율
    bd_mtd: str | None = None  # 사채만기일
    bddd: str | None = None  # 이사회결의일


class ExchangeableBondListResponse(msgspec.Struct, kw_only=True):
    """교환사채권 발행결정 응답."""

    status: str
    message: str
    items: list[ExchangeableBond] = msgspec.field(default_factory=list, name="list")


class CreditorManagementStop(msgspec.Struct, kw_only=True):
    """채권자 관리절차 중지."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    spnd_rs: str | None = None  # 중지사유
    spnd_dt: str | None = None  # 중지일자
    ft_ctp: str | None = None  # 향후대책
    cfd: str | None = None  # 확인일자


class CreditorManagementStopListResponse(msgspec.Struct, kw_only=True):
    """채권자 관리절차 중지 응답."""

    status: str
    message: str
    items: list[CreditorManagementStop] = msgspec.field(
        default_factory=list, name="list"
    )


class WriteOffContingentCapital(msgspec.Struct, kw_only=True):
    """상각형 조건부자본증권 발행결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bd_tm: str | None = None  # 사채의종류(회차)
    bd_knd: str | None = None  # 사채의종류(종류)
    bd_fta: str | None = None  # 사채의권면총액
    bd_intr_sf: str | None = None  # 표면이자율
    bd_intr_ex: str | None = None  # 만기이자율
    bd_mtd: str | None = None  # 사채만기일
    bddd: str | None = None  # 이사회결의일


class WriteOffContingentCapitalListResponse(msgspec.Struct, kw_only=True):
    """상각형 조건부자본증권 발행결정 응답."""

    status: str
    message: str
    items: list[WriteOffContingentCapital] = msgspec.field(
        default_factory=list, name="list"
    )


class TreasuryStockAcquisition(msgspec.Struct, kw_only=True):
    """자기주식 취득 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    aqpln_stk_ostk: str | None = None  # 취득예정주식(보통주식)
    aqpln_stk_estk: str | None = None  # 취득예정주식(기타주식)
    aqpln_prc_ostk: str | None = None  # 취득예정금액(보통주식)
    aqpln_prc_estk: str | None = None  # 취득예정금액(기타주식)
    aqexpd_bgd: str | None = None  # 취득예상기간(시작일)
    aqexpd_edd: str | None = None  # 취득예상기간(종료일)
    aq_pp: str | None = None  # 취득목적
    aq_mth: str | None = None  # 취득방법
    aq_dd: str | None = None  # 취득결정일


class TreasuryStockAcquisitionListResponse(msgspec.Struct, kw_only=True):
    """자기주식 취득 결정 응답."""

    status: str
    message: str
    items: list[TreasuryStockAcquisition] = msgspec.field(
        default_factory=list, name="list"
    )


class TreasuryStockDisposal(msgspec.Struct, kw_only=True):
    """자기주식 처분 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    dppln_stk_ostk: str | None = None  # 처분예정주식(보통주식)
    dppln_stk_estk: str | None = None  # 처분예정주식(기타주식)
    dppln_prc_ostk: str | None = None  # 처분예정금액(보통주식)
    dppln_prc_estk: str | None = None  # 처분예정금액(기타주식)
    dpexpd_bgd: str | None = None  # 처분예상기간(시작일)
    dpexpd_edd: str | None = None  # 처분예상기간(종료일)
    dp_pp: str | None = None  # 처분목적
    dp_mth: str | None = None  # 처분방법
    dp_dd: str | None = None  # 처분결정일


class TreasuryStockDisposalListResponse(msgspec.Struct, kw_only=True):
    """자기주식 처분 결정 응답."""

    status: str
    message: str
    items: list[TreasuryStockDisposal] = msgspec.field(
        default_factory=list, name="list"
    )


class TreasuryTrustContract(msgspec.Struct, kw_only=True):
    """자기주식취득 신탁계약 체결결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ctr_prc: str | None = None  # 계약금액
    ctr_pd_bgd: str | None = None  # 계약기간(시작일)
    ctr_pd_edd: str | None = None  # 계약기간(종료일)
    ctr_trstee: str | None = None  # 수탁기관
    ctr_pp: str | None = None  # 계약목적
    bddd: str | None = None  # 이사회결의일


class TreasuryTrustContractListResponse(msgspec.Struct, kw_only=True):
    """자기주식취득 신탁계약 체결결정 응답."""

    status: str
    message: str
    items: list[TreasuryTrustContract] = msgspec.field(
        default_factory=list, name="list"
    )


class TreasuryTrustTermination(msgspec.Struct, kw_only=True):
    """자기주식취득 신탁계약 해지결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    ctr_prc: str | None = None  # 계약금액
    trm_prc: str | None = None  # 해지금액
    trm_dt: str | None = None  # 해지일자
    ctr_trstee: str | None = None  # 수탁기관
    trm_rs: str | None = None  # 해지사유
    bddd: str | None = None  # 이사회결의일


class TreasuryTrustTerminationListResponse(msgspec.Struct, kw_only=True):
    """자기주식취득 신탁계약 해지결정 응답."""

    status: str
    message: str
    items: list[TreasuryTrustTermination] = msgspec.field(
        default_factory=list, name="list"
    )


class BusinessAcquisition(msgspec.Struct, kw_only=True):
    """영업양수 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsninh_cn: str | None = None  # 영업양수내용
    bsninh_prc: str | None = None  # 영업양수가액
    bsninh_cpn: str | None = None  # 영업양수상대회사
    bsninh_dd: str | None = None  # 영업양수일
    bddd: str | None = None  # 이사회결의일


class BusinessAcquisitionListResponse(msgspec.Struct, kw_only=True):
    """영업양수 결정 응답."""

    status: str
    message: str
    items: list[BusinessAcquisition] = msgspec.field(default_factory=list, name="list")


class BusinessDisposal(msgspec.Struct, kw_only=True):
    """영업양도 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bsntrf_cn: str | None = None  # 영업양도내용
    bsntrf_prc: str | None = None  # 영업양도가액
    bsntrf_cpn: str | None = None  # 영업양도상대회사
    bsntrf_dd: str | None = None  # 영업양도일
    bddd: str | None = None  # 이사회결의일


class BusinessDisposalListResponse(msgspec.Struct, kw_only=True):
    """영업양도 결정 응답."""

    status: str
    message: str
    items: list[BusinessDisposal] = msgspec.field(default_factory=list, name="list")


class TangibleAssetAcquisition(msgspec.Struct, kw_only=True):
    """유형자산 양수 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    tgastaq_cn: str | None = None  # 양수내용
    tgastaq_prc: str | None = None  # 양수가액
    tgastaq_cpn: str | None = None  # 양수상대회사
    tgastaq_dd: str | None = None  # 양수일
    bddd: str | None = None  # 이사회결의일


class TangibleAssetAcquisitionListResponse(msgspec.Struct, kw_only=True):
    """유형자산 양수 결정 응답."""

    status: str
    message: str
    items: list[TangibleAssetAcquisition] = msgspec.field(
        default_factory=list, name="list"
    )


class TangibleAssetDisposal(msgspec.Struct, kw_only=True):
    """유형자산 양도 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    tgasttrf_cn: str | None = None  # 양도내용
    tgasttrf_prc: str | None = None  # 양도가액
    tgasttrf_cpn: str | None = None  # 양도상대회사
    tgasttrf_dd: str | None = None  # 양도일
    bddd: str | None = None  # 이사회결의일


class TangibleAssetDisposalListResponse(msgspec.Struct, kw_only=True):
    """유형자산 양도 결정 응답."""

    status: str
    message: str
    items: list[TangibleAssetDisposal] = msgspec.field(
        default_factory=list, name="list"
    )


class OtherCorpStockAcquisition(msgspec.Struct, kw_only=True):
    """타법인 주식 양수 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    stkaq_cpn: str | None = None  # 양수대상회사
    stkaq_stk_knd: str | None = None  # 양수주식종류
    stkaq_stk_cnt: str | None = None  # 양수주식수
    stkaq_prc: str | None = None  # 양수가액
    stkaq_dd: str | None = None  # 양수일
    bddd: str | None = None  # 이사회결의일


class OtherCorpStockAcquisitionListResponse(msgspec.Struct, kw_only=True):
    """타법인 주식 양수 결정 응답."""

    status: str
    message: str
    items: list[OtherCorpStockAcquisition] = msgspec.field(
        default_factory=list, name="list"
    )


class OtherCorpStockDisposal(msgspec.Struct, kw_only=True):
    """타법인 주식 양도 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    stktrf_cpn: str | None = None  # 양도대상회사
    stktrf_stk_knd: str | None = None  # 양도주식종류
    stktrf_stk_cnt: str | None = None  # 양도주식수
    stktrf_prc: str | None = None  # 양도가액
    stktrf_dd: str | None = None  # 양도일
    bddd: str | None = None  # 이사회결의일


class OtherCorpStockDisposalListResponse(msgspec.Struct, kw_only=True):
    """타법인 주식 양도 결정 응답."""

    status: str
    message: str
    items: list[OtherCorpStockDisposal] = msgspec.field(
        default_factory=list, name="list"
    )


class StockRelatedBondAcquisition(msgspec.Struct, kw_only=True):
    """주식관련사채권 양수 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    srlbdaq_cpn: str | None = None  # 양수발행회사
    srlbdaq_bd_knd: str | None = None  # 양수사채종류
    srlbdaq_prc: str | None = None  # 양수가액
    srlbdaq_dd: str | None = None  # 양수일
    bddd: str | None = None  # 이사회결의일


class StockRelatedBondAcquisitionListResponse(msgspec.Struct, kw_only=True):
    """주식관련사채권 양수 결정 응답."""

    status: str
    message: str
    items: list[StockRelatedBondAcquisition] = msgspec.field(
        default_factory=list, name="list"
    )


class StockRelatedBondDisposal(msgspec.Struct, kw_only=True):
    """주식관련사채권 양도 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    srlbdtrf_cpn: str | None = None  # 양도발행회사
    srlbdtrf_bd_knd: str | None = None  # 양도사채종류
    srlbdtrf_prc: str | None = None  # 양도가액
    srlbdtrf_dd: str | None = None  # 양도일
    bddd: str | None = None  # 이사회결의일


class StockRelatedBondDisposalListResponse(msgspec.Struct, kw_only=True):
    """주식관련사채권 양도 결정 응답."""

    status: str
    message: str
    items: list[StockRelatedBondDisposal] = msgspec.field(
        default_factory=list, name="list"
    )


class SplitMergerDecision(msgspec.Struct, kw_only=True):
    """분할합병 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    spmg_cpn: str | None = None  # 분할합병상대회사
    spmg_mthn: str | None = None  # 분할합병방법
    spmg_rt: str | None = None  # 분할합병비율
    spmg_pp: str | None = None  # 분할합병목적
    spmg_bdddr: str | None = None  # 이사회결의일
    spmg_shddsr: str | None = None  # 주주총회예정일
    spmg_cdd: str | None = None  # 분할합병기일


class SplitMergerDecisionListResponse(msgspec.Struct, kw_only=True):
    """분할합병 결정 응답."""

    status: str
    message: str
    items: list[SplitMergerDecision] = msgspec.field(default_factory=list, name="list")


class StockExchangeDecision(msgspec.Struct, kw_only=True):
    """주식의 포괄적 교환·이전 결정."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    extr_cpn: str | None = None  # 교환이전상대회사
    extr_mthn: str | None = None  # 교환이전방법
    extr_rt: str | None = None  # 교환이전비율
    extr_pp: str | None = None  # 교환이전목적
    extr_bdddr: str | None = None  # 이사회결의일
    extr_shddsr: str | None = None  # 주주총회예정일
    extr_cdd: str | None = None  # 교환이전기일


class StockExchangeDecisionListResponse(msgspec.Struct, kw_only=True):
    """주식의 포괄적 교환·이전 결정 응답."""

    status: str
    message: str
    items: list[StockExchangeDecision] = msgspec.field(
        default_factory=list, name="list"
    )
