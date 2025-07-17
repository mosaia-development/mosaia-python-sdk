"""
Clients API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, ClientInterface

class Clients:
    """
    Clients API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Clients API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all clients with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of clients
        """
        return self.client.GET('/clients', params)
    
    def get_by_id(self, client_id: str) -> APIResponse:
        """
        Get client by ID.
        
        Args:
            client_id (str): Client ID
            
        Returns:
            APIResponse: Client information
        """
        return self.client.GET(f'/clients/{client_id}')
    
    def create(self, client_data: Union[Dict[str, Any], ClientInterface]) -> APIResponse:
        """
        Create a new client.
        
        Args:
            client_data (Union[Dict[str, Any], ClientInterface]): Client data
            
        Returns:
            APIResponse: Created client
        """
        if isinstance(client_data, ClientInterface):
            client_data = client_data.dict(exclude_none=True)
        return self.client.POST('/clients', client_data)
    
    def update(self, client_id: str, client_data: Union[Dict[str, Any], ClientInterface]) -> APIResponse:
        """
        Update a client.
        
        Args:
            client_id (str): Client ID
            client_data (Union[Dict[str, Any], ClientInterface]): Updated client data
            
        Returns:
            APIResponse: Updated client
        """
        if isinstance(client_data, ClientInterface):
            client_data = client_data.dict(exclude_none=True)
        return self.client.PUT(f'/clients/{client_id}', client_data)
    
    def delete(self, client_id: str) -> APIResponse:
        """
        Delete a client.
        
        Args:
            client_id (str): Client ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/clients/{client_id}') 