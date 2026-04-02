"""App webhook model (Node parity: models/app-webhook.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class AppWebhook(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/hook")
