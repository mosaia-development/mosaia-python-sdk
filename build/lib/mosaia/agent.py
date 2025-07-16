from typing import Dict
from .core_requester import make_request

class Agent:
    def __init__(self, uri: str, api_key: str):
        self.uri = uri
        self.api_key = api_key

    def get(self, params: Dict[str, str] = None, id: str = None):
        url = f"{self.uri}/agent"

        if id is not None:
            url = f"{url}/{id}"

        results = make_request(url, method="GET", params=params, api_key=self.api_key)
        return results['data']
    
    def create(self, data = None, params: Dict[str, str] = None):
        if data is None:
            raise ValueError("data is required")

        results = make_request(f"{self.uri}/agent", method="POST", params=params, data=data,api_key=self.api_key)
        return results['data']
    
    def update(self, params: Dict[str, str] = None, id: str = None, data = None):
        if id is None:
            raise ValueError("id is required")
        
        if data is None:
            raise ValueError("data is required")

        results = make_request(f"{self.uri}/agent/{id}", method="PUT", params=params, data=data, api_key=self.api_key)
        return results['data']
    
    def delete(self, id: str = None):
        if id is None:
            raise ValueError("id is required")

        return make_request(f"{self.uri}/agent/{id}", method="DELETE", api_key=self.api_key)
    
    # @property
    # def chat(self):
    #     return Agent(self.core_url, self.api_key)