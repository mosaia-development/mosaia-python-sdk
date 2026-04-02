"""Agent log model (Node parity: models/log.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Log(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/log")

    @property
    def messages(self):
        from ..collections.messages import Messages

        return Messages(self.get_uri())

    @property
    def snapshots(self):
        from ..collections.snapshots import Snapshots

        return Snapshots(self.get_uri())
