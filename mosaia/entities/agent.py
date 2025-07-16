from __future__ import annotations
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator
from .base_entity import BaseEntity
from .user import User
from .org import Organization
from .model import Model
from datetime import datetime
from .utils import validate_identifier_name

class ForkedAgent(BaseModel):
    from_: Optional[Union[str, 'Agent']] = Field(None, description="The agent that was forked from")
    created_at: Optional[datetime] = Field(None, description="The date and time the agent was forked")

class Agent(BaseEntity):
    org: Optional[Union[str, Organization]] = Field(None, description="Reference to Organization")
    user: Optional[Union[str, User]] = Field(None, description="Reference to User")
    name: str = Field(description="Name of the agent")  # Required field
    image: Optional[str] = Field(None, description="Image of the agent")
    model: Optional[List[Union[str, Model]]] = Field(None, description="List of models used by the agent")
    description: Optional[str] = Field(None, description="Description of the agent")
    readme: Optional[str] = Field(None, description="Readme of the agent")
    system_message: Optional[str] = Field(None, description="System message of the agent")
    max_tokens: Optional[int] = Field(None, description="Max tokens of the agent")
    temperature: float = Field(
        default=0.7,
        ge=0,
        le=2,
        description="Temperature value between 0 and 2"
    )
    public: bool = Field(default=False, description="Whether the agent is public")
    active: bool = Field(default=True, description="Whether the agent is active")
    forked: Optional[Union[str, 'ForkedAgent']] = Field(None, description="The agent that was forked from")

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        return validate_identifier_name(v)

# Rebuild models to resolve forward references
Agent.model_rebuild()
ForkedAgent.model_rebuild()