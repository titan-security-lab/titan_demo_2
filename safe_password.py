import bcrypt

def hash_password(password):
    """
    SAFE: Secure password hashing with bcrypt
    """
    # Generate salt with proper work factor
    salt = bcrypt.gensalt(rounds=12)
    
    # Hash password with salt
    hashed = bcrypt.hashpw(
        password.encode('utf-8'), 
        salt
    )
    
    return hashed.decode('utf-8')

def verify_password(password, hashed):
    """
    SAFE: Secure password verification
    """
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed.encode('utf-8')
    )
