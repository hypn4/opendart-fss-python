"""DS003 정기보고서 재무정보 모델."""

import msgspec


class FinancialAccount(msgspec.Struct, kw_only=True):
    """재무제표 주요계정."""

    rcept_no: str  # 접수번호
    reprt_code: str | None = None  # 보고서 코드
    bsns_year: str | None = None  # 사업연도
    corp_code: str | None = None  # 고유번호
    stock_code: str | None = None  # 종목코드
    fs_div: str | None = None  # 개별/연결구분 (CFS/OFS)
    fs_nm: str | None = None  # 개별/연결명
    sj_div: str | None = None  # 재무제표구분 (BS/IS/CIS/CF/SCE)
    sj_nm: str | None = None  # 재무제표명
    account_id: str | None = None  # 계정ID
    account_nm: str | None = None  # 계정명
    account_detail: str | None = None  # 계정상세
    thstrm_nm: str | None = None  # 당기명
    thstrm_amount: str | None = None  # 당기금액
    thstrm_add_amount: str | None = None  # 당기누적금액
    frmtrm_nm: str | None = None  # 전기명
    frmtrm_amount: str | None = None  # 전기금액
    frmtrm_q_nm: str | None = None  # 전기명(분/반기)
    frmtrm_q_amount: str | None = None  # 전기금액(분/반기)
    frmtrm_add_amount: str | None = None  # 전기누적금액
    bfefrmtrm_nm: str | None = None  # 전전기명
    bfefrmtrm_amount: str | None = None  # 전전기금액
    ord: str | None = None  # 계정과목 정렬순서
    currency: str | None = None  # 통화단위


class FinancialAccountListResponse(msgspec.Struct, kw_only=True):
    """재무제표 주요계정 응답."""

    status: str
    message: str
    items: list[FinancialAccount] = msgspec.field(default_factory=list, name="list")


class FinancialIndicator(msgspec.Struct, kw_only=True):
    """재무지표."""

    rcept_no: str | None = None  # 접수번호
    bsns_year: str | None = None  # 사업연도
    corp_code: str | None = None  # 고유번호
    stock_code: str | None = None  # 종목코드
    reprt_code: str | None = None  # 보고서 코드
    stlm_dt: str | None = None  # 결산기준일
    idx_cl_code: str | None = None  # 지표분류코드
    idx_cl_nm: str | None = None  # 지표분류명
    idx_code: str | None = None  # 지표코드
    idx_nm: str | None = None  # 지표명
    idx_val: str | None = None  # 지표값


class FinancialIndicatorListResponse(msgspec.Struct, kw_only=True):
    """재무지표 응답."""

    status: str
    message: str
    items: list[FinancialIndicator] = msgspec.field(default_factory=list, name="list")


class XbrlTaxonomy(msgspec.Struct, kw_only=True):
    """XBRL 택사노미."""

    sj_div: str  # 재무제표구분
    account_id: str | None = None  # 계정ID
    account_nm: str | None = None  # 계정명
    bsns_de: str | None = None  # 개시일자
    label_kor: str | None = None  # 한글라벨
    label_eng: str | None = None  # 영문라벨
    data_tp: str | None = None  # 데이터타입
    ifrs_ref: str | None = None  # IFRS참조


class XbrlTaxonomyListResponse(msgspec.Struct, kw_only=True):
    """XBRL 택사노미 응답."""

    status: str
    message: str
    items: list[XbrlTaxonomy] = msgspec.field(default_factory=list, name="list")
