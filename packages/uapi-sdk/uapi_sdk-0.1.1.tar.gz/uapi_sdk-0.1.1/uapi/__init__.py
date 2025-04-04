"""UAPI SDK for discovering and accessing API endpoints."""

from typing import List, Dict, Any, Optional

from .client import UAPIClient
from .version import __version__

__all__ = ["discover", "UAPIClient", "__version__"]

def discover(query: str, api_key: str, top_results: int = 5, base_url: Optional[str] = None) -> List[Dict[str, Any]]:
    """Convenience function to discover APIs without explicitly creating a client.
    
    Args:
        query (str): Search query to find relevant API endpoints
        api_key (str): Your API key for the service
        top_results (int, optional): Number of top results to return. Defaults to 5.
        base_url (str, optional): Base URL for API requests. If not provided, will use UAPI_BASE_URL environment variable.
        
    Returns:
        List[Dict[str, Any]]: List of discovered API endpoints and their details
        
    Example:
        >>> from uapi import discover
        >>> results = discover("clothing products", api_key="your-api-key", top_results=2)
        >>> print(results)
    """
    client = UAPIClient(base_url=base_url)
    return client.discover(query, api_key, top_results) 