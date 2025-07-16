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

if __name__ == "__main__":
    success = test_init()
    if success:
        print("\nAll tests passed! 🎉")
    else:
        print("\nSome tests failed! 😢")
        sys.exit(1)
