my_list = [1, 2, 3, "four", 5.0]

empty_list = []

nested_list = [[1, 2, 3], ["a", "b", "c"]]

my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Output: apple
print(my_list[2])  # Output: cherry

print(my_list[-1])  # Output: cherry
print(my_list[-2])  # Output: banana

print(my_list[3])  # Error: IndexError: list index out of range


my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[::2])  # Output: [10, 30, 50]
print(my_list[1::2])  # Output: [20, 40]


my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


my_list.insert(1, "a")
print(my_list)  # Output: [1, "a", 2, 3]


my_list.remove(2)
print(my_list)  # Output: [1, "a", 3]



last_item = my_list.pop()
print(last_item)  # Output: 3
print(my_list)  # Output: [1, "a"]



numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]


numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]



my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]
