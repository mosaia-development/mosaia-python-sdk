"""Task model (Node parity: models/task.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Task(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/task")

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
