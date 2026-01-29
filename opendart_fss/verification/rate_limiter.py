"""적응형 Rate Limiter."""

import asyncio
import time


class AdaptiveRateLimiter:
    """지수 백오프를 사용하는 적응형 Rate Limiter.

    Rate limit 오류 발생 시 지수적으로 대기 시간을 증가시키고,
    성공 시 점진적으로 감소시킵니다.

    Example:
        ```python
        limiter = AdaptiveRateLimiter()

        async def make_request():
            await limiter.wait()
            try:
                result = await api_call()
                limiter.on_success()
                return result
            except RateLimitError:
                limiter.on_rate_limit()
                raise
        ```
    """

    def __init__(
        self,
        min_delay: float = 0.5,
        max_delay: float = 16.0,
        backoff_factor: float = 2.0,
        recovery_factor: float = 0.9,
    ) -> None:
        """Rate Limiter 초기화.

        Args:
            min_delay: 최소 요청 간격 (초)
            max_delay: 최대 요청 간격 (초)
            backoff_factor: Rate limit 시 지연 증가 배수
            recovery_factor: 성공 시 지연 감소 배수
        """
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.backoff_factor = backoff_factor
        self.recovery_factor = recovery_factor

        self._current_delay = min_delay
        self._last_request_time: float = 0.0
        self._rate_limit_count = 0

    @property
    def current_delay(self) -> float:
        """현재 요청 간격."""
        return self._current_delay

    @property
    def rate_limit_count(self) -> int:
        """Rate limit 발생 횟수."""
        return self._rate_limit_count

    async def wait(self) -> None:
        """다음 요청 전 필요한 시간만큼 대기."""
        now = time.monotonic()
        elapsed = now - self._last_request_time

        if elapsed < self._current_delay:
            await asyncio.sleep(self._current_delay - elapsed)

        self._last_request_time = time.monotonic()

    def on_success(self) -> None:
        """요청 성공 시 호출. 대기 시간 점진적 감소."""
        self._current_delay = max(
            self.min_delay,
            self._current_delay * self.recovery_factor,
        )

    def on_rate_limit(self) -> None:
        """Rate limit 발생 시 호출. 대기 시간 지수적 증가."""
        self._rate_limit_count += 1
        self._current_delay = min(
            self.max_delay,
            self._current_delay * self.backoff_factor,
        )

    def reset(self) -> None:
        """Rate limiter 상태 초기화."""
        self._current_delay = self.min_delay
        self._last_request_time = 0.0
        self._rate_limit_count = 0
