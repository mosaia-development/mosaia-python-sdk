from .base_entity import BaseEntity
from typing import (
    Dict,
    Annotated,
    Optional
)
from pydantic import (
    Field,
    BeforeValidator
)
from .utils import (
    validate_identifier_name,
    validate_email,
    validate_url
)

class User(BaseEntity):
    username: Optional[Annotated[str, BeforeValidator(validate_identifier_name, 'username')]] = Field(None, description="Username of the user")
    name: Optional[str] = Field(None, description="Name of the user")
    image: Optional[Annotated[str, BeforeValidator(validate_url, 'image')]] = Field(None, description="Image of the user")
    description: Optional[str] = Field(None, description="Description of the user")
    email: Optional[Annotated[str, BeforeValidator(validate_email, 'email')]] = Field(None, description="Email of the user")
    url: Optional[Annotated[str, BeforeValidator(validate_url, 'url')]] = Field(None, description="URL of the user")
    location: Optional[str] = Field(None, description="Location of the user")
    links: Dict = Field(default_factory=dict, description="Links of the user")

    @property
    def agents(self):
        from ..requests import AgentRequest
        return AgentRequest(f"{self._core_url}/{self.id}", self._api_key)
    
    @property
    def agent_groups(self):
        from ..requests import AgentGroupRequest
        return AgentGroupRequest(f"{self._core_url}/{self.id}", self._api_key)