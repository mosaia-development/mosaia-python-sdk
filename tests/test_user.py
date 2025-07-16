import sys
import subprocess
import pytest
import os

from dotenv import load_dotenv

load_dotenv()

def user_agent():
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
        from mosaia.entities import User

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

    # Test User Model
    try:
        # Test valid User creation
        valid_user = User(
            username="Aaron",
            name="Aaron",
            image="image_url",
            description="description",
            email="aaron@mosaia.com",
            url="https://mosaia.com",
            location="location",
            links={
                "website": "https://mosaia.com",
                "twitter": "https://twitter.com/mosaia",
                "linkedin": "https://linkedin.com/company/mosaia"
            }
        )
        assert valid_user.username == "Aaron"
        assert valid_user.temperature == 0.7

        # Test invalid username pattern
        with pytest.raises(ValueError):
            User(username="test agent with spaces")  # Should fail due to spaces

        # Test invalid email pattern
        with pytest.raises(ValueError):
            User(email="aaron@mosaia")  # Should fail due to invalid email format
        
        # Test invalid email pattern
        with pytest.raises(ValueError):
            User(url="aaron .com")  # Should fail due to invalid url format

    except Exception as e:
        pytest.fail(f"User model validation failed: {e}")

    # Get Agent from API
    try:
        users = mosaia.users.get()
        assert users, "Agents response is empty"
        
        # Validate response structure if possible
        if isinstance(users, list) and users:
            print(users[0])
            # Attempt to create Agent model from first response
            assert isinstance(users[0], User), "Failed to parse API response into User model"
            
    except Exception as e:
        pytest.fail(f"Could not get agent: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
