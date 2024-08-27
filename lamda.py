add_two = lambda x: x + 2
print(add_two(3))  # Output: 5

numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]


nums = [2, 4, 6]
doubled = map(lambda x: x * 2, nums)
print(list(doubled))  # Output: [4, 8, 12]

nums = [1, 2, 3, 4, 5, 6]
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # Output: [2, 4, 6]


points = [(2, 3), (1, 2), (4, 1)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3)]




