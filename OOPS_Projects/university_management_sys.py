
# Person Class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
# Student Class
class Student(Person):
    def __init__(self, name, age , roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number
        self.course = []

    def register_course(self,course):
        self.course.append(course.course_name)
        course.students.append(self.name)

    def get_details(self):
        print("Student Name",self.name)
        print("Student Age",self.age)
        print("Student Roll Number",self.roll_number)
        print("Student Course",self.course)

# Instructor Class
class Instructor(Person):
    def __init__(self, name, age , salary):
        super().__init__(name,age)
        self.salary = salary
        self.course = []

    def register_course(self,course):
        self.course.append(course.course_name)
        course.instructors.append(self.name)

    def get_details(self):
        print("Instructor Name",self.name)
        print("Instructor Age",self.age)
        print("Instructor Salary",self.salary)
        print("Instructor Course",self.course)

# Department Class
class Department():
    def __init__(self,name):
        self.deprtment_name = name
        self.course = []

    def add_course(self,course):
        self.course.append(course.course_name)

    def get_details(self):
        print("Department Name :",self.deprtment_name)
        print("Course :",self.course)

# Cousres Class
class Course():
    def __init__(self,id,course):
        self.id = id
        self.course_name = course
        self.instructors = []
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def add_instructor(self,instructor):
        self.instructors.append(instructor)

    def get_details(self):
        print("Course Id :",self.id)
        print("Course Name :",self.course_name)
        print("Course Students :",self.students)
        print("Course Instructors :",self.instructors)

d1 = Department("Agentic AI")
c1 = Course(1,"AI")
c2 = Course(1,"Cloud Native")
d1.add_course(c1)
d1.add_course(c2)
d1.get_details()

s1 = Student("Muneeb",17,23)
s1.register_course(c1)
s1.get_details()
c1.get_details()



