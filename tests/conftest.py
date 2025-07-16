import pytest

@pytest.fixture
def mosaia_import():
    """Fixture to ensure mosaia can be imported."""
    import importlib
    import mosaia
    return mosaia

# You can use this fixture in your tests like:
# def test_something(mosaia_import):
#     assert mosaia_import.some_function() == expected_result 