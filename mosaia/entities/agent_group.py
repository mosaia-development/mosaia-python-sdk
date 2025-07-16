from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel, Field, field_validator
from enum import Enum
from .base_entity import BaseEntity
from .user import User
from .org import Organization
from .model import Model
from .record_history import RecordHistory
from .utils import validate_identifier_name

class AgentGroupStatus(str, Enum):
    PENDING = "PENDING"
    BUILDING = "BUILDING"
    READY = "READY"
    ERROR = "ERROR"

class DefaultLLMConfig(BaseModel):
    temperature: float = 0
    cache_seed: Optional[Any] = None

class CodeExecutionConfig(BaseModel):
    last_n_messages: int = 1
    work_dir: str = "groupchat"
    use_docker: bool = False
    timeout: int = 10

class AgentGroup(BaseEntity):
    org: Optional[Union[str, Organization]] = Field(None, description="Reference to Organization")
    user: Optional[Union[str, User]] = Field(None, description="Reference to User")
    name: Optional[str] = Field(None, description="Name of the agent group")
    description: Optional[str] = Field(None, description="Description of the agent group")
    image: Optional[str] = Field(None, description="Image of the agent group")
    readme: Optional[str] = Field(None, description="Readme of the agent group")
    building_task: Optional[str] = Field(None, description="Building task of the agent group")
    builder_model: List[Union[str, Model]] = Field(default_factory=list, description="List of builder models")
    agent_model: List[Union[str, Model]] = Field(default_factory=list, description="List of agent models")
    coding: bool = Field(default=False, description="Whether the agent group is coding")
    default_llm_config: DefaultLLMConfig = Field(default_factory=DefaultLLMConfig, description="Default LLM config")
    code_execution_config: CodeExecutionConfig = Field(default_factory=CodeExecutionConfig, description="Code execution config")
    status: AgentGroupStatus = Field(default=AgentGroupStatus.PENDING, description="Status of the agent group")
    public: bool = Field(default=False, description="Whether the agent group is public")
    active: bool = Field(default=True, description="Whether the agent group is active")
    keywords: List[str] = Field(default_factory=list, description="Keywords of the agent group")
    tags: List[str] = Field(default_factory=list, description="Tags of the agent group")
    external_id: Optional[str] = Field(None, index=True, description="External ID of the agent group")
    extensors: Optional[Dict[str, Any]] = None
    record_history: Optional[RecordHistory] = None

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        if v is not None:
            return validate_identifier_name(v)
        return v