import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    #keeps the name of the original function
    @functools.wraps(func)
    #o *args, **kwargs serve para a função poder receber qualquer quantidade de argumentos
    # ou atributos, ficando dinamica
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

#prevent the function to creat a function with different name
@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password())




