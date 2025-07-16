"""
Tool entity model
"""

from typing import Optional, List, Dict, Any
from pydantic import Field
from .base_entity import BaseEntity

class Tool(BaseEntity):
    """Tool entity"""
    
    org: Optional[str] = Field(None, description="Organization ID")
    user: Optional[str] = Field(None, description="User ID")
    name: Optional[str] = Field(None, description="Name of the tool")
    friendly_name: Optional[str] = Field(None, description="Friendly name of the tool")
    short_description: str = Field(..., description="Short description of the tool")
    tool_schema: str = Field(..., description="Tool schema")
    required_environment_variables: Optional[List[str]] = Field(None, description="Required environment variables")
    source_url: Optional[str] = Field(None, description="Source URL")
    url: Optional[str] = Field(None, description="URL")
    public: Optional[bool] = Field(None, description="Whether the tool is public")
    
    def __init__(self, api_client, data: Dict[str, Any], **kwargs):
        super().__init__(**data)
        self._api_client = api_client
    
    def update(self, **kwargs) -> 'Tool':
        """
        Update the tool
        
        Args:
            **kwargs: Fields to update
            
        Returns:
            Tool: Updated tool instance
        """
        if not self.id:
            raise ValueError("Cannot update tool without ID")
        
        update_data = {**self.dict(), **kwargs}
        response = self._api_client.PUT(f"/{self.id}", update_data)
        return Tool(self._api_client, response.data)
    
    def delete(self) -> None:
        """
        Delete the tool
        
        Raises:
            ValueError: If tool has no ID
        """
        if not self.id:
            raise ValueError("Cannot delete tool without ID")
        
        self._api_client.DELETE(f"/{self.id}") 