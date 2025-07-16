"""
OAuth implementation for the Mosaia SDK
"""

import hashlib
import secrets
import urllib.parse
from typing import Dict, Any, Optional
from mosaia.types import OAuthConfig, OAuthTokenResponse, OAuthErrorResponse
from mosaia.config import DEFAULT_CONFIG

class OAuth:
    """OAuth client for handling OAuth2 Authorization Code flow with PKCE"""
    
    def __init__(self, config: OAuthConfig):
        """
        Initialize the OAuth client
        
        Args:
            config: OAuth configuration
        """
        self.config = config
    
    def _generate_pkce(self) -> Dict[str, str]:
        """
        Generate PKCE code verifier and code challenge
        
        Returns:
            Dict[str, str]: Object containing code_verifier and code_challenge
        """
        # Generate code verifier
        code_verifier = secrets.token_urlsafe(32)[:128]
        
        # Generate code challenge
        code_challenge = hashlib.sha256(code_verifier.encode()).digest()
        code_challenge = urllib.parse.quote_plus(
            code_challenge,
            safe=''
        ).rstrip('=')
        
        return {
            'code_verifier': code_verifier,
            'code_challenge': code_challenge
        }
    
    def get_authorization_url_and_code_verifier(self) -> Dict[str, str]:
        """
        Generate the authorization URL for the OAuth flow
        
        Returns:
            Dict[str, str]: Object containing the authorization URL and code verifier
        """
        pkce = self._generate_pkce()
        
        params = {
            'client_id': self.config.client_id,
            'redirect_uri': self.config.redirect_uri,
            'response_type': 'code',
            'code_challenge': pkce['code_challenge'],
            'code_challenge_method': 'S256',
        }
        
        if self.config.scopes:
            params['scope'] = ' '.join(self.config.scopes)
        
        if self.config.state:
            params['state'] = self.config.state
        
        query_string = urllib.parse.urlencode(params)
        url = f"{DEFAULT_CONFIG['FRONTEND']['URL']}/oauth?{query_string}"
        
        return {
            'url': url,
            'code_verifier': pkce['code_verifier']
        }
    
    async def exchange_code_for_token(self, code: str, code_verifier: str) -> OAuthTokenResponse:
        """
        Exchange the authorization code for an access token
        
        Args:
            code: The authorization code received from the redirect
            code_verifier: The code verifier that was used in the authorization request
            
        Returns:
            OAuthTokenResponse: The token response
            
        Raises:
            OAuthErrorResponse: If the token exchange fails
        """
        import aiohttp
        
        params = {
            'client_id': self.config.client_id,
            'redirect_uri': self.config.redirect_uri,
            'code': code,
            'code_verifier': code_verifier,
            'grant_type': 'authorization_code'
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{DEFAULT_CONFIG['API']['BASE_URL']}/auth/token",
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data=urllib.parse.urlencode(params)
                ) as response:
                    data = await response.json()
                    
                    if not response.ok:
                        raise OAuthErrorResponse(**data)
                    
                    return OAuthTokenResponse(**data)
                    
        except Exception as e:
            if isinstance(e, OAuthErrorResponse):
                raise e
            raise OAuthErrorResponse(
                error='network_error',
                error_description=str(e)
            )
    
    async def refresh_token(self, refresh_token: str) -> OAuthTokenResponse:
        """
        Refresh an access token using a refresh token
        
        Args:
            refresh_token: The refresh token
            
        Returns:
            OAuthTokenResponse: The new token response
            
        Raises:
            OAuthErrorResponse: If the refresh fails
        """
        import aiohttp
        
        params = {
            'client_id': self.config.client_id,
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{DEFAULT_CONFIG['API']['BASE_URL']}/oauth/token",
                    headers={'Content-Type': 'application/x-www-form-urlencoded'},
                    data=urllib.parse.urlencode(params)
                ) as response:
                    data = await response.json()
                    
                    if not response.ok:
                        raise OAuthErrorResponse(**data)
                    
                    return OAuthTokenResponse(**data)
                    
        except Exception as e:
            if isinstance(e, OAuthErrorResponse):
                raise e
            raise OAuthErrorResponse(
                error='network_error',
                error_description=str(e)
            ) 