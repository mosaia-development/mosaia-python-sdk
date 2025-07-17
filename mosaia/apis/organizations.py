"""
Organizations API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, OrganizationInterface

class Organizations:
    """
    Organizations API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Organizations API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    def get_all(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all organizations with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of organizations
        """
        return self.client.GET('/orgs', params)
    
    def get_by_id(self, org_id: str) -> APIResponse:
        """
        Get organization by ID.
        
        Args:
            org_id (str): Organization ID
            
        Returns:
            APIResponse: Organization information
        """
        return self.client.GET(f'/orgs/{org_id}')
    
    def create(self, org_data: Union[Dict[str, Any], OrganizationInterface]) -> APIResponse:
        """
        Create a new organization.
        
        Args:
            org_data (Union[Dict[str, Any], OrganizationInterface]): Organization data
            
        Returns:
            APIResponse: Created organization
        """
        if isinstance(org_data, OrganizationInterface):
            org_data = org_data.dict(exclude_none=True)
        return self.client.POST('/orgs', org_data)
    
    def update(self, org_id: str, org_data: Union[Dict[str, Any], OrganizationInterface]) -> APIResponse:
        """
        Update an organization.
        
        Args:
            org_id (str): Organization ID
            org_data (Union[Dict[str, Any], OrganizationInterface]): Updated organization data
            
        Returns:
            APIResponse: Updated organization
        """
        if isinstance(org_data, OrganizationInterface):
            org_data = org_data.dict(exclude_none=True)
        return self.client.PUT(f'/orgs/{org_id}', org_data)
    
    def delete(self, org_id: str) -> APIResponse:
        """
        Delete an organization.
        
        Args:
            org_id (str): Organization ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/orgs/{org_id}') 