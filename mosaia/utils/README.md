# Mosaia Python SDK - Utils Module

This module provides utility functions for the Mosaia Python SDK, offering common functionality used throughout the SDK for validation, error handling, query generation, and other common tasks.

## Features

- **ObjectID Validation**: Validate MongoDB ObjectID strings
- **Error Handling**: Standardize error objects and responses
- **Query Generation**: Build URL query strings from parameters
- **Timestamp Validation**: Check if timestamps are expired
- **Response Helpers**: Create standardized success/failure responses
- **API Client**: Async HTTP client for API communication

## Installation

The utils module is part of the main mosaia package:

```bash
pip install mosaia
```

## Usage

### Basic Imports

```python
from mosaia.utils import (
    is_valid_object_id,
    parse_error,
    query_generator,
    is_timestamp_expired,
    failure,
    success,
    server_error_to_string,
    is_sdk_error,
    APIClient
)
```

### ObjectID Validation

```python
from mosaia.utils import is_valid_object_id

# Valid ObjectIDs
is_valid_object_id('507f1f77bcf86cd799439011')  # True
is_valid_object_id('507f1f77bcf86cd799439012')  # True

# Invalid ObjectIDs
is_valid_object_id('invalid-id')  # False
is_valid_object_id('123')  # False
is_valid_object_id('507f1f77bcf86cd79943901')  # False (23 chars)
is_valid_object_id('507f1f77bcf86cd7994390111')  # False (25 chars)
```

### Error Handling

```python
from mosaia.utils import parse_error, is_sdk_error

# Parse any error object
try:
    # Some operation that might fail
    raise ValueError("Test error")
except Exception as error:
    standardized_error = parse_error(error)
    print(standardized_error['message'])  # "Test error"
    print(standardized_error['status_code'])  # 400
    print(standardized_error['status'])  # "UNKNOWN"

# Check if error is an SDK error
sdk_error = {
    'message': 'API error',
    'code': 'API_ERROR',
    'status': 400
}
is_sdk_error(sdk_error)  # True
```

### Query Generation

```python
from mosaia.utils import query_generator

# Basic parameters
params = {
    'limit': 10,
    'offset': 0,
    'search': 'john',
    'active': True
}
query = query_generator(params)
# Result: "?limit=10&offset=0&search=john&active=True"

# Array parameters
params = {
    'tags': ['ai', 'automation', 'support'],
    'categories': ['featured', 'popular']
}
query = query_generator(params)
# Result: "?tags[]=ai&tags[]=automation&tags[]=support&categories[]=featured&categories[]=popular"

# Complex filtering
filter_params = {
    'user': 'user-123',
    'org': 'org-456',
    'status': ['active', 'pending'],
    'created_after': '2024-01-01',
    'sort_by': 'created_at',
    'sort_order': 'desc',
    'include_metadata': True
}
query = query_generator(filter_params)
# Result: "?user=user-123&org=org-456&status[]=active&status[]=pending&created_after=2024-01-01&sort_by=created_at&sort_order=desc&include_metadata=True"
```

### Timestamp Validation

```python
from mosaia.utils import is_timestamp_expired
import time

# Future timestamp (not expired)
future_timestamp = str(int(time.time() * 1000) + 3600000)  # 1 hour from now
is_timestamp_expired(future_timestamp)  # False

# Past timestamp (expired)
past_timestamp = str(int(time.time() * 1000) - 3600000)  # 1 hour ago
is_timestamp_expired(past_timestamp)  # True

# Invalid timestamps
is_timestamp_expired('')  # False
is_timestamp_expired('invalid')  # False
is_timestamp_expired(None)  # False
```

### Response Helpers

```python
from mosaia.utils import failure, success

# Create failure response
result = failure('User not found')
# Result: FailureResponse(data=None, error='User not found')

# Create success response
data = {'id': '123', 'name': 'John'}
result = success(data)
# Result: SuccessResponse(data={'id': '123', 'name': 'John'}, error=None)
```

### Server Error Handling

```python
from mosaia.utils import server_error_to_string

# Regular error
error = Exception("Database connection failed")
result = server_error_to_string(error)
# Result: "Database connection failed"

# Error with digest
class DigestError:
    def __init__(self):
        self.message = "Test error"
        self.digest = "abc123"

error = DigestError()
result = server_error_to_string(error)
# Result: "Unexpected Error (digest: abc123)"
```

### API Client

```python
from mosaia.utils import APIClient

# Basic usage
async with APIClient() as client:
    # GET request
    users = await client.get('/user')
    
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
    
    # With query parameters
    filtered_users = await client.get('/user', {
        'limit': 10,
        'offset': 0,
        'search': 'john',
        'active': True
    })

# Manual usage
client = APIClient()
try:
    users = await client.get('/user')
finally:
    await client.close()
```

## API Reference

### Functions

#### `is_valid_object_id(id_str: str) -> bool`

Validates if a string is a valid MongoDB ObjectID.

**Parameters:**
- `id_str`: The string to validate as an ObjectID

**Returns:**
- `bool`: True if the string is a valid ObjectID, False otherwise

#### `parse_error(error: Any) -> Dict[str, Any]`

Parses and standardizes error objects.

**Parameters:**
- `error`: Any error object to parse and standardize

**Returns:**
- `Dict[str, Any]`: Standardized error object with consistent structure

#### `query_generator(params: Optional[Dict[str, Any]] = None) -> str`

Generates a URL query string from an object of parameters.

**Parameters:**
- `params`: Object containing query parameters (optional)

**Returns:**
- `str`: URL query string

#### `is_timestamp_expired(timestamp: Union[str, int, float]) -> bool`

Validates if a timestamp string is expired.

**Parameters:**
- `timestamp`: The timestamp to validate (can be string, int, or float)

**Returns:**
- `bool`: True if the timestamp is in the past (expired), False otherwise

#### `failure(error: str) -> FailureResponse`

Creates a standardized failure response.

**Parameters:**
- `error`: Error message describing the failure

**Returns:**
- `FailureResponse`: Object with None data and the error message

#### `success(data: Any = None) -> SuccessResponse`

Creates a standardized success response.

**Parameters:**
- `data`: The data to include in the success response

**Returns:**
- `SuccessResponse`: Object with the data and None error

#### `server_error_to_string(err: Any) -> str`

Converts server errors to readable string format.

**Parameters:**
- `err`: Server error object

**Returns:**
- `str`: Formatted error string

#### `is_sdk_error(err: Any) -> bool`

Type guard to check if an error is an SDK error.

**Parameters:**
- `err`: Any error object to check

**Returns:**
- `bool`: True if the error is an SDK error, False otherwise

### Classes

#### `APIClient`

Internal API client for making HTTP requests to the Mosaia API.

**Methods:**
- `get(path: str, params: Optional[Dict[str, Any]] = None) -> Union[APIResponse[T], T]`
- `post(path: str, data: Optional[Dict[str, Any]] = None) -> Union[APIResponse[T], T]`
- `put(path: str, data: Optional[Dict[str, Any]] = None) -> Union[APIResponse[T], T]`
- `delete(path: str, params: Optional[Dict[str, Any]] = None) -> Union[APIResponse[T], T]`
- `close() -> None`

## Testing

Run the utils tests:

```bash
python test_utils.py
```

## Contributing

When contributing to the utils module:

1. Follow Python best practices and PEP 8 style guidelines
2. Add comprehensive docstrings for all functions and classes
3. Include examples in docstrings
4. Write tests for new functionality
5. Ensure backward compatibility
6. Update this README when adding new features

## License

This module is part of the Mosaia Python SDK and is licensed under the MIT License.
