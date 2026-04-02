"""Drive item model (Node parity: models/drive-item.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class DriveItem(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/item")

    async def download_url(self, expires_in: Optional[int] = None) -> str:
        if not self.data.get("id"):
            raise Exception("Cannot get download URL for unsaved drive item")
        cfg = self.config_manager.get_config()
        api = (getattr(cfg, "api_url", None) or "").rstrip("/")
        path = f"{self.get_uri()}/download"
        if not path.startswith("/"):
            path = "/" + path
        suffix = f"?expires_in={expires_in}" if expires_in is not None else ""
        return f"{api}{path}{suffix}"

    @property
    def indexes(self):
        if not self.data.get("id"):
            raise Exception("Cannot access indexes for unsaved drive item")
        from ..collections.vector_indexes import VectorIndexes

        return VectorIndexes(self.get_uri())

    @property
    def access(self):
        if not self.data.get("id"):
            raise Exception("Cannot access permissions for unsaved drive item")
        from ..functions.access import Access

        return Access(self.get_uri())
