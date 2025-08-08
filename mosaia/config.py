"""
Configuration management for the Mosaia Python SDK.

This module provides configuration management functionality including
the ConfigurationManager singleton and default configuration values.
"""

import os
from typing import Any, Dict, Optional
from dataclasses import dataclass, field

from .types import MosaiaConfig, SessionInterface


# Default configuration values
DEFAULT_CONFIG = {
    'API': {
        'BASE_URL': 'https://api.mosaia.ai',
        'VERSION': '1',
        'CONTENT_TYPE': 'application/json'
    },
    'AUTH': {
        'TOKEN_PREFIX': 'Bearer'
    },
    'ERRORS': {
        'UNKNOWN_ERROR': 'An unknown error occurred',
        'DEFAULT_STATUS_CODE': 400
    }
}


class ConfigurationManager:
    """
    Singleton configuration manager for the Mosaia SDK.
    
    This class manages configuration settings for the SDK, including
    API keys, URLs, and other settings. It follows the singleton pattern
    to ensure consistent configuration across the application.
    
    Examples:
        Basic usage:
        >>> config_manager = ConfigurationManager.get_instance()
        >>> config_manager.initialize({
        ...     'api_key': 'your-api-key',
        ...     'api_url': 'https://api.mosaia.ai'
        ... })
        >>> config = config_manager.get_config()
        
        Using environment variables:
        >>> config_manager = ConfigurationManager.get_instance()
        >>> config_manager.initialize_from_env()
        >>> config = config_manager.get_config()
    """
    
    _instance: Optional['ConfigurationManager'] = None
    _config: Optional[MosaiaConfig] = None
    
    def __new__(cls):
        """Ensure singleton pattern."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instance(cls) -> 'ConfigurationManager':
        """
        Get the singleton instance of ConfigurationManager.
        
        Returns:
            ConfigurationManager instance
        """
        if cls._instance is None:
            cls._instance = ConfigurationManager()
        return cls._instance
    
    def initialize(self, config_data: Dict[str, Any]) -> None:
        """
        Initialize the configuration with the provided data.
        
        Args:
            config_data: Configuration data dictionary
            
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> config_manager.initialize({
            ...     'api_key': 'your-api-key',
            ...     'api_url': 'https://api.mosaia.ai',
            ...     'version': '1',
            ...     'verbose': True
            ... })
        """
        # Convert dict to MosaiaConfig
        session_data = config_data.get('session')
        session = None
        if session_data:
            session = SessionInterface(**session_data)
        
        self._config = MosaiaConfig(
            api_key=config_data.get('api_key'),
            api_url=config_data.get('api_url'),
            version=config_data.get('version'),
            client_id=config_data.get('client_id'),
            client_secret=config_data.get('client_secret'),
            verbose=config_data.get('verbose', False),
            session=session
        )
    
    def initialize_from_env(self) -> None:
        """
        Initialize configuration from environment variables.
        
        Reads configuration from environment variables with the MOSAIA_ prefix.
        
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> config_manager.initialize_from_env()
        """
        config_data = {
            'api_key': os.getenv('MOSAIA_API_KEY'),
            'api_url': os.getenv('MOSAIA_API_URL'),
            'version': os.getenv('MOSAIA_VERSION'),
            'client_id': os.getenv('MOSAIA_CLIENT_ID'),
            'client_secret': os.getenv('MOSAIA_CLIENT_SECRET'),
            'verbose': os.getenv('MOSAIA_VERBOSE', 'false').lower() == 'true'
        }
        
        # Remove None values
        config_data = {k: v for k, v in config_data.items() if v is not None}
        
        self.initialize(config_data)
    
    def get_config(self) -> MosaiaConfig:
        """
        Get the current configuration.
        
        Returns:
            Current MosaiaConfig instance
            
        Raises:
            RuntimeError: If configuration is not initialized
            
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> config = config_manager.get_config()
            >>> print(config.api_key)
        """
        if self._config is None:
            raise RuntimeError('Configuration not initialized. Call initialize() first.')
        return self._config
    
    def set_config(self, config: MosaiaConfig) -> None:
        """
        Set the configuration directly.
        
        Args:
            config: MosaiaConfig instance to set
            
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> new_config = MosaiaConfig(api_key='new-key')
            >>> config_manager.set_config(new_config)
        """
        self._config = config
    
    def reset(self) -> None:
        """
        Reset the configuration to None.
        
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> config_manager.reset()
        """
        self._config = None
    
    def update_config(self, updates: Dict[str, Any]) -> None:
        """
        Update the current configuration with new values.
        
        Args:
            updates: Dictionary of configuration updates
            
        Examples:
            >>> config_manager = ConfigurationManager.get_instance()
            >>> config_manager.update_config({'verbose': True})
        """
        if self._config is None:
            raise RuntimeError('Configuration not initialized. Call initialize() first.')
        
        # Update the config with new values
        for key, value in updates.items():
            if hasattr(self._config, key):
                setattr(self._config, key, value)
