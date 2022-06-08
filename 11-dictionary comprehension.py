users = [
    (0, "Bob", "passowrd"),
    (1, "Rolf", "bob123")
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, passowrd = username_mapping[username_input]

if password_input == passowrd:
    print("Password correct")