"""Plans collection (Node parity: collections/plans.ts)."""

from typing import Any, Dict

from ..models.plan import Plan
from .base_collection import BaseCollection


class Plans(BaseCollection[Dict[str, Any], Plan, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/plan", Plan)
