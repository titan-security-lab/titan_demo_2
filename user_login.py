import sqlite3

def authenticate_user(username, password):
    """
    Vulnerable to SQL injection - user input directly in query
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: String concatenation in SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    if result:
        return {"status": "success", "user": result[0]}
    else:
        return {"status": "failed", "message": "Invalid credentials"}