"""
Apps API for managing applications
"""

from typing import Optional, List, Union
from mosaia.types import MosiaConfig, AppInterface
from mosaia.entities.app import App
from mosaia.api_client import APIClient
from mosaia.config import DEFAULT_CONFIG

class Apps:
    """Apps API client"""
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Apps API client
        
        Args:
            config: Configuration object
        """
        base_url = f"{config.base_url}{DEFAULT_CONFIG['ENDPOINTS']['APPS']}"
        
        self.config = config
        self.config.base_url = base_url
        self.client = APIClient(self.config)
    
    def get(self, app: Optional[AppInterface] = None) -> Union[List[App], App, None]:
        """
        Get apps or a specific app
        
        Args:
            app: Optional app interface with ID to get specific app
            
        Returns:
            Union[List[App], App, None]: List of apps, single app, or None
        """
        uri = ''
        
        if app and app.id:
            uri += f"/{app.id}"
        
        response = self.client.GET(uri)
        data = response.data
        
        if isinstance(data, list):
            return [App(self.client, app_data) for app_data in data]
        
        if data:
            return App(self.client, data)
        
        return None
    
    def create(self, app: AppInterface) -> App:
        """
        Create a new app
        
        Args:
            app: App interface with app data
            
        Returns:
            App: Created app instance
        """
        response = self.client.POST('', app.dict())
        return App(self.client, response.data)
    
    def update(self, app: AppInterface) -> App:
        """
        Update an existing app
        
        Args:
            app: App interface with app data and ID
            
        Returns:
            App: Updated app instance
        """
        if not app.id:
            raise ValueError("App ID is required for update")
        
        response = self.client.PUT(f"/{app.id}", app.dict())
        return App(self.client, response.data)
    
    def delete(self, app: AppInterface) -> None:
        """
        Delete an app
        
        Args:
            app: App interface with ID
            
        Returns:
            None
        """
        if not app.id:
            raise ValueError("App ID is required for delete")
        
        self.client.DELETE(f"/{app.id}") 