'''
#31 Write a class called Student. The class should the following member variables:

age
name
student_id
The class should have the following methods:

add_course()
list_courses()
add_course() should take the name of the course to be added and list_courses() should return a list
of all the courses that have been added to the that instance of Student.

The initializer should take 3 parameters: age, name and student_id

the class should work so that the following code:

joe = Student("Joe", 25, "f1234")
josie = Student("Josie", 21 "f5678")
print joe.list_courses()
joe.add_course("script programming")
print joe.list_courses()
josie.add_course("network programming")
josie.add_course("mathematics 2")
print josie.list_courses()
produces the following output:

[]
['script programming']
['network programming', "mathematics"]
HINT: You have to define a list as a member variable of student to which you append things with
add_course(). This list should not be passed as a parameter to __init__, but __init__ should create
it.
'''

class Student:
    def __init__(self,age,name,student_id):
        self.age = age
        self.name = name
        self.student_id = student_id
        self.courses = []
    def add_course(self,name):
        self.courses.append(name)
    def list_courses(self):
        print self.courses

#init
joe = Student("Joe", 25, "f1234")
josie = Student("Josie", 21, "f5678")
print joe.list_courses()
joe.add_course("script programming")
print joe.list_courses()
josie.add_course("network programming")
josie.add_course("mathematics 2")
print josie.list_courses()
#produces the following output:
'''
[]
None
['script programming']
None
['network programming', 'mathematics 2']
None
'''
