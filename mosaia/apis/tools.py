"""
Tools API for managing tools
"""

from typing import Optional, List, Union
from mosaia.types import MosiaConfig, ToolInterface
from mosaia.entities.tool import Tool
from mosaia.api_client import APIClient
from mosaia.config import DEFAULT_CONFIG

class Tools:
    """Tools API client"""
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Tools API client
        
        Args:
            config: Configuration object
        """
        if config.user:
            base_url = f"{config.base_url}/user/{config.user}{DEFAULT_CONFIG['ENDPOINTS']['TOOLS']}"
        elif config.org:
            base_url = f"{config.base_url}/org/{config.org}{DEFAULT_CONFIG['ENDPOINTS']['TOOLS']}"
        else:
            raise ValueError("User or org ID is required to call tools endpoint")
        
        self.config = config
        self.config.base_url = base_url
        self.client = APIClient(self.config)
    
    def get(self, tool: Optional[ToolInterface] = None) -> Union[List[Tool], Tool, None]:
        """
        Get tools or a specific tool
        
        Args:
            tool: Optional tool interface with ID to get specific tool
            
        Returns:
            Union[List[Tool], Tool, None]: List of tools, single tool, or None
        """
        uri = ''
        
        if tool and tool.id:
            uri += f"/{tool.id}"
        
        response = self.client.GET(uri)
        data = response.data
        
        if isinstance(data, list):
            return [Tool(self.client, tool_data) for tool_data in data]
        
        if data:
            return Tool(self.client, data)
        
        return None
    
    def get_by_name(self, name: str) -> Optional[Tool]:
        """
        Get a tool by name
        
        Args:
            name: Name of the tool to find
            
        Returns:
            Optional[Tool]: Tool instance or None if not found
        """
        uri = f"?name={name}"
        response = self.client.GET(uri)
        data = response.data
        
        if isinstance(data, list):
            if data:
                return Tool(self.client, data[0])
            else:
                return None
        
        if data:
            return Tool(self.client, data)
        
        return None
    
    def create(self, tool: ToolInterface) -> Tool:
        """
        Create a new tool
        
        Args:
            tool: Tool interface with tool data
            
        Returns:
            Tool: Created tool instance
        """
        response = self.client.POST('', tool.dict())
        return Tool(self.client, response.data)
    
    def update(self, tool: ToolInterface) -> Tool:
        """
        Update an existing tool
        
        Args:
            tool: Tool interface with tool data and ID
            
        Returns:
            Tool: Updated tool instance
        """
        if not tool.id:
            raise ValueError("Tool ID is required for update")
        
        response = self.client.PUT(f"/{tool.id}", tool.dict())
        return Tool(self.client, response.data)
    
    def delete(self, tool: ToolInterface) -> None:
        """
        Delete a tool
        
        Args:
            tool: Tool interface with ID
            
        Returns:
            None
        """
        if not tool.id:
            raise ValueError("Tool ID is required for delete")
        
        self.client.DELETE(f"/{tool.id}") 