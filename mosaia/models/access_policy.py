"""Access policy model (Node parity: models/access-policy.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class AccessPolicy(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/iam/policy")
