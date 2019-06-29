from .db import *

def authenticate(username, password):
    query = "SELECT * FROM users WHERE USERNAME='%s'"%(username,)
    user = select_query(query).fetchone()
    if user is not None:
        if(password == user[2]):
            return user
    return None

def identity(payload):
    user_id = payload['identity']
    query = "SELECT * FROM users WHERE id='%s'"%(user_id)
    user = select_query(query).fetchone()
    return user
