"""OAuth scopes client (Node parity: collections/scopes.ts)."""

from typing import Any

from ..utils.api_client import APIClient


class Scopes:
    def __init__(self, uri: str = "") -> None:
        self._uri = f"{uri}/scope"
        self._api_client = APIClient()

    async def get(self) -> Any:
        response = await self._api_client.get(self._uri)
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response
