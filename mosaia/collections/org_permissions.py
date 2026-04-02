"""Org permissions collection (Node parity: collections/org-permissions.ts)."""

from typing import Any, Dict

from ..models.org_permission import OrgPermission
from .base_collection import BaseCollection


class OrgPermissions(BaseCollection[Dict[str, Any], OrgPermission, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/iam/permission", OrgPermission)
