"""Snapshots collection (Node parity: collections/snapshots.ts)."""

from typing import Any, Dict

from ..models.snapshot import Snapshot
from .base_collection import BaseCollection


class Snapshots(BaseCollection[Dict[str, Any], Snapshot, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/snapshot", Snapshot)
