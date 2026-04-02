"""Agent tool model (Node parity: models/agent-tool.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class AgentTool(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/tool")
