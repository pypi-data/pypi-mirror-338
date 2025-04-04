from typing import List, Dict, Any, Optional

from .config import Config
from .core import make_request, format_discover_request, format_auth_headers

class UAPIClient:
    """Main client for interacting with the UAPI service."""
    
    def __init__(self, base_url: Optional[str] = None):
        """Initialize the UAPI client.
        
        Args:
            base_url (str, optional): Base URL for API requests. If not provided, will use UAPI_BASE_URL environment variable.
        """
        self.base_url = Config.get_base_url(base_url)
        
    def discover(self, query: str, api_key: str, top_results: int = 5) -> List[Dict[str, Any]]:
        """Discover relevant API endpoints based on your search query.
        
        Args:
            query (str): Search query to find relevant API endpoints
            api_key (str): Your API key for the service
            top_results (int, optional): Number of top results to return. Defaults to 5.
            
        Returns:
            List[Dict[str, Any]]: List of discovered API endpoints and their details
            
        Example:
            >>> client = UAPIClient()
            >>> results = client.discover("clothing products", api_key="your-api-key", top_results=2)
            >>> print(results)
        """
        params = format_discover_request(query, top_results)
        headers = format_auth_headers(api_key)
        
        return make_request(
            params=params,
            headers=headers,
            base_url=self.base_url
        ) 