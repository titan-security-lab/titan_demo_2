import requests

def fetch_url(url):
    """
    VULNERABLE: Server-Side Request Forgery (SSRF) - CWE-918
    Attacker can access: http://169.254.169.254/latest/meta-data/
    """
    # No URL validation - allows access to internal resources!
    response = requests.get(url)
    
    return response.text
