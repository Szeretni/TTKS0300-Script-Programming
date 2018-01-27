print "Function: sum2(). Parameter is an integers."
print "ie. sum2(5)"
def sum2(number):
    sum = 0
    i = 0
    while i<=number: #in order to run last round
        sum = sum + i
        i += 1
    print sum
