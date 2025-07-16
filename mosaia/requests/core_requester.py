from typing import Optional, Union, Dict, Any, List
import requests

def parse_response(response: requests.Response) -> Union[Dict[str, Any], List[Any]]:
    """
    Parse the API response and handle different status codes.
    
    Args:
        response (requests.Response): The response from the API
        
    Returns:
        Union[Dict[str, Any], List[Any]]: Parsed response data
        
    Raises:
        requests.exceptions.HTTPError: If the response contains an error
    """
    try:
        response_data = response.json()
        
        # Check if response contains an error
        if not response.ok and "error" in response_data:
            raise requests.exceptions.HTTPError(
                f"Request failed: {response_data['error']}", 
                response=response
            )
        # For successful responses, return the data            
        return response_data
        
    except ValueError as e:
        raise requests.exceptions.HTTPError(
            f"Failed to parse JSON response: {str(e)}", 
            response=response
        )

def core_request(
    url: str,
    method: str = "GET",
    params: Optional[dict] = None,
    data: Optional[dict] = None,
    api_key: Optional[str] = None,
) -> Union[Dict[str, Any], List[Any]]:
    """
    Internal method to make HTTP requests.
    
    Args:
        api_key (str): API key to use for the request
        url (str): API endpoint URL
        method (str): HTTP method (GET, POST, PUT, DELETE)
        params (dict, optional): Query parameters for the request
        data (dict, optional): Request body for POST/PUT requests
        
    Returns:
        Union[Dict[str, Any], List[Any]]: Parsed response data
        
    Raises:
        ValueError: If no API key is available or invalid method
        requests.exceptions.HTTPError: If the API request fails
    """
    method = method.upper()
    if method not in ["GET", "POST", "PUT", "DELETE"]:
        raise ValueError(f"Unsupported HTTP method: {method}")
        
    headers = {
        'Content-Type': 'application/json'
    }

    if api_key is not None:
        headers['Authorization'] = f'Bearer {api_key}'
    
    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        params=params,
        json=data
    )
    return parse_response(response)