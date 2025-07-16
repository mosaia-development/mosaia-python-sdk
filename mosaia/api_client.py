"""
API Client for making HTTP requests to the Mosaia API
"""

import requests
from typing import Optional, Dict, Any, Union
from mosaia.config import DEFAULT_CONFIG
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse
from mosaia.utils import create_error_response

class APIClient:
    """HTTP client for making API requests"""
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the API client
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            'Content-Type': DEFAULT_CONFIG['API']['CONTENT_TYPE'],
        })
        
        # Set authorization header if API key is provided
        if config.api_key:
            self.session.headers.update({
                'Authorization': f"{DEFAULT_CONFIG['AUTH']['TOKEN_PREFIX']} {config.api_key}"
            })
    
    def _handle_error(self, response: requests.Response) -> ErrorResponse:
        """
        Handle HTTP errors and create standardized error responses
        
        Args:
            response: The HTTP response
            
        Returns:
            ErrorResponse: Standardized error response
        """
        try:
            error_data = response.json()
            message = error_data.get('message', DEFAULT_CONFIG['ERRORS']['UNKNOWN_ERROR'])
            code = error_data.get('code', 'UNKNOWN_ERROR')
        except (ValueError, KeyError):
            message = response.text or DEFAULT_CONFIG['ERRORS']['UNKNOWN_ERROR']
            code = 'UNKNOWN_ERROR'
        
        return create_error_response(
            message=message,
            code=code,
            status=response.status_code
        )
    
    def _make_request(
        self, 
        method: str, 
        path: str, 
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> APIResponse:
        """
        Make an HTTP request
        
        Args:
            method: HTTP method
            path: API path
            params: Query parameters
            data: Request body
            
        Returns:
            APIResponse: The API response
            
        Raises:
            ErrorResponse: If the request fails
        """
        url = f"{self.config.base_url}{path}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data
            )
            
            if not response.ok:
                error = self._handle_error(response)
                raise error
            
            return APIResponse(
                data=response.json(),
                status=response.status_code
            )
            
        except requests.exceptions.RequestException as e:
            error = create_error_response(
                message=str(e),
                code='NETWORK_ERROR',
                status=DEFAULT_CONFIG['ERRORS']['DEFAULT_STATUS_CODE']
            )
            raise error
    
    def GET(self, path: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a GET request
        
        Args:
            path: API path
            params: Query parameters
            
        Returns:
            APIResponse: The API response
        """
        return self._make_request('GET', path, params=params)
    
    def POST(self, path: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a POST request
        
        Args:
            path: API path
            data: Request body
            
        Returns:
            APIResponse: The API response
        """
        return self._make_request('POST', path, data=data)
    
    def PUT(self, path: str, data: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a PUT request
        
        Args:
            path: API path
            data: Request body
            
        Returns:
            APIResponse: The API response
        """
        return self._make_request('PUT', path, data=data)
    
    def DELETE(self, path: str, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Make a DELETE request
        
        Args:
            path: API path
            params: Query parameters
            
        Returns:
            APIResponse: The API response
        """
        return self._make_request('DELETE', path, params=params) 