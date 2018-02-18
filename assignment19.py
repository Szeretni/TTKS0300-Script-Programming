#Version 2018-02-12
def division(num1,num2):
    try:
        var = num1/num2
        print var
    except ZeroDivisionError:
        print "Divided by zero!"
    except TypeError:
        print "One or both of your parameters are wrong type!"

#call
division(4,"a")

#prints
'''
One or both of your parameters are wrong type!
>>> 
'''
