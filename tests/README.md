# Mosaia Python SDK - Test Suite

This directory contains the comprehensive test suite for the Mosaia Python SDK.

## Test Structure

```
tests/
├── __init__.py                 # Test package initialization
├── conftest.py                 # Pytest configuration and shared fixtures
├── unit/                       # Unit tests
│   ├── __init__.py
│   ├── test_basic.py          # Basic functionality tests
│   └── test_models.py         # Model and type tests
├── integration/                # Integration tests
│   └── __init__.py
└── utils/                      # Utility function tests
    ├── __init__.py
    └── test_utils.py          # Utils module tests
```

## Test Categories

### Unit Tests (`tests/unit/`)
- **Purpose**: Test individual components in isolation
- **Scope**: Single functions, classes, or modules
- **Dependencies**: Minimal external dependencies
- **Speed**: Fast execution
- **Markers**: `@pytest.mark.unit`

### Integration Tests (`tests/integration/`)
- **Purpose**: Test how components work together
- **Scope**: Component interactions and API integration
- **Dependencies**: May require external services or databases
- **Speed**: Slower execution
- **Markers**: `@pytest.mark.integration`

### Utils Tests (`tests/utils/`)
- **Purpose**: Test utility functions and helper classes
- **Scope**: Common utility functions used throughout the SDK
- **Dependencies**: Minimal external dependencies
- **Speed**: Fast execution
- **Markers**: `@pytest.mark.utils`

## Running Tests

### Using pytest directly

```bash
# Run all tests
pytest

# Run specific test categories
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests only
pytest -m utils         # Utils tests only

# Run tests in specific directories
pytest tests/unit/      # All unit tests
pytest tests/utils/     # All utils tests

# Run specific test files
pytest tests/unit/test_basic.py
pytest tests/utils/test_utils.py

# Verbose output
pytest -v

# With coverage
pytest --cov=mosaia --cov-report=term-missing
```

### Using the test runner script

```bash
# Run all tests
python run_tests.py

# Run specific categories
python run_tests.py --category unit
python run_tests.py --category integration
python run_tests.py --category utils

# Verbose output
python run_tests.py --verbose

# With coverage
python run_tests.py --coverage

# Fast tests only (skip slow markers)
python run_tests.py --fast

# Combine options
python run_tests.py --category utils --verbose --coverage
```

## Test Fixtures

The `conftest.py` file provides shared fixtures for all tests:

### Configuration Fixtures
- `config_manager`: Clean ConfigurationManager instance
- `test_config`: Test configuration data
- `initialized_config_manager`: Pre-initialized ConfigurationManager

### Data Fixtures
- `sample_user_data`: Sample user data
- `sample_organization_data`: Sample organization data
- `sample_agent_data`: Sample agent data
- `sample_app_data`: Sample app data
- `sample_tool_data`: Sample tool data

### Test Data Fixtures
- `valid_object_ids`: Valid MongoDB ObjectIDs
- `invalid_object_ids`: Invalid ObjectIDs
- `sample_query_params`: Sample query parameters
- `sample_error_data`: Sample error data

### Async Support
- `event_loop`: Async event loop for async tests

## Test Markers

The test suite uses pytest markers for categorization:

- `@pytest.mark.unit`: Unit tests
- `@pytest.mark.integration`: Integration tests
- `@pytest.mark.utils`: Utility function tests
- `@pytest.mark.slow`: Slow-running tests
- `@pytest.mark.api`: API-related tests

## Writing Tests

### Test Structure

```python
import pytest
from mosaia import SomeClass

@pytest.mark.unit
class TestSomeClass:
    """Test SomeClass functionality."""
    
    def test_some_method(self, sample_data):
        """Test some method."""
        instance = SomeClass()
        result = instance.some_method(sample_data)
        assert result == expected_value
    
    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            SomeClass().some_method(invalid_data)
```

### Using Fixtures

```python
def test_with_fixtures(config_manager, test_config):
    """Test using fixtures."""
    config_manager.initialize(test_config)
    config = config_manager.get_config()
    assert config.api_key == 'test-api-key'
```

### Async Tests

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    """Test async function."""
    result = await some_async_function()
    assert result == expected_value
```

## Test Configuration

### pytest.ini
- Test discovery paths
- Python file patterns
- Default options
- Test markers

### conftest.py
- Shared fixtures
- Test configuration
- Common test data

## Coverage

To run tests with coverage:

```bash
# Using pytest
pytest --cov=mosaia --cov-report=term-missing --cov-report=html

# Using test runner
python run_tests.py --coverage
```

This will generate:
- Terminal coverage report
- HTML coverage report in `htmlcov/`

## Continuous Integration

The test suite is designed to work with CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run tests
  run: |
    pip install pytest pytest-cov
    python run_tests.py --coverage
```

## Best Practices

1. **Test Isolation**: Each test should be independent
2. **Descriptive Names**: Use clear, descriptive test names
3. **Arrange-Act-Assert**: Structure tests with clear sections
4. **Use Fixtures**: Leverage shared fixtures for common setup
5. **Test Edge Cases**: Include tests for error conditions
6. **Async Support**: Use proper async/await for async tests
7. **Type Hints**: Include type hints in test functions
8. **Documentation**: Add docstrings to test classes and methods

## Adding New Tests

1. **Choose Category**: Place tests in appropriate directory
2. **Add Markers**: Use appropriate pytest markers
3. **Use Fixtures**: Leverage existing fixtures or create new ones
4. **Follow Naming**: Use `test_*.py` for test files
5. **Update Documentation**: Update this README if needed

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure the mosaia package is installed in development mode
2. **Fixture Errors**: Check that fixtures are properly defined in conftest.py
3. **Async Errors**: Use `@pytest.mark.asyncio` for async tests
4. **Configuration Errors**: Ensure ConfigurationManager is properly reset between tests

### Debug Mode

```bash
# Run with debug output
pytest -s -v --tb=long

# Run single test with debug
pytest tests/unit/test_basic.py::TestConfigurationManager::test_initialization -s -v
```
