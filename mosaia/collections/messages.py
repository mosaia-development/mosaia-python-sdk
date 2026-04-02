"""Log messages collection (Node parity: collections/messages.ts)."""

from typing import Any, Dict

from ..models.message import Message
from .base_collection import BaseCollection


class Messages(BaseCollection[Dict[str, Any], Message, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/message", Message)
