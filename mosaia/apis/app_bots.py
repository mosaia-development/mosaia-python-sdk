"""
App Bots API for managing app bots
"""

from typing import Optional, List, Union, Dict, Any
from mosaia.types import MosiaConfig, AppInterface, AppBotInterface
from mosaia.entities.app_bot import AppBot
from mosaia.api_client import APIClient
from mosaia.config import DEFAULT_CONFIG

class AppBots:
    """App Bots API client"""
    
    def __init__(self, apps, app: Optional[Union[str, AppInterface, Dict[str, Any]]] = None):
        """
        Initialize the App Bots API client
        
        Args:
            apps: Apps API instance
            app: Optional app identifier (string ID, AppInterface, or dict)
        """
        config = apps.config
        base_url = config.base_url
        
        # Handle different app parameter types
        app_id = None
        if isinstance(app, str):
            app_id = app
        elif isinstance(app, AppInterface) and app.id:
            app_id = app.id
        elif isinstance(app, dict) and app.get('id'):
            app_id = app['id']
        
        if app_id:
            base_url += f"/{app_id}"
        
        base_url += DEFAULT_CONFIG['ENDPOINTS']['BOTS']
        
        self.config = config
        self.config.base_url = base_url
        self.client = APIClient(self.config)
    
    def get(self, bot: Optional[Union[str, AppBotInterface, Dict[str, Any]]] = None, **kwargs) -> Union[List[AppBot], AppBot, None]:
        """
        Get app bots or a specific app bot
        
        Args:
            bot: Optional bot identifier (string ID, AppBotInterface, or dict)
            **kwargs: Additional query parameters
            
        Returns:
            Union[List[AppBot], AppBot, None]: List of app bots, single bot, or None
        """
        uri = ''
        
        # Handle different bot parameter types
        bot_id = None
        if isinstance(bot, str):
            bot_id = bot
        elif isinstance(bot, AppBotInterface) and bot.id:
            bot_id = bot.id
        elif isinstance(bot, dict) and bot.get('id'):
            bot_id = bot['id']
        
        if bot_id:
            uri += f"/{bot_id}"
        
        # Add query parameters from kwargs
        if kwargs:
            query_params = '&'.join([f"{k}={v}" for k, v in kwargs.items()])
            uri += f"?{query_params}" if '?' not in uri else f"&{query_params}"
        
        response = self.client.GET(uri)
        data = response.data
        
        if isinstance(data, list):
            return [AppBot(self.client, bot_data) for bot_data in data]
        
        if data:
            return AppBot(self.client, data)
        
        return None
    
    def get_by_id(self, bot_id: str) -> Optional[AppBot]:
        """
        Get an app bot by ID (Pythonic version)
        
        Args:
            bot_id (str): Bot ID
            
        Returns:
            Optional[AppBot]: App bot instance or None if not found
        """
        if not bot_id:
            raise ValueError("Bot ID is required")
        
        return self.get(bot_id)
    
    def create(self, bot_data: Union[AppBotInterface, Dict[str, Any]], **kwargs) -> AppBot:
        """
        Create a new app bot
        
        Args:
            bot_data: Bot data (AppBotInterface or dict)
            **kwargs: Additional bot properties
            
        Returns:
            AppBot: Created app bot instance
        """
        # Convert to dict if needed
        if isinstance(bot_data, AppBotInterface):
            data = bot_data.dict()
        else:
            data = bot_data.copy()
        
        # Add kwargs to data
        data.update(kwargs)
        
        response = self.client.POST('', data)
        return AppBot(self.client, response.data)
    
    def update(self, bot_id: str, bot_data: Union[AppBotInterface, Dict[str, Any]], **kwargs) -> AppBot:
        """
        Update an existing app bot
        
        Args:
            bot_id (str): Bot ID to update
            bot_data: Bot data (AppBotInterface or dict)
            **kwargs: Additional bot properties
            
        Returns:
            AppBot: Updated app bot instance
        """
        if not bot_id:
            raise ValueError("Bot ID is required for update")
        
        # Convert to dict if needed
        if isinstance(bot_data, AppBotInterface):
            data = bot_data.dict()
        else:
            data = bot_data.copy()
        
        # Add kwargs to data
        data.update(kwargs)
        
        response = self.client.PUT(f"/{bot_id}", data)
        return AppBot(self.client, response.data)
    
    def delete(self, bot_id: str) -> None:
        """
        Delete an app bot
        
        Args:
            bot_id (str): Bot ID to delete
            
        Returns:
            None
        """
        if not bot_id:
            raise ValueError("Bot ID is required for delete")
        
        self.client.DELETE(f"/{bot_id}")
    
    # Legacy methods for backward compatibility
    def get_by_interface(self, bot: AppBotInterface) -> Optional[AppBot]:
        """Legacy method - use get() instead"""
        return self.get(bot)
    
    def create_by_interface(self, bot: AppBotInterface) -> AppBot:
        """Legacy method - use create() instead"""
        return self.create(bot)
    
    def update_by_interface(self, bot: AppBotInterface) -> AppBot:
        """Legacy method - use update() instead"""
        if not bot.id:
            raise ValueError("Bot ID is required for update")
        return self.update(bot.id, bot)
    
    def delete_by_interface(self, bot: AppBotInterface) -> None:
        """Legacy method - use delete() instead"""
        if not bot.id:
            raise ValueError("Bot ID is required for delete")
        return self.delete(bot.id) 