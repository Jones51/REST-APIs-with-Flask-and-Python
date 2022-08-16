add = lambda x, y: x+y #alway return something, no need to declare it

print(add(5,7))

def double(x):
    return x*2

sequence = [1,3,5,9]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)
#does the same as above, map returns a object, to interact, use list as below
doubled = list(map(lambda  x: x*2, sequence))