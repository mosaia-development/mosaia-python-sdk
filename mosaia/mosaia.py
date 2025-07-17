"""
Main Mosaia SDK client
"""

from typing import Dict, Optional
from mosaia.config import DEFAULT_CONFIG
from mosaia.types import MosiaConfig, OAuthConfig
from mosaia.apis import Apps, Tools, AppBots, Auth, Users, Organizations, Agents, AgentGroups, Models, Clients, Billing, Permissions
from mosaia.oauth import OAuth
from mosaia.utils import is_sdk_error

class Mosaia:
    """
    Main client class for the Mosaia SDK.
    """
    
    def __init__(self, config: Optional[MosiaConfig] = None):
        """
        Initialize the client with configuration settings.
        
        Args:
            config (MosiaConfig, optional): Configuration object
        """
        if config is None:
            config = MosiaConfig()
        
        # Set defaults
        base_url = config.base_url or DEFAULT_CONFIG['API']['BASE_URL']
        version = config.version or DEFAULT_CONFIG['API']['VERSION']
        frontend_url = config.frontend_url or DEFAULT_CONFIG['FRONTEND']['URL']
        
        # Construct full base URL
        full_base_url = f"{base_url}/v{version}"
        
        self.config = MosiaConfig(
            api_key=config.api_key,
            version=version,
            base_url=full_base_url,
            frontend_url=frontend_url,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user=config.user,
            org=config.org
        )
    
    def generate_api_key(self, client_id: str, client_secret: str) -> str:
        """
        Generate an API key using client credentials and sets it as the api_key attribute.

        Args:
            client_id (str): The client ID for API authentication
            client_secret (str): The client secret for API authentication

        Raises:
            requests.exceptions.HTTPError: If the API request fails
        """
        import requests
        
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            "grant_type": "client",
        }
        url = f"{self.config.base_url}/auth/signin"
        
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        results = response.json()
        self.config.api_key = results["data"].get('access_token')
        return self.config.api_key
    
    @property
    def apps(self) -> Apps:
        """Get the Apps API client"""
        return Apps(self.config)
    
    @property
    def tools(self) -> Tools:
        """Get the Tools API client"""
        return Tools(self.config)
    
    @property
    def api_key(self) -> Optional[str]:
        """Get the current API key"""
        return self.config.api_key
    
    @property
    def app_bots(self) -> AppBots:
        """Get the App Bots API client"""
        return AppBots(self.apps, None)
    
    @property
    def auth(self) -> Auth:
        """Get the Auth API client"""
        return Auth(self.config)
    
    @property
    def users(self) -> Users:
        """Get the Users API client"""
        return Users(self.config)
    
    @property
    def organizations(self) -> Organizations:
        """Get the Organizations API client"""
        return Organizations(self.config)
    
    @property
    def agents(self) -> Agents:
        """Get the Agents API client"""
        return Agents(self.config)
    
    @property
    def agent_groups(self) -> AgentGroups:
        """Get the Agent Groups API client"""
        return AgentGroups(self.config)
    
    @property
    def models(self) -> Models:
        """Get the Models API client"""
        return Models(self.config)
    
    @property
    def clients(self) -> Clients:
        """Get the Clients API client"""
        return Clients(self.config)
    
    @property
    def billing(self) -> Billing:
        """Get the Billing API client"""
        return Billing(self.config)
    
    @property
    def permissions(self) -> Permissions:
        """Get the Permissions API client"""
        return Permissions(self.config)
    
    def oauth(self, redirect_uri: str, scopes: Optional[list] = None) -> OAuth:
        """
        Creates a new OAuth instance for handling OAuth2 Authorization Code flow with PKCE
        
        Args:
            redirect_uri (str): The redirect URI for the OAuth flow
            scopes (list, optional): List of scopes to request
            
        Returns:
            OAuth: OAuth instance
            
        Raises:
            ValueError: If client ID is not configured
        """
        if not self.config.client_id:
            raise ValueError('Client ID is required to initialize OAuth')
        
        oauth_config = OAuthConfig(
            client_id=self.config.client_id,
            redirect_uri=redirect_uri,
            scopes=scopes
        )
        
        return OAuth(oauth_config)
    
    # Legacy properties for backward compatibility
    @property
    def orgs(self):
        """Legacy property - use organizations instead"""
        return self.organizations

    @property
    def users_legacy(self):
        """Legacy property - use users instead"""
        from mosaia.requests.user_request import UserRequest
        return UserRequest(self.config.base_url, self.config.api_key)

    @property
    def agents_legacy(self):
        """Legacy property - use agents instead"""
        from mosaia.requests.agent_request import AgentRequest
        return AgentRequest(self.config.base_url, self.config.api_key)

    @property
    def agent_groups_legacy(self):
        """Legacy property - use agent_groups instead"""
        from mosaia.requests.agent_group_request import AgentGroupRequest
        return AgentGroupRequest(self.config.base_url, self.config.api_key)
