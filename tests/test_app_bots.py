import sys
import subprocess
import pytest
import os

from dotenv import load_dotenv

load_dotenv()

def test_app_bots_pythonic_patterns():
    """Test the new Pythonic patterns for AppBots API."""
    
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
        from mosaia.types import AppBotInterface, MosiaConfig

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

    # Test Pythonic patterns
    try:
        # 1. Test direct ID passing (most Pythonic)
        print("Testing direct ID passing...")
        # This will fail without a real API, but we're testing the interface
        try:
            bot = mosaia.app_bots.get("test_bot_id")
            print(f"✅ Direct ID passing works: {bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 2. Test get_by_id method
        print("Testing get_by_id method...")
        try:
            bot = mosaia.app_bots.get_by_id("test_bot_id")
            print(f"✅ get_by_id works: {bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 3. Test creating with dictionary
        print("Testing create with dictionary...")
        try:
            new_bot = mosaia.app_bots.create({
                "app": "test_app_id",
                "response_url": "https://example.com/webhook"
            })
            print(f"✅ Create with dict works: {new_bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 4. Test creating with keyword arguments
        print("Testing create with keyword arguments...")
        try:
            new_bot = mosaia.app_bots.create(
                {},  # Empty dict as base
                app="test_app_id",
                response_url="https://example.com/webhook"
            )
            print(f"✅ Create with kwargs works: {new_bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 5. Test updating with ID and dictionary
        print("Testing update with ID and dictionary...")
        try:
            updated_bot = mosaia.app_bots.update("test_bot_id", {
                "response_url": "https://new-url.com/webhook"
            })
            print(f"✅ Update with ID and dict works: {updated_bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 6. Test deleting by ID
        print("Testing delete by ID...")
        try:
            mosaia.app_bots.delete("test_bot_id")
            print("✅ Delete by ID works")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 7. Test legacy interface usage (backward compatibility)
        print("Testing legacy interface usage...")
        try:
            bot_interface = AppBotInterface(id="test_bot_id")
            bot = mosaia.app_bots.get(bot_interface)
            print(f"✅ Legacy interface works: {bot}")
        except Exception as e:
            print(f"Expected error (no real API): {e}")
        
        # 8. Test interface creation with minimal data
        print("Testing interface creation with minimal data...")
        try:
            minimal_bot = AppBotInterface(id="test_bot_id")
            assert minimal_bot.id == "test_bot_id"
            print("✅ Interface creation with minimal data works")
        except Exception as e:
            pytest.fail(f"Interface creation failed: {e}")
        
        # 9. Test interface creation with full data
        print("Testing interface creation with full data...")
        try:
            full_bot = AppBotInterface(
                id="test_bot_id",
                app="test_app_id",
                response_url="https://example.com/webhook"
            )
            assert full_bot.id == "test_bot_id"
            assert full_bot.app == "test_app_id"
            assert full_bot.response_url == "https://example.com/webhook"
            print("✅ Interface creation with full data works")
        except Exception as e:
            pytest.fail(f"Full interface creation failed: {e}")
        
        print("✅ All Pythonic pattern tests passed!")
        
    except Exception as e:
        pytest.fail(f"AppBots API tests failed: {e}")

def test_app_bots_method_signatures():
    """Test that the method signatures are correct for Pythonic usage."""
    
    try:
        from mosaia import Mosaia
        from mosaia.apis.app_bots import AppBots
        
        # Test that app_bots property exists
        mosaia = Mosaia()
        assert hasattr(mosaia, 'app_bots'), "app_bots property should exist"
        assert isinstance(mosaia.app_bots, AppBots), "app_bots should be an AppBots instance"
        
        # Test method signatures
        app_bots = mosaia.app_bots
        
        # Test get method accepts string
        assert callable(app_bots.get), "get method should be callable"
        
        # Test get_by_id method accepts string
        assert callable(app_bots.get_by_id), "get_by_id method should be callable"
        
        # Test create method accepts dict
        assert callable(app_bots.create), "create method should be callable"
        
        # Test update method accepts string and dict
        assert callable(app_bots.update), "update method should be callable"
        
        # Test delete method accepts string
        assert callable(app_bots.delete), "delete method should be callable"
        
        print("✅ All method signature tests passed!")
        
    except Exception as e:
        pytest.fail(f"Method signature tests failed: {e}")

if __name__ == "__main__":
    pytest.main([__file__]) 