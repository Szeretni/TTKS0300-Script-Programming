#Version 2018-02-19
'''
Extend the function in the previous assignment to handle TypeError which is caused when you try to
divide a number with a non-number (e.g. character).
'''
def calculator(oper,num1,num2):
    if (oper == "add"):
        try:
            result = num1 + num2
        except TypeError:
            result = "TypeError occurred."
    if (oper == "sub"):
        try:
            result = num1 - num2
        except TypeError:
            result = "TypeError occurred."
    if (oper == "multiply"):
        try:
            result = num1 * num2
        except TypeError:
            result = "TypeError occurred."
    if (oper == "divide"):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result =  None
        except TypeError:
            result = "TypeError occurred."
    print result

#calls
calculator("add", 1, 2)
calculator("sub", 1, 2)
calculator("multiply", 1, 2)
calculator("divide",5,2.0)
calculator("divide",5,0)
calculator("divide",5,'a')
calculator("divide",5,"a")
#calculator("divide",5,5⁄2) Doesn't work. Can't send operations as args?

#prints
'''
3
-1
2
2.5
None
TypeError occurred.
TypeError occurred.
'''
