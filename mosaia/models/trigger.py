"""
Trigger model for scheduled and event-based triggers (CRON, WEBHOOK, EVENT, MANUAL).

Triggers can be scoped to an agent, task, or plan. CRON triggers run on a schedule;
use config.cron_expression, config.timezone, and config.run_once for one-shot.
pause_on_completion controls whether the trigger is auto-paused when task/plan completes.
"""

from typing import Any, Dict, Optional

from ..types import TriggerExecuteResponse
from .base import BaseModel


class Trigger(BaseModel[Dict[str, Any]]):
    """
    Trigger class for managing scheduled and event-based triggers.

    Triggers can be scoped to an agent, task, or plan. CRON triggers run on a schedule;
    use config.cron_expression, config.timezone, and config.run_once for one-shot.
    """

    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data or {}, uri or "/trigger")

    async def execute(self) -> TriggerExecuteResponse:
        """
        Manually execute the trigger (async; invokes trigger-executor).

        Returns immediately with a confirmation; the actual run is asynchronous.

        Returns:
            TriggerExecuteResponse with message and trigger_id.

        Raises:
            Exception: When trigger has no id or execute API returns invalid response.

        Examples:
            >>> trigger = await mosaia.triggers.get({}, trigger_id)
            >>> result = await trigger.execute()
            >>> print(result.message)  # 'Trigger execution initiated'
        """
        if not self.has_id():
            raise Exception("Trigger ID is required to execute")
        path = f"{self.get_uri()}/execute"
        response = await self.api_client.post(path, {})
        if not response:
            raise Exception("Invalid response from execute API")
        data = response.get("data", response)
        if not data:
            raise Exception("Invalid response from execute API")
        trigger_id = data.get("triggerId") or data.get("trigger_id")
        return TriggerExecuteResponse(
            message=data.get("message", ""),
            trigger_id=trigger_id,
        )
