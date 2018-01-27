print "Function: reverse(). Parameter is a list."
print "ie. reverse([1,2,3,4])"
def reverse(list):
    number = 0
    for item in list:
        number += 1
    while number>0:
        remove = list.pop(number-1) # to avoid out of range 
        list.append(remove)
        number -= 1
    print list
        
    
    
