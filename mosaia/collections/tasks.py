"""Tasks collection (Node parity: collections/tasks.ts)."""

from typing import Any, Dict, List

from ..models.task import Task
from .base_collection import BaseCollection


class Tasks(BaseCollection[Dict[str, Any], Task, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/task", Task)

    async def batch_delete(
        self,
        ids: List[str],
        *,
        hard_delete: bool = False,
    ) -> Dict[str, Any]:
        """Batch delete multiple tasks by ID.

        Args:
            ids: List of Task IDs to delete.
            hard_delete: If ``True``, permanently removes tasks (default soft-delete).

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
