# Mosaia Python SDK

A comprehensive Python SDK for the Mosaia AI platform, providing access to all platform features including user management, organization management, AI agents, tools, applications, and more.

## Features

- **Complete API Coverage**: Access to all Mosaia platform APIs
- **Authentication Support**: API key and OAuth2 authentication
- **Type Safety**: Full type hints and dataclass support
- **Pythonic Design**: Follows Python best practices and conventions
- **Async Support**: Built-in async/await support for all operations
- **Error Handling**: Comprehensive error handling and validation
- **Documentation**: Extensive docstrings and examples

## Installation

```bash
pip install mosaia
```

## Quick Start

### Basic Usage

```python
from mosaia import MosaiaClient

# Initialize with API key
client = MosaiaClient({
    "api_key": "your-api-key",
    "api_url": "https://api.mosaia.ai"
})

# Get all users
users = await client.users.get()

# Create a new agent
agent = await client.agents.create({
    "name": "My Agent",
    "short_description": "A helpful AI agent"
})
```

### Using Individual Collections

```python
from mosaia import Users, Agents, Apps

# Create collection instances
users = Users()
agents = Agents()
apps = Apps()

# Perform operations
all_users = await users.get()
agent = await agents.get(id="agent-id")
new_app = await apps.create({
    "name": "My App",
    "short_description": "Description"
})
```

## Sandbox Testing

The SDK includes a sandbox environment for testing and experimentation, similar to the Node.js `sandbox.ts` file.

### Quick Setup

1. **Install the SDK in development mode**:
   ```bash
   pip install -e .
   ```

2. **Set up environment variables** (choose one option):

   **Option 1: Using .env file (recommended)**
   ```bash
   # Install python-dotenv
   pip install python-dotenv
   
   # Create .env file in project root
   echo "API_URL=https://api.mosaia.ai
   CLIENT_ID=your-client-id
   USER_EMAIL=user@example.com
   USER_PASSWORD=your-password" > .env
   ```

   **Option 2: Set environment variables manually**
   ```bash
   export API_URL="https://api.mosaia.ai"
   export CLIENT_ID="your-client-id"
   export USER_EMAIL="user@example.com"
   export USER_PASSWORD="your-password"
   ```

3. **Run the sandbox**:
   ```bash
   python sandbox.py
   ```

### Sandbox Features

The sandbox tests the following functionality:
- ✅ **Authentication** - Email/password authentication
- ✅ **Agents** - Agent listing and chat completions
- ✅ **Users** - User session and user-related operations
- ✅ **Organizations** - Organization listing and details
- ✅ **Tools** - Tool listing and details

### Example Output

```
🧪 Mosaia Python SDK Sandbox
========================================
🚀 Initializing Mosaia SDK...
   Attempting to sign in...
✅ Authentication successful!
   Session user: John Doe
   Session org: My Organization

🔍 Testing agents functionality...
   Found 3 agents
   First agent: Cafe Assistant
   Description: AI assistant for cafe operations
   Testing chat completion...
   Agent response: Hello! I'm the Cafe Assistant, an AI designed to help with cafe operations...

👥 Testing users functionality...
   Current user: John Doe (john@example.com)
   User agents: 2 found
   User organizations: 1 found

🏢 Testing organizations functionality...
   Found 1 organizations
   First organization: My Organization
   Description: Main organization for development

🛠️ Testing tools functionality...
   Found 5 tools
   First tool: Weather Tool
   Description: Get current weather information

✅ Sandbox tests completed successfully!
```

For more information, see [SANDBOX_README.md](SANDBOX_README.md).

## Authentication

### API Key Authentication

```python
from mosaia import MosaiaClient

client = MosaiaClient({
    "api_key": "your-api-key"
})
```

### OAuth2 Authentication

```python
from mosaia import MosaiaClient

# Initialize client with OAuth support
client = MosaiaClient({
    "client_id": "your-client-id",
    "client_secret": "your-client-secret"
})

# Create OAuth instance
oauth = client.oauth({
    "redirect_uri": "https://your-app.com/callback",
    "scopes": ["read", "write"]
})

# Get authorization URL and code verifier
auth_url, code_verifier = oauth.get_authorization_url_and_code_verifier()

# Redirect user to auth_url
# After user authorizes, you'll receive a code in your callback

# Exchange code for tokens
tokens = await oauth.authenticate_with_code_and_verifier(code, code_verifier)
```

## API Collections

### Users

