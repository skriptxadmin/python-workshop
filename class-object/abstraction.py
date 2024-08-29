from abc import ABC, abstractmethod

class Human():
   def __init__(self):
      pass

class Person(ABC):
   @abstractmethod
   def final_mark(self):
        grace_mark = 5
        # print(self.mark+grace_mark)
        return self.mark+grace_mark
   def designation(self):
        return "Employee"

class Student(Person):
    def __init__(self, fname, lname, mark):
        self.mark = mark
        pass
    def final_mark(self):
        result = super().final_mark()
        return result
      
# obj = Human() # does not throw error
# print(obj)

# obj = Person()  # throws error, means not accessible
# print(obj)

stu = Student("John", "Doe", 40)

print(stu.mark)

print(stu.final_mark())

print(stu.designation())
