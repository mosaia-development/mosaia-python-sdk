from typing import Dict
from .core_requester import make_request
from .agent import Agent

class Mosaia:
    """
    Main client class for the SDK.
    """
    def __init__(
        self,
        config: Dict[str, str] = None
    ):
        """
        Initialize the client with configuration settings.
        
        Args:
            config (Dict[str, str], optional): Configuration dictionary that may contain:
                - version: API version to use (defaults to "1")
                - base_url: Base URL for API requests (defaults to "https://api.mosaia.ai")
                - api_key: API key for authentication (defaults to None)
        """
        default_config = {
            "version": "1",
            "base_url": "https://api.mosaia.ai",
            "api_key": None
        }
        
        config = config or {}
        final_config = {**default_config, **config}
        
        self.version = final_config["version"]
        self.base_url = final_config["base_url"].rstrip('/')  # Remove trailing slash if present
        self.api_key = final_config["api_key"]

        self.core_url = f"{self.base_url}/v{self.version}"
        
    def generate_api_key(self, client_id: str, client_secret: str) -> str:
        """
        Generate an API key using client credentials and sets it as the api_key attribute.

        Args:
            client_id (str): The client ID for API authentication
            client_secret (str): The client secret for API authentication

        Raises:
            requests.exceptions.HTTPError: If the API request fails
        """
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            "grant_type": "client",
        }
        url = f"{self.core_url}/auth/signin"
        results = make_request(url, method="POST", data=data)        
        self.api_key = results["data"].get('access_token')
        return self.api_key
    
    @property
    def agent(self):
        return Agent(self.core_url, self.api_key)
