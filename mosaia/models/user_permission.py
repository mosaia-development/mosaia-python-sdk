"""User permission model (Node parity: models/user-permission.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class UserPermission(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/iam/permission")
