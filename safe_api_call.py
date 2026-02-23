import requests
from urllib.parse import urlparse

ALLOWED_DOMAINS = ['api.example.com', 'data.example.com']

def safe_api_call(url, params):
    """
    SAFE: Secure API call with validation and timeout
    """
    # Validate URL domain
    parsed = urlparse(url)
    if parsed.netloc not in ALLOWED_DOMAINS:
        raise ValueError(f"Domain {parsed.netloc} not allowed")
    
    # Enforce HTTPS
    if parsed.scheme != 'https':
        raise ValueError("Only HTTPS allowed")
    
    # Sanitize parameters
    safe_params = {
        k: str(v)[:100]  # Limit param length
        for k, v in params.items()
        if k.isalnum()  # Only alphanumeric keys
    }
    
    # Make request with timeout and verify SSL
    response = requests.get(
        url,
        params=safe_params,
        timeout=5,
        verify=True
    )
    
    response.raise_for_status()
    return response.json()
