class Student:

    total_student = 0

    def __init__(self , name, email):
        if not Student.check_email(email):
            raise ValueError("Please enter a valid")
        self.email = email
        self.name = name
        self.course = []

    def enroll(self,course):
        self.course.append(course)
        Student.total_student += 1

    @classmethod
    def students(cls):
        print(f"Total Student is {cls.total_student}")

    @staticmethod
    def check_email(email):
        return "@" in email and "." in email
    

s1 = Student("Muneeb","muneeb@gmailcom")
s1.enroll("AI Agent")
s1.students()