"""
App Bots API for managing app bots
"""

from typing import Optional, List, Union
from mosaia.types import MosiaConfig, AppInterface, AppBotInterface
from mosaia.entities.app_bot import AppBot
from mosaia.api_client import APIClient
from mosaia.config import DEFAULT_CONFIG

class AppBots:
    """App Bots API client"""
    
    def __init__(self, apps, app: Optional[AppInterface] = None):
        """
        Initialize the App Bots API client
        
        Args:
            apps: Apps API instance
            app: Optional app interface
        """
        config = apps.config
        base_url = config.base_url
        
        if app and app.id:
            base_url += f"/{app.id}"
        
        base_url += DEFAULT_CONFIG['ENDPOINTS']['BOTS']
        
        self.config = config
        self.config.base_url = base_url
        self.client = APIClient(self.config)
    
    def get(self, bot: Optional[AppBotInterface] = None) -> Union[List[AppBot], AppBot, None]:
        """
        Get app bots or a specific app bot
        
        Args:
            bot: Optional app bot interface with ID to get specific bot
            
        Returns:
            Union[List[AppBot], AppBot, None]: List of app bots, single bot, or None
        """
        uri = ''
        
        if bot and bot.id:
            uri += f"/{bot.id}"
        
        response = self.client.GET(uri)
        data = response.data
        
        if isinstance(data, list):
            return [AppBot(self.client, bot_data) for bot_data in data]
        
        if data:
            return AppBot(self.client, data)
        
        return None
    
    def get_by_id(self, bot: AppBotInterface) -> Optional[AppBot]:
        """
        Get an app bot by ID
        
        Args:
            bot: App bot interface with ID
            
        Returns:
            Optional[AppBot]: App bot instance or None if not found
        """
        if not bot.id:
            raise ValueError("Bot ID is required")
        
        uri = f"/{bot.id}"
        response = self.client.GET(uri)
        data = response.data
        
        if data:
            # Merge api_key if provided
            if bot.api_key:
                data['api_key'] = bot.api_key
            return AppBot(self.client, data)
        
        return None
    
    def create(self, bot: AppBotInterface) -> AppBot:
        """
        Create a new app bot
        
        Args:
            bot: App bot interface with bot data
            
        Returns:
            AppBot: Created app bot instance
        """
        response = self.client.POST('', bot.dict())
        return AppBot(self.client, response.data)
    
    def update(self, bot: AppBotInterface) -> AppBot:
        """
        Update an existing app bot
        
        Args:
            bot: App bot interface with bot data and ID
            
        Returns:
            AppBot: Updated app bot instance
        """
        if not bot.id:
            raise ValueError("Bot ID is required for update")
        
        response = self.client.PUT(f"/{bot.id}", bot.dict())
        return AppBot(self.client, response.data)
    
    def delete(self, bot: AppBotInterface) -> None:
        """
        Delete an app bot
        
        Args:
            bot: App bot interface with ID
            
        Returns:
            None
        """
        if not bot.id:
            raise ValueError("Bot ID is required for delete")
        
        self.client.DELETE(f"/{bot.id}") 