## this lib makes string comparison safe
from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    ## get value from dict, return None if not found
    user = User.find_by_username(username)
    print(user)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload["identity"]
    print   
    return User.find_by_id(user_id)