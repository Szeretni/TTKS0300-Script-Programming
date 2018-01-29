print "function: sumEven(int,int)"
print "#sums parameters and checks if the sum is divisible by 2"
def sumEven(num1,num2):
    temp = num1 + num2
    if (temp % 2) == 0:
        print "Yes, it is!"
    else:
        print "Nope."
