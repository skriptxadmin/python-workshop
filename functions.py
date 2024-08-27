def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(5,3))

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)

def greet(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")

greet("Charlie")  # Uses default age


def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # Output: 20


def divide(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

q, r = divide(10, 3)
print(q, r)  # Output: 3 1


