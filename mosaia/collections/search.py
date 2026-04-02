"""Universal search client (Node parity: collections/search.ts)."""

from typing import Any, Dict

from ..utils.api_client import APIClient


class Search:
    def __init__(self, uri: str = "") -> None:
        self._uri = f"{uri}/search"
        self._api_client = APIClient()

    async def query(self, params: Dict[str, Any]) -> Any:
        response = await self._api_client.get(self._uri, params)
        if (
            isinstance(response, dict)
            and "data" in response
            and isinstance(response["data"], dict)
            and "data" in response["data"]
        ):
            return response["data"]
        return response
