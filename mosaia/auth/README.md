# Mosaia Python SDK - Auth Module

This module provides authentication functionality for the Mosaia Python SDK, including password-based authentication, client credentials authentication, OAuth2 flows, and token management.

## Overview

The auth module provides comprehensive authentication functionality with:
- **MosaiaAuth**: Main authentication class for password and client credentials
- **OAuth**: OAuth2 Authorization Code flow with PKCE support
- **Token Management**: Automatic token refresh and session handling
- **Multiple Auth Flows**: Support for various authentication methods

## Features

- **Password Authentication**: Email/password-based authentication
- **Client Credentials**: Server-to-server authentication
- **OAuth2 Support**: Full OAuth2 Authorization Code flow with PKCE
- **Token Refresh**: Automatic token refresh and session management
- **Session Handling**: Secure session storage and management
- **Error Handling**: Comprehensive error handling and validation
- **Type Safety**: Full type hints and validation
- **Async Support**: Native async/await support

## Installation

The auth module is part of the main mosaia package:

```bash
pip install mosaia
```

## Usage

### Basic Imports

```python
from mosaia.auth import (
    MosaiaAuth,
    OAuth
)
```

### MosaiaAuth

The `MosaiaAuth` class provides the main authentication functionality:

```python
from mosaia.auth import MosaiaAuth

# Create auth instance
auth = MosaiaAuth()

# Sign in with password
try:
    config = await auth.sign_in_with_password('user@example.com', 'password')
    print('Successfully authenticated')
except Exception as error:
    print(f'Authentication failed: {error}')

# Sign in with client credentials
try:
    config = await auth.sign_in_with_client('client-id', 'client-secret')
    print('Successfully authenticated with client credentials')
except Exception as error:
    print(f'Client authentication failed: {error}')

# Refresh token
try:
    new_config = await auth.refresh_token()
    print('Token refreshed successfully')
except Exception as error:
    print(f'Token refresh failed: {error}')

# Sign out
try:
    await auth.sign_out()
    print('Successfully signed out')
except Exception as error:
    print(f'Sign out failed: {error}')
```

### OAuth

The `OAuth` class provides OAuth2 Authorization Code flow with PKCE:

```python
from mosaia.auth import OAuth

# Initialize OAuth client
oauth = OAuth({
    'client_id': 'your-client-id',
    'redirect_uri': 'https://your-app.com/callback',
    'scopes': ['read', 'write'],
    'app_url': 'https://mosaia.ai',
    'api_url': 'https://api.mosaia.ai',
    'api_version': '1'
})

# Step 1: Get authorization URL and code verifier
auth_data = oauth.get_authorization_url_and_code_verifier()
url = auth_data['url']
code_verifier = auth_data['code_verifier']

# Store code verifier securely (e.g., session storage)
session_storage.set_item('code_verifier', code_verifier)

# Step 2: Redirect user to authorization URL
# window.location.href = url

# Step 3: Handle OAuth callback
code = url_params.get('code')
stored_verifier = session_storage.get_item('code_verifier')

if code and stored_verifier:
    try:
        config = await oauth.authenticate_with_code_and_verifier(code, stored_verifier)
        print('OAuth authentication successful')
    except Exception as error:
        print(f'OAuth authentication failed: {error}')
```

## API Reference

### MosaiaAuth

#### `__init__(config: Optional[MosaiaConfig] = None)`

Create a new Authentication API client instance.

**Parameters:**
- `config`: Optional configuration object

#### `async sign_in_with_password(email: str, password: str) -> MosaiaConfig`

Sign in using email and password authentication.

**Parameters:**
- `email`: The user's email address
- `password`: The user's password

**Returns:**
- Configured MosaiaConfig

#### `async sign_in_with_client(client_id: str, client_secret: str) -> MosaiaConfig`

Sign in using client credentials authentication.

**Parameters:**
- `client_id`: The OAuth client ID
- `client_secret`: The OAuth client secret

**Returns:**
- Configured MosaiaConfig

#### `async refresh_token(token: Optional[str] = None) -> MosaiaConfig`

Refresh an access token using a refresh token.

**Parameters:**
- `token`: Optional refresh token

**Returns:**
- Updated MosaiaConfig

#### `async refresh_oauth_token(refresh_token: str) -> MosaiaConfig`

Refresh an OAuth access token using a refresh token.

**Parameters:**
- `refresh_token`: The refresh token

**Returns:**
- New OAuth token response

#### `async sign_out(api_key: Optional[str] = None) -> None`

Sign out and invalidate the current session.

**Parameters:**
- `api_key`: Optional API key to sign out

#### `async refresh() -> MosaiaConfig`

Refresh the current session using the appropriate method.

**Returns:**
- Updated MosaiaConfig

### OAuth

#### `__init__(config: Optional[Dict[str, Any]] = None)`

Create a new OAuth instance.

**Parameters:**
- `config`: OAuth configuration object

#### `_generate_pkce() -> Dict[str, str]`

Generate PKCE code verifier and challenge.

**Returns:**
- Object containing code_verifier and code_challenge

#### `get_authorization_url_and_code_verifier() -> Dict[str, str]`

Generate authorization URL and PKCE code verifier.

**Returns:**
- Object containing url and code_verifier

