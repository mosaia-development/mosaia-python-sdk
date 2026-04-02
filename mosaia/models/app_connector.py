"""App connector model (Node parity: models/app-connector.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class AppConnector(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/connector")
