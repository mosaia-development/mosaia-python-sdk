"""Notifications client (Node parity: collections/notifications.ts)."""

from typing import Any, Dict

from ..utils.api_client import APIClient


class Notifications:
    def __init__(self, uri: str = "") -> None:
        self._base = f"{uri}/notify"
        self._api_client = APIClient()

    async def send_email(self, email: Dict[str, Any]) -> Any:
        response = await self._api_client.post(f"{self._base}/email", email)
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response
