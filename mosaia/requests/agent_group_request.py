from typing import Dict
from .core_requester import core_request
from ..entities import AgentGroup

class AgentGroupRequest:
    def __init__(self, core_url: str, api_key: str):
        self.core_url = core_url
        self.api_key = api_key

    def get(self, params: Dict[str, str] = None, id: str = None):
        url = f"{self.core_url}/group"

        if id is not None:
            url = f"{url}/{id}"

        results = core_request(url, method="GET", params=params, api_key=self.api_key)
        data = results['data']
        
        # Handle array of agent_groups
        if isinstance(data, list):
            return [AgentGroup(**agent_group_data, core_url=self.core_url, api_key=self.api_key) for agent_group_data in data]
        # Handle single agent_group
        return AgentGroup(**data, core_url=self.core_url, api_key=self.api_key)
    
    def create(self, data = None, params: Dict[str, str] = None):
        if data is None:
            raise ValueError("data is required")

        results = core_request(f"{self.core_url}/group", method="POST", params=params, data=data,api_key=self.api_key)
        return AgentGroup(**results['data'], core_url=self.core_url, api_key=self.api_key)
    
    def update(self, params: Dict[str, str] = None, id: str = None, data = None):
        if id is None:
            raise ValueError("id is required")
        
        if data is None:
            raise ValueError("data is required")

        results = core_request(f"{self.core_url}/group/{id}", method="PUT", params=params, data=data, api_key=self.api_key)
        return AgentGroup(**results['data'], core_url=self.core_url, api_key=self.api_key)
    
    def delete(self, id: str = None):
        if id is None:
            raise ValueError("id is required")

        return core_request(f"{self.core_url}/group/{id}", method="DELETE", api_key=self.api_key)