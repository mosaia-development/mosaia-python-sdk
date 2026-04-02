"""Vector embedding model (Node parity: models/vector.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class Vector(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/vector")
