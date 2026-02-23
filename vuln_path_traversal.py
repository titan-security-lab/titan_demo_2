import os

def read_user_file(filename):
    """
    VULNERABLE: Path Traversal (CWE-22)
    Attacker can access: ../../../../etc/passwd
    """
    # No sanitization - allows directory traversal!
    file_path = f"/var/www/uploads/{filename}"
    
    with open(file_path, 'r') as f:
        return f.read()
