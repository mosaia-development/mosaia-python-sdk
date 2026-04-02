"""Drives collection (Node parity: collections/drives.ts)."""

from typing import Any, Dict

from ..models.drive import Drive
from .base_collection import BaseCollection


class Drives(BaseCollection[Dict[str, Any], Drive, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/drive", Drive)
