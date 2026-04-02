"""Agent tools collection (Node parity: collections/agent-tools.ts)."""

from typing import Any, Dict

from ..models.agent_tool import AgentTool
from .base_collection import BaseCollection


class AgentTools(BaseCollection[Dict[str, Any], AgentTool, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/tool", AgentTool)
