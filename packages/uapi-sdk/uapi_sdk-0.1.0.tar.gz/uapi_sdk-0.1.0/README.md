# UAPI SDK

A simple Python SDK for discovering and accessing API endpoints through natural language queries.

## Installation

```bash
pip install uapi-sdk
```

## Quick Start

```python
from uapi import discover

# Simple usage
results = discover(
    query="clothing products",
    api_key="your-api-key",
    top_results=2
)

# The results will contain relevant API endpoints and their details
print(results)
```

## Features

- Natural language API discovery
- Simple and intuitive interface
- Type hints for better IDE support
- Comprehensive error handling

## Authentication

You can provide your API key in two ways:

1. Directly in the code:
```python
results = discover("clothing products", api_key="your-api-key")
```

2. Through environment variables:
```bash
export UAPI_KEY="your-api-key"
```
Then in your code:
```python
results = discover("clothing products")  # Will automatically use UAPI_KEY from environment
```

## Example Response

```python
[
  {
    "providers": {
      "Shopify": {
        "description": "APIs for accessing Shopify store data...",
        "apis": {
          "shopify.get_products": {
            "description": "Get product listings from a Shopify store...",
            "endpoint": "https://api.shopify.com/admin/api/2023-01/products.json",
            "parameters": {
              "store": "The unique identifier for the Shopify store.",
              "limit": "Number of products to retrieve (integer)."
            }
          }
        }
      }
    }
  }
]
```

## Error Handling

The SDK will raise exceptions with descriptive messages if:
- The API key is missing or invalid
- The request fails
- The server returns an error

## Requirements

- Python 3.7+
- requests
- typing-extensions

## License

MIT License 