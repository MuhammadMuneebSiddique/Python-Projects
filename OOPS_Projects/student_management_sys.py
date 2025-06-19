
# Create a person class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age       

# create a Subjects
class Subject:
    def __init__(self,id,name,marks):
        self.name = name.lower()
        self.id = id
        self.marks = marks
        self.students = []
        self.teachers = []

    def get_details(self):
        print("Subject Name:",self.name)
        print("Subject Id:",self.id)
        print("Subject Marks:",self.marks)
        print("Subject Students:",self.students)
        print("Subject Teacher:",self.teachers)

# ceating a Students 
class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number
        self.subjects = []
        self.marks = {}

    # Enroll Students in Subject
    def enroll_subject(self,subject:Subject):
        self.subjects.append({"subject_name":subject.name,"subject_marks":subject.marks,"student_obt_marks":0})
        subject.students.append(self.name)

    # Add subject obtained marks in marks object
    def add_marks(self,subject,marks):
        if subject.lower() in [subject_name["subject_name"] for subject_name in self.subjects]:
            for items in self.subjects:
                if subject.lower() in items.values():
                    items["student_obt_marks"] = marks
                    break
        else:
            print(f"{subject} Subject is not found in {self.name} Student Subjects")

    # Ready Student Report
    def get_report_card(self):
        self.total_marks = 0
        self.total_obt_marks = 0
        self.student_subject = []
        for items in self.subjects:
            self.student_subject.append((items["subject_name"],items["student_obt_marks"]))
            self.total_marks += items["subject_marks"]
            self.total_obt_marks += items["student_obt_marks"]
        print(self.student_subject)
        print(f"\n ------ {self.name.upper()} REPORT CARD ------ \n")
        print(" Student Details \n")
        print("Student Name: ",self.name)
        print("Student Age: ",self.age)
        print("Student Roll Number: ",self.roll_number)
        print("\n Student Subjects \n")
        for sub,marks in self.student_subject:
            print(f"{sub.capitalize()} Marks: {marks}")
        print("Total Number: ",self.total_marks)
        print("Student Obtained Marks: ",self.total_obt_marks)
        print(f"Percentage: {(self.total_obt_marks/self.total_marks)*100}")
        if int((self.total_obt_marks/self.total_marks)*100) > 90 and int((self.total_obt_marks/self.total_marks)*100) < 99 :
            print("Grade A++" )
        elif int((self.total_obt_marks/self.total_marks)*100) > 80 and int((self.total_obt_marks/self.total_marks)*100) < 89 :
            print("Grade A+" )
        elif int((self.total_obt_marks/self.total_marks)*100) > 70 and int((self.total_obt_marks/self.total_marks)*100) < 79 :
            print("Grade B")
        elif int((self.total_obt_marks/self.total_marks)*100) > 60 and int((self.total_obt_marks/self.total_marks)*100) < 69:
            print("Grade C")
        elif int((self.total_obt_marks/self.total_marks)*100) > 50 and int((self.total_obt_marks/self.total_marks)*100) < 59:
            print("Grade D")
        else:
            print("Failed")


    # Get Student details
    def get_details(self):
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student Subjects:",self.subjects)
        # print("Student Result:",self.name)


class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.__salary = salary
        self.subjects = []

    def assign_subject(self,subject:Subject):
        self.subjects.append(subject.name)

    def get_details(self):
        print("Teacher Name:",self.name)
        print("Teacher Age:",self.age)
        print("Teacher Subjects:",self.subjects)






# test case
subject_01 = Subject(1,"English",100)
subject_02 = Subject(2,"Math",75)
subject_03 = Subject(3,"Urdu",100)

student_01 = Student("Muneeb",18,13)
student_01.enroll_subject(subject_01)
student_01.enroll_subject(subject_03)
student_01.enroll_subject(subject_02)
student_01.add_marks("english",87)
student_01.add_marks("urdu",70)
student_01.add_marks("math",70)
student_01.get_report_card()
# student_01.get_details()