number = 7
user_input = input('Enter "y" if you would like to play the game:').lower()

if user_input == 'y':
    user_number = int(input('Guess our number: '))
    if(user_number == user_input):
        print("You guesses correctly!")
    elif abs(number - user_number) in (1, -1):
        print("You were off by one!")
    else:
        print("Sorry, you are wrong!")