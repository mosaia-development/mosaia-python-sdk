# Mosaia Python SDK - Utils Implementation

This document summarizes the implementation of the utils module for the Mosaia Python SDK, which provides parity with the Node.js SDK utils.

## Overview

The utils module has been successfully implemented with full parity to the Node.js SDK, providing Pythonic implementations of all utility functions and the API client.

## Implemented Components

### 1. Core Utility Functions (`mosaia/utils/helpers.py`)

#### Validation Functions
- **`is_valid_object_id(id_str: str) -> bool`**: Validates MongoDB ObjectID strings
  - Supports 24-character hexadecimal strings
  - Handles edge cases (empty strings, invalid characters, wrong lengths)
  - Returns `True` for valid ObjectIDs, `False` otherwise

#### Error Handling Functions
- **`parse_error(error: Any) -> Dict[str, Any]`**: Standardizes error objects
  - Converts any error object to consistent format
  - Handles custom error objects with attributes
  - Returns standardized error dictionary

- **`is_sdk_error(err: Any) -> bool`**: Type guard for SDK errors
  - Checks if error has required SDK error properties
  - Supports both dictionary and object formats

- **`server_error_to_string(err: Any) -> str`**: Converts server errors to readable strings
  - Handles errors with digest information
  - Returns formatted error messages

#### Query Generation
- **`query_generator(params: Optional[Dict[str, Any]] = None) -> str`**: Builds URL query strings
  - Supports simple key-value parameters
  - Handles array parameters with `[]` notation
  - Filters out `None` and empty values
  - Returns properly formatted query strings

#### Timestamp Validation
- **`is_timestamp_expired(timestamp: Union[str, int, float]) -> bool`**: Checks timestamp expiration
  - Supports string, int, and float timestamps
  - Handles invalid timestamps gracefully
  - Compares against current time in milliseconds

#### Response Helpers
- **`failure(error: str) -> FailureResponse`**: Creates standardized failure responses
  - Returns `FailureResponse` dataclass with `None` data and error message

- **`success(data: Any = None) -> SuccessResponse`**: Creates standardized success responses
  - Returns `SuccessResponse` dataclass with data and `None` error

### 2. API Client (`mosaia/utils/api_client.py`)

#### Features
- **Async/await support**: Full async HTTP client using `aiohttp`
- **Authentication handling**: Automatic token management and refresh
- **Request/response standardization**: Consistent error handling and response processing
- **Query parameter building**: Automatic query string generation
- **Content type management**: JSON serialization/deserialization
- **Logging support**: Verbose mode for debugging
- **Context manager support**: Async context manager for resource management

#### Methods
- **`get(path: str, params: Optional[Dict[str, Any]] = None) -> Any`**: GET requests
- **`post(path: str, data: Optional[Dict[str, Any]] = None) -> Any`**: POST requests
- **`put(path: str, data: Optional[Dict[str, Any]] = None) -> Any`**: PUT requests
- **`delete(path: str, params: Optional[Dict[str, Any]] = None) -> Any`**: DELETE requests
- **`close() -> None`**: Close the HTTP session

### 3. Supporting Modules

#### Types (`mosaia/types.py`)
- **`MosaiaConfig`**: Configuration dataclass
- **`SessionInterface`**: Session data structure
- **`APIResponse`**: Standard API response format
- **`ErrorResponse`**: Error response format
- **`UserInterface`**, **`OrganizationInterface`**, etc.: Entity interfaces
- **`AuthType`**, **`GrantType`**: Enum types

#### Configuration (`mosaia/config.py`)
- **`ConfigurationManager`**: Singleton configuration manager
- **`DEFAULT_CONFIG`**: Default configuration values
- Environment variable support
- Configuration initialization and management

#### Base API (`mosaia/base_api.py`)
- **`BaseAPI`**: Abstract base class for API operations
- Generic type support
- Common HTTP method implementations

## Key Features

### Pythonic Design
- **Type hints**: Full type annotations for all functions and classes
- **Dataclasses**: Modern Python dataclasses for data structures
- **Async/await**: Native async support with `aiohttp`
- **Context managers**: Resource management with async context managers
- **Docstrings**: Comprehensive documentation with examples

### Error Handling
- **Graceful degradation**: Fallback implementations when dependencies are missing
- **Standardized errors**: Consistent error format across the SDK
- **Type safety**: Type guards and validation

### Testing
- **Comprehensive tests**: Full test suite in `test_utils.py`
- **Edge cases**: Tests for invalid inputs and error conditions
- **Examples**: Docstring examples for all functions

## Usage Examples

### Basic Utils
```python
from mosaia.utils import (
    is_valid_object_id,
    parse_error,
    query_generator,
    is_timestamp_expired,
    failure,
    success
)

# ObjectID validation
is_valid = is_valid_object_id('507f1f77bcf86cd799439011')

# Query generation
query = query_generator({
    'limit': 10,
    'search': 'john',
    'tags': ['ai', 'automation']
})

# Error handling
try:
    # Some operation
    pass
except Exception as error:
    standardized_error = parse_error(error)
```

### API Client
```python
from mosaia.utils import APIClient

async with APIClient() as client:
    # GET request
    users = await client.get('/user', {'limit': 10})
    
    # POST request
    new_user = await client.post('/user', {
        'name': 'John Doe',
        'email': 'john@example.com'
    })
    
    # PUT request
    updated_user = await client.put('/user/123', {
        'name': 'John Smith'
    })
    
    # DELETE request
    await client.delete('/user/123')
```

## Parity with Node.js SDK

### Function Mappings
| Node.js Function | Python Function | Status |
|------------------|-----------------|--------|
| `isValidObjectId` | `is_valid_object_id` | ✅ Complete |
| `parseError` | `parse_error` | ✅ Complete |
| `queryGenerator` | `query_generator` | ✅ Complete |
| `isTimestampExpired` | `is_timestamp_expired` | ✅ Complete |
| `failure` | `failure` | ✅ Complete |
| `success` | `success` | ✅ Complete |
| `serverErrorToString` | `server_error_to_string` | ✅ Complete |
| `isSdkError` | `is_sdk_error` | ✅ Complete |
| `APIClient` | `APIClient` | ✅ Complete |

### Key Differences
1. **Async/await**: Python version uses native async/await instead of Promises
2. **Type hints**: Python version includes comprehensive type annotations
3. **Dataclasses**: Python version uses dataclasses for data structures
4. **Context managers**: Python version supports async context managers
5. **Error handling**: Python version uses exceptions instead of Promise rejections

## Testing

The implementation includes comprehensive tests in `test_utils.py`:

```bash
python test_utils.py
```

All tests pass successfully, covering:
- ObjectID validation
- Error parsing and handling
- Query string generation
- Timestamp validation
- Response helpers
- Server error handling
- SDK error detection

## Documentation

- **Module README**: `mosaia/utils/README.md` with comprehensive documentation
- **Docstrings**: All functions and classes have detailed docstrings with examples
- **Type hints**: Full type annotations for IDE support

## Future Enhancements

1. **Caching**: Add request caching for improved performance
2. **Retry logic**: Implement automatic retry for failed requests
3. **Rate limiting**: Add rate limiting support
4. **WebSocket support**: Add WebSocket client for real-time communication
5. **Streaming**: Add streaming response support
6. **Middleware**: Add middleware support for request/response processing

## Conclusion

The utils module has been successfully implemented with full parity to the Node.js SDK, providing a robust foundation for the Mosaia Python SDK. The implementation follows Python best practices, includes comprehensive testing, and maintains backward compatibility while adding modern Python features like async/await support and type hints.
