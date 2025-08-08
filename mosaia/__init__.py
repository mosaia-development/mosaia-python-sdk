"""
Mosaia Python SDK

A comprehensive Python SDK for the Mosaia AI platform.
"""

__version__ = "1.0.0"
__author__ = "Mosaia Team"
__email__ = "support@mosaia.ai"

# Import main components
from .config import ConfigurationManager
from .api_client import APIClient
from .base_api import BaseAPI
from .types import (
    MosaiaConfig,
    UserInterface,
    OrganizationInterface,
    AppInterface,
    AgentInterface,
    ToolInterface,
    QueryParams,
    APIResponse,
    BatchAPIResponse,
    ErrorResponse,
    AuthType,
    GrantType
)

# Import utils
from .utils import (
    is_valid_object_id,
    parse_error,
    query_generator,
    is_timestamp_expired,
    failure,
    success,
    server_error_to_string,
    is_sdk_error
)

# Import functions
from .functions import (
    BaseFunctions,
    Chat,
    Completions
)

# Import auth
from .auth import (
    MosaiaAuth,
    OAuth
)

# Import models
from .models import (
    BaseModel,
    User,
    App,
    Session,
    Agent,
    Organization,
    OrgUser,
    AppBot,
    AgentGroup,
    Tool,
    Client,
    Model
)

__all__ = [
    "ConfigurationManager",
    "APIClient", 
    "BaseAPI",
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
    "AppBot",
    "AgentGroup",
    "Tool",
    "Client",
    "Model"
]
