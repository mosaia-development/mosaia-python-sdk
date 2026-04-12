"""Agent logs collection (Node parity: collections/logs.ts)."""

from typing import Any, Dict, List

from ..models.log import Log
from .base_collection import BaseCollection


class Logs(BaseCollection[Dict[str, Any], Log, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/log", Log)

    async def batch_delete(
        self,
        ids: List[str],
        *,
        hard_delete: bool = False,
    ) -> Dict[str, Any]:
        """Batch delete multiple agent logs by ID.

        Args:
            ids: List of AgentLog IDs to delete.
            hard_delete: If ``True``, permanently removes logs (default soft-delete).

        Returns:
            Dict with ``deleted`` (list of IDs) and ``failed`` (list of dicts
            with ``id`` and ``error``).
        """
        if not ids:
            raise Exception("ids must be a non-empty list")

        body: Dict[str, Any] = {"ids": ids}
        if hard_delete:
            body["delete"] = True

        response = await self.api_client.post(f"{self.uri}/batch-delete", body)

        data = response.get("data") if isinstance(response, dict) else response
        if not isinstance(data, dict):
            data = {}
        return {
            "deleted": data.get("deleted", []),
            "failed": data.get("failed", []),
        }
