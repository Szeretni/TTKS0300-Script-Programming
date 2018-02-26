#Version 2018-02-19
'''
Extend the function in the previous assignment to handle TypeError which is caused when you try to
divide a number with a non-number (e.g. character).
'''
def calculator(oper,num1,num2):
    try:
        if (oper == "add"):
            result = num1 + num2
        elif (oper == "sub"):
            result = num1 - num2
        elif (oper == "multiply"):
            result = num1 * num2
        elif (oper == "divide"):
            result = num1 / num2
    except TypeError:
            result = "TypeError occurred."
    except ZeroDivisionError:
            result =  None
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
