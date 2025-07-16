#!/usr/bin/env python3
"""
Simple test script to verify the Mosaia Python SDK implementation
"""

import sys
import os

# Add the current directory to the path so Python can find the mosaia package
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test that all modules can be imported"""
    try:
        from mosaia import (
            Mosaia, MosiaConfig, Apps, Tools, AppBots, OAuth,
            AppInterface, ToolInterface, AppBotInterface,
            is_sdk_error, create_error_response, DEFAULT_CONFIG
        )
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """Test configuration creation"""
    try:
        from mosaia import MosiaConfig, DEFAULT_CONFIG
        
        config = MosiaConfig(
            api_key="test_key",
            version="1",
            base_url="https://api.mosaia.ai"
        )
        
        print("✅ Configuration creation successful")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_client_creation():
    """Test client creation"""
    try:
        from mosaia import Mosaia, MosiaConfig
        
        config = MosiaConfig(api_key="test_key", user="test_user")
        client = Mosaia(config)
        
        # Test that APIs are available
        assert hasattr(client, 'apps')
        assert hasattr(client, 'tools')
        assert hasattr(client, 'oauth')
        
        print("✅ Client creation successful")
        return True
    except Exception as e:
        print(f"❌ Client creation error: {e}")
        return False

def test_types():
    """Test type creation"""
    try:
        from mosaia import AppInterface, ToolInterface, AppBotInterface
        
        # Test AppInterface
        app = AppInterface(
            name="Test App",
            short_description="A test app"
        )
        
        # Test ToolInterface
        tool = ToolInterface(
            name="test_tool",
            short_description="A test tool",
            tool_schema='{"type": "object"}'
        )
        
        # Test AppBotInterface
        bot = AppBotInterface(
            app="app_id",
            response_url="https://example.com/webhook"
        )
        
        print("✅ Type creation successful")
        return True
    except Exception as e:
        print(f"❌ Type creation error: {e}")
        return False

def test_oauth():
    """Test OAuth functionality"""
    try:
        from mosaia import OAuth, OAuthConfig
        
        config = OAuthConfig(
            client_id="test_client_id",
            redirect_uri="https://example.com/callback"
        )
        
        oauth = OAuth(config)
        auth_data = oauth.get_authorization_url_and_code_verifier()
        
        assert 'url' in auth_data
        assert 'code_verifier' in auth_data
        
        print("✅ OAuth functionality successful")
        return True
    except Exception as e:
        print(f"❌ OAuth error: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Mosaia Python SDK...")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_config,
        test_client_creation,
        test_types,
        test_oauth
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 