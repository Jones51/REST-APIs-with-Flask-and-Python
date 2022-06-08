number = 7


while True:
    user_input = input('Enter "y" if you would like to play the game? (Y/n)').lower()

    if user_input == 'n':
        break

    user_number = int(input('Guess our number: '))
    if(user_number == number):
        print("You guesses correctly!")
    elif abs(number - user_number) in (1, -1):
        print("You were off by one!")
    else:
        print("Sorry, you are wrong!")
