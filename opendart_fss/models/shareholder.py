"""DS004 지분공시 종합정보 모델."""

import msgspec


class MajorStock(msgspec.Struct, kw_only=True):
    """대량보유 상황보고."""

    rcept_no: str  # 접수번호
    rcept_dt: str | None = None  # 접수일자
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    report_tp: str | None = None  # 보고구분
    repror: str | None = None  # 보고자
    stkqy: str | None = None  # 보유주식등의수
    stkqy_irds: str | None = None  # 보유주식등의수증감
    stkrt: str | None = None  # 보유비율
    stkrt_irds: str | None = None  # 보유비율증감
    ctr_stkqy: str | None = None  # 주요체결등의수
    ctr_stkrt: str | None = None  # 주요체결등비율
    report_resn: str | None = None  # 보고사유


class MajorStockListResponse(msgspec.Struct, kw_only=True):
    """대량보유 상황보고 응답."""

    status: str
    message: str
    items: list[MajorStock] = msgspec.field(default_factory=list, name="list")


class ExecutiveStock(msgspec.Struct, kw_only=True):
    """임원/주요주주 소유보고."""

    rcept_no: str  # 접수번호
    rcept_dt: str | None = None  # 접수일자
    corp_code: str | None = None  # 고유번호
    corp_name: str | None = None  # 회사명
    repror: str | None = None  # 보고자
    isu_exctv_rgist_at: str | None = None  # 발행회사관계(임원등기여부)
    isu_exctv_ofcps: str | None = None  # 발행회사관계(직위)
    isu_main_shrholdr: str | None = None  # 발행회사관계(주요주주)
    sp_stock_lmp_cnt: str | None = None  # 특정증권등소유수(주권)
    sp_stock_lmp_irds_cnt: str | None = None  # 특정증권등소유수증감(주권)
    sp_stock_lmp_rate: str | None = None  # 특정증권등소유비율(주권)
    sp_stock_lmp_irds_rate: str | None = None  # 특정증권등소유비율증감(주권)


class ExecutiveStockListResponse(msgspec.Struct, kw_only=True):
    """임원/주요주주 소유보고 응답."""

    status: str
    message: str
    items: list[ExecutiveStock] = msgspec.field(default_factory=list, name="list")
