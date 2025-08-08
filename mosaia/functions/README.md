# Mosaia Python SDK - Functions Module

This module provides function classes for managing API operations including base functions, chat operations, and completions.

## Overview

The functions module provides a structured approach to API operations with:
- **BaseFunctions**: Abstract base class for common CRUD operations
- **Chat**: Chat-specific functionality with completions access
- **Completions**: AI model completion operations

## Features

- **Standardized CRUD Operations**: Common get, create, update, delete methods
- **Type Safety**: Full type hints and generic support
- **Error Handling**: Consistent error handling across all functions
- **Async Support**: Native async/await support
- **Configuration Management**: Automatic configuration handling
- **Chat Integration**: Seamless chat and completions integration

## Installation

The functions module is part of the main mosaia package:

```bash
pip install mosaia
```

## Usage

### Basic Imports

```python
from mosaia.functions import (
    BaseFunctions,
    Chat,
    Completions
)
```

### BaseFunctions

The `BaseFunctions` class provides the foundation for all API operations:

```python
from mosaia.functions import BaseFunctions

class Users(BaseFunctions):
    def __init__(self):
        super().__init__('/user')

# Create instance
users = Users()

# Get all users
all_users = await users.get()

# Get specific user
user = await users.get({}, 'user-id')

# Create new user
new_user = await users.create({
    'email': 'john@example.com',
    'first_name': 'John',
    'last_name': 'Doe'
})

# Update user
updated_user = await users.update('user-id', {
    'email': 'newemail@example.com'
})

# Delete user
await users.delete('user-id')
```

### Chat Functions

The `Chat` class provides chat-specific functionality:

```python
from mosaia.functions import Chat

# Create chat instance
chat = Chat('/agent/123')

# Access completions
completions = chat.completions

# Create chat completion
response = await completions.create({
    'messages': [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'Hello, how are you?'}
    ],
    'max_tokens': 150,
    'temperature': 0.7,
    'stream': False
})

print('AI Response:', response['choices'][0]['message']['content'])
```

### Completions

The `Completions` class handles AI model completions:

```python
from mosaia.functions import Completions

# Create completions instance
completions = Completions('/agent/123/chat')

# Create completion
response = await completions.create({
    'messages': [
        {'role': 'user', 'content': 'What is the weather like?'}
    ],
    'max_tokens': 100,
    'temperature': 0.7
})
```

## API Reference

### BaseFunctions

#### `__init__(uri: Optional[str] = None)`

Initialize the BaseFunctions.

**Parameters:**
- `uri`: Optional base URI for the API endpoint

#### `config: MosaiaConfig`

Property that returns the current configuration.

#### `async get(params: Optional[Dict[str, Any]] = None, id: Optional[str] = None) -> GetPayload`

Get entities with optional filtering and pagination.

**Parameters:**
- `params`: Optional query parameters for filtering and pagination
- `id`: Optional specific entity ID to retrieve

**Returns:**
- Entity data

#### `async create(entity: T, params: Optional[Dict[str, Any]] = None) -> CreatePayload`

Create a new entity.

**Parameters:**
- `entity`: Entity data for the new entity
- `params`: Optional query parameters

**Returns:**
- The created entity

#### `async update(id: str, entity: Dict[str, Any], params: Optional[Dict[str, Any]] = None) -> CreatePayload`

Update an existing entity.

**Parameters:**
- `id`: The entity ID to update
- `entity`: Entity data for the update
- `params`: Optional query parameters

**Returns:**
- The updated entity

#### `async delete(id: str, params: Optional[Dict[str, Any]] = None) -> None`

Delete an entity.

**Parameters:**
- `id`: The entity ID to delete
- `params`: Optional query parameters

### Chat

#### `__init__(uri: str = "")`

Create a new Chat instance.

**Parameters:**
- `uri`: Base URI for the chat endpoint

#### `completions: Completions`

Property that returns a Completions instance.

### Completions

#### `__init__(uri: str = "")`

Create a new Completions instance.

**Parameters:**
- `uri`: Base URI for the completions endpoint

