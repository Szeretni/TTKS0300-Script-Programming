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

#reading and selecting a word from a file
f = open("hangman_words.txt","r")

#number of words in the file
lineCount = 0
for line in f:
    lineCount += 1
print lineCount
f.close()

#random word from the file
f = open("hangman_words.txt","r")
rand = random.randint(0,lineCount)
print rand
theWord = ""
for line in f:
    if lineCount is rand:
        theWord = line
    lineCount -= 1
    print lineCount
print theWord
f.close()
