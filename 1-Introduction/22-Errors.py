def divided (dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return dividend/divisor

grades = []

print("Welcome to the grade program")
try:
    average = divided(sum(grades), len(grades))
    print(f"The avarage grade is {average}")
except ZeroDivisionError as e:
    print("There are no grades yet in your list")