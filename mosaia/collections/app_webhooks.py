"""App webhooks collection (Node parity: collections/app-webhooks.ts)."""

from typing import Any, Dict

from ..models.app_webhook import AppWebhook
from .base_collection import BaseCollection


class AppWebhooks(BaseCollection[Dict[str, Any], AppWebhook, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/hook", AppWebhook)
