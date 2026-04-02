"""Upload job model (Node parity: models/upload-job.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class UploadJob(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/upload")
