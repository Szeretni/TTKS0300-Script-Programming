#Version 2018-02-19
'''
Write a function called calculator that takes 3 parameters: a string which can be either “add”, “sub”
or “multiply”. Number. Another number. Hhen the string is “add”, the two numbers are added together
and the result is returned from the function. “sub”, the two numbers are subtracted and the result is
returned from the function. “multiply” the two numbers are multiplied and the result is returned from
the function. In other words, the function should work like this:
print calculator("add", 1, 2) # should print 3
print calculator("sub", 1, 2) # should print -1
print calculator("multiply", 1, 2) # should print 2
'''

def calculator(oper,num1,num2):
    if (oper == "add"):
        result = num1 + num2
    if (oper == "sub"):
        result = num1 - num2
    if (oper == "multiply"):
        result = num1 * num2
    print result

#calls
calculator("add", 1, 2)
calculator("sub", 1, 2)
calculator("multiply", 1, 2)

#prints
'''
3
-1
2
'''
