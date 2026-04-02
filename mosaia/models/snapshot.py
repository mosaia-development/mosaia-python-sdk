"""Snapshot model (Node parity: models/snapshot.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Snapshot(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/snapshot")
