import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    #keeps the name of the original function
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

#prevent the function to creat a function with different name
@make_secure
def get_admin_password():
    return "1234"

print(get_admin_password())

print(get_admin_password.__name__)



