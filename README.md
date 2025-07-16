# Mosaia Python SDK

A comprehensive Python SDK for the Mosaia platform, providing feature parity with the Node.js SDK. This SDK enables you to build 3rd party app integrations, manage applications, tools, and bots with a Pythonic, type-safe interface.

## 🚀 Features

- **Full Feature Parity**: Complete implementation matching the Node.js SDK capabilities
- **Pythonic Design**: Intuitive, Python-native API patterns
- **Type Safety**: Comprehensive Pydantic v2 type definitions
- **OAuth Support**: PKCE flow for secure authentication
- **Error Handling**: Structured error responses with detailed information
- **Comprehensive Testing**: Full test suite with 100% pass rate
- **Modern Python**: Python 3.10+ with async/await support

## 📦 Installation

```bash
pip install mosaia
```

## 🏁 Quick Start

```python
from mosaia import Mosaia, MosiaConfig

# Initialize with configuration
config = MosiaConfig(
    api_key="your_api_key",
    version="1",
    base_url="https://api.mosaia.ai"
)
client = Mosaia(config)

# Or initialize with defaults and generate API key
client = Mosaia()
client.generate_api_key("your_client_id", "your_client_secret")
```

## 📚 API Reference

### Apps API

Manage applications on the Mosaia platform:

```python
# Get all apps
apps = client.apps.get()

# Get a specific app (Pythonic way)
app = client.apps.get("app_id")

# Get app by ID
app = client.apps.get_by_id("app_id")

# Create a new app
new_app = client.apps.create({
    "name": "My App",
    "short_description": "A great app",
    "org": "org_id"
})

# Update an app
updated_app = client.apps.update("app_id", {
    "name": "Updated App Name",
    "short_description": "Updated description"
})

# Delete an app
client.apps.delete("app_id")
```

### Tools API

Manage tools for your applications:

```python
# Initialize with user/org context
config = MosiaConfig(user="user_id")  # or org="org_id"
client = Mosaia(config)

# Get all tools
tools = client.tools.get()

# Get a specific tool
tool = client.tools.get("tool_id")

# Get tool by name
tool = client.tools.get_by_name("tool_name")

# Create a new tool
new_tool = client.tools.create({
    "name": "my_tool",
    "short_description": "A useful tool",
    "tool_schema": '{"type": "object"}'
})

# Update a tool
updated_tool = client.tools.update("tool_id", {
    "name": "updated_tool",
    "short_description": "Updated description"
})

# Delete a tool
client.tools.delete("tool_id")
```

### App Bots API

Manage bots for your applications:

```python
# Get all bots for an app
bots = client.app_bots.get()

# Get a specific bot
bot = client.app_bots.get("bot_id")

# Get bot by ID
bot = client.app_bots.get_by_id("bot_id")

# Create a new bot
new_bot = client.app_bots.create({
    "app": "app_id",
    "response_url": "https://example.com/webhook"
})

# Update a bot
updated_bot = client.app_bots.update("bot_id", {
    "response_url": "https://new-url.com/webhook"
})

# Delete a bot
client.app_bots.delete("bot_id")
```

### OAuth Support

Handle OAuth2 Authorization Code flow with PKCE:

```python
# Initialize OAuth
oauth = client.oauth(
    redirect_uri="https://your-app.com/callback",
    scopes=["read", "write"]
)

# Get authorization URL
auth_data = oauth.get_authorization_url_and_code_verifier()
auth_url = auth_data["url"]
code_verifier = auth_data["code_verifier"]

# Exchange code for token (after user authorizes)
token_response = await oauth.exchange_code_for_token(
    code="authorization_code",
    code_verifier=code_verifier
)

# Refresh token
new_token_response = await oauth.refresh_token(
    refresh_token=token_response.refresh_token
)
```

## 🎯 Pythonic Patterns

The SDK supports multiple Pythonic usage patterns:

```python
# 1. Direct ID passing (most Pythonic)
app = client.apps.get("app_id")
tool = client.tools.get("tool_id")
bot = client.app_bots.get("bot_id")

# 2. Using dictionaries
new_app = client.apps.create({
    "name": "My App",
    "short_description": "Description"
})

# 3. Using keyword arguments
new_bot = client.app_bots.create(
    {},  # Empty dict as base
    app="app_id",
    response_url="https://example.com/webhook"
)

# 4. Legacy interface support (still available)
from mosaia.types import AppInterface
app = client.apps.get(AppInterface(id="app_id"))
```

## ⚠️ Error Handling

The SDK provides structured error handling:

```python
from mosaia import is_sdk_error

try:
    app = client.apps.get("invalid_id")
except Exception as e:
    if is_sdk_error(e):
        print(f"SDK Error: {e.message} (Code: {e.code})")
    else:
        print(f"Network Error: {e}")
```

## ⚙️ Configuration

Comprehensive configuration options:

```python
config = MosiaConfig(
    api_key="your_api_key",
    version="1",
    base_url="https://api.mosaia.ai",
    frontend_url="https://mosaia.ai",
    client_id="your_client_id",
    client_secret="your_client_secret",
    user="user_id",        # For user-scoped operations
    org="org_id"          # For org-scoped operations
)
```

## 📋 Types

Complete type definitions for type safety:

```python
from mosaia.types import (
    MosiaConfig, APIResponse, ErrorResponse,
    AppInterface, ToolInterface, AppBotInterface,
    OAuthConfig, OAuthTokenResponse, OAuthErrorResponse
)
```

## 🧪 Testing

The SDK includes a comprehensive test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_agent.py -v
```

All tests pass with 100% success rate, covering:
- Package installation and imports
- Configuration and client creation
- API method signatures and patterns
- OAuth functionality
- Error handling
- Type validation

## 🔄 Legacy Support

The SDK maintains backward compatibility:

```python
# Legacy properties (still available)
orgs = client.orgs
users = client.users
agents = client.agents
agent_groups = client.agent_groups
```

## 📦 Requirements

- Python 3.10+
- requests>=2.25.0
- pydantic>=2.0.0
- bson>=0.5.0
- aiohttp>=3.8.0 (for OAuth)

## 🆕 What's New

### Version 0.1.0
- ✅ **Complete Feature Parity**: All Node.js SDK features implemented
- ✅ **Pythonic API Design**: Intuitive, Python-native patterns
- ✅ **Pydantic v2 Compatibility**: Modern type system with full validation
- ✅ **Comprehensive Test Suite**: 100% test coverage
- ✅ **OAuth Support**: PKCE flow implementation
- ✅ **Error Handling**: Structured error responses
- ✅ **Type Safety**: Complete type definitions
- ✅ **Documentation**: Comprehensive examples and guides

## 📄 License

Apache-2.0

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

