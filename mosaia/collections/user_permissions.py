"""User permissions collection (Node parity: collections/user-permissions.ts)."""

from typing import Any, Dict

from ..models.user_permission import UserPermission
from .base_collection import BaseCollection


class UserPermissions(BaseCollection[Dict[str, Any], UserPermission, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/iam/permission", UserPermission)
