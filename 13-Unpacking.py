def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1,2,5))

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator"

print(apply(1,3,6,7, operator="+"))



def named(name, age):
    print(name,age)

details ={"name": "Bob", "age": 25}

named(**details)
