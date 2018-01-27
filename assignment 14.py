print "Function: symbols(). Parameter is a string (+,=,letters)."
print 'ie. symbols("+a+==x==+b+")'
def symbols(string):
# symbols("++++")        prints: True  
# symbols("====")        prints: True  
# symbols("+=+=")        prints: True  
# symbols("++++=++++=")  prints: True  
# symbols("a")           prints: False, 'a' is not surrounded by + symbols at all!  
# symbols("a+")          prints: False, 'a' is surrounded by + only on the left side!  
# symbols("+a")          prints: False, 'a' is surrounded by + only on the right side!  
# symbols("+a+")         prints: True  
# symbols("+a+====+b+")  prints: True  
# symbols("+a+==x==+b+") prints: False, 'x' is not surrounded by + symbols at all

    #long, but powerful. Accepts every symbol, not just a-z.
   
    #initialization
    plus = '+'
    equal = '='
    stringArray = []
    dict = {}
    true = True
    
    #adding chars to array
    for char in string:
        stringArray.append(char)

    #counting number of chars in array
    ind = 0
    for l in stringArray:
        ind += 1

    #adding chars from array to dict
    for i in range(0,ind):
        dict[i] = stringArray[i]

    #symbol checking begins
    for key in dict:
        prev = 1
        next = 1
        #only 1 symbol
        if (ind == 1):
            #if letter
            if (dict[key] != plus and dict[key] != equal):              
                print "False, '" + dict[key] + "' is not surrounded by + symbols at all"
                true = False
            else:
                print true
        #2 symbols
        elif (ind == 2):
            #if letter
            if (dict[key] != plus and dict[key] != equal):
                #to avoid going out of bounds
                if (key == 0):
                    prev = 0
                elif (key == 1):
                    next = 0
                #checking next/previous
                if (dict[key-prev] == plus or dict[key+next] != plus):
                    print "False, '" + dict[key] + "' is surrounded by + only on the left side!"
                    true = False
                elif (dict[key-prev] != plus or dict[key+next] == plus):
                    print "False, '" + dict[key] + "' is surrounded by + only on the right side!"
                    true = False
        #3 or more symbols
        else:
            #if letter
            if (dict[key] != plus and dict[key] != equal):
                #checking neighbours
                if (dict[key-prev] != plus and dict[key+next] != plus):
                    print "False, '" + dict[key] + "' is not surrounded by + symbols at all"
                    true = False
                elif (dict[key-prev] == plus and dict[key+next] != plus):
                    print "False, '" + dict[key] + "' is surrounded by + only on the right side!"
                    true = False
                elif (dict[key-prev] != plus and dict[key+next] == plus):
                    print "False, '" + dict[key] + "' is surrounded by + only on the left side!"
                    true = False
    #0 false states found
    if (true == True):
        print true
