'''
#32

Use the Student class created in the previous assignment and create a program that reads a list of
students from a file and instantiates Student objects based on the data in the file. The data in the
file should be formatted like this:

name;age;student_id;course1,course2,course3
In other words each line contains information for a single student separated by a semicolon (;). The
last section contains a list of courses that the student is participating in separated by a comma
(,).

Write a function called read_student_data() that takes a single parameter. The parameter should be
the filename from which to read the student data. The function should read each line of the file
and create an instance of Student based on the data in that line. After the Student instance is
created it should be placed to a list called students and that list should be returned to the
caller of the function.

The function should be called and the returned list should be used to print out the name and
student id of each student in the list.

Here is an example student-data.txt file:

joe;20;f1234;script programming,physics 1,nose picking 101
josie;21;f5678;script programming,mathematics 2,german 1
adam;22;f1122;mathematics 1,physics 2,german 1
alice;22;d2233;mathematics 2,physics 2,german 2
bob;23;d3344;mathematics 3,physics 3,algorithms and data structures
Here’s an example output from the finished program:

joe f1234
josie f5678
adam f1122
alice d2233
bob d3344
'''
import sys

class Student:
    def __init__(self,name,age,student_id):
        self.age = age
        self.name = name
        self.student_id = student_id
        self.courses = []
    def add_course(self,name):
        self.courses.append(name)
    def list_courses(self):
        print self.courses

def read_student_data(filename):
    listOfStudents = []
    #open file
    f = open(filename,"r")
    #manipulating content of the file
    for l in f:
        #removing newline \n
        line = l.strip()
        #splitting each line by ; to a list of four elements (name,age,student_id,courses)
        split = line.split(";")
        #appending new student object to list of students
        #0 = name, 1 = age, 2  = student_id
        listOfStudents.append(Student(split[0],split[1],split[2]))
        #creating a list of courses from the courses-string
        courses = split[3].split(",")
        #adding courses for the student by calling student-class' method
        for c in courses:
            listOfStudents[-1].add_course(c) #-1 = the last element of the list, in this case the most recent
    #end of file operations
    f.close()
    return listOfStudents

def formatted_print(listOfObjects):
    for o in student_data:
        sys.stdout.write(o.name + " " + o.student_id + " ") #to avoid newline
        o.list_courses()
    

#init
student_data = read_student_data("student_data.txt")
formatted_print(student_data)




#print
'''
joe f1234 ['script programming', 'physics 1', 'nose picking 101']
josie f5678 ['script programming', 'mathematics 2', 'german 1']
adam f1122 ['mathematics 1', 'physics 2', 'german 1']
alice d2233 ['mathematics 2', 'physics 2', 'german 2']
bob d3344 ['mathematics 3', 'physics 3', 'algorithms and data structures']
'''
