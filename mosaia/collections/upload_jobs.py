"""Upload jobs collection (Node parity: collections/upload-jobs.ts)."""

from typing import Any, Dict

from ..models.upload_job import UploadJob
from .base_collection import BaseCollection


class UploadJobs(BaseCollection[Dict[str, Any], UploadJob, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/upload", UploadJob)
