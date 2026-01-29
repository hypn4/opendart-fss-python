"""엔드포인트 검증 설정."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class VerificationStatus(StrEnum):
    """검증 상태."""

    SUCCESS = "SUCCESS"
    NO_DATA = "NO_DATA"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass
class VerificationResult:
    """검증 결과."""

    endpoint_id: str
    endpoint_name: str
    category: str
    status: VerificationStatus
    response_time_ms: float = 0.0
    error_message: str | None = None
    response_data: Any = None


@dataclass
class EndpointConfig:
    """엔드포인트 설정."""

    id: str
    name: str
    category: str
    service: str
    method: str
    params: dict[str, str] = field(default_factory=dict)
    requires_rcept_no: bool = False
    description: str = ""


# 기본 테스트 데이터
DEFAULT_TEST_DATA = {
    "corp_code": "00126380",  # 삼성전자
    "bsns_year": "2023",
    "reprt_code": "11011",  # 사업보고서
    "bgn_de": "20230101",
    "end_de": "20231231",
    "fs_div": "CFS",  # 연결재무제표
    "sj_div": "BS",  # 재무상태표
}

# 대체 기업 코드 (삼성전자에 데이터가 없을 경우)
FALLBACK_CORP_CODES = [
    "00164779",  # SK하이닉스
    "00401731",  # 현대자동차
    "00155246",  # LG전자
]

# 모든 엔드포인트 설정 (28개)
ENDPOINT_CONFIGS: list[EndpointConfig] = [
    # DS001 - 공시정보 (4개)
    EndpointConfig(
        id="DS001-01",
        name="disclosure.search",
        category="DS001",
        service="disclosure",
        method="search",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="공시검색",
    ),
    EndpointConfig(
        id="DS001-02",
        name="disclosure.get_company",
        category="DS001",
        service="disclosure",
        method="get_company",
        params={"corp_code": "{corp_code}"},
        description="기업개황 조회",
    ),
    EndpointConfig(
        id="DS001-03",
        name="disclosure.download_document",
        category="DS001",
        service="disclosure",
        method="download_document",
        params={"rcept_no": "{rcept_no}"},
        requires_rcept_no=True,
        description="공시서류 원본 다운로드",
    ),
    EndpointConfig(
        id="DS001-04",
        name="disclosure.download_corp_codes",
        category="DS001",
        service="disclosure",
        method="download_corp_codes",
        params={},
        description="고유번호 전체 다운로드",
    ),
    # DS002 - 정기보고서 주요정보 (8개)
    EndpointConfig(
        id="DS002-01",
        name="report.get_stock_changes",
        category="DS002",
        service="report",
        method="get_stock_changes",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="증자(감자) 현황 조회",
    ),
    EndpointConfig(
        id="DS002-02",
        name="report.get_dividends",
        category="DS002",
        service="report",
        method="get_dividends",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="배당에 관한 사항 조회",
    ),
    EndpointConfig(
        id="DS002-03",
        name="report.get_treasury_stock",
        category="DS002",
        service="report",
        method="get_treasury_stock",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="자기주식 현황 조회",
    ),
    EndpointConfig(
        id="DS002-04",
        name="report.get_largest_shareholders",
        category="DS002",
        service="report",
        method="get_largest_shareholders",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="최대주주 현황 조회",
    ),
    EndpointConfig(
        id="DS002-05",
        name="report.get_executives",
        category="DS002",
        service="report",
        method="get_executives",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="임원 현황 조회",
    ),
    EndpointConfig(
        id="DS002-06",
        name="report.get_employees",
        category="DS002",
        service="report",
        method="get_employees",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="직원 현황 조회",
    ),
    EndpointConfig(
        id="DS002-07",
        name="report.get_individual_compensation",
        category="DS002",
        service="report",
        method="get_individual_compensation",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="개인별 보수 현황 조회",
    ),
    EndpointConfig(
        id="DS002-08",
        name="report.get_director_compensation",
        category="DS002",
        service="report",
        method="get_director_compensation",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="이사/감사 보수 현황 조회",
    ),
    # DS003 - 정기보고서 재무정보 (6개)
    EndpointConfig(
        id="DS003-01",
        name="financial.get_single_account",
        category="DS003",
        service="financial",
        method="get_single_account",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
            "fs_div": "{fs_div}",
        },
        description="단일회사 주요계정 조회",
    ),
    EndpointConfig(
        id="DS003-02",
        name="financial.get_multi_account",
        category="DS003",
        service="financial",
        method="get_multi_account",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
            "fs_div": "{fs_div}",
        },
        description="다중회사 주요계정 조회",
    ),
    EndpointConfig(
        id="DS003-03",
        name="financial.get_full_statements",
        category="DS003",
        service="financial",
        method="get_full_statements",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
            "fs_div": "{fs_div}",
        },
        description="단일회사 전체 재무제표 조회",
    ),
    EndpointConfig(
        id="DS003-04",
        name="financial.download_xbrl",
        category="DS003",
        service="financial",
        method="download_xbrl",
        params={
            "rcept_no": "{rcept_no}",
            "reprt_code": "{reprt_code}",
        },
        requires_rcept_no=True,
        description="XBRL 원본파일 다운로드",
    ),
    EndpointConfig(
        id="DS003-05",
        name="financial.get_xbrl_taxonomy",
        category="DS003",
        service="financial",
        method="get_xbrl_taxonomy",
        params={"sj_div": "{sj_div}"},
        description="XBRL 택사노미 조회",
    ),
    EndpointConfig(
        id="DS003-06",
        name="financial.get_indicators",
        category="DS003",
        service="financial",
        method="get_indicators",
        params={
            "corp_code": "{corp_code}",
            "bsns_year": "{bsns_year}",
            "reprt_code": "{reprt_code}",
        },
        description="재무지표 조회",
    ),
    # DS004 - 지분공시 종합정보 (2개)
    EndpointConfig(
        id="DS004-01",
        name="shareholder.get_major_stock",
        category="DS004",
        service="shareholder",
        method="get_major_stock",
        params={"corp_code": "{corp_code}"},
        description="대량보유 상황보고 조회",
    ),
    EndpointConfig(
        id="DS004-02",
        name="shareholder.get_executive_stock",
        category="DS004",
        service="shareholder",
        method="get_executive_stock",
        params={"corp_code": "{corp_code}"},
        description="임원/주요주주 소유보고 조회",
    ),
    # DS005 - 주요사항보고서 주요정보 (6개)
    EndpointConfig(
        id="DS005-01",
        name="major_event.get_paid_capital_increase",
        category="DS005",
        service="major_event",
        method="get_paid_capital_increase",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="유상증자 결정 조회",
    ),
    EndpointConfig(
        id="DS005-02",
        name="major_event.get_bonus_issue",
        category="DS005",
        service="major_event",
        method="get_bonus_issue",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="무상증자 결정 조회",
    ),
    EndpointConfig(
        id="DS005-03",
        name="major_event.get_capital_reduction",
        category="DS005",
        service="major_event",
        method="get_capital_reduction",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="감자 결정 조회",
    ),
    EndpointConfig(
        id="DS005-04",
        name="major_event.get_convertible_bond",
        category="DS005",
        service="major_event",
        method="get_convertible_bond",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="전환사채권 발행결정 조회",
    ),
    EndpointConfig(
        id="DS005-05",
        name="major_event.get_merger_decision",
        category="DS005",
        service="major_event",
        method="get_merger_decision",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="합병 결정 조회",
    ),
    EndpointConfig(
        id="DS005-06",
        name="major_event.get_split_decision",
        category="DS005",
        service="major_event",
        method="get_split_decision",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="분할 결정 조회",
    ),
    # DS006 - 증권신고서 주요정보 (4개)
    EndpointConfig(
        id="DS006-01",
        name="registration.get_equity_securities",
        category="DS006",
        service="registration",
        method="get_equity_securities",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="지분증권 발행 조회",
    ),
    EndpointConfig(
        id="DS006-02",
        name="registration.get_debt_securities",
        category="DS006",
        service="registration",
        method="get_debt_securities",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="채무증권 발행 조회",
    ),
    EndpointConfig(
        id="DS006-03",
        name="registration.get_merger_registration",
        category="DS006",
        service="registration",
        method="get_merger_registration",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="합병 신고 조회",
    ),
    EndpointConfig(
        id="DS006-04",
        name="registration.get_split_registration",
        category="DS006",
        service="registration",
        method="get_split_registration",
        params={
            "corp_code": "{corp_code}",
            "bgn_de": "{bgn_de}",
            "end_de": "{end_de}",
        },
        description="분할 신고 조회",
    ),
]

# 카테고리 설명
CATEGORY_DESCRIPTIONS = {
    "DS001": "공시정보",
    "DS002": "정기보고서 주요정보",
    "DS003": "정기보고서 재무정보",
    "DS004": "지분공시 종합정보",
    "DS005": "주요사항보고서 주요정보",
    "DS006": "증권신고서 주요정보",
}
