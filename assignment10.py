print "Function: largest(). Parameter is a list of integers."
print "ie. largest([1,2,3,4,5])"
def largest(list):
    highest = list[0]
    for x in list:
        if (x > highest):
            highest = x
    print highest
