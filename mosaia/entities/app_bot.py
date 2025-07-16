"""
App Bot entity model
"""

from typing import Optional, List, Dict, Any, Union
from pydantic import Field
from .base_entity import BaseEntity
from .app import App

class AppBot(BaseEntity):
    """App Bot entity"""
    
    app: Union[str, App] = Field(..., description="App ID or App object")
    response_url: str = Field(..., description="Response URL")
    org: Optional[str] = Field(None, description="Organization ID")
    user: Optional[str] = Field(None, description="User ID")
    agent: Optional[str] = Field(None, description="Agent ID")
    agent_group: Optional[str] = Field(None, description="Agent group ID")
    api_key: Optional[str] = Field(None, description="API key")
    api_key_partial: Optional[str] = Field(None, description="Partial API key")
    
    def __init__(self, api_client, data: Dict[str, Any], **kwargs):
        super().__init__(**data)
        self._api_client = api_client
    
    def update(self, **kwargs) -> 'AppBot':
        """
        Update the app bot
        
        Args:
            **kwargs: Fields to update
            
        Returns:
            AppBot: Updated app bot instance
        """
        if not self.id:
            raise ValueError("Cannot update app bot without ID")
        
        update_data = {**self.dict(), **kwargs}
        response = self._api_client.PUT(f"/{self.id}", update_data)
        return AppBot(self._api_client, response.data)
    
    def delete(self) -> None:
        """
        Delete the app bot
        
        Raises:
            ValueError: If app bot has no ID
        """
        if not self.id:
            raise ValueError("Cannot delete app bot without ID")
        
        self._api_client.DELETE(f"/{self.id}") 