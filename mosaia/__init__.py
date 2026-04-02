"""
Mosaia Python SDK

A comprehensive Python SDK for the Mosaia AI platform.

This module provides the primary interface for interacting with the Mosaia API.
It exports the main MosaiaClient class, all collection classes for API operations,
model classes for data structures, authentication utilities, and configuration
management tools.

The SDK supports both API key and OAuth2 authentication methods, and provides
comprehensive access to all Mosaia platform features including user management,
organization management, AI agents, tools, applications, and more.

Examples:
    >>> from mosaia import MosaiaClient

    # Create a new Mosaia SDK instance
    >>> mosaia = MosaiaClient({
    ...     'api_key': 'your-api-key',
    ...     'api_url': 'https://api.mosaia.ai',
    ...     'version': '1'
    ... })

    # Get all users
    >>> users = await mosaia.users.get()

    # Create an OAuth instance
    >>> oauth = mosaia.oauth({
    ...     'redirect_uri': 'https://your-app.com/callback',
    ...     'scopes': ['read', 'write']
    ... })
"""

__version__ = "0.0.1"
__author__ = "Mosaia Team"
__email__ = "support@mosaia.ai"

from .api_client import APIClient

# Import auth
from .auth import MosaiaAuth, OAuth
from .base_api import BaseAPI

# Import main client class
from .client import MosaiaClient

# Import collections (Node parity)
from .collections import (
    AccessPolicies,
    AgentTools,
    Agents,
    AppConnectors,
    AppWebhooks,
    Apps,
    BaseCollection,
    Clients,
    DriveItems,
    Drives,
    Logs,
    Messages,
    Meters,
    Models,
    Notifications,
    OrgPermissions,
    OrgUsers,
    Organizations,
    Plans,
    Scopes,
    Search,
    Snapshots,
    SSO,
    Tasks,
    Tools,
    Triggers,
    UploadJobs,
    UserPermissions,
    Users,
    VectorIndexes,
    Vectors,
    Wallets,
)

# Import main components
from .config import DEFAULT_CONFIG, ConfigurationManager

# Import functions
from .functions import Access, BaseFunctions, Chat, Completions

# Import models (Node parity)
from .models import (
    AccessPolicy,
    Agent,
    AgentTool,
    App,
    AppConnector,
    AppWebhook,
    BaseModel,
    Client,
    Drive,
    DriveItem,
    Log,
    Message,
    Meter,
    Model,
    OrgPermission,
    OrgUser,
    Organization,
    Plan,
    Session,
    Snapshot,
    Task,
    Tool,
    Trigger,
    UploadJob,
    User,
    UserPermission,
    Vector,
    VectorIndex,
    Wallet,
)
from .types import (
    AgentInterface,
    APIResponse,
    AppInterface,
    AuthType,
    BatchAPIResponse,
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatMessage,
    ErrorResponse,
    GrantType,
    MosaiaConfig,
    OAuthConfig,
    OAuthErrorResponse,
    OAuthTokenResponse,
    OrganizationInterface,
    PagingInterface,
    QueryParams,
    SessionInterface,
    ToolInterface,
    TriggerConfig,
    TriggerExecuteResponse,
    TriggerInterface,
    TriggerStatus,
    TriggerType,
    UserInterface,
)

# Import utils
from .utils import (
    failure,
    is_sdk_error,
    is_timestamp_expired,
    is_valid_object_id,
    parse_error,
    query_generator,
    server_error_to_string,
    success,
)

__all__ = [
    # Main client
    "MosaiaClient",
    # Configuration
    "ConfigurationManager",
    "DEFAULT_CONFIG",
    # API components
    "APIClient",
    "BaseAPI",
    # Types
    "MosaiaConfig",
    "UserInterface",
    "OrganizationInterface",
    "AppInterface",
    "AgentInterface",
    "ToolInterface",
    "QueryParams",
    "APIResponse",
    "BatchAPIResponse",
    "ErrorResponse",
    "AuthType",
    "GrantType",
    "SessionInterface",
    "PagingInterface",
    "OAuthConfig",
    "OAuthTokenResponse",
    "OAuthErrorResponse",
    "ChatMessage",
    "ChatCompletionRequest",
    "ChatCompletionResponse",
    "TriggerType",
    "TriggerStatus",
    "TriggerConfig",
    "TriggerInterface",
    "TriggerExecuteResponse",
    # Utils
    "is_valid_object_id",
    "parse_error",
    "query_generator",
    "is_timestamp_expired",
    "failure",
    "success",
    "server_error_to_string",
    "is_sdk_error",
    # Functions
    "Access",
    "BaseFunctions",
    "Chat",
    "Completions",
    # Auth
    "MosaiaAuth",
    "OAuth",
    # Models
    "BaseModel",
    "User",
    "App",
    "Session",
    "Agent",
    "Organization",
    "OrgUser",
    "AppConnector",
    "AppWebhook",
    "Tool",
    "Trigger",
    "Client",
    "Model",
    "Drive",
    "DriveItem",
    "UploadJob",
    "Log",
    "Message",
    "Snapshot",
    "VectorIndex",
    "Vector",
    "Task",
    "Plan",
    "AccessPolicy",
    "OrgPermission",
    "UserPermission",
    "Meter",
    "Wallet",
    "AgentTool",
    # Collections
    "BaseCollection",
    "Agents",
    "Apps",
    "Users",
    "Organizations",
    "OrgUsers",
    "Tools",
    "Triggers",
    "Clients",
    "Models",
    "AgentTools",
    "AppConnectors",
    "AppWebhooks",
    "Search",
    "Drives",
    "DriveItems",
    "UploadJobs",
    "Logs",
    "Messages",
    "Snapshots",
    "Scopes",
    "SSO",
    "Notifications",
    "VectorIndexes",
    "Vectors",
    "Tasks",
    "Plans",
    "AccessPolicies",
    "OrgPermissions",
    "UserPermissions",
    "Meters",
    "Wallets",
]

# Default export for single primary class pattern
__default__ = MosaiaClient
