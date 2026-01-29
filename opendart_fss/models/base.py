"""기본 응답 모델."""

import msgspec


class BaseResponse(msgspec.Struct, kw_only=True):
    """API 기본 응답."""

    status: str
    message: str
