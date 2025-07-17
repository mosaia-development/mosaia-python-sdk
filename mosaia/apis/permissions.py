"""
Permissions API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, AccessPolicyInterface, OrgPermissionInterface, UserPermissionInterface

class Permissions:
    """
    Permissions API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Permissions API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    # Access Policy operations
    def get_access_policies(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all access policies with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of access policies
        """
        return self.client.GET('/permissions/access-policies', params)
    
    def get_access_policy(self, policy_id: str) -> APIResponse:
        """
        Get access policy by ID.
        
        Args:
            policy_id (str): Policy ID
            
        Returns:
            APIResponse: Access policy information
        """
        return self.client.GET(f'/permissions/access-policies/{policy_id}')
    
    def create_access_policy(self, policy_data: Union[Dict[str, Any], AccessPolicyInterface]) -> APIResponse:
        """
        Create a new access policy.
        
        Args:
            policy_data (Union[Dict[str, Any], AccessPolicyInterface]): Policy data
            
        Returns:
            APIResponse: Created access policy
        """
        if isinstance(policy_data, AccessPolicyInterface):
            policy_data = policy_data.dict(exclude_none=True)
        return self.client.POST('/permissions/access-policies', policy_data)
    
    def update_access_policy(self, policy_id: str, policy_data: Union[Dict[str, Any], AccessPolicyInterface]) -> APIResponse:
        """
        Update an access policy.
        
        Args:
            policy_id (str): Policy ID
            policy_data (Union[Dict[str, Any], AccessPolicyInterface]): Updated policy data
            
        Returns:
            APIResponse: Updated access policy
        """
        if isinstance(policy_data, AccessPolicyInterface):
            policy_data = policy_data.dict(exclude_none=True)
        return self.client.PUT(f'/permissions/access-policies/{policy_id}', policy_data)
    
    def delete_access_policy(self, policy_id: str) -> APIResponse:
        """
        Delete an access policy.
        
        Args:
            policy_id (str): Policy ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/permissions/access-policies/{policy_id}')
    
    # Org Permission operations
    def get_org_permissions(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all org permissions with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of org permissions
        """
        return self.client.GET('/permissions/org-permissions', params)
    
    def get_org_permission(self, permission_id: str) -> APIResponse:
        """
        Get org permission by ID.
        
        Args:
            permission_id (str): Permission ID
            
        Returns:
            APIResponse: Org permission information
        """
        return self.client.GET(f'/permissions/org-permissions/{permission_id}')
    
    def create_org_permission(self, permission_data: Union[Dict[str, Any], OrgPermissionInterface]) -> APIResponse:
        """
        Create a new org permission.
        
        Args:
            permission_data (Union[Dict[str, Any], OrgPermissionInterface]): Permission data
            
        Returns:
            APIResponse: Created org permission
        """
        if isinstance(permission_data, OrgPermissionInterface):
            permission_data = permission_data.dict(exclude_none=True)
        return self.client.POST('/permissions/org-permissions', permission_data)
    
    def update_org_permission(self, permission_id: str, permission_data: Union[Dict[str, Any], OrgPermissionInterface]) -> APIResponse:
        """
        Update an org permission.
        
        Args:
            permission_id (str): Permission ID
            permission_data (Union[Dict[str, Any], OrgPermissionInterface]): Updated permission data
            
        Returns:
            APIResponse: Updated org permission
        """
        if isinstance(permission_data, OrgPermissionInterface):
            permission_data = permission_data.dict(exclude_none=True)
        return self.client.PUT(f'/permissions/org-permissions/{permission_id}', permission_data)
    
    def delete_org_permission(self, permission_id: str) -> APIResponse:
        """
        Delete an org permission.
        
        Args:
            permission_id (str): Permission ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/permissions/org-permissions/{permission_id}')
    
    # User Permission operations
    def get_user_permissions(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all user permissions with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of user permissions
        """
        return self.client.GET('/permissions/user-permissions', params)
    
    def get_user_permission(self, permission_id: str) -> APIResponse:
        """
        Get user permission by ID.
        
        Args:
            permission_id (str): Permission ID
            
        Returns:
            APIResponse: User permission information
        """
        return self.client.GET(f'/permissions/user-permissions/{permission_id}')
    
    def create_user_permission(self, permission_data: Union[Dict[str, Any], UserPermissionInterface]) -> APIResponse:
        """
        Create a new user permission.
        
        Args:
            permission_data (Union[Dict[str, Any], UserPermissionInterface]): Permission data
            
        Returns:
            APIResponse: Created user permission
        """
        if isinstance(permission_data, UserPermissionInterface):
            permission_data = permission_data.dict(exclude_none=True)
        return self.client.POST('/permissions/user-permissions', permission_data)
    
    def update_user_permission(self, permission_id: str, permission_data: Union[Dict[str, Any], UserPermissionInterface]) -> APIResponse:
        """
        Update a user permission.
        
        Args:
            permission_id (str): Permission ID
            permission_data (Union[Dict[str, Any], UserPermissionInterface]): Updated permission data
            
        Returns:
            APIResponse: Updated user permission
        """
        if isinstance(permission_data, UserPermissionInterface):
            permission_data = permission_data.dict(exclude_none=True)
        return self.client.PUT(f'/permissions/user-permissions/{permission_id}', permission_data)
    
    def delete_user_permission(self, permission_id: str) -> APIResponse:
        """
        Delete a user permission.
        
        Args:
            permission_id (str): Permission ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/permissions/user-permissions/{permission_id}') 