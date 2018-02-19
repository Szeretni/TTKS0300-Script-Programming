#Version 2018-02-19
'''
Write a Python script that mimics the cat UNIX tool. cat reads a given file and prints it’s content
to stdout. In other words, you have to write an application that reads a filename from the command
line arguments (sys.argv list). So if you execute the application from the command line (cmd on
Windows) like this:

python assignment29.py test.txt

contents of test.txt get printed out if the file exists. And if you execute the application like this:

python assignment29.py test2.txt

Contents of the file test2.txt get printed out.

Note that both test.txt and test2.txt have to be in the same folder as assignment29.py.

The whole point with these command line arguments is that you can print out different files without
changing the Python code

Optional:

If no command line arguments are given the program should print an error “not enough arguments”. Hint:
sys.argv is a list (remember len())
If the file is not found or it cannot be read the exception should be handled and an error message
should be printed (the relevant exception is IOError)
'''
import sys

f = open(sys.argv[1],"r") #argument index 1 is the file ie. python assignment29.py players.txt
for line in f:
     line
f.close()

#cmd prints
'''
C:\Users\l2912\Source\Repos\TTKS0300-Script-Programming>python assignment29.py players.txt
Lee Sedol

Park Junghwan

Xie He

Chen Yaoye

Tan Xiao

Iyama Yuta

Piao Wenyao

Gu Li

Kong Jie

Jian Weijie

Zhou Ruiyan

Ida Atsushi

C:\Users\l2912\Source\Repos\TTKS0300-Script-Programming>
'''
