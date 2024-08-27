student = {
"name": "John",
"age": 20,
"courses": ["Math", "Science"]
}


print(student["name"])  # Output: John


print(student.get("age"))  # Output: 20

print(student.get("grade", "Not Available"))  # Output: Not Available

print(student["name"])  # Output: John

print(student.get("age"))  # Output: 20

print(student.get("grade", "Not Available"))  # Output: Not Available

student["grade"] = "A"

print(student)  # Output: {'name': 'John', 'age': 20, 'courses': ['Math', 'Science'], 'grade': 'A'}


student["age"] = 21

print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'Science'], 'grade': 'A'}

age = student.pop("age")
print(age)  # Output: 21
print(student)  # Output:


del student["age"]
print(student)  # Output: {'name': 'John', 'courses': ['Math', 'Science']}


last_item = student.popitem()
print(last_item)  # Output: ('courses', ['Math', 'Science'])
print(student)  # Output: {'name': 'John'}



student.clear()
print(student)  # Output: {}



keys = student.keys()
print(keys)  # Output: dict_keys(['name'])


values = student.values()
print(values)  # Output: dict_values(['John'])


items = student.items()
print(items)  # Output: dict_items([('name', 'John')])

student.update({"age": 22, "grade": "B"})
print(student)  # Output: {'name': 'John', 'age': 22, 'grade': 'B'}







