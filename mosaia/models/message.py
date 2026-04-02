"""Log message model (Node parity: models/message.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Message(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/message")
