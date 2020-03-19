import functools

user = {"username": "max", "access_level": "blub"}

def make_secure(access_level):
    def decorator(func):
    ## to keep the original __name__ of get_admin_password, respectively the decorator
        @functools.wraps(func)
        def secure_function(panel):
            if user["access_level"] == "admin":
                return func(*args,**kwargs)
            else:
                return f"The user {user['username']} has no admin access."

        return secure_function
    
    return decorator

@make_secure("admin")
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_pw"

print(get_password("billing"))