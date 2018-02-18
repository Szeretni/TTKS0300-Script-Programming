#Version 2018-02-12
#source for exception descriptions
#https://docs.python.org/2/library/exceptions.html

def nameerror(s):
    print s

def indexError(num):
    #creating list
    numlist = []
    for x in range(0,2):
        numlist.append(x)
    #looping list
    for i in range(0,num):
        numlist[i]

def keyError(num):
    #creating dict
    dictionary = {}
    for x in range(0,2):
        dictionary[x] = x
    #printing specific key
    print dictionary[num]

def errors():
    try:
        #hannu not defined
        nameerror(hannu)
    except NameError:
        print "NameError"
    except IndexError:
        print "IndexError"
    except KeyError:
        print "KeyError"

    try:
        #will go out of index
        indexError(5)
    except NameError:
        print "NameError"
    except IndexError:
        print "IndexError"
    except KeyError:
        print "KeyError"

    try:
        #no such key
        keyError(5)
    except NameError:
        print "NameError"
    except IndexError:
        print "IndexError"
    except KeyError:
        print "KeyError"

#call
errors()

#prints
'''
NameError
IndexError
KeyError
>>> 
'''
