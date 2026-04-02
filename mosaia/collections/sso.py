"""SSO client (Node parity: collections/sso.ts)."""

from typing import Any, Dict

from ..utils.api_client import APIClient


class SSO:
    def __init__(self, uri: str = "") -> None:
        self._uri = f"{uri}/sso"
        self._api_client = APIClient()

    async def authenticate(self, request: Dict[str, Any]) -> Any:
        response = await self._api_client.post(self._uri, request)
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response
