"""
Type definitions for the Mosaia SDK
"""

from typing import Dict, Any, Optional, List, Union
from pydantic import BaseModel

class MosiaConfig(BaseModel):
    """Configuration interface for the Mosaia SDK"""
    api_key: Optional[str] = None
    version: Optional[str] = None
    base_url: Optional[str] = None
    frontend_url: Optional[str] = None
    client_id: Optional[str] = None
    client_secret: Optional[str] = None
    user: Optional[str] = None
    org: Optional[str] = None

class APIResponse(BaseModel):
    """API response interface"""
    data: Any
    status: int
    message: Optional[str] = None

class ErrorResponse(BaseModel):
    """Error response interface"""
    message: str
    code: str
    status: int

class PagingInterface(BaseModel):
    """Paging interface for paginated responses"""
    offset: Optional[int] = None
    limit: Optional[int] = None
    total: Optional[int] = None
    page: Optional[int] = None
    total_pages: Optional[int] = None

class AppInterface(BaseModel):
    """App interface"""
    id: Optional[str] = None
    name: str
    org: Optional[str] = None
    user: Optional[str] = None
    short_description: str
    long_description: Optional[str] = None
    image: Optional[str] = None
    external_app_url: Optional[str] = None
    external_api_key: Optional[str] = None
    external_headers: Optional[Dict[str, str]] = None
    active: Optional[bool] = None
    tags: Optional[List[str]] = None
    keywords: Optional[List[str]] = None
    extensors: Optional[Dict[str, str]] = None
    external_id: Optional[str] = None

class ToolInterface(BaseModel):
    """Tool interface"""
    id: Optional[str] = None
    org: Optional[str] = None
    user: Optional[str] = None
    name: Optional[str] = None
    friendly_name: Optional[str] = None
    short_description: str
    tool_schema: str
    required_environment_variables: Optional[List[str]] = None
    source_url: Optional[str] = None
    url: Optional[str] = None
    public: Optional[bool] = None
    active: Optional[bool] = None
    keywords: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    external_id: Optional[str] = None
    extensors: Optional[Dict[str, str]] = None

class AppBotInterface(BaseModel):
    """App Bot interface"""
    id: Optional[str] = None
    app: Union[str, AppInterface]
    response_url: str
    org: Optional[str] = None
    user: Optional[str] = None
    agent: Optional[str] = None
    agent_group: Optional[str] = None
    api_key: Optional[str] = None
    api_key_partial: Optional[str] = None
    active: Optional[bool] = None
    tags: Optional[List[str]] = None
    extensors: Optional[Dict[str, str]] = None
    external_id: Optional[str] = None
    record_history: Optional[Dict[str, str]] = None

class DehydratedAppBotInterface(BaseModel):
    """Dehydrated App Bot interface (without nested objects)"""
    id: str
    app: str
    response_url: str
    org: Optional[str] = None
    user: Optional[str] = None
    agent: Optional[str] = None
    agent_group: Optional[str] = None
    api_key: Optional[str] = None
    api_key_partial: Optional[str] = None
    active: Optional[bool] = None
    tags: Optional[List[str]] = None
    extensors: Optional[Dict[str, str]] = None
    external_id: Optional[str] = None
    record_history: Optional[Dict[str, str]] = None

class GetAppBotsPayload(BaseModel):
    """Get App Bots payload"""
    data: List[DehydratedAppBotInterface]
    paging: Optional[PagingInterface] = None

class GetAppBotPayload(BaseModel):
    """Get App Bot payload"""
    data: DehydratedAppBotInterface
    paging: Optional[PagingInterface] = None

class GetAppsPayload(BaseModel):
    """Get Apps payload"""
    data: List[AppInterface]
    paging: Optional[PagingInterface] = None

class GetAppPayload(BaseModel):
    """Get App payload"""
    data: AppInterface
    paging: Optional[PagingInterface] = None

class OAuthConfig(BaseModel):
    """OAuth configuration interface"""
    client_id: str
    redirect_uri: str
    scopes: Optional[List[str]] = None
    state: Optional[str] = None

class OAuthTokenResponse(BaseModel):
    """OAuth token response interface"""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str
    expires_in: int
    sub: str
    iat: str
    exp: str

class OAuthErrorResponse(BaseModel):
    """OAuth error response interface"""
    error: str
    error_description: Optional[str] = None
    error_uri: Optional[str] = None 