## Examples

### User Management

```python
from mosaia.functions import BaseFunctions

class Users(BaseFunctions):
    def __init__(self):
        super().__init__('/user')

users = Users()

# Get all users with filtering
filtered_users = await users.get({
    'limit': 10,
    'offset': 0,
    'q': 'john',
    'active': True
})

# Create user with external ID
new_user = await users.create({
    'email': 'john@example.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'external_id': 'user-123',
    'extensors': {
        'department': 'Engineering'
    }
})

# Update user
updated_user = await users.update('user-id', {
    'email': 'john.doe@example.com',
    'active': False
})

# Force delete user
await users.delete('user-id', {'force': True})
```

### Agent Chat

```python
from mosaia.functions import Chat

# Agent chat
agent_chat = Chat('/agent/agent-123')
completions = agent_chat.completions

# Simple chat completion
response = await completions.create({
    'messages': [
        {'role': 'user', 'content': 'What is the capital of France?'}
    ],
    'max_tokens': 50,
    'temperature': 0.7
})

print(response['choices'][0]['message']['content'])
```

### Model Chat

```python
from mosaia.functions import Chat

# Model chat
model_chat = Chat('/model/gpt-4')
completions = model_chat.completions

# Complex chat completion
response = await completions.create({
    'messages': [
        {'role': 'system', 'content': 'You are a helpful AI assistant.'},
        {'role': 'user', 'content': 'Explain quantum computing in simple terms.'}
    ],
    'max_tokens': 200,
    'temperature': 0.3,
    'stream': False
})
```

### Agent Group Chat

```python
from mosaia.functions import Chat

# Agent group chat
group_chat = Chat('/agent-group/group-123')
completions = group_chat.completions

# Group chat completion
response = await completions.create({
    'messages': [
        {'role': 'user', 'content': 'Help me with my project.'}
    ],
    'max_tokens': 150,
    'temperature': 0.5
})
```

## Error Handling

All functions provide consistent error handling:

```python
from mosaia.functions import BaseFunctions

class Users(BaseFunctions):
    def __init__(self):
        super().__init__('/user')

users = Users()

try:
    user = await users.get({}, 'non-existent-id')
except Exception as error:
    print(f"Error: {error}")
    # Error: User not found
```

## Type Safety

The functions module provides full type safety:

```python
from typing import Dict, Any
from mosaia.functions import BaseFunctions

class Users(BaseFunctions[Dict[str, Any], Dict[str, Any], Dict[str, Any]]):
    def __init__(self):
        super().__init__('/user')

# Type-safe operations
users = Users()
user_data: Dict[str, Any] = await users.get()
```

## Configuration

Functions automatically use the current configuration:

```python
from mosaia import ConfigurationManager
from mosaia.functions import BaseFunctions

# Initialize configuration
config_manager = ConfigurationManager.get_instance()
config_manager.initialize({
    'api_key': 'your-api-key',
    'api_url': 'https://api.mosaia.ai',
    'version': '1'
})

# Functions will use the configured settings
class Users(BaseFunctions):
    def __init__(self):
        super().__init__('/user')

users = Users()
# Automatically uses the configured API key and URL
```

## Testing

Run the functions tests:

```bash
# Run all functions tests
python run_tests.py --category functions

# Run with verbose output
python run_tests.py --category functions --verbose

# Run with coverage
python run_tests.py --category functions --coverage
```

## Best Practices

1. **Use Type Hints**: Always use type hints for better code clarity
2. **Error Handling**: Always wrap function calls in try-catch blocks
3. **Configuration**: Ensure configuration is properly initialized
4. **Async/Await**: Use async/await for all function calls
5. **Resource Management**: Use context managers when available

## Contributing

When contributing to the functions module:

1. Follow Python best practices and PEP 8 style guidelines
2. Add comprehensive docstrings for all functions and classes
3. Include examples in docstrings
4. Write tests for new functionality
5. Ensure backward compatibility
6. Update this README when adding new features

## License

This module is part of the Mosaia Python SDK and is licensed under the MIT License.
