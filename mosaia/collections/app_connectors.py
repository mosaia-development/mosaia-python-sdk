"""App connectors collection (Node parity: collections/app-connectors.ts)."""

from typing import Any, Dict

from ..models.app_connector import AppConnector
from .base_collection import BaseCollection


class AppConnectors(BaseCollection[Dict[str, Any], AppConnector, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/connector", AppConnector)
