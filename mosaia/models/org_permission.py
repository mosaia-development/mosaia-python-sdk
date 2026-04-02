"""Org permission model (Node parity: models/org-permission.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class OrgPermission(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/iam/permission")
