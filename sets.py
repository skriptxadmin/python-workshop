my_set = {1, 2, 3, 4, 5}

my_set = {1, 2, 2, 3}  # Result: {1, 2, 3}

my_set = {1, 2, 3}
another_set = set([4, 5, 6])

empty_set = set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}


symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set)  # Output: {1, 2, 4, 5}


small_set = {1, 2}
print(small_set.issubset(set1))  # Output: True
print(set1.issuperset(small_set))  # Output: True


my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 6}



my_set.remove(3)
my_set.discard(7)  # No error if 7 is not present


popped_element = my_set.pop()
print(popped_element)  # Output: 1 (or another element)
print(my_set)  # Output: Remaining elements



my_set.clear()
print(my_set)  # Output: set()



new_set = my_set.copy()
print(new_set)  # Output: {2, 3, 4, 5} (or whatever elements were in `my_set`)


my_set.update([7, 8])
print(my_set)  # Output: {1, 2, 3, 4, 5, 7, 8}






