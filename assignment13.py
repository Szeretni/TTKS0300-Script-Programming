print "Function: sum2(). Parameter is an integer."
print 'ie. vowels("aeiouy")'
def vowels(string):
    vowels = ['a','e','i','o','u','y']
    vowelcounter = 0
    for c in string:
        for l in vowels:
            if c == l:
                vowelcounter += 1
    print vowelcounter
