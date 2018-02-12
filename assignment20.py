def division(num1,num2):
    try:
        var = num1/num2
        print var
    except ZeroDivisionError:
        print "Divided by zero!"
    except TypeError:
        print "One or both of your parameters are wrong type!"

def call():
    try:
        division(4,"a",3)
    except:
        print "Wrong amount of parameters"

call()
'''
>>> call()
Wrong amount of parameters
'''
