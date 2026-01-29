"""OpenDART API 예외 클래스."""

from opendart_fss.constants import STATUS_MESSAGES, StatusCode


class OpenDartError(Exception):
    """OpenDART API 기본 예외."""

    def __init__(self, message: str, status: str | None = None):
        self.status = status
        self.message = message
        super().__init__(message)


class APIError(OpenDartError):
    """API 응답 오류."""

    def __init__(self, status: str, message: str | None = None):
        try:
            status_code = StatusCode(status)
            default_message = STATUS_MESSAGES.get(status_code, "알 수 없는 오류")
        except ValueError:
            default_message = "알 수 없는 오류"
        super().__init__(message or default_message, status)


class AuthenticationError(APIError):
    """인증 관련 오류 (010, 011, 012)."""

    pass


class RateLimitError(APIError):
    """요청 제한 오류 (013, 014, 015, 016)."""

    pass


class ValidationError(APIError):
    """파라미터 검증 오류 (020, 021, 022, 023)."""

    pass


class NotFoundError(APIError):
    """데이터 없음 오류 (100, 101)."""

    pass


class ServerError(APIError):
    """서버 오류 (800, 900)."""

    pass


def raise_for_status(status: str, message: str | None = None) -> None:
    """상태 코드에 따른 예외 발생."""
    if status == StatusCode.SUCCESS:
        return

    error_class: type[APIError]
    if status in (
        StatusCode.UNREGISTERED_KEY,
        StatusCode.INACTIVE_KEY,
        StatusCode.INVALID_KEY,
    ):
        error_class = AuthenticationError
    elif status in (
        StatusCode.USAGE_LIMIT_EXCEEDED,
        StatusCode.DAILY_LIMIT_EXCEEDED_FIELD,
        StatusCode.DAILY_LIMIT_EXCEEDED_REQUESTS,
        StatusCode.MONTHLY_LIMIT_EXCEEDED,
    ):
        error_class = RateLimitError
    elif status in (
        StatusCode.INVALID_PARAMETER,
        StatusCode.MISSING_REQUIRED_PARAMETER,
        StatusCode.INVALID_REPORT_CODE,
        StatusCode.INVALID_DATE,
    ):
        error_class = ValidationError
    elif status in (StatusCode.NO_DATA, StatusCode.FILE_NOT_FOUND):
        error_class = NotFoundError
    elif status in (StatusCode.SYSTEM_ERROR, StatusCode.MAINTENANCE):
        error_class = ServerError
    else:
        error_class = APIError

    raise error_class(status, message)
