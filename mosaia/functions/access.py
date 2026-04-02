"""
Drive / drive-item access control (Node parity: src/functions/access.ts).
"""

from typing import Any, Dict, Optional

from ..utils.api_client import APIClient

Accessor = Dict[str, Any]
GrantAccessOptions = Dict[str, Any]


def _normalize_accessor(accessor: Accessor) -> Dict[str, Optional[str]]:
    out: Dict[str, Optional[str]] = {}
    for key in ("user", "org_user", "agent", "client"):
        val = accessor.get(key)
        if val is None:
            continue
        if isinstance(val, str):
            out[key] = val
        else:
            oid = getattr(val, "id", None) or (
                val.get("id") if isinstance(val, dict) else None
            )
            out[key] = str(oid) if oid is not None else None
    return out


class Access:
    """Role-based grant/revoke/list for a drive or drive item resource."""

    def __init__(self, uri: str = "") -> None:
        self._api_client = APIClient()
        base = uri.rstrip("/")
        self._uri = f"{base}/access"

    async def grant_by_role(
        self,
        accessor: Accessor,
        role: str,
        options: Optional[GrantAccessOptions] = None,
    ) -> Any:
        normalized = _normalize_accessor(accessor)
        body: Dict[str, Any] = {
            "accessor": normalized,
            "role": role.upper(),
        }
        if options:
            body["options"] = options
        response = await self._api_client.post(self._uri, body)
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response

    async def grant(self, accessor: Accessor, action: str) -> Any:
        normalized = _normalize_accessor(accessor)
        response = await self._api_client.post(
            self._uri, {"accessor": normalized, "action": action}
        )
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response

    async def revoke(self, accessor: Accessor) -> Any:
        normalized = _normalize_accessor(accessor)
        response = await self._api_client.delete(
            self._uri, data={"accessor": normalized}
        )
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response

    async def list(self) -> Any:
        response = await self._api_client.get(self._uri)
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response
