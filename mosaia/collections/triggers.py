"""
Triggers API client for the Mosaia SDK.

Provides CRUD operations for triggers (CRON, WEBHOOK, EVENT, MANUAL).
Can be used top-level (mosaia.triggers) or scoped to a task or plan (e.g. task.triggers).
"""

from typing import Any, Dict

from ..models.trigger import Trigger
from .base_collection import BaseCollection


class Triggers(BaseCollection[Dict[str, Any], Trigger, Any, Any]):
    """
    Triggers API client for the Mosaia SDK.

    Provides CRUD operations for triggers (CRON, WEBHOOK, EVENT, MANUAL).
    """

    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/trigger", Trigger)
