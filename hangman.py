#Hannu Oksman 2018-03-12
#Hangman
'''
Write a hangman game in Python. The game should

Read a list of words from a file (words.txt, one word per line)
Write the words in lower case to the file!
OPTIONAL: Make the game convert all words that contain upper case letter to lower case.
Choose a random word from the list
Let the player know how many letters the word has
The player is allowed to guess wrong 7 times. After that the game ends.
The player should be allowed to only to make guesses that are one character long, if his guess is longer the game should print an error message and let the player try again (number of remaining guesses should not change)
Player should only be allowed to make guesses that are lower case. If the player inputs a character that is upper case the game should print an error and let the player try again (number of guesses should not change)
After each guess, the game should display the correct word to the user with unguessed letters replaced by an underscore. For example, if the correct word is “rainbow” and the user has already guessed a and o the program should display a____o
Try to come up with the ending condition on your own. Hint: Remember that words can contain the same character multiple times!
Start by breaking the assignment down to pieces:

Write a function that reads the the file and returns a list of the words.
Write a function that calls the previous function, picks a word from the list and returns it to the caller.
Write a function that takes a string (the correct word) and a list of characters (correct guesses) and returns the string in the correct format (e.g. a____o)
Write a function that determines whether or not the user’s guess is valid
Write a function that takes a string (the correct word) and a character and returns whether or not the character is in the string.
Example game:

Hangman game!
The word has 6 letters
Guess: a
wrong, sorry. You have 6 attempts left
______
Guess: s
correct!
s_____
Guess: j
wrong, sorry. You have 5 attempts left
s_____
Guess: AA
Not a valid guess, try again
Guess: A
Not a valid guess, try again
Guess: u
correct!
su____
Guess: m
correct!
summ__
Guess: e
correct!
summe_
Guess: r
correct!
summer
'''
import random
import sys

def hangman():
    #words from the file and number of words in the file
    wordList = []
    words = -1
    f = open("hangman_words.txt","r")
    for line in f:
        wordList.append(line)
    words += 1
    f.close()

    #random word from the file
    rand = random.randint(0,words)
    theWord = wordList[rand]

    #the game
    #topic
    print "Hangman game!\nThe word has " + str(len(theWord)) + " letters"

    #number of guesses
    maxGuesses = 7

    #visible word
    visibleWord = ""
    for x in range(0,len(theWord)):
        visibleWord += "_"

    #validation
    #valid chars
    validChars = []
    numOfLetters = ord('z')-ord('a') #ascii arithmetics, syntax from https://stackoverflow.com/questions/2156892/python-how-can-i-increment-a-char
    for x in range(0,numOfLetters+1):
        validChars.append(chr(ord('a')+x))

    #lenght, valid char
    while (maxGuesses > 0):
        guess = raw_input("Guess: ")
        if len(guess) > 1:
            print "Too long guess, try again."
        elif not validGuess(guess,validChars):
            print "Not a valid character, try again."
        else:
            #valid guess, checks if guess char is in the word
            counter = 1
            for c in theWord:
                if guess is c:
                    visibleWord[counter]=c
            print visibleWord
            maxGuesses -= 1

#functions    
#valid guess
def validGuess(guess,validChars):
    valid = False
    for c in validChars:
        if guess is c:
            valid = True
    return valid

#init
hangman()
