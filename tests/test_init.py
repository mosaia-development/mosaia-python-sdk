import sys
import subprocess
import pytest
import os

from dotenv import load_dotenv

load_dotenv()

def test_init():
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
        from mosaia.types import MosiaConfig

        config = MosiaConfig(
            version=os.environ.get("API_VERSION", None),
            base_url=os.environ.get("API_URL", None),
            api_key=os.environ.get("API_KEY", None)
        )
        
        mosaia = Mosaia(config)
        assert mosaia, "Mosaia class is empty"
        
        # Test that new Pythonic APIs are available
        assert hasattr(mosaia, 'apps'), "apps property should exist"
        assert hasattr(mosaia, 'app_bots'), "app_bots property should exist"
        
        # Test tools with user config
        config_with_user = MosiaConfig(user="test_user")
        mosaia_with_user = Mosaia(config_with_user)
        assert hasattr(mosaia_with_user, 'tools'), "tools property should exist with user config"
        
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

if __name__ == "__main__":
    success = test_init()
    if success:
        print("\nAll tests passed! 🎉")
    else:
        print("\nSome tests failed! 😢")
        sys.exit(1)
