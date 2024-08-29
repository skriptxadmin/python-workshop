class Person:
    def __init__(self):
        
        return
    def gender_text(self):
        if self.gender == 1:
            return 'Male'
        elif self.gender == 2:
            return 'Female'
        else:
            return 'Unknown'
    def designation(self):
        return "Employee"

class Student(Person):
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        return
    def designation(self):
        return "Student"
    
class Teacher(Person):
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        return

class OfficeStaff(Person):
    def __init__(self, fname, lname, gender):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        return
    

stu = Student("Alaksandar", "Jesus Gene", 1)
teacher = Teacher("Jane", "Doe", 2)
coordinator = OfficeStaff("John", "Doe", 1)

print(stu.designation())

print(teacher.designation())

print(coordinator.designation())
