"""
Authentication API for the Mosaia SDK
"""

from typing import Dict, Any, Optional
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse

class Auth:
    """
    Authentication API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Auth API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def sign_in_with_password(self, email: str, password: str, client_id: str) -> APIResponse:
        """
        Sign in with email and password.
        
        Args:
            email (str): User email
            password (str): User password
            client_id (str): Client ID
            
        Returns:
            APIResponse: Authentication response
        """
        data = {
            'email': email,
            'password': password,
            'client_id': client_id,
            'grant_type': 'password'
        }
        return self.client.POST('/auth/signin', data)
    
    def sign_in_with_client(self, client_id: str, client_secret: str) -> APIResponse:
        """
        Sign in with client credentials.
        
        Args:
            client_id (str): Client ID
            client_secret (str): Client secret
            
        Returns:
            APIResponse: Authentication response
        """
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client'
        }
        return self.client.POST('/auth/signin', data)
    
    def refresh_token(self, refresh_token: str) -> APIResponse:
        """
        Refresh access token.
        
        Args:
            refresh_token (str): Refresh token
            
        Returns:
            APIResponse: Token refresh response
        """
        data = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        return self.client.POST('/auth/refresh', data)
    
    def sign_out(self) -> APIResponse:
        """
        Sign out the current user.
        
        Returns:
            APIResponse: Sign out response
        """
        return self.client.POST('/auth/signout')
    
    def get_session(self) -> APIResponse:
        """
        Get current session information.
        
        Returns:
            APIResponse: Session information
        """
        return self.client.GET('/auth/session')
    
    def get_self(self) -> APIResponse:
        """
        Get current user information.
        
        Returns:
            APIResponse: User information
        """
        return self.client.GET('/auth/self') 