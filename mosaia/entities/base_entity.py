from typing import (
    List,
    Optional,
    Dict,
    Any
)
from pydantic import (
    BaseModel, 
    Field,
    PrivateAttr
)
from .record_history import RecordHistory

class BaseEntity(BaseModel):
    _core_url: str = PrivateAttr(default=None)
    _api_key: str = PrivateAttr(default=None)

    id: Optional[str] = Field(None, description="Main entity identifier")
    active: bool = Field(default=True, description="Whether the entity is active")
    keywords: List[str] = Field(default_factory=list, description="Keywords of the entity")
    tags: List[str] = Field(default_factory=list, description="Tags of the entity")
    external_id: Optional[str] = Field(None, description="External ID of the entity")
    extensors: Optional[Dict[str, Any]] = Field(None, description="Extensors of the entity")
    record_history: Optional[RecordHistory] = Field(None, description="Record history of the entity")

    def __init__(self, core_url: str = None, api_key: str = None, **data):
        super().__init__(**data)
        self._core_url = core_url
        self._api_key = api_key