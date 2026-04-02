"""Agent logs collection (Node parity: collections/logs.ts)."""

from typing import Any, Dict

from ..models.log import Log
from .base_collection import BaseCollection


class Logs(BaseCollection[Dict[str, Any], Log, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/log", Log)
