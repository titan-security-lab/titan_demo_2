import pickle
import base64

def load_user_session(session_data):
    """
    VULNERABLE: Insecure Deserialization - CWE-502
    Attacker can execute arbitrary code via crafted pickle
    """
    # Unpickling untrusted data - EXTREMELY DANGEROUS!
    decoded = base64.b64decode(session_data)
    session = pickle.loads(decoded)
    
    return session
