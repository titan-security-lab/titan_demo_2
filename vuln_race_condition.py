import os

def withdraw_money(account_id, amount):
    """
    VULNERABLE: Race Condition - CWE-race condition
    TOCTOU: Time-of-check to time-of-use
    """
    # Check balance
    balance = get_balance(account_id)
    
    # Race condition window here!
    if balance >= amount:
        # Another transaction could happen here
        new_balance = balance - amount
        update_balance(account_id, new_balance)
        return True
    
    return False

def get_balance(account_id):
    return 1000

def update_balance(account_id, amount):
    pass
