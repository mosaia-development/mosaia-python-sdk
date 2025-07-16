"""
Utility functions for the Mosaia SDK
"""

from typing import Any, Dict
from .types import ErrorResponse

def is_sdk_error(error: Any) -> bool:
    """
    Check if an error is an SDK error
    
    Args:
        error: The error to check
        
    Returns:
        bool: True if it's an SDK error, False otherwise
    """
    return isinstance(error, dict) and 'message' in error and 'code' in error and 'status' in error

def create_error_response(message: str, code: str = "UNKNOWN_ERROR", status: int = 400) -> ErrorResponse:
    """
    Create a standardized error response
    
    Args:
        message: Error message
        code: Error code
        status: HTTP status code
        
    Returns:
        ErrorResponse: The error response
    """
    return ErrorResponse(
        message=message,
        code=code,
        status=status
    ) 