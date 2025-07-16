from .base_entity import BaseEntity
from typing import (
    Dict,
    Optional,
    Literal
)
from pydantic import Field, field_validator
from .utils import (
    validate_identifier_name,
    validate_url
)

class Organization(BaseEntity):
    name: Optional[str] = Field(None, description="Name of the organization")
    image: Optional[str] = Field(None, description="Image of the organization")
    description: Optional[str] = Field(None, description="Description of the organization")
    type: Optional[Literal['SUPERORG', 'VENDOR', 'CLIENT', 'ECOSYSTEM', 'MARKETPLACE']] = Field(default='CLIENT', description="Type of the organization")
    url: Optional[str] = Field(None, description="URL of the organization")
    size: Optional[str] = Field(None, description="Size of the organization")
    location: Optional[str] = Field(None, description="Location of the organization")
    mosaia_recommendation: Optional[str] = Field(None, description="Mosaia recommendation of the organization")
    links: Dict = Field(default_factory=dict, description="Links of the organization")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if v is not None:
            return validate_identifier_name(v)
        return v

    @field_validator('url')
    @classmethod
    def validate_url_field(cls, v):
        if v is not None:
            return validate_url(v)
        return v

    @property
    def agents(self):
        from ..requests import AgentRequest
        return AgentRequest(f"{self._core_url}/{self.id}", self._api_key)
    
    @property
    def agent_groups(self):
        from ..requests import AgentGroupRequest
        return AgentGroupRequest(f"{self._core_url}/{self.id}", self._api_key)

# Alias for backward compatibility
Org = Organization