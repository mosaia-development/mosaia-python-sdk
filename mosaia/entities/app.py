"""
App entity model
"""

from typing import Optional, List, Dict, Any
from pydantic import Field
from .base_entity import BaseEntity

class App(BaseEntity):
    """App entity"""
    
    name: str = Field(..., description="Name of the app")
    org: Optional[str] = Field(None, description="Organization ID")
    user: Optional[str] = Field(None, description="User ID")
    short_description: str = Field(..., description="Short description of the app")
    long_description: Optional[str] = Field(None, description="Long description of the app")
    image: Optional[str] = Field(None, description="Image URL of the app")
    external_app_url: Optional[str] = Field(None, description="External app URL")
    external_api_key: Optional[str] = Field(None, description="External API key")
    external_headers: Optional[Dict[str, str]] = Field(None, description="External headers")
    
    def __init__(self, api_client, data: Dict[str, Any], **kwargs):
        super().__init__(**data)
        self._api_client = api_client
    
    def update(self, **kwargs) -> 'App':
        """
        Update the app
        
        Args:
            **kwargs: Fields to update
            
        Returns:
            App: Updated app instance
        """
        if not self.id:
            raise ValueError("Cannot update app without ID")
        
        update_data = {**self.dict(), **kwargs}
        response = self._api_client.PUT(f"/{self.id}", update_data)
        return App(self._api_client, response.data)
    
    def delete(self) -> None:
        """
        Delete the app
        
        Raises:
            ValueError: If app has no ID
        """
        if not self.id:
            raise ValueError("Cannot delete app without ID")
        
        self._api_client.DELETE(f"/{self.id}") 