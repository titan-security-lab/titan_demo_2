import jwt
import secrets
from datetime import datetime, timedelta

def generate_jwt_token(user_id, secret_key):
    """
    SAFE: Secure JWT token generation
    """
    # Use cryptographically secure random for JTI
    jti = secrets.token_urlsafe(32)
    
    payload = {
        'user_id': user_id,
        'jti': jti,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=1),
        'nbf': datetime.utcnow()
    }
    
    # Use strong algorithm
    token = jwt.encode(
        payload, 
        secret_key, 
        algorithm='HS256'
    )
    
    return token
