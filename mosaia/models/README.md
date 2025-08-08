# Mosaia Python SDK - Models Module

This module provides model classes that represent entities in the Mosaia platform. Each model provides data management, validation, and API integration capabilities for their respective entity types.

## Overview

The models module provides comprehensive data management functionality with:
- **BaseModel**: Abstract base class providing common functionality for all models
- **User**: User account and profile management
- **App**: Application container and configuration management
- **Session**: Current authenticated entity information
- **Agent**: AI agent configuration and operations
- **Organization**: Organization structure and settings
- **OrgUser**: User-organization relationship management
- **AppBot**: Application-bot integration management
- **AgentGroup**: AI agent collection and coordination
- **Tool**: External integration and utility management
- **Client**: OAuth client application management
- **Model**: AI model configuration and operations

## Features

- **Data Management**: Automatic property mapping from data
- **CRUD Operations**: Save, delete, update operations
- **Configuration Management**: Integration with ConfigurationManager
- **Data Validation**: Type safety and validation
- **JSON Serialization**: Easy data conversion
- **API Payload Generation**: Clean API request payloads
- **Error Handling**: Comprehensive error handling
- **Type Safety**: Full type hints and validation
- **Async Support**: Native async/await support

## Installation

The models module is part of the main mosaia package:

```bash
pip install mosaia
```

## Usage

### Basic Imports

```python
from mosaia.models import (
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
```

### BaseModel

The `BaseModel` class provides the foundation for all models:

```python
from mosaia.models import BaseModel

class CustomModel(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or '/custom')
    
    # Add custom methods
    async def custom_operation(self):
        # Custom logic here
        pass
```

### User Model

The `User` class represents user accounts in the platform:

```python
from mosaia.models import User

# Create user profile
user = User({
    'username': 'jsmith',
    'name': 'John Smith',
    'email': 'john@example.com',
    'metadata': {
        'title': 'Senior Developer',
        'department': 'Engineering',
        'location': 'San Francisco'
    }
})

await user.save()

# Access user's resources
agents = await user.agents.get()
apps = await user.apps.get()
models = await user.models.get()

# Create new agent
agent = await user.agents.create({
    'name': 'Personal Assistant',
    'model': 'gpt-4',
    'temperature': 0.7,
    'system_prompt': 'You are a helpful assistant.'
})

# Create application
app = await user.apps.create({
    'name': 'Task Manager',
    'short_description': 'AI-powered task management'
})

# Check organization memberships
orgs = await user.orgs.get()
for org in orgs:
    print(f"{org['org']['name']}: {org['permission']}")
```

### Agent Model

The `Agent` class represents AI agents:

```python
from mosaia.models import Agent

# Create an agent instance
agent = Agent({
    'name': 'Customer Support Agent',
    'short_description': 'AI agent for customer inquiries',
    'model': 'gpt-4',
    'temperature': 0.7,
    'system_prompt': 'You are a helpful customer support agent.'
})

await agent.save()

# Upload an agent avatar
with open('agent-avatar.png', 'rb') as f:
    await agent.upload_image(f)

# Chat with the agent
response = await agent.chat.completions.create({
    'messages': [
        {'role': 'user', 'content': 'How can I reset my password?'}
    ],
    'temperature': 0.7,
    'max_tokens': 150
})

print('Agent response:', response['choices'][0]['message']['content'])
```

### Organization Model

The `Organization` class represents organizations:

```python
from mosaia.models import Organization

# Create organization
org = Organization({
    'name': 'Acme Corp',
    'short_description': 'Technology company',
    'metadata': {
        'industry': 'Technology',
        'size': '100-500',
        'location': 'San Francisco'
    }
})

await org.save()

# Add organization logo
with open('logo.png', 'rb') as f:
    await org.upload_logo(f)

# Access organization's resources
agents = await org.agents.get()
apps = await org.apps.get()
users = await org.users.get()

print('Organization Resources:')
print(f'- {len(agents)} AI agents')
print(f'- {len(apps)} applications')
print(f'- {len(users)} users')
```

### App Model

The `App` class represents application containers:

```python
from mosaia.models import App

# Create application
app = App({
    'name': 'Task Manager',
    'short_description': 'AI-powered task management',
    'metadata': {
        'category': 'Productivity',
        'version': '1.0.0'
    }
})

await app.save()
```

### Session Model

The `Session` class represents the current authenticated session:

```python
from mosaia.models import Session

# Get current session
session = Session({})

# Access session data
user_info = session.data.get('user')
if user_info:
    print(f"Logged in as: {user_info['name']}")
```

### OrgUser Model

The `OrgUser` class represents user-organization relationships:

```python
from mosaia.models import OrgUser

# Create org user relationship
org_user = OrgUser({
    'user_id': 'user-123',
    'org_id': 'org-456',
    'permission': 'admin',
    'role': 'member'
})

await org_user.save()
```

### AppBot Model

The `AppBot` class represents app-bot integrations:

```python
from mosaia.models import AppBot

# Create app bot integration
app_bot = AppBot({
    'app_id': 'app-123',
    'bot_id': 'bot-456',
    'config': {
        'enabled': True,
        'auto_reply': False
    }
})

await app_bot.save()
```

### AgentGroup Model

The `AgentGroup` class represents AI agent collections:

```python
from mosaia.models import AgentGroup

# Create agent group
group = AgentGroup({
    'name': 'Support Team',
    'description': 'Customer support agents',
    'agents': ['agent-1', 'agent-2', 'agent-3']
})

await group.save()
```

### Tool Model

The `Tool` class represents external integrations:

