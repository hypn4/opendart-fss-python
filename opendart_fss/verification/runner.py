"""엔드포인트 검증 실행기."""

import time
from typing import Any

from opendart_fss.client import OpenDartClient
from opendart_fss.exceptions import (
    APIError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)
from opendart_fss.verification.config import (
    DEFAULT_TEST_DATA,
    ENDPOINT_CONFIGS,
    EndpointConfig,
    VerificationResult,
    VerificationStatus,
)
from opendart_fss.verification.rate_limiter import AdaptiveRateLimiter


class EndpointVerifier:
    """OpenDART API 엔드포인트 검증기.

    Example:
        ```python
        async with EndpointVerifier() as verifier:
            # 모든 엔드포인트 검증
            results = await verifier.verify_all()

            # 특정 카테고리만 검증
            results = await verifier.verify_category("DS001")

            # 특정 엔드포인트만 검증
            result = await verifier.verify_endpoint("DS001-01")
        ```
    """

    def __init__(
        self,
        api_key: str | None = None,
        test_data: dict[str, str] | None = None,
        max_retries: int = 3,
    ) -> None:
        """검증기 초기화.

        Args:
            api_key: OpenDART API 키 (환경변수에서 자동 로드 가능)
            test_data: 테스트 데이터 (기본값 사용 가능)
            max_retries: Rate limit 시 최대 재시도 횟수
        """
        self._api_key = api_key
        self._test_data = {**DEFAULT_TEST_DATA, **(test_data or {})}
        self._max_retries = max_retries
        self._rate_limiter = AdaptiveRateLimiter()
        self._client: OpenDartClient | None = None
        self._rcept_no: str | None = None  # 공시 검색에서 획득

    async def __aenter__(self) -> "EndpointVerifier":
        """컨텍스트 매니저 진입."""
        self._client = OpenDartClient(api_key=self._api_key)
        return self

    async def __aexit__(self, *args: Any) -> None:
        """컨텍스트 매니저 종료."""
        if self._client:
            await self._client.close()

    async def verify_all(
        self,
        category: str | None = None,
    ) -> list[VerificationResult]:
        """모든 엔드포인트 검증.

        Args:
            category: 특정 카테고리만 검증 (예: "DS001")

        Returns:
            검증 결과 목록
        """
        configs = ENDPOINT_CONFIGS
        if category:
            configs = [c for c in configs if c.category == category]

        results: list[VerificationResult] = []
        for config in configs:
            result = await self._verify_with_retry(config)
            results.append(result)

        return results

    async def verify_category(self, category: str) -> list[VerificationResult]:
        """특정 카테고리의 모든 엔드포인트 검증.

        Args:
            category: 카테고리 ID (예: "DS001")

        Returns:
            검증 결과 목록
        """
        return await self.verify_all(category=category)

    async def verify_endpoint(self, endpoint_id: str) -> VerificationResult:
        """특정 엔드포인트 검증.

        Args:
            endpoint_id: 엔드포인트 ID (예: "DS001-01")

        Returns:
            검증 결과
        """
        config = next(
            (c for c in ENDPOINT_CONFIGS if c.id == endpoint_id),
            None,
        )
        if not config:
            return VerificationResult(
                endpoint_id=endpoint_id,
                endpoint_name="unknown",
                category="unknown",
                status=VerificationStatus.FAILED,
                error_message=f"Unknown endpoint: {endpoint_id}",
            )

        return await self._verify_with_retry(config)

    async def _verify_with_retry(
        self,
        config: EndpointConfig,
    ) -> VerificationResult:
        """재시도 로직을 포함한 엔드포인트 검증.

        Args:
            config: 엔드포인트 설정

        Returns:
            검증 결과
        """
        for attempt in range(self._max_retries + 1):
            await self._rate_limiter.wait()

            result = await self._verify_single(config)

            if result.status == VerificationStatus.FAILED:
                if "rate limit" in (result.error_message or "").lower():
                    self._rate_limiter.on_rate_limit()
                    if attempt < self._max_retries:
                        continue
                    result.error_message = (
                        f"{result.error_message} (after {attempt + 1} retries)"
                    )
            else:
                self._rate_limiter.on_success()

            return result

        return result

    async def _verify_single(self, config: EndpointConfig) -> VerificationResult:
        """단일 엔드포인트 검증.

        Args:
            config: 엔드포인트 설정

        Returns:
            검증 결과
        """
        if not self._client:
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.FAILED,
                error_message="Client not initialized. Use async with.",
            )

        # rcept_no가 필요한데 없으면 스킵
        if config.requires_rcept_no and not self._rcept_no:
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.SKIPPED,
                error_message="Requires rcept_no from disclosure.search",
            )

        # 파라미터 치환
        params = self._resolve_params(config.params)

        start_time = time.perf_counter()
        try:
            # 서비스와 메서드 가져오기
            service = getattr(self._client, config.service)
            method = getattr(service, config.method)

            # API 호출
            result = await method(**params)
            elapsed_ms = (time.perf_counter() - start_time) * 1000

            # 결과 분석
            status = self._analyze_result(result)

            # 공시 검색 결과에서 rcept_no 저장
            if config.method == "search" and result:
                self._rcept_no = result[0].rcept_no

            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=status,
                response_time_ms=elapsed_ms,
                response_data=self._summarize_result(result),
            )

        except NotFoundError as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.NO_DATA,
                response_time_ms=elapsed_ms,
                error_message=str(e),
            )

        except RateLimitError as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.FAILED,
                response_time_ms=elapsed_ms,
                error_message=f"Rate limit: {e}",
            )

        except ValidationError as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.FAILED,
                response_time_ms=elapsed_ms,
                error_message=f"Validation error: {e}",
            )

        except APIError as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.FAILED,
                response_time_ms=elapsed_ms,
                error_message=f"API error ({e.status}): {e}",
            )

        except Exception as e:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            return VerificationResult(
                endpoint_id=config.id,
                endpoint_name=config.name,
                category=config.category,
                status=VerificationStatus.FAILED,
                response_time_ms=elapsed_ms,
                error_message=str(e),
            )

    def _resolve_params(self, params: dict[str, str]) -> dict[str, Any]:
        """파라미터 템플릿을 실제 값으로 치환.

        Args:
            params: 템플릿 파라미터

        Returns:
            치환된 파라미터
        """
        resolved = {}
        for key, value in params.items():
            if value.startswith("{") and value.endswith("}"):
                param_name = value[1:-1]
                if param_name == "rcept_no":
                    resolved[key] = self._rcept_no
                else:
                    resolved[key] = self._test_data.get(param_name, value)
            else:
                resolved[key] = value
        return resolved

    def _analyze_result(self, result: Any) -> VerificationStatus:
        """결과를 분석하여 상태 반환.

        Args:
            result: API 응답

        Returns:
            검증 상태
        """
        if result is None:
            return VerificationStatus.NO_DATA
        if isinstance(result, (list, tuple)):
            return VerificationStatus.SUCCESS if result else VerificationStatus.NO_DATA
        if isinstance(result, bytes):
            return VerificationStatus.SUCCESS if result else VerificationStatus.NO_DATA
        return VerificationStatus.SUCCESS

    def _summarize_result(self, result: Any) -> dict[str, Any]:
        """결과 요약.

        Args:
            result: API 응답

        Returns:
            요약된 결과
        """
        if result is None:
            return {"type": "null"}
        if isinstance(result, bytes):
            return {"type": "bytes", "size": len(result)}
        if isinstance(result, (list, tuple)):
            return {"type": "list", "count": len(result)}
        return {"type": type(result).__name__}
