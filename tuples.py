my_tuple = (1, 2, 3)
my_tuple[0] = 10  # Error: TypeError: 'tuple' object does not support item assignment


my_tuple = ("a", "b", "c")
print(my_tuple[1])  # Output: b


my_tuple = (1, 2, 2, 3, 3)
print(my_tuple)  # Output: (1, 2, 2, 3, 3)

mixed_tuple = ("Hello", 100, 3.14, [1, 2], (3, 4))


my_tuple = (10, 20, 30)

single_element_tuple = (50,)  # Correct

not_a_tuple = (50)  # Just an integer


empty_tuple = ()


packed_tuple = 1, 2, "three"  # Tuple packing
a, b, c = packed_tuple  # Tuple unpacking
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: three



my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # Output: banana



print(my_tuple[-1])  # Output: cherry


print(my_tuple[0:2])  # Output: ("apple", "banana")

numbers = (1, 2, 2, 3)
print(numbers.count(2))  # Output: 2



fruits = ("apple", "banana", "cherry")
print(fruits.index("banana"))  # Output: 1



def get_point():
    return (3, 4)
x, y = get_point()
print(x, y)  # Output: 3 4



location = {(40.7128, -74.0060): "New York"}
