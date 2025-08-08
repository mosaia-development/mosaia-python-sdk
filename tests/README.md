# Mosaia Python SDK Test Suite

This directory contains comprehensive test cases for the Mosaia Python SDK, covering configuration management, type definitions, and the main SDK class.

## Test Files

### 1. `test_config.py` - Configuration Manager Tests
Tests for the `ConfigurationManager` class and `DEFAULT_CONFIG` object.

**Coverage:**
- ✅ DEFAULT_CONFIG validation
- ✅ ConfigurationManager singleton pattern
- ✅ Configuration initialization with defaults and custom values
- ✅ Configuration getters and setters
- ✅ Configuration updates and validation
- ✅ Error handling for uninitialized configuration
- ✅ Edge cases (empty values, null/undefined, special characters)

**Key Test Scenarios:**
- Singleton instance management
- Configuration initialization with various input types
- Configuration updates and validation
- API URL generation with versioning
- Read-only configuration access
- Configuration reset functionality

### 2. `test_types.py` - Type Definition Tests
Tests for all Python dataclasses and types defined in the SDK.

**Coverage:**
- ✅ MosaiaConfig dataclass validation
- ✅ AuthType and GrantType enums
- ✅ APIResponse and ErrorResponse structures
- ✅ Pagination and query parameter interfaces
- ✅ Base entity and record history interfaces
- ✅ All entity interfaces (User, Organization, App, Tool, Agent, etc.)
- ✅ Chat completion interfaces
- ✅ OAuth configuration and response interfaces
- ✅ Complex nested interface structures
- ✅ Type compatibility between related interfaces

**Key Test Scenarios:**
- Dataclass property validation
- Optional vs required property handling
- Complex nested object structures
- Type inheritance and extension
- Enum values and validation
- Generic type usage

### 3. `test_client.py` - Main SDK Class Tests
Tests for the main `MosaiaClient` class and its methods.

**Coverage:**
- ✅ Constructor initialization
- ✅ Configuration getters and setters
- ✅ API client instantiation
- ✅ OAuth instance creation
- ✅ Error handling and validation
- ✅ Integration with ConfigurationManager
- ✅ Mock API client interactions
- ✅ Edge cases and error scenarios

**Key Test Scenarios:**
- SDK initialization with various configurations
- Configuration updates through setters
- API client method calls and responses
- OAuth configuration validation
- Error handling for missing configuration
- Integration testing with mocked dependencies

### 4. `test_collections.py` - Collection Classes Tests
Tests for all collection classes (Agents, Apps, Users, etc.).

**Coverage:**
- ✅ BaseCollection abstract class
- ✅ All collection class initializations
- ✅ URI and model class assignments
- ✅ API method calls and responses
- ✅ Error handling and validation
- ✅ Mock interactions and responses

**Key Test Scenarios:**
- Collection class initialization
- URI construction and validation
- Model class assignments
- API method interactions
- Error handling scenarios
- Mock response processing

## Test Setup

### Prerequisites
- Python 3.8+
- pip
- pytest
- pytest-asyncio
- pytest-cov

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install pytest pytest-asyncio pytest-cov
```

### Running Tests

#### Run All Tests
```bash
# Using pytest directly
pytest

# Using the test runner
python tests/run_tests.py
```

#### Run Tests with Coverage
```bash
# Using pytest with coverage
pytest --cov=mosaia --cov-report=html --cov-report=term

# Using the test runner
python tests/run_tests.py --coverage
```

#### Run Tests in Watch Mode
```bash
# Using pytest-watch (if installed)
ptw

# Using pytest with watch
pytest --watch
```

#### Run Specific Test File
```bash
# Run only configuration tests
pytest tests/test_config.py

# Run only type tests
pytest tests/test_types.py

# Run only client tests
pytest tests/test_client.py

# Run only collection tests
pytest tests/test_collections.py

# Using the test runner
python tests/run_tests.py --config
python tests/run_tests.py --types
python tests/run_tests.py --client
python tests/run_tests.py --collections
```

#### Run Tests with Verbose Output
```bash
pytest -v

# Using the test runner
python tests/run_tests.py --verbose
```

## Test Configuration

### Pytest Configuration
The tests use pytest with async support. Configuration is in `pytest.ini`:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --tb=short
    --strict-markers
    --disable-warnings
markers =
    asyncio: marks tests as async
    slow: marks tests as slow
    integration: marks tests as integration tests
```

### Test Setup
The `conftest.py` file configures the test environment:

- Provides common test fixtures
- Sets up async event loop
- Configures mock objects
- Provides test data utilities

## Test Utilities

### Global Test Utilities
The conftest file provides global utilities:

```python
# Create mock configuration
config = test_config()

# Create mock API response
response = {'data': {'id': 'test-123'}, 'paging': {'total': 1}}

# Create mock error response
error = {'error': {'message': 'Test error', 'code': 'TEST_ERROR'}}

# Reset ConfigurationManager singleton
config_manager.reset()
```

