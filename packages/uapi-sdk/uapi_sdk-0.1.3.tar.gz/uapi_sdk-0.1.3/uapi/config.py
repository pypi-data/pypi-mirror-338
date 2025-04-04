import os
from typing import Optional

class Config:
    """Global configuration for the UAPI SDK."""
    
    # API Configuration
    BASE_URL = os.getenv("UAPI_BASE_URL", "https://sage-ai-labs--search-api-search-endpoint.modal.run")  # Default to Modal endpoint
    
    @classmethod
    def get_base_url(cls, base_url: Optional[str] = None) -> str:
        """Get base URL from parameter or environment variable.
        
        Args:
            base_url (str, optional): Base URL provided directly
            
        Returns:
            str: The base URL
        """
        if base_url is not None:
            return base_url
            
        return cls.BASE_URL 