"""Drive items collection (Node parity: collections/drive-items.ts)."""

from typing import Any, Dict, List, Union

from ..models.drive_item import DriveItem
from .base_collection import BaseCollection


class DriveItems(BaseCollection[Dict[str, Any], DriveItem, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/item", DriveItem)

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
