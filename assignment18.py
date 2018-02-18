#Version 2018-02-12
def division(num1,num2):
    try:
        var = num1/num2
        print var
    except ZeroDivisionError:
        print "Tried to divide by zero!"
        
#call
division(4,0)
division(4,2)

#prints
'''
Tried to divide by zero!
2
'''
