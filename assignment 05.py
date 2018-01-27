last = 11
#if last = 11, then height is 10 rows and width 20 chars
#modify last to change print size
for x in range (1,last):
    if x == 1 or x == (last-1):
        print "+" + "-"*((last-2)*2) + "+"
    else:
        print "|" + "."*((last-2)*2) + "|"
