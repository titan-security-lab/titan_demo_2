import psycopg2

def connect_to_database():
    """
    VULNERABLE: Hardcoded Credentials - CWE-798
    Credentials exposed in source code
    """
    # Hardcoded password - major security issue!
    connection = psycopg2.connect(
        host="db.example.com",
        database="production",
        user="admin",
        password="SuperSecret123!"
    )
    
    return connection
