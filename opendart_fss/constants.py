"""OpenDART API 상수 정의."""

from enum import StrEnum

BASE_URL = "https://opendart.fss.or.kr"


class StatusCode(StrEnum):
    """API 응답 상태 코드."""

    SUCCESS = "000"
    UNREGISTERED_KEY = "010"
    INACTIVE_KEY = "011"
    INVALID_KEY = "012"
    USAGE_LIMIT_EXCEEDED = "013"
    DAILY_LIMIT_EXCEEDED_FIELD = "014"
    DAILY_LIMIT_EXCEEDED_REQUESTS = "015"
    MONTHLY_LIMIT_EXCEEDED = "016"
    INVALID_PARAMETER = "020"
    MISSING_REQUIRED_PARAMETER = "021"
    INVALID_REPORT_CODE = "022"
    INVALID_DATE = "023"
    NO_DATA = "100"
    FILE_NOT_FOUND = "101"
    SYSTEM_ERROR = "800"
    MAINTENANCE = "900"
    UNKNOWN = "999"


STATUS_MESSAGES: dict[StatusCode, str] = {
    StatusCode.SUCCESS: "정상",
    StatusCode.UNREGISTERED_KEY: "등록되지 않은 키",
    StatusCode.INACTIVE_KEY: "사용할 수 없는 키",
    StatusCode.INVALID_KEY: "잘못된 키",
    StatusCode.USAGE_LIMIT_EXCEEDED: "일시적 사용 제한",
    StatusCode.DAILY_LIMIT_EXCEEDED_FIELD: "필드 일일 조회 한도 초과",
    StatusCode.DAILY_LIMIT_EXCEEDED_REQUESTS: "요청 일일 한도 초과",
    StatusCode.MONTHLY_LIMIT_EXCEEDED: "월간 조회 한도 초과",
    StatusCode.INVALID_PARAMETER: "잘못된 파라미터",
    StatusCode.MISSING_REQUIRED_PARAMETER: "필수 파라미터 누락",
    StatusCode.INVALID_REPORT_CODE: "잘못된 보고서 코드",
    StatusCode.INVALID_DATE: "잘못된 날짜",
    StatusCode.NO_DATA: "조회된 데이터 없음",
    StatusCode.FILE_NOT_FOUND: "파일 없음",
    StatusCode.SYSTEM_ERROR: "시스템 오류",
    StatusCode.MAINTENANCE: "시스템 점검",
    StatusCode.UNKNOWN: "알 수 없는 오류",
}


class ReportCode(StrEnum):
    """보고서 코드."""

    Q1 = "11013"  # 1분기보고서
    HALF = "11012"  # 반기보고서
    Q3 = "11014"  # 3분기보고서
    ANNUAL = "11011"  # 사업보고서


class CorpClass(StrEnum):
    """기업 분류 코드."""

    KOSPI = "Y"  # 유가증권시장
    KOSDAQ = "K"  # 코스닥시장
    KONEX = "N"  # 코넥스시장
    ETC = "E"  # 기타법인


class DisclosureType(StrEnum):
    """공시 유형 코드."""

    A = "A"  # 정기공시
    B = "B"  # 주요사항보고
    C = "C"  # 발행공시
    D = "D"  # 지분공시
    E = "E"  # 기타공시
    F = "F"  # 외부감사관련
    G = "G"  # 펀드공시
    H = "H"  # 자산유동화
    I = "I"  # 거래소공시  # noqa: E741
    J = "J"  # 공정위공시


class FinancialStatementType(StrEnum):
    """재무제표 구분 코드."""

    CONSOLIDATED = "CFS"  # 연결재무제표
    SEPARATE = "OFS"  # 개별재무제표
