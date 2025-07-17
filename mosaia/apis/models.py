"""
Models API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, ModelInterface

class Models:
    """
    Models API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Models API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all models with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of models
        """
        return self.client.GET('/models', params)
    
    def get_by_id(self, model_id: str) -> APIResponse:
        """
        Get model by ID.
        
        Args:
            model_id (str): Model ID
            
        Returns:
            APIResponse: Model information
        """
        return self.client.GET(f'/models/{model_id}')
    
    def create(self, model_data: Union[Dict[str, Any], ModelInterface]) -> APIResponse:
        """
        Create a new model.
        
        Args:
            model_data (Union[Dict[str, Any], ModelInterface]): Model data
            
        Returns:
            APIResponse: Created model
        """
        if isinstance(model_data, ModelInterface):
            model_data = model_data.dict(exclude_none=True)
        return self.client.POST('/models', model_data)
    
    def update(self, model_id: str, model_data: Union[Dict[str, Any], ModelInterface]) -> APIResponse:
        """
        Update a model.
        
        Args:
            model_id (str): Model ID
            model_data (Union[Dict[str, Any], ModelInterface]): Updated model data
            
        Returns:
            APIResponse: Updated model
        """
        if isinstance(model_data, ModelInterface):
            model_data = model_data.dict(exclude_none=True)
        return self.client.PUT(f'/models/{model_id}', model_data)
    
    def delete(self, model_id: str) -> APIResponse:
        """
        Delete a model.
        
        Args:
            model_id (str): Model ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/models/{model_id}')
    
    def chat_completion(self, completion_data: Dict[str, Any]) -> APIResponse:
        """
        Perform chat completion with a model.
        
        Args:
            completion_data (Dict[str, Any]): Chat completion data
            
        Returns:
            APIResponse: Chat completion response
        """
        return self.client.POST('/chat/completions', completion_data) 