#Hannu Oksman 2018-03-16
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
#initialization begins
    #generating list of words and counting how many words are available
    wordList = ReadFile()
    wordsInList = len(wordList)

    #random word from the file
    theWord = RandomWord(wordList,wordsInList)

    #print topic
    print "Hangman game!\nThe word has " + str(len(theWord)) + " letters"

    #determine the number of guesses
    maxGuesses = 10 #increased to 10 from specs 7 because of words like "underscore"

    #valid chars
    validChars = ValidChars()

    #init visible word
    visibleWord = VisibleWord(theWord)

    #win flag
    win = False

#initialization done

#guessing begins
    #guess-loop
    while (maxGuesses > 0):
        #asking for a guess
        guess = raw_input("Guess: ")
        #is the guess valid?
        validation = Validation(guess,validChars)
        if (validation):
            #valid guess
            #updating visible word
            visibleWord = UpdateVisibleWord(visibleWord,theWord,guess)
            #print visible word
            PrintVisible(visibleWord) #visible word is a list, so print isn't pretty without this
            #wincheck
            win = WinCheck(visibleWord)
            if win:
                break
            #updating the number of available guesses
            maxGuesses -= 1
        
    #out of the guess-loop, game over
    if win:
        print "You guessed the word!"
    else:
        print "Game over, you didn't guess the word!"
#guessing done





#functions
#words from the file
def ReadFile():
    wordList = []
    f = open("hangman_words.txt","r")
    for line in f:
        wordList.append(line.strip()) #in order to remove newline \n https://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
    f.close()
    return wordList

#the word from the list
def RandomWord(wordList,wordsInList):
    rand = random.randint(0,wordsInList-1) #-1 to avoid out of index
    theWord = wordList[rand]
    return theWord

#valid chars
def ValidChars():
    validChars = []
    numOfLetters = ord('z')-ord('a') #ascii arithmetics, python syntax from https://stackoverflow.com/questions/2156892/python-how-can-i-increment-a-char
    for x in range(0,numOfLetters+1): #+1 to include last int
        validChars.append(chr(ord('a')+x))
    return validChars

#visible word init
def VisibleWord(theWord):
    visibleWord = []
    for x in range(0,len(theWord)):
        visibleWord.append('_')
    return visibleWord

#validation
def Validation(guess,validChars):
    isValid = False
    #is lenght valid?
    if len(guess) > 1:
        print "Too long guess, try again."
    #is char valid?
    elif not ValidGuess(guess,validChars):
        print "Not a valid character, try again."
    else:
        isValid = True
    return isValid

#valid guess
def ValidGuess(guess,validChars):
    valid = False
    for c in validChars:
        if guess is c:
            #guessed char is a valid char
            valid = True
    return valid

#update visible word
def UpdateVisibleWord(visibleWord,theWord,guess):
    index=0
    for c in theWord:
        #if char is in the word, update visible word
        if guess is c:
            visibleWord[index]=c
        index += 1
    return visibleWord

#print visible word
def PrintVisible(visibleWord):
    for x in visibleWord:
        sys.stdout.write(x) #no newline
    print

#wincheck
def WinCheck(visibleWord):
    win = True
    for c in visibleWord:
        if c == '_':
            #underscore-char found, therefore player hasn't guessed all of the chars
            win = False
    return win





#init
hangman()

'''
 RESTART: C:\Users\l2912\Source\Repos\TTKS0300-Script-Programming\hangman.py 
Hangman game!
The word has 7 letters
Guess: h
h______
Guess: a
ha___a_
Guess: n
han__an
Guess: g
hang_an
Guess: m
hangman
You guessed the word!
>>> 
'''
