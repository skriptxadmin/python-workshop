class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        return
    def fullname(self):
        return self.fname+" "+self.lname
    
stu = Person("Alaksandar", "Jesus")

print(stu.fullname())