"""Plan model (Node parity: models/plan.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Plan(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/plan")

    @property
    def tasks(self):
        from ..collections.tasks import Tasks

        return Tasks(self.get_uri())

    @property
    def triggers(self):
        from ..collections.triggers import Triggers

        return Triggers(self.get_uri())

    async def execute(self, message: Optional[Dict[str, Any]] = None) -> Any:
        body = {}
        if message:
            body = {
                "content": message.get("content", ""),
                "role": message.get("role", "user"),
            }
        response = await self.api_client.post(f"{self.get_uri()}/execute", body)
        if isinstance(response, dict) and "data" in response:
            data = response["data"]
            if isinstance(data, dict):
                self.update(data)
            return data
        return response

    async def approve(self, options: Optional[Dict[str, Any]] = None) -> Any:
        response = await self.api_client.post(
            f"{self.get_uri()}/approve", options or {}
        )
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response
