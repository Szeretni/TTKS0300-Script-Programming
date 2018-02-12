def division(num1,num2):
    try:
        var = num1/num2
        print var
    except ZeroDivisionError:
        print "Divided by zero!"

'''
>>> division(4,0)
Divided by zero!
>>> division(4,2)
2
>>> 
'''
