import re
from html import escape

def sanitize_user_input(user_input):
    """
    SAFE: Proper input sanitization
    """
    # Remove null bytes
    cleaned = user_input.replace('\x00', '')
    
    # Limit length
    if len(cleaned) > 1000:
        raise ValueError("Input too long")
    
    # Escape HTML
    cleaned = escape(cleaned)
    
    # Validate format (alphanumeric + basic punctuation)
    if not re.match(r'^[a-zA-Z0-9\s\.,!?-]+$', cleaned):
        raise ValueError("Invalid characters in input")
    
    return cleaned
