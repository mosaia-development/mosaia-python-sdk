"""Tasks collection (Node parity: collections/tasks.ts)."""

from typing import Any, Dict

from ..models.task import Task
from .base_collection import BaseCollection


class Tasks(BaseCollection[Dict[str, Any], Task, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/task", Task)
