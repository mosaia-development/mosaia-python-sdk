"""
Global configuration file for the Mosaia SDK
"""

from typing import Dict, Any

DEFAULT_CONFIG = {
    # API Configuration
    "API": {
        "BASE_URL": "https://api.mosaia.ai",
        "VERSION": "1",
        "CONTENT_TYPE": "application/json",
    },

    # Frontend Configuration
    "FRONTEND": {
        "URL": "https://mosaia.ai",
    },

    # Authentication
    "AUTH": {
        "TOKEN_PREFIX": "Bearer",
    },

    # Error Messages
    "ERRORS": {
        "NO_AUTH": "Run bot.auth($YOUR_MOSAIA_BOT_KEY) first",
        "UNKNOWN_ERROR": "Unknown Error",
        "DEFAULT_STATUS": "UNKNOWN",
        "DEFAULT_STATUS_CODE": 400,
    },

    # API Endpoints
    "ENDPOINTS": {
        "APPS": "/app",
        "TOOLS": "/tool",
        "BOTS": "/bot",
    },

    # Response Types
    "RESPONSE": {
        "SUCCESS": {
            "data": None,
            "error": None
        }
    }
}

# Type for the configuration
MosaiaConfig = Dict[str, Any] 