```python
from mosaia.models import Tool

# Create tool
tool = Tool({
    'name': 'Weather API',
    'type': 'api',
    'config': {
        'endpoint': 'https://api.weather.com',
        'api_key': 'your-api-key'
    }
})

await tool.save()
```

### Client Model

The `Client` class represents OAuth client applications:

```python
from mosaia.models import Client

# Create OAuth client
client = Client({
    'name': 'My App',
    'client_id': 'client-123',
    'redirect_uri': 'https://myapp.com/callback',
    'scopes': ['read', 'write']
})

await client.save()
```

### Model Class

The `Model` class represents AI model configurations:

```python
from mosaia.models import Model

# Create AI model
model = Model({
    'name': 'GPT-4',
    'type': 'openai',
    'config': {
        'model': 'gpt-4',
        'temperature': 0.7,
        'max_tokens': 1000
    }
})

await model.save()
```

## API Reference

### BaseModel

#### `__init__(data: Dict[str, Any], uri: Optional[str] = None)`

Initialize the BaseModel.

**Parameters:**
- `data`: Model data dictionary
- `uri`: Optional URI path for the model endpoint

#### `config: MosaiaConfig`

Get the current configuration from the ConfigurationManager.

#### `is_active() -> bool`

Check if the entity is active.

#### `to_json() -> Dict[str, Any]`

Convert model instance to interface data.

#### `to_api_payload() -> Dict[str, Any]`

Convert model instance to API payload.

#### `update(updates: Dict[str, Any]) -> None`

Update model data with new values.

#### `async save() -> Dict[str, Any]`

Save the model instance to the API.

#### `async delete() -> None`

Delete the model instance from the API.

#### `has_id() -> bool`

Check if the model has an ID.

#### `get_id() -> str`

Get the model's ID.

#### `get_uri() -> str`

Get the model's complete API URI.

### User

#### `agents`

Get the agents collection for this user.

#### `apps`

Get the apps collection for this user.

#### `clients`

Get the clients collection for this user.

#### `groups`

Get the agent groups collection for this user.

#### `models`

Get the models collection for this user.

#### `orgs`

Get the organization users collection for this user.

#### `tools`

Get the tools collection for this user.

#### `async upload_profile_image(file) -> User`

Upload a profile image for the user.

### Agent

#### `chat`

Get the chat instance for this agent.

#### `async upload_image(file) -> Agent`

Upload an image for the agent.

### Organization

#### `agents`

Get the agents collection for this organization.

#### `apps`

Get the apps collection for this organization.

#### `users`

Get the users collection for this organization.

#### `tools`

Get the tools collection for this organization.

#### `async upload_logo(file) -> Organization`

Upload a logo for the organization.

## Examples

### Basic Model Usage

```python
from mosaia.models import User, Agent, Organization

# Create model instances
user = User({
    'name': 'John Doe',
    'email': 'john@example.com'
})

agent = Agent({
    'name': 'Support Agent',
    'model': 'gpt-4'
})

organization = Organization({
    'name': 'Acme Corp',
    'short_description': 'Technology company'
})

# Save models
await user.save()
await agent.save()
await organization.save()

# Update models
user.update({'last_name': 'Smith'})
await user.save()

# Convert to JSON
user_data = user.to_json()
agent_data = agent.to_json()
org_data = organization.to_json()

# Check if active
if user.is_active():
    print('User is active')

# Delete models
await user.delete()
await agent.delete()
await organization.delete()
```

### Resource Management

```python
from mosaia.models import User, Organization

# User resource management
user = User({'name': 'Test User'})

# Access user's agents
agents = await user.agents.get()
for agent in agents:
    print(f"Agent: {agent['name']}")

# Create new agent
new_agent = await user.agents.create({
    'name': 'My Agent',
    'model': 'gpt-4',
    'temperature': 0.7
})

# Organization resource management
org = Organization({'name': 'Test Org'})

# Access organization's users
users = await org.users.get()
for user in users:
    print(f"User: {user['user']['name']}")
    print(f"Permission: {user['permission']}")
```

### Error Handling

```python
from mosaia.models import User

user = User({'name': 'Test User'})

try:
    await user.save()
    print('User saved successfully')
except Exception as error:
    print(f'Failed to save user: {error}')

try:
    await user.delete()
    print('User deleted successfully')
except Exception as error:
    print(f'Failed to delete user: {error}')
```

## Configuration

Models automatically use the current configuration:

```python
from mosaia import ConfigurationManager
from mosaia.models import User

# Initialize configuration
config_manager = ConfigurationManager.get_instance()
config_manager.initialize({
    'api_key': 'your-api-key',
    'api_url': 'https://api.mosaia.ai',
    'version': '1'
})

# Models will use the configured settings
user = User({'name': 'Test User'})
```

## Testing

Run the models tests:

```bash
# Run all models tests
python run_tests.py --category models

# Run with verbose output
python run_tests.py --category models --verbose

# Run with coverage
python run_tests.py --category models --coverage
```

## Best Practices

1. **Use Type Hints**: Always use type hints for better code clarity
2. **Error Handling**: Always wrap model operations in try-catch blocks
3. **Configuration**: Ensure configuration is properly initialized
4. **Async/Await**: Use async/await for all model operations
5. **Data Validation**: Validate data before creating models
6. **Resource Management**: Properly manage model resources and cleanup

## Contributing

When contributing to the models module:

1. Follow Python best practices and PEP 8 style guidelines
2. Add comprehensive docstrings for all functions and classes
3. Include examples in docstrings
4. Write tests for new functionality
5. Ensure backward compatibility
6. Update this README when adding new features

## License

This module is part of the Mosaia Python SDK and is licensed under the MIT License.
