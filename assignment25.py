#Version 2018-02-19
'''
Add a "divide" operation to your calculator from the previous assignment and make sure it can handle
division by zero(use try and except). If a division by zero occurs return None. What happens when you
try to divide 5⁄2? Try to come up with a reason why the result is a bit off. Note: Returning None
like this is usually not the correct choice, but in this case it is done for simplicity.
'''
def calculator(oper,num1,num2):
    if (oper == "add"):
        result = num1 + num2
    if (oper == "sub"):
        result = num1 - num2
    if (oper == "multiply"):
        result = num1 * num2
    if (oper == "divide"):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result =  None
    print result

#calls
calculator("divide",5,2.0)
calculator("divide",5,0)
#calculator("divide",5,5⁄2) Doesn't work. Can't send operations as args?

#prints
'''
2.5
None
'''
