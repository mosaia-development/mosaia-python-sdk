"""Access policies collection (Node parity: collections/access-policies.ts)."""

from typing import Any, Dict

from ..models.access_policy import AccessPolicy
from .base_collection import BaseCollection


class AccessPolicies(BaseCollection[Dict[str, Any], AccessPolicy, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/iam/policy", AccessPolicy)
