from typing import (
    Optional,
    Literal,
    Union
)
from pydantic import Field
from .base_entity import BaseEntity
from .org import Organization
from .user import User

class Model(BaseEntity):
    org: Optional[Union[str, Organization]] = Field(None, description="Reference to Organization")
    user: Optional[Union[str, User]] = Field(None, description="Reference to User")
    name: Optional[str] = Field(None, description="Name of the model")
    model: Optional[str] = Field(None, description="Model of the model")
    image: Optional[str] = Field(None, description="Image of the model")
    description: Optional[str] = Field(None, description="Description of the model")
    readme: Optional[str] = Field(None, description="Readme of the model")
    type: Optional[Literal[
        "chat",
        "image",
        "rerank",
        "moderation",
        "language",
        "embedding"
    ]] = Field(default="chat", description="Type of the model")
    input_usd_price_per_1k_tokens: Optional[float] = Field(None, description="Input USD price per 1k tokens of the model")
    output_usd_price_per_1k_tokens: Optional[float] = Field(None, description="Output USD price per 1k tokens of the model")
    public: bool = Field(default=False, description="Whether the model is public")