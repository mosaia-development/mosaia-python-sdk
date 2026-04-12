"""Drive items collection (Node parity: collections/drive-items.ts)."""

from typing import Any, Dict, List, Union

from ..models.drive_item import DriveItem
from .base_collection import BaseCollection


class DriveItems(BaseCollection[Dict[str, Any], DriveItem, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/item", DriveItem)

    async def batch_delete(
        self,
        ids: List[str],
        *,
        hard_delete: bool = False,
    ) -> Dict[str, Any]:
        """Batch delete multiple drive items by ID.

        Sends a single request to delete multiple items.  Each item is
        access-controlled individually on the server — items that fail
        validation or permission checks are reported in ``failed`` without
        blocking the rest.

        Args:
            ids: List of DriveItem IDs to delete.
            hard_delete: If ``True``, permanently removes items (default soft-delete).

        Returns:
            Dict with ``deleted`` (list of IDs) and ``failed`` (list of dicts
            with ``id`` and ``error``).

        Example::

            drive = await client.drives.get({}, drive_id)
            result = await drive.items.batch_delete(["id1", "id2", "id3"])
            print(f"Deleted: {len(result['deleted'])}")
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

    async def find_by_path(
        self,
        path: str,
        *,
        case_sensitive: bool = True,
    ) -> Union[DriveItem, List[DriveItem], None]:
        if not path or not str(path).strip():
            raise Exception("Path is required")
        normalized = path[1:] if path.startswith("/") else path
        base = self.uri.rstrip("/")
        path_uri = base if not normalized else f"{base}/{normalized}"
        params: Dict[str, Any] = {}
        if not case_sensitive:
            params["caseSensitive"] = "false"
        try:
            response = await self.api_client.get(path_uri, params if params else None)
        except Exception as e:
            if "404" in str(e).lower():
                return None
            raise
        if response is None:
            return None
        data = response.get("data") if isinstance(response, dict) else response
        if data is None:
            return None
        if isinstance(data, list):
            return [DriveItem(item, path_uri) for item in data]
        if isinstance(data, dict):
            return DriveItem(data, path_uri)
        return None
