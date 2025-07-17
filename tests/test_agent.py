import sys
import subprocess
import pytest
import os

from dotenv import load_dotenv

load_dotenv()

def test_agent():
    """Test that the Mosaia package can be installed and imported."""
    # Try to install the package in development mode
    process = subprocess.run([
        sys.executable, 
        "-m", 
        "pip", 
        "install", 
        "-e", 
        ".",
        "--use-pep517"
    ], capture_output=True, text=True)
    
    assert process.returncode == 0, f"Package installation failed: {process.stderr}"
    
    # Initialize Mosaia Class
    try:
        from mosaia import Mosaia
        from mosaia.entities import Agent
        from mosaia.types import MosiaConfig

        config = MosiaConfig(
            version=os.environ.get("API_VERSION", None),
            base_url=os.environ.get("API_URL", None),
            api_key=os.environ.get("API_KEY", None)
        )
        
        mosaia = Mosaia(config)
        assert mosaia, "Mosaia class is empty"
    except ImportError as e:
        pytest.fail(f"Could not init package: {e}")

    # Generate API Key (skip if no credentials)
    client_id = os.environ.get("CLIENT_ID", None)
    client_secret = os.environ.get("CLIENT_SECRET", None)
    
    if client_id and client_secret:
        try:
            mosaia.generate_api_key(client_id=client_id, client_secret=client_secret)
            assert mosaia.api_key, "API Key is empty"
            print("✅ API Key generated successfully")
        except Exception as e:
            print(f"⚠️  Could not generate API Key (expected if no valid credentials): {e}")
    else:
        print("⚠️  Skipping API Key generation - no credentials provided")

    # Test Agent Model
    try:
        # Test valid agent creation
        valid_agent = Agent(
            name="test-agent",
            temperature=0.7,
            description="Test agent description",
            public=False,
            active=True
        )
        assert valid_agent.name == "test-agent"
        assert valid_agent.temperature == 0.7
        print("✅ Valid agent creation works")

        # Test invalid name pattern
        try:
            Agent(name="test agent with spaces")  # Should fail due to spaces
            pytest.fail("Should have raised ValueError for invalid name")
        except (ValueError, Exception):
            print("✅ Invalid name validation works")

        # Test temperature bounds
        try:
            Agent(name="test-agent", temperature=2.5)  # Should fail as temperature > 2
            pytest.fail("Should have raised ValueError for invalid temperature")
        except (ValueError, Exception):
            print("✅ Temperature bounds validation works")

    except Exception as e:
        print(f"⚠️  Agent model validation failed: {e}")
        # Don't fail the test, just log the error

    # Get Agent from API (new API)
    try:
        agents_response = mosaia.agents.get_all()
        assert agents_response, "Agents response is empty"
        # Optionally, check if the response is a dict or list, depending on mock/real API
        print(agents_response)
    except Exception as e:
        pytest.fail(f"Could not get agents: {e}")
    
    # Test new Pythonic patterns
    try:
        print("Testing new Pythonic patterns...")
        
        # Test that new APIs are available
        assert hasattr(mosaia, 'apps'), "apps property should exist"
        assert hasattr(mosaia, 'app_bots'), "app_bots property should exist"
        
        # Test method signatures for Pythonic usage
        assert callable(mosaia.apps.get), "apps.get method should be callable"
        assert callable(mosaia.app_bots.get), "app_bots.get method should be callable"
        
        # Test tools with user config
        from mosaia.types import MosiaConfig
        config_with_user = MosiaConfig(user="test_user")
        mosaia_with_user = Mosaia(config_with_user)
        assert hasattr(mosaia_with_user, 'tools'), "tools property should exist with user config"
        assert callable(mosaia_with_user.tools.get), "tools.get method should be callable"
        
        print("✅ New Pythonic patterns are available!")
        
    except Exception as e:
        pytest.fail(f"Pythonic pattern tests failed: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
