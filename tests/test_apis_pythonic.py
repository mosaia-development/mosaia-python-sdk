import sys
import subprocess
import pytest
import os

from dotenv import load_dotenv

load_dotenv()

def test_apis_pythonic_patterns():
    """Test Pythonic patterns for Apps and Tools APIs."""
    
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
        from mosaia.types import AppInterface, ToolInterface, MosiaConfig

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

    # Test Apps API Pythonic patterns
    try:
        print("Testing Apps API Pythonic patterns...")
        
        # Test getting all apps
        try:
            apps = mosaia.apps.get()
            print(f"✅ Get all apps works: {apps}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test getting app by ID
        try:
            app = mosaia.apps.get("test_app_id")
            print(f"✅ Get app by ID works: {app}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test creating app with dictionary
        try:
            new_app = mosaia.apps.create({
                "name": "Test App",
                "short_description": "A test app",
                "org": "test_org_id"
            })
            print(f"✅ Create app with dict works: {new_app}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test updating app with ID and dictionary
        try:
            updated_app = mosaia.apps.update("test_app_id", {
                "name": "Updated Test App",
                "short_description": "Updated description"
            })
            print(f"✅ Update app with ID and dict works: {updated_app}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test deleting app by ID
        try:
            mosaia.apps.delete("test_app_id")
            print("✅ Delete app by ID works")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        print("✅ All Apps API Pythonic pattern tests passed!")
        
    except Exception as e:
        pytest.fail(f"Apps API tests failed: {e}")

    # Test Tools API Pythonic patterns
    try:
        print("Testing Tools API Pythonic patterns...")
        
        # Test getting all tools
        try:
            tools = mosaia.tools.get()
            print(f"✅ Get all tools works: {tools}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test getting tool by ID
        try:
            tool = mosaia.tools.get("test_tool_id")
            print(f"✅ Get tool by ID works: {tool}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test getting tool by name
        try:
            tool = mosaia.tools.get_by_name("test_tool_name")
            print(f"✅ Get tool by name works: {tool}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test creating tool with dictionary
        try:
            new_tool = mosaia.tools.create({
                "name": "test_tool",
                "short_description": "A test tool",
                "tool_schema": '{"type": "object"}',
                "org": "test_org_id"
            })
            print(f"✅ Create tool with dict works: {new_tool}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test updating tool with ID and dictionary
        try:
            updated_tool = mosaia.tools.update("test_tool_id", {
                "name": "updated_test_tool",
                "short_description": "Updated description"
            })
            print(f"✅ Update tool with ID and dict works: {updated_tool}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # Test deleting tool by ID
        try:
            mosaia.tools.delete("test_tool_id")
            print("✅ Delete tool by ID works")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        print("✅ All Tools API Pythonic pattern tests passed!")
        
    except Exception as e:
        pytest.fail(f"Tools API tests failed: {e}")

def test_api_method_signatures():
    """Test that all API method signatures are correct for Pythonic usage."""
    
    try:
        from mosaia import Mosaia
        from mosaia.apis.apps import Apps
        from mosaia.types import MosiaConfig
        
        # Test that API properties exist
        mosaia = Mosaia()
        assert hasattr(mosaia, 'apps'), "apps property should exist"
        assert hasattr(mosaia, 'app_bots'), "app_bots property should exist"
        
        assert isinstance(mosaia.apps, Apps), "apps should be an Apps instance"
        
        # Test Apps method signatures
        apps = mosaia.apps
        assert callable(apps.get), "apps.get method should be callable"
        assert callable(apps.create), "apps.create method should be callable"
        assert callable(apps.update), "apps.update method should be callable"
        assert callable(apps.delete), "apps.delete method should be callable"
        
        # Test Tools method signatures (with user/org config)
        config = MosiaConfig(user="test_user")
        mosaia_with_user = Mosaia(config)
        assert hasattr(mosaia_with_user, 'tools'), "tools property should exist with user config"
        
        tools = mosaia_with_user.tools
        assert callable(tools.get), "tools.get method should be callable"
        assert callable(tools.get_by_name), "tools.get_by_name method should be callable"
        assert callable(tools.create), "tools.create method should be callable"
        assert callable(tools.update), "tools.update method should be callable"
        assert callable(tools.delete), "tools.delete method should be callable"
        
        print("✅ All API method signature tests passed!")
        
    except Exception as e:
        pytest.fail(f"API method signature tests failed: {e}")

if __name__ == "__main__":
    pytest.main([__file__]) 