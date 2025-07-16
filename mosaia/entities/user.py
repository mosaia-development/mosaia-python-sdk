from .base_entity import BaseEntity
from typing import (
    Dict,
    Optional
)
from pydantic import (
    Field,
    field_validator
)
from .utils import (
    validate_identifier_name,
    validate_email,
    validate_url
)

class User(BaseEntity):
    username: Optional[str] = Field(None, description="Username of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    image: Optional[str] = Field(None, description="Image of the user")
    description: Optional[str] = Field(None, description="Description of the user")
    email: Optional[str] = Field(None, description="Email of the user")
    url: Optional[str] = Field(None, description="URL of the user")
    location: Optional[str] = Field(None, description="Location of the user")
    links: Dict = Field(default_factory=dict, description="Links of the user")

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if v is not None:
            return validate_identifier_name(v)
        return v

    @field_validator('image')
    @classmethod
    def validate_image(cls, v):
        if v is not None:
            return validate_url(v, 'image')
        return v

    @field_validator('email')
    @classmethod
    def validate_email_field(cls, v):
        if v is not None:
            return validate_email(v, 'email')
        return v

    @field_validator('url')
    @classmethod
    def validate_url_field(cls, v):
        if v is not None:
            return validate_url(v, 'url')
        return v

    @property
    def agents(self):
        from ..requests import AgentRequest
        return AgentRequest(f"{self._core_url}/{self.id}", self._api_key)
    
    @property
    def agent_groups(self):
        from ..requests import AgentGroupRequest
        return AgentGroupRequest(f"{self._core_url}/{self.id}", self._api_key)