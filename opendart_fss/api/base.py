"""API 기본 클래스."""

from typing import TYPE_CHECKING

import httpx
import msgspec

from opendart_fss.constants import BASE_URL
from opendart_fss.exceptions import raise_for_status

if TYPE_CHECKING:
    from opendart_fss.client import OpenDartClient


class BaseAPI:
    """API 기본 클래스."""

    def __init__(self, client: "OpenDartClient") -> None:
        self._client = client

    @property
    def _http(self) -> httpx.AsyncClient:
        return self._client._http

    @property
    def _api_key(self) -> str:
        return self._client.api_key

    async def _request[T: msgspec.Struct](
        self,
        method: str,
        endpoint: str,
        response_type: type[T],
        *,
        params: dict | None = None,
    ) -> T:
        """API 요청 수행."""
        url = f"{BASE_URL}{endpoint}"
        request_params = {"crtfc_key": self._api_key}
        if params:
            request_params.update({k: v for k, v in params.items() if v is not None})

        response = await self._http.request(method, url, params=request_params)
        response.raise_for_status()

        result = msgspec.json.decode(response.content, type=response_type)

        if hasattr(result, "status"):
            raise_for_status(result.status, getattr(result, "message", None))

        return result

    async def _get[T: msgspec.Struct](
        self,
        endpoint: str,
        response_type: type[T],
        *,
        params: dict | None = None,
    ) -> T:
        """GET 요청."""
        return await self._request("GET", endpoint, response_type, params=params)

    async def _download(self, endpoint: str, *, params: dict | None = None) -> bytes:
        """파일 다운로드 (ZIP, XML 등)."""
        url = f"{BASE_URL}{endpoint}"
        request_params = {"crtfc_key": self._api_key}
        if params:
            request_params.update({k: v for k, v in params.items() if v is not None})

        response = await self._http.get(url, params=request_params)
        response.raise_for_status()
        return response.content
