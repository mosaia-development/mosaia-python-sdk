"""
Users API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, UserInterface

class Users:
    """
    Users API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Users API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all users with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of users
        """
        return self.client.GET('/users', params)
    
    def get_by_id(self, user_id: str) -> APIResponse:
        """
        Get user by ID.
        
        Args:
            user_id (str): User ID
            
        Returns:
            APIResponse: User information
        """
        return self.client.GET(f'/users/{user_id}')
    
    def create(self, user_data: Union[Dict[str, Any], UserInterface]) -> APIResponse:
        """
        Create a new user.
        
        Args:
            user_data (Union[Dict[str, Any], UserInterface]): User data
            
        Returns:
            APIResponse: Created user
        """
        if isinstance(user_data, UserInterface):
            user_data = user_data.dict(exclude_none=True)
        return self.client.POST('/users', user_data)
    
    def update(self, user_id: str, user_data: Union[Dict[str, Any], UserInterface]) -> APIResponse:
        """
        Update a user.
        
        Args:
            user_id (str): User ID
            user_data (Union[Dict[str, Any], UserInterface]): Updated user data
            
        Returns:
            APIResponse: Updated user
        """
        if isinstance(user_data, UserInterface):
            user_data = user_data.dict(exclude_none=True)
        return self.client.PUT(f'/users/{user_id}', user_data)
    
    def delete(self, user_id: str) -> APIResponse:
        """
        Delete a user.
        
        Args:
            user_id (str): User ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/users/{user_id}')
    
    def get_session(self, user_id: str) -> APIResponse:
        """
        Get user session information.
        
        Args:
            user_id (str): User ID
            
        Returns:
            APIResponse: Session information
        """
        return self.client.GET(f'/users/{user_id}/session') 