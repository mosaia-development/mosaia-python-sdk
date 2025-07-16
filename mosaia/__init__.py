"""
Mosaia SDK initialization
"""
from mosaia.mosaia import Mosaia
from mosaia.types import (
    MosiaConfig, APIResponse, ErrorResponse, PagingInterface,
    AppInterface, ToolInterface, AppBotInterface, DehydratedAppBotInterface,
    GetAppBotsPayload, GetAppBotPayload, GetAppsPayload, GetAppPayload,
    OAuthConfig, OAuthTokenResponse, OAuthErrorResponse
)
from mosaia.apis import Apps, Tools, AppBots
from mosaia.oauth import OAuth
from mosaia.utils import is_sdk_error, create_error_response
from mosaia.config import DEFAULT_CONFIG

__version__ = "0.1.0"

# Define what gets exported with "from mosaia import *"
__all__ = [
    'Mosaia',
    'MosiaConfig', 'APIResponse', 'ErrorResponse', 'PagingInterface',
    'AppInterface', 'ToolInterface', 'AppBotInterface', 'DehydratedAppBotInterface',
    'GetAppBotsPayload', 'GetAppBotPayload', 'GetAppsPayload', 'GetAppPayload',
    'OAuthConfig', 'OAuthTokenResponse', 'OAuthErrorResponse',
    'Apps', 'Tools', 'AppBots',
    'OAuth',
    'is_sdk_error', 'create_error_response',
    'DEFAULT_CONFIG'
]