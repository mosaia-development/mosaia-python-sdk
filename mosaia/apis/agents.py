"""
Agents API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, AgentInterface

class Agents:
    """
    Agents API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Agents API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all agents with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of agents
        """
        return self.client.GET('/agents', params)
    
    def get_by_id(self, agent_id: str) -> APIResponse:
        """
        Get agent by ID.
        
        Args:
            agent_id (str): Agent ID
            
        Returns:
            APIResponse: Agent information
        """
        return self.client.GET(f'/agents/{agent_id}')
    
    def create(self, agent_data: Union[Dict[str, Any], AgentInterface]) -> APIResponse:
        """
        Create a new agent.
        
        Args:
            agent_data (Union[Dict[str, Any], AgentInterface]): Agent data
            
        Returns:
            APIResponse: Created agent
        """
        if isinstance(agent_data, AgentInterface):
            agent_data = agent_data.dict(exclude_none=True)
        return self.client.POST('/agents', agent_data)
    
    def update(self, agent_id: str, agent_data: Union[Dict[str, Any], AgentInterface]) -> APIResponse:
        """
        Update an agent.
        
        Args:
            agent_id (str): Agent ID
            agent_data (Union[Dict[str, Any], AgentInterface]): Updated agent data
            
        Returns:
            APIResponse: Updated agent
        """
        if isinstance(agent_data, AgentInterface):
            agent_data = agent_data.dict(exclude_none=True)
        return self.client.PUT(f'/agents/{agent_id}', agent_data)
    
    def delete(self, agent_id: str) -> APIResponse:
        """
        Delete an agent.
        
        Args:
            agent_id (str): Agent ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/agents/{agent_id}')
    
    def chat_completion(self, completion_data: Dict[str, Any]) -> APIResponse:
        """
        Perform chat completion with an agent.
        
        Args:
            completion_data (Dict[str, Any]): Chat completion data
            
        Returns:
            APIResponse: Chat completion response
        """
        return self.client.POST('/chat/completions', completion_data)
    
    def async_chat_completion(self, completion_data: Dict[str, Any]) -> APIResponse:
        """
        Perform async chat completion with an agent.
        
        Args:
            completion_data (Dict[str, Any]): Async chat completion data
            
        Returns:
            APIResponse: Async chat completion response
        """
        return self.client.POST('/chat/completions/async', completion_data) 