# contains the data and methods in one single object
# the data can be public or private

class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        # self.__age = age  # throws error since it goes to private by prefixing __
        return
    def fullname(self):
        return self.fname+" "+self.lname
    
stu = Person("Alaksandar", "Jesus", 25)

print(stu.age)