```python
from mosaia import Users

users = Users()

# Get all users
all_users = await users.get()

# Get users with pagination
users_page = await users.get({"limit": 10, "offset": 0})

# Get specific user
user = await users.get(id="user-id")

# Create new user
new_user = await users.create({
    "email": "user@example.com",
    "name": "John Doe"
})

# Update user
updated_user = await users.update("user-id", {
    "name": "John Smith"
})

# Delete user
await users.delete("user-id")

# Search users
results = await users.search("john", limit=10)

# Get active users
active_users = await users.get_active_users(limit=50)
```

### Agents

```python
from mosaia import Agents

agents = Agents()

# Get all agents
all_agents = await agents.get()

# Get specific agent
agent = await agents.get(id="agent-id")

# Create new agent
new_agent = await agents.create({
    "name": "My Agent",
    "short_description": "A helpful AI agent",
    "model": "gpt-4"
})

# Chat completion
completion = await agents.chat_completion("agent-id", {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}]
})
```

### Applications

```python
from mosaia import Apps

apps = Apps()

# Get all applications
all_apps = await apps.get()

# Get specific application
app = await apps.get(id="app-id")

# Create new application
new_app = await apps.create({
    "name": "My App",
    "short_description": "Description"
})
```

### Organizations

```python
from mosaia import Organizations

orgs = Organizations()

# Get all organizations
all_orgs = await orgs.get()

# Get specific organization
org = await orgs.get(id="org-id")

# Create new organization
new_org = await orgs.create({
    "name": "My Organization",
    "short_description": "Description"
})
```

## Models

### User Model

```python
from mosaia.models import User

# Create user instance
user = User({
    "email": "john@example.com",
    "name": "John Doe",
    "username": "johndoe"
})

# Access properties
print(user.email)  # john@example.com
print(user.name)   # John Doe

# Update user
user.update({"name": "John Smith"})
await user.save()

# Convert to JSON
user_data = user.to_json()
```

### Session Model

```python
from mosaia import MosaiaClient

client = MosaiaClient({"api_key": "your-api-key"})

# Get current session
session = await client.session()

# Access user and organization
if session.user:
    print(f"User: {session.user.email}")

if session.org:
    print(f"Organization: {session.org.name}")

# Check permissions
if session.has_permission("read", "users"):
    print("User can read users")
```

## Configuration

### Configuration Manager

```python
from mosaia import ConfigurationManager

# Get singleton instance
config_manager = ConfigurationManager.get_instance()

# Initialize with configuration
config_manager.initialize({
    "api_key": "your-api-key",
    "api_url": "https://api.mosaia.ai",
    "version": "1",
    "client_id": "your-client-id",
    "client_secret": "your-client-secret",
    "verbose": True
})

# Access configuration
config = config_manager.get_config()
print(config.api_key)  # your-api-key
```

### Environment Variables

You can also use environment variables for configuration:

```bash
export MOSAIA_API_KEY="your-api-key"
export MOSAIA_API_URL="https://api.mosaia.ai"
export MOSAIA_CLIENT_ID="your-client-id"
export MOSAIA_CLIENT_SECRET="your-client-secret"
```

## Error Handling

```python
from mosaia import MosaiaClient

client = MosaiaClient({"api_key": "your-api-key"})

try:
    users = await client.users.get()
except Exception as e:
    print(f"Error: {e}")
    # Handle error appropriately
```

## Utilities

```python
from mosaia.utils import (
    is_valid_object_id,
    parse_error,
    query_generator,
    is_timestamp_expired
)

# Validate ObjectId
is_valid = is_valid_object_id("507f1f77bcf86cd799439011")

# Parse error
error_info = parse_error(exception)

# Generate query string
query_string = query_generator({
    "limit": 10,
    "offset": 0,
    "search": "john"
})

# Check if timestamp is expired
is_expired = is_timestamp_expired("2024-01-01T00:00:00Z")
```

## Development

### Installation for Development

```bash
git clone https://github.com/mosaia-development/mosaia-python-sdk.git
cd mosaia-python-sdk
pip install -e .
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black mosaia/
isort mosaia/
```

## Documentation

For detailed documentation, visit [https://docs.mosaia.ai/python-sdk](https://docs.mosaia.ai/python-sdk)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Documentation: [https://docs.mosaia.ai/python-sdk](https://docs.mosaia.ai/python-sdk)
- Issues: [https://github.com/mosaia-development/mosaia-python-sdk/issues](https://github.com/mosaia-development/mosaia-python-sdk/issues)
- Email: support@mosaia.ai 