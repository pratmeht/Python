## Writing a Guess the Number game
def numGame():
    import random
    print()
    print('Hey ' + name)
    print('Welcome to Guess the Number Game')
    print('------- -- ----- --- ------ ----')
    print()
    print('I am a Computer and am thinking of a number between 1 to 20')
    n = 1
    actual_num = random.randint(1,20)
    guess_num = int(input('Take a guess: '))
    while actual_num != guess_num:
        if actual_num > guess_num:
            print('Your guess is too low')
        else:
            print('Your guess is too high')
        guess_num = int(input('Take another guess: '))
        n = n + 1
    print()
    print('Congratulations ' +name+ '! You guessed it right in ' + str(n) + ' trials')

def mainFn():
    numGame()
    while True:
        choice = input('Do you wish to play the game again? (y/n) ')
        if (choice == 'y' or choice == 'Y'):
            numGame()
        elif (choice == 'n' or choice == 'N'):
            print()
            print('Thank you ' +name+ ' for playing this game. Hope you enjoyed playing it.')
            break
        else:
            print('Hey ' + name+ ', it is an invalid choice')

name = input('Your name please: ')
mainFn()
