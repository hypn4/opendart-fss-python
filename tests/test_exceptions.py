"""예외 테스트."""

import pytest

from opendart_fss.constants import StatusCode
from opendart_fss.exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
    raise_for_status,
)


class TestExceptions:
    """예외 클래스 테스트."""

    def test_raise_for_status_success(self) -> None:
        """성공 상태 코드 테스트."""
        # 성공 시 예외가 발생하지 않아야 함
        raise_for_status(StatusCode.SUCCESS)

    def test_raise_for_status_authentication_error(self) -> None:
        """인증 오류 테스트."""
        with pytest.raises(AuthenticationError) as exc_info:
            raise_for_status(StatusCode.UNREGISTERED_KEY)
        assert exc_info.value.status == StatusCode.UNREGISTERED_KEY

        with pytest.raises(AuthenticationError):
            raise_for_status(StatusCode.INACTIVE_KEY)

        with pytest.raises(AuthenticationError):
            raise_for_status(StatusCode.INVALID_KEY)

    def test_raise_for_status_rate_limit_error(self) -> None:
        """요청 제한 오류 테스트."""
        with pytest.raises(RateLimitError):
            raise_for_status(StatusCode.USAGE_LIMIT_EXCEEDED)

        with pytest.raises(RateLimitError):
            raise_for_status(StatusCode.DAILY_LIMIT_EXCEEDED_FIELD)

        with pytest.raises(RateLimitError):
            raise_for_status(StatusCode.DAILY_LIMIT_EXCEEDED_REQUESTS)

        with pytest.raises(RateLimitError):
            raise_for_status(StatusCode.MONTHLY_LIMIT_EXCEEDED)

    def test_raise_for_status_validation_error(self) -> None:
        """검증 오류 테스트."""
        with pytest.raises(ValidationError):
            raise_for_status(StatusCode.INVALID_PARAMETER)

        with pytest.raises(ValidationError):
            raise_for_status(StatusCode.MISSING_REQUIRED_PARAMETER)

        with pytest.raises(ValidationError):
            raise_for_status(StatusCode.INVALID_REPORT_CODE)

        with pytest.raises(ValidationError):
            raise_for_status(StatusCode.INVALID_DATE)

    def test_raise_for_status_not_found_error(self) -> None:
        """데이터 없음 오류 테스트."""
        with pytest.raises(NotFoundError):
            raise_for_status(StatusCode.NO_DATA)

        with pytest.raises(NotFoundError):
            raise_for_status(StatusCode.FILE_NOT_FOUND)

    def test_raise_for_status_server_error(self) -> None:
        """서버 오류 테스트."""
        with pytest.raises(ServerError):
            raise_for_status(StatusCode.SYSTEM_ERROR)

        with pytest.raises(ServerError):
            raise_for_status(StatusCode.MAINTENANCE)

    def test_raise_for_status_unknown_error(self) -> None:
        """알 수 없는 오류 테스트."""
        with pytest.raises(APIError):
            raise_for_status(StatusCode.UNKNOWN)

        with pytest.raises(APIError):
            raise_for_status("999")

    def test_error_message(self) -> None:
        """오류 메시지 테스트."""
        with pytest.raises(APIError) as exc_info:
            raise_for_status(StatusCode.NO_DATA, "커스텀 메시지")
        assert exc_info.value.message == "커스텀 메시지"
