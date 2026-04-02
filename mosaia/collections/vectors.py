"""Vectors collection (Node parity: collections/vectors.ts)."""

from typing import Any, Dict

from ..models.vector import Vector
from .base_collection import BaseCollection


class Vectors(BaseCollection[Dict[str, Any], Vector, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/vector", Vector)
