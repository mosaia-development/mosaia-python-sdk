from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class RecordHistory(BaseModel):
    created_at: Optional[datetime] = Field(None, description="Created at")
    created_by: Optional[str] = Field(None, description="Created by")
    created_by_type: Optional[str] = Field(None, description="Created by type")
    updated_at: Optional[datetime] = Field(None, description="Updated at")
    updated_by: Optional[str] = Field(None, description="Updated by")
    updated_by_type: Optional[str] = Field(None, description="Updated by type")