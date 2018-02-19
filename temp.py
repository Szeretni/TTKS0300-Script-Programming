import sys

try:
    print 5/0
except ZeroDivisionError:
    print "divided by zero"
    sys.exit(-1)
