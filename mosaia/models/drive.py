"""Drive model (Node parity: models/drive.ts)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from .base import BaseModel


class Drive(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/drive")

    @property
    def items(self):
        from ..collections.drive_items import DriveItems

        return DriveItems(self.get_uri())

    @property
    def uploads(self):
        from ..collections.upload_jobs import UploadJobs

        return UploadJobs(self.get_uri())

    @property
    def indexes(self):
        from ..collections.vector_indexes import VectorIndexes

        return VectorIndexes(self.get_uri())

    @property
    def access(self):
        from ..functions.access import Access

        return Access(self.get_uri())

    async def find_item_by_path(
        self,
        path: str,
        *,
        case_sensitive: bool = True,
    ) -> Union["DriveItem", List["DriveItem"], None]:
        if not self.data.get("id"):
            raise Exception("Cannot find item by path for unsaved drive")
        return await self.items.find_by_path(path, case_sensitive=case_sensitive)