## Mocking Strategy

### Dependencies Mocked
- `APIClient` - Mocked for HTTP request testing
- `ConfigurationManager` - Mocked for configuration testing
- `OAuth` class - Mocked for OAuth flow testing
- `Session` model - Mocked for model instantiation testing

### Mock Examples
```python
# Mock APIClient
with patch('mosaia.client.APIClient') as mock_api_client:
    mock_client_instance = AsyncMock()
    mock_api_client.return_value = mock_client_instance
    
    # Test code here
    result = await client.session()

# Mock ConfigurationManager
with patch('mosaia.client.ConfigurationManager') as mock_config_manager:
    mock_instance = Mock()
    mock_config_manager.get_instance.return_value = mock_instance
    
    # Test code here
    client = MosaiaClient(config)
```

## Test Categories

### 1. Unit Tests
- Individual class and method testing
- Configuration management
- Type validation
- Utility functions

### 2. Integration Tests
- API client interactions
- OAuth flow testing
- Model instantiation
- Configuration integration

### 3. Edge Cases
- Error handling
- Invalid inputs
- Missing configuration
- Network failures

### 4. Type Safety
- Dataclass validation
- Type compatibility
- Generic type usage
- Enum handling

## Coverage Goals

- **Line Coverage**: >90%
- **Branch Coverage**: >85%
- **Function Coverage**: >95%
- **Statement Coverage**: >90%

## Best Practices

### Test Structure
```python
class TestClassName:
    """Test ClassName class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        # Setup code here
        pass
    
    def test_method_name_should_do_something(self):
        """Test that methodName does something."""
        # Arrange
        input_data = 'test'
        
        # Act
        result = instance.method_name(input_data)
        
        # Assert
        assert result == 'expected'
```

### Naming Conventions
- Test files: `test_*.py`
- Test classes: `TestClassName`
- Test methods: `test_method_name_should_do_something`
- Mock variables: `mock_class_name`

### Assertions
- Use descriptive assertion messages
- Test both success and failure cases
- Verify mock calls and parameters
- Test edge cases and error conditions

## Troubleshooting

### Common Issues

#### 1. ConfigurationManager Singleton Issues
```python
# Reset singleton before each test
def setup_method(self):
    ConfigurationManager._instance = None
    ConfigurationManager._config = None
```

#### 2. Mock Not Working
```python
# Ensure mocks are cleared between tests
def teardown_method(self):
    patch.stopall()
```

#### 3. Async Test Issues
```python
# Use proper async/await patterns
@pytest.mark.asyncio
async def test_async_method(self):
    result = await instance.async_method()
    assert result is not None
```

#### 4. Import Issues
```python
# Use proper import paths
from mosaia import MosaiaClient, ConfigurationManager
```

## Contributing

When adding new tests:

1. Follow the existing test structure
2. Use descriptive test names
3. Test both success and failure cases
4. Add appropriate mocks for dependencies
5. Update this README if adding new test categories
6. Ensure tests pass before submitting PR

## Continuous Integration

Tests are automatically run in CI/CD pipelines:

- **Pre-commit**: Basic test suite
- **Pull Request**: Full test suite with coverage
- **Release**: Complete test suite with performance testing

## Performance Testing

For performance-critical code, add performance tests:

```python
import time

def test_performance_method(self):
    """Test that performance method completes within time limit."""
    start = time.time()
    instance.performance_method()
    end = time.time()
    
    assert (end - start) < 0.1  # 100ms limit
```

## Test Data

### Sample Data Fixtures
The `conftest.py` file provides sample data fixtures:

```python
@pytest.fixture
def sample_user_data():
    """Provide sample user data for testing."""
    return {
        'id': 'user-123',
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    }

@pytest.fixture
def sample_organization_data():
    """Provide sample organization data for testing."""
    return {
        'id': 'org-456',
        'name': 'Test Organization',
        'short_description': 'A test organization'
    }
```

## Test Environment

### Environment Variables
Tests can use environment variables for configuration:

```bash
# Set test environment variables
export MOSAIA_API_KEY=test-key
export MOSAIA_API_URL=https://test-api.mosaia.ai
export MOSAIA_VERSION=1
```

### Test Database
For integration tests that require a database:

```python
@pytest.fixture(scope="session")
def test_database():
    """Provide test database connection."""
    # Database setup code here
    yield database_connection
    # Database cleanup code here
```

## Reporting

### Coverage Reports
Generate coverage reports:

```bash
# Generate HTML coverage report
pytest --cov=mosaia --cov-report=html

# Generate XML coverage report for CI
pytest --cov=mosaia --cov-report=xml
```

### Test Reports
Generate test reports:

```bash
# Generate JUnit XML report
pytest --junitxml=test-results.xml

# Generate HTML report
pytest --html=test-report.html
```
