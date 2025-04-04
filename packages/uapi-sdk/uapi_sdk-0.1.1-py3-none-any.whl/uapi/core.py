import requests
from typing import Dict, Any, List

def make_request(
    method: str = "POST",
    params: Dict[str, Any] = None,
    headers: Dict[str, str] = None,
    base_url: str = None
) -> Dict[str, Any]:
    """Make an HTTP request to the UAPI service.
    
    Args:
        method (str, optional): HTTP method. Defaults to "POST".
        params (Dict[str, Any], optional): Request parameters. Defaults to None.
        headers (Dict[str, str], optional): Request headers. Defaults to None.
        base_url (str, optional): Base URL for the request. Defaults to None.
        
    Returns:
        Dict[str, Any]: API response
        
    Raises:
        Exception: If the request fails
    """
    try:
        # Use the base_url directly as the complete endpoint
        url = base_url
        
        response = requests.request(
            method=method,
            url=url,
            json=params,
            headers=headers
        )
        
        if response.status_code == 404:
            raise Exception(f"Endpoint not found. Please check if the API endpoint '{url}' is correct.")
        elif response.status_code == 405:
            raise Exception(f"Method {method} not allowed. The server does not support this HTTP method.")
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {str(e)}")

def format_discover_request(query: str, top_results: int) -> Dict[str, Any]:
    """Format the discover API request parameters.
    
    Args:
        query (str): Search query
        top_results (int): Number of results to return
        
    Returns:
        Dict[str, Any]: Formatted request parameters
    """
    return {
        "query": query,
        "top_results": top_results
    }

def format_auth_headers(api_key: str) -> Dict[str, str]:
    """Format authentication headers.
    
    Args:
        api_key (str): API key
        
    Returns:
        Dict[str, str]: Formatted headers
    """
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    } 