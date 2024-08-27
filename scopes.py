def my_function():
    local_var = 10  # Local variable
    print(local_var)

my_function()
print(local_var)  # Error: local_var is not defined outside the function


global_var = 20  # Global variable

def my_function():
    print(global_var)  # Accessing global variable within a function

my_function()  # Output: 20
print(global_var)  # Output: 20




counter = 0  # Global variable

def increment():
    global counter
    counter += 1

increment()
print(counter)  # Output: 1


def outer_function():
    outer_var = "I'm outside!"
    
    def inner_function():
        print(outer_var)  # Accessing the outer function's variable
    
    inner_function()

outer_function()  # Output: I'm outside!



def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()  # Output: inner: nonlocal, outer: nonlocal