#### `async authenticate_with_code_and_verifier(code: str, code_verifier: str) -> MosaiaConfig`

Exchange authorization code for access and refresh tokens.

**Parameters:**
- `code`: Authorization code from OAuth callback
- `code_verifier`: PKCE code verifier

**Returns:**
- Complete MosaiaConfig

## Examples

### Password Authentication

```python
from mosaia.auth import MosaiaAuth

auth = MosaiaAuth()

# Sign in with email and password
try:
    config = await auth.sign_in_with_password('john@example.com', 'password123')
    print(f'Access token: {config.api_key}')
    print(f'User ID: {config.session.sub}')
except Exception as error:
    print(f'Authentication failed: {error}')
```

### Client Credentials Authentication

```python
from mosaia.auth import MosaiaAuth

auth = MosaiaAuth()

# Sign in with client credentials
try:
    config = await auth.sign_in_with_client('client-id', 'client-secret')
    print(f'Access token: {config.api_key}')
    print(f'Token expires: {config.session.exp}')
except Exception as error:
    print(f'Client authentication failed: {error}')
```

### OAuth2 Flow

```python
from mosaia.auth import OAuth

# Initialize OAuth
oauth = OAuth({
    'client_id': 'your-client-id',
    'redirect_uri': 'https://your-app.com/callback',
    'scopes': ['read', 'write'],
    'app_url': 'https://mosaia.ai',
    'api_url': 'https://api.mosaia.ai',
    'api_version': '1'
})

# Get authorization URL
auth_data = oauth.get_authorization_url_and_code_verifier()
print(f'Authorization URL: {auth_data["url"]}')
print(f'Code verifier: {auth_data["code_verifier"]}')

# Handle callback (in your callback route)
code = request.args.get('code')
verifier = session.get('code_verifier')

if code and verifier:
    try:
        config = await oauth.authenticate_with_code_and_verifier(code, verifier)
        print('OAuth authentication successful')
        # Use config with SDK
    except Exception as error:
        print(f'OAuth authentication failed: {error}')
```

### Token Refresh

```python
from mosaia.auth import MosaiaAuth

auth = MosaiaAuth()

# Refresh token when needed
try:
    new_config = await auth.refresh_token()
    print('Token refreshed successfully')
    print(f'New access token: {new_config.api_key}')
except Exception as error:
    print(f'Token refresh failed: {error}')
    # User needs to re-authenticate
```

### Session Management

```python
from mosaia.auth import MosaiaAuth

auth = MosaiaAuth()

# Check if session is valid
if auth.config.session:
    print(f'Session type: {auth.config.session.auth_type}')
    print(f'Token expires: {auth.config.session.exp}')
    
    # Refresh if needed
    if auth.config.session.exp < time.time():
        try:
            new_config = await auth.refresh()
            print('Session refreshed')
        except Exception as error:
            print(f'Session refresh failed: {error}')
```

## Error Handling

All authentication methods provide comprehensive error handling:

```python
from mosaia.auth import MosaiaAuth

auth = MosaiaAuth()

try:
    config = await auth.sign_in_with_password('user@example.com', 'password')
except Exception as error:
    if 'Invalid credentials' in str(error):
        print('Invalid email or password')
    elif 'User not found' in str(error):
        print('User does not exist')
    elif 'Account locked' in str(error):
        print('Account is locked')
    else:
        print(f'Authentication error: {error}')
```

## Configuration

Authentication classes automatically use the current configuration:

```python
from mosaia import ConfigurationManager
from mosaia.auth import MosaiaAuth

# Initialize configuration
config_manager = ConfigurationManager.get_instance()
config_manager.initialize({
    'api_key': 'your-api-key',
    'api_url': 'https://api.mosaia.ai',
    'version': '1',
    'client_id': 'your-client-id'
})

# Auth will use the configured settings
auth = MosaiaAuth()
```

## Security Best Practices

1. **Secure Storage**: Store tokens securely (e.g., encrypted storage)
2. **Token Refresh**: Implement automatic token refresh
3. **Error Handling**: Handle authentication errors gracefully
4. **Session Management**: Clear sessions on logout
5. **PKCE**: Use PKCE for OAuth flows (implemented by default)
6. **State Parameter**: Use state parameter for CSRF protection

## Testing

Run the auth tests:

```bash
# Run all auth tests
python run_tests.py --category auth

# Run with verbose output
python run_tests.py --category auth --verbose

# Run with coverage
python run_tests.py --category auth --coverage
```

## Best Practices

1. **Use Type Hints**: Always use type hints for better code clarity
2. **Error Handling**: Always wrap authentication calls in try-catch blocks
3. **Configuration**: Ensure configuration is properly initialized
4. **Async/Await**: Use async/await for all authentication calls
5. **Token Management**: Implement proper token refresh logic
6. **Security**: Follow security best practices for token storage

## Contributing

When contributing to the auth module:

1. Follow Python best practices and PEP 8 style guidelines
2. Add comprehensive docstrings for all functions and classes
3. Include examples in docstrings
4. Write tests for new functionality
5. Ensure backward compatibility
6. Update this README when adding new features

## License

This module is part of the Mosaia Python SDK and is licensed under the MIT License.
