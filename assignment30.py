#Hannu Oksman 2018-03-12
'''
Write a Python script that acts a simple calculator. The script should present the user with a list
of numbered actions to perform (addition, substraction, division or multiplication) and two numbers
afer that.

If the user inputs an invalid choice the program should print an error and prompt the user to try
again. If the user inputs anything else than numbers the program should print an error and prompt
the user to try again. If the user attempts to divide by zero the program should print an error
message. Print the result as a float If the user inputs -1 when choosing the action, the program
should terminate. Try to utilize the fact that Python has functions as first class values! You can
for example place anonymous functions inside a variables and call them or use reduce function.

Example execution:

0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 0
number: 1
number: 2
The result is: 3.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 2
number: 5
number: 5
The result is: 25.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: -1
'''
#main
def main():
    menu()
    print "Bye."

#menu
def menu():
    menuSelection = 0
    while True:
        try:
            menuSelection = int(raw_input("0) add\n1) sub\n2) multiply\n3) divide\n-1) quit\nchoice: "))
        except ValueError:
            print "You didn't enter integer. Please try again."
        else:
            if menuSelection is -1:
                break
            elif menuSelection < -1 or menuSelection > 3:
                print "Integer isn't valid. Please try again."
            else:
                nums(menuSelection)

#user's numbers
def nums(menuSelection):
    try:
        float1 = float(raw_input("number: "))
        float2 = float(raw_input("number: "))
    except ValueError:
        print "ValueError"
    else:
        calcs(menuSelection,float1,float2)

#calculations
def calcs(menuSelection,float1,float2):
    f = 0
    if menuSelection is 0:
        f = lambda x,y: x+y
    elif menuSelection is 1:
        f = lambda x,y: x-y
    elif menuSelection is 2:
        f = lambda x,y: x*y
    elif menuSelection is 3:
        f = lambda x,y: x/y
    try:
        lambdaStr = "{:.6f}".format(f(float1,float2)) #precision source: https://stackoverflow.com/questions/15263597/convert-floating-point-number-to-certain-precision-then-copy-to-string
        print "The result is: " + lambdaStr
    except ZeroDivisionError:
        print "ZeroDivisionError"

#init
main()

#print
'''
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 0
number: 1.2346
number: -5
The result is: -3.765400
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 1
number: 6464687
number: 4667
The result is: 6460020.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 2
number: 5
number: 5
The result is: 25.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 3
number: 5
number: 0
ZeroDivisionError
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: 3
number: 65467
number: 0.00004
The result is: 1636675000.000000
0) add
1) sub
2) multiply
3) divide
-1) quit
choice: -1
Bye.
'''
