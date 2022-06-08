def user_age_in_months():
    user_age = input("Inform your age: ")
    month = int(user_age) * 12
    print(f"Your age is {user_age} and its value in months is {month}")

user_age_in_months()

def multiply(x,y=5):
    return x*y

result = multiply(8)
print(result)