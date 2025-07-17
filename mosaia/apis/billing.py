"""
Billing API for the Mosaia SDK
"""

from typing import Dict, Any, Optional, Union
from mosaia.api_client import APIClient
from mosaia.types import MosiaConfig, APIResponse, ErrorResponse, WalletInterface, MeterInterface

class Billing:
    """
    Billing API client for the Mosaia SDK.
    """
    
    def __init__(self, config: MosiaConfig):
        """
        Initialize the Billing API client.
        
        Args:
            config (MosiaConfig): Configuration object
        """
        self.config = config
        self.client = APIClient(config)
    
    # Wallet operations
    def get_wallets(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all wallets with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of wallets
        """
        return self.client.GET('/billing/wallets', params)
    
    def get_wallet(self, wallet_id: str) -> APIResponse:
        """
        Get wallet by ID.
        
        Args:
            wallet_id (str): Wallet ID
            
        Returns:
            APIResponse: Wallet information
        """
        return self.client.GET(f'/billing/wallets/{wallet_id}')
    
    def create_wallet(self, wallet_data: Union[Dict[str, Any], WalletInterface]) -> APIResponse:
        """
        Create a new wallet.
        
        Args:
            wallet_data (Union[Dict[str, Any], WalletInterface]): Wallet data
            
        Returns:
            APIResponse: Created wallet
        """
        if isinstance(wallet_data, WalletInterface):
            wallet_data = wallet_data.dict(exclude_none=True)
        return self.client.POST('/billing/wallets', wallet_data)
    
    def update_wallet(self, wallet_id: str, wallet_data: Union[Dict[str, Any], WalletInterface]) -> APIResponse:
        """
        Update a wallet.
        
        Args:
            wallet_id (str): Wallet ID
            wallet_data (Union[Dict[str, Any], WalletInterface]): Updated wallet data
            
        Returns:
            APIResponse: Updated wallet
        """
        if isinstance(wallet_data, WalletInterface):
            wallet_data = wallet_data.dict(exclude_none=True)
        return self.client.PUT(f'/billing/wallets/{wallet_id}', wallet_data)
    
    def delete_wallet(self, wallet_id: str) -> APIResponse:
        """
        Delete a wallet.
        
        Args:
            wallet_id (str): Wallet ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/billing/wallets/{wallet_id}')
    
    # Meter operations
    def get_meters(self, params: Optional[Dict[str, Any]] = None) -> APIResponse:
        """
        Get all meters with optional filtering.
        
        Args:
            params (Dict[str, Any], optional): Query parameters
            
        Returns:
            APIResponse: List of meters
        """
        return self.client.GET('/billing/meters', params)
    
    def get_meter(self, meter_id: str) -> APIResponse:
        """
        Get meter by ID.
        
        Args:
            meter_id (str): Meter ID
            
        Returns:
            APIResponse: Meter information
        """
        return self.client.GET(f'/billing/meters/{meter_id}')
    
    def create_meter(self, meter_data: Union[Dict[str, Any], MeterInterface]) -> APIResponse:
        """
        Create a new meter.
        
        Args:
            meter_data (Union[Dict[str, Any], MeterInterface]): Meter data
            
        Returns:
            APIResponse: Created meter
        """
        if isinstance(meter_data, MeterInterface):
            meter_data = meter_data.dict(exclude_none=True)
        return self.client.POST('/billing/meters', meter_data)
    
    def update_meter(self, meter_id: str, meter_data: Union[Dict[str, Any], MeterInterface]) -> APIResponse:
        """
        Update a meter.
        
        Args:
            meter_id (str): Meter ID
            meter_data (Union[Dict[str, Any], MeterInterface]): Updated meter data
            
        Returns:
            APIResponse: Updated meter
        """
        if isinstance(meter_data, MeterInterface):
            meter_data = meter_data.dict(exclude_none=True)
        return self.client.PUT(f'/billing/meters/{meter_id}', meter_data)
    
    def delete_meter(self, meter_id: str) -> APIResponse:
        """
        Delete a meter.
        
        Args:
            meter_id (str): Meter ID
            
        Returns:
            APIResponse: Deletion response
        """
        return self.client.DELETE(f'/billing/meters/{meter_id}') 