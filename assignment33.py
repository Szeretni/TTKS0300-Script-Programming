'''
#33

Add a function to the previous program called filter_by_course(). The function takes 2 parameters,
the list of Student instances and a course name. The function then returns a list of Student
instances that are on the course specified by the second parameter.

Call the function and print out the names and student IDs of each student on the list returned by
filter_by_course()

Here’s a program to demonstrate the usage of filter_by_course()

students = read_student_data("student_data.txt")
math2_students = filter_by_course(students, "mathematics 2")
# print names and ids of each student in the math2_students list
# you will have to do this part yourself ;)
And here’s the example output with the example file provided in the previous assignment:

josie f5678
alice d22334
HINT: use filter() inside the filter_by_course() function!
'''
import sys

def filter_by_course(objects,name): #list,string
    attending_students = []
    #looping objects
    for o in objects:
        #filtering object's courses by comparing course's name to the parameter "name"
        if filter(lambda x: x==name,o.courses): #if match, doesn't return None ie. False
            #appending attending students info to the list of attendees
            attending_students.append(o.name + " " + o.student_id)
    return attending_students

#<------------- old code from the previous assignment ------------->
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
attendees = filter_by_course(student_data,"mathematics 2")
for a in attendees:
    print a

#print
'''
josie f5678
alice d2233
'''
