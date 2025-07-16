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

        mosaia = Mosaia({
            "version": os.environ.get("API_VERSION", None),
            "base_url": os.environ.get("API_URL", None),
            "api_key": os.environ.get("API_KEY", None)
        })
        assert mosaia, "Mosaia class is empty"
    except ImportError as e:
        pytest.fail(f"Could not init package: {e}")

    # Generate API Key
    try:
        mosaia.generate_api_key(client_id=os.environ.get("CLIENT_ID", None), client_secret=os.environ.get("CLIENT_SECRET", None))
        assert mosaia.api_key, "API Key is empty"
    except Exception as e:
        print(e)
        pytest.fail(f"Could not generate API Key: {e}")

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

        # Test invalid name pattern
        with pytest.raises(ValueError):
            Agent(name="test agent with spaces")  # Should fail due to spaces

        # Test temperature bounds
        with pytest.raises(ValueError):
            Agent(temperature=2.5)  # Should fail as temperature > 2

    except Exception as e:
        pytest.fail(f"Agent model validation failed: {e}")

    # Get Agent from API
    try:
        agents = mosaia.agents.get()
        assert agents, "Agents response is empty"
        
        # Validate response structure if possible
        if isinstance(agents, list) and agents:
            print(agents[0])
            # Attempt to create Agent model from first response
            assert isinstance(agents[0], Agent), "Failed to parse API response into Agent model"
            
    except Exception as e:
        pytest.fail(f"Could not get agent: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
