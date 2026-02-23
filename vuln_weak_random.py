import random

def generate_session_token():
    """
    VULNERABLE: Insufficient Randomness - CWE-330
    Predictable tokens can be guessed
    """
    # Using weak random - predictable for security!
    token = ''.join([
        str(random.randint(0, 9)) 
        for _ in range(32)
    ])
    
    return token
