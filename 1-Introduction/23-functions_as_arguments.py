def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
    
    return dividend/divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20,4, operator=divide)
#print(result)

#-------------------------------
def search(sequence , expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    
    raise RuntimeError(f"Could not fuind an element with {expected}")


friends = [
    {"name": "Rolf Smith", "Age": 24},
    {"name": "Adam Smith", "Age": 34},
    {"name": "Cloud Smith", "Age": 25}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Adam Smith", get_friend_name))