"""DS006 증권신고서 주요정보 모델."""

import msgspec


class EquitySecurities(msgspec.Struct, kw_only=True):
    """지분증권 발행 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    stk_knd: str | None = None  # 주식종류
    stk_issustk_isk_cnt: str | None = None  # 발행주식수
    stk_issustk_isk_pr: str | None = None  # 발행가격
    stk_issustk_isk_fv: str | None = None  # 액면가
    stk_fvpl: str | None = None  # 액면총액
    stk_issustk_isk_fvt: str | None = None  # 발행총액
    stk_issustk_isk_mthn: str | None = None  # 발행방법


class EquitySecuritiesListResponse(msgspec.Struct, kw_only=True):
    """지분증권 발행 정보 응답."""

    status: str
    message: str
    items: list[EquitySecurities] = msgspec.field(default_factory=list, name="list")


class DebtSecurities(msgspec.Struct, kw_only=True):
    """채무증권 발행 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    bnd_nm: str | None = None  # 채권명
    bnd_fta: str | None = None  # 권면총액
    bnd_int_rt: str | None = None  # 이자율
    bnd_mtd: str | None = None  # 만기일
    bnd_repay: str | None = None  # 상환방법
    bnd_grn: str | None = None  # 보증여부
    bnd_grncpn: str | None = None  # 보증기관


class DebtSecuritiesListResponse(msgspec.Struct, kw_only=True):
    """채무증권 발행 정보 응답."""

    status: str
    message: str
    items: list[DebtSecurities] = msgspec.field(default_factory=list, name="list")


class MergerRegistration(msgspec.Struct, kw_only=True):
    """합병 신고 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    mg_cpn: str | None = None  # 합병상대회사
    mg_rt: str | None = None  # 합병비율
    mg_mthn: str | None = None  # 합병방법
    mg_pp: str | None = None  # 합병목적
    mg_stk: str | None = None  # 합병주식발행
    mg_cdd: str | None = None  # 합병기일


class MergerRegistrationListResponse(msgspec.Struct, kw_only=True):
    """합병 신고 정보 응답."""

    status: str
    message: str
    items: list[MergerRegistration] = msgspec.field(default_factory=list, name="list")


class SplitRegistration(msgspec.Struct, kw_only=True):
    """분할 신고 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    dv_mthn: str | None = None  # 분할방법
    dv_nspcpn: str | None = None  # 분할신설회사
    dv_rt: str | None = None  # 분할비율
    dv_pp: str | None = None  # 분할목적
    dv_cdd: str | None = None  # 분할기일


class SplitRegistrationListResponse(msgspec.Struct, kw_only=True):
    """분할 신고 정보 응답."""

    status: str
    message: str
    items: list[SplitRegistration] = msgspec.field(default_factory=list, name="list")


class DepositaryReceipt(msgspec.Struct, kw_only=True):
    """증권예탁증권 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    title: str | None = None  # 그룹명칭
    sbd: str | None = None  # 청약기일
    pymd: str | None = None  # 납입기일
    sband: str | None = None  # 청약공고일
    asand: str | None = None  # 배정공고일
    asstd: str | None = None  # 배정기준일
    exstk: str | None = None  # 신주인수권 행사대상증권
    exprc: str | None = None  # 신주인수권 행사가격
    expd: str | None = None  # 신주인수권 행사기간
    rpt_rcpn: str | None = None  # 주요사항보고서 접수번호
    stksen: str | None = None  # 증권의종류
    stkcnt: str | None = None  # 증권수량
    fv: str | None = None  # 액면가액
    slprc: str | None = None  # 모집(매출)가액
    slta: str | None = None  # 모집(매출)총액
    slmthn: str | None = None  # 모집(매출)방법
    actsen: str | None = None  # 인수인구분
    actnmn: str | None = None  # 인수인명
    udtcnt: str | None = None  # 인수수량
    udtamt: str | None = None  # 인수금액
    udtprc: str | None = None  # 인수대가
    udtmth: str | None = None  # 인수방법
    se: str | None = None  # 구분
    amt: str | None = None  # 금액
    hdr: str | None = None  # 보유자
    rl_cmp: str | None = None  # 회사와의관계
    bfsl_hdstk: str | None = None  # 매출전보유증권수
    slstk: str | None = None  # 매출증권수
    atsl_hdstk: str | None = None  # 매출후보유증권수


class DepositaryReceiptListResponse(msgspec.Struct, kw_only=True):
    """증권예탁증권 정보 응답."""

    status: str
    message: str
    items: list[DepositaryReceipt] = msgspec.field(default_factory=list, name="list")


class StockExchangeTransfer(msgspec.Struct, kw_only=True):
    """주식의 포괄적 교환·이전 정보."""

    rcept_no: str  # 접수번호
    corp_cls: str | None = None  # 법인구분
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    title: str | None = None  # 그룹명칭
    stn: str | None = None  # 형태
    bddd: str | None = None  # 이사회 결의일
    ctrd: str | None = None  # 계약일
    gmtsck_shddstd: str | None = None  # 주주총회를 위한 주주확정일
    ap_gmtsck: str | None = None  # 승인을 위한 주주총회일
    aprskh_pd_bgd: str | None = None  # 주식매수청구권 행사 기간 시작일
    aprskh_pd_edd: str | None = None  # 주식매수청구권 행사 기간 종료일
    aprskh_prc: str | None = None  # 주식매수청구가격
    mgdt_etc: str | None = None  # 합병기일등
    rt_vl: str | None = None  # 비율 또는 가액
    exevl_int: str | None = None  # 외부평가기관
    grtmn_etc: str | None = None  # 지급 교부금 등
    rpt_rcpn: str | None = None  # 주요사항보고서 접수번호
    kndn: str | None = None  # 종류
    cnt: str | None = None  # 수량
    fv: str | None = None  # 액면가액
    slprc: str | None = None  # 모집(매출)가액
    slta: str | None = None  # 모집(매출)총액
    cmpnm: str | None = None  # 회사명
    sen: str | None = None  # 구분
    tast: str | None = None  # 총자산
    cpt: str | None = None  # 자본금
    isstk_knd: str | None = None  # 발행주식수(주식의종류)
    isstk_cnt: str | None = None  # 발행주식수(주식수)


class StockExchangeTransferListResponse(msgspec.Struct, kw_only=True):
    """주식의 포괄적 교환·이전 정보 응답."""

    status: str
    message: str
    items: list[StockExchangeTransfer] = msgspec.field(
        default_factory=list, name="list"
    )
