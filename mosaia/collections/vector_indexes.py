"""Vector indexes collection (Node parity: collections/vector-indexes.ts)."""

from typing import Any, Dict

from ..models.vector_index import VectorIndex
from .base_collection import BaseCollection


class VectorIndexes(BaseCollection[Dict[str, Any], VectorIndex, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/index", VectorIndex)
