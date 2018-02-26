#Version 2018-02-19
'''
Write a Python script that generates a random number between 0 and 20 (0 and 20 are included in the
range) and asks the user to guess the number. Requirements: The program should ask the number 5 times. If the user guesses correctly the program should print
“correct!” and exit. If the user doesn’t guess correctly after 5 times the program should print
“game over, you lost! the correct number was ??” and exit. The game should display a how many times
the user has guessed and how many tries he has left. If the user inputs a number that is less than 0
or bigger than 20, the game should print an error message and let the user guess again (number of
remaining guesses shouldn’t change). If the user inputs a non-number, the program should print an
error and let the user try again (number of remaining guesses shouldn’t change)
'''

import random

def guessingGame():
    print "++ Guessing Game ++\nGuess a number between 0 and 20"

    #number to guess
    correct = random.randint(0,20) 

    #loop
    total = 5 #max guesses
    current = 1 #current guess
    while (current < total + 1):
        try:
            guess = int(raw_input("Guess " + str(current) + "/" + str(total) + ": "))
        except ValueError:
            print "Not a number, try again"
        else:
            if (guess == correct):
                print "You guessed the number. Congratulations!"
                break;
            elif (guess < 0 or guess > 20):
                print "The guess should be between 0 and 20, try again"
            else:
                print "Sorry, try again!"
                current += 1
                if (current == 6): #game over
                    print "Game over, you lost! the correct number was " + str(correct)
    
#calls
guessingGame()

#prints
'''
++ Guessing Game ++
Guess a number between 0 and 20
Guess 1/5: a
Not a number, try again
Guess 1/5: 999
The guess should be between 0 and 20, try again
Guess 1/5: -1000
The guess should be between 0 and 20, try again
Guess 1/5: 5
Sorry, try again!
Guess 2/5: 6
Sorry, try again!
Guess 3/5: 7
Sorry, try again!
Guess 4/5: 8
You guessed the number. Congratulations!
'''
#Game over, you lost! the correct number was 20
