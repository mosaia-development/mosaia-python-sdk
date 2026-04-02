"""Meters collection (Node parity: collections/meters.ts)."""

from typing import Any, Dict

from ..models.meter import Meter
from .base_collection import BaseCollection


class Meters(BaseCollection[Dict[str, Any], Meter, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/billing/usage", Meter)
