"""
Agent Groups API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, AgentGroupInterface

class AgentGroups:
    """
    Agent Groups API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Agent Groups API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all agent groups with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of agent groups
        """
        return self.client.GET('/agent-groups', params)
    
    def get_by_id(self, group_id: str) -> APIResponse:
        """
        Get agent group by ID.
        
        Args:
            group_id (str): Agent group ID
            
        Returns:
            APIResponse: Agent group information
        """
        return self.client.GET(f'/agent-groups/{group_id}')
    
    def create(self, group_data: Union[Dict[str, Any], AgentGroupInterface]) -> APIResponse:
        """
        Create a new agent group.
        
        Args:
            group_data (Union[Dict[str, Any], AgentGroupInterface]): Agent group data
            
        Returns:
            APIResponse: Created agent group
        """
        if isinstance(group_data, AgentGroupInterface):
            group_data = group_data.dict(exclude_none=True)
        return self.client.POST('/agent-groups', group_data)
    
    def update(self, group_id: str, group_data: Union[Dict[str, Any], AgentGroupInterface]) -> APIResponse:
        """
        Update an agent group.
        
        Args:
            group_id (str): Agent group ID
            group_data (Union[Dict[str, Any], AgentGroupInterface]): Updated agent group data
            
        Returns:
            APIResponse: Updated agent group
        """
        if isinstance(group_data, AgentGroupInterface):
            group_data = group_data.dict(exclude_none=True)
        return self.client.PUT(f'/agent-groups/{group_id}', group_data)
    
    def delete(self, group_id: str) -> APIResponse:
        """
        Delete an agent group.
        
        Args:
            group_id (str): Agent group ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/agent-groups/{group_id}')
    
    def chat_completion(self, completion_data: Dict[str, Any]) -> APIResponse:
        """
        Perform chat completion with an agent group.
        
        Args:
            completion_data (Dict[str, Any]): Chat completion data
            
        Returns:
            APIResponse: Chat completion response
        """
        return self.client.POST('/chat/completions', completion_data) 