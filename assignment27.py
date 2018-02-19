#Version 2018-02-19
'''
Write a Python script that generates and prints a pseudo random number between 0 and 10 using the
standard library’s random module’s randint function. You can find the documentation for the random
module here (you want to read about randint, you can glance at the other stuff too if you want)
'''

import random

def randomPrint():
    rand = random.randint(0,10)
    print rand

#calls
randomPrint()
randomPrint()
randomPrint()
randomPrint()
randomPrint()

#prints
'''
7
10
5
2
0
'''
