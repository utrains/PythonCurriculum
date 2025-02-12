"""Module 6: Lists in Python (Ordered & Mutable)"""

"""
Introduction to Lists
A list in Python is an ordered, mutable collection that can hold multiple data types. 
Lists allow modification of their elements and support various operations to manipulate and organize data efficiently.
"""

"""
Creating a List
A list is created using square brackets [] and can contain integers, strings, floats, or even other lists.
"""

# Creating an empty list
empty_list = []

# List with different data types
mixed_list = [10, "Python", 3.14, True]

# Nested list
nested_list = [[1, 2, 3], ["a", "b", "c"]]

print(mixed_list)
print(nested_list)


"""
Accessing Elements (Indexing & Slicing)
Indexing: Access elements using their index (0 for the first, -1 for the last).
Slicing: Extract multiple elements using start:end:step.
"""

numbers = [10, 20, 30, 40, 50]

# Accessing first and last elements
print(numbers[0])   # 10
print(numbers[-1])  # 50

# Slicing a sublist
print(numbers[1:4])    # [20, 30, 40]
print(numbers[:3])     # [10, 20, 30]
print(numbers[::2])    # [10, 30, 50] (Every second element)


"""
Modifying and Updating Lists
Lists are mutable, meaning we can update their elements directly.
"""

#Example: Modifying Lists

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # Changing "banana" to "blueberry"

print(fruits)

"""
Common List Methods
"""
"""append() – Add an Element at the End"""

fruits = ["apple", "banana"]
fruits.append("cherry")

print(fruits)

"""extend() – Extend a List with Another List"""

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])

print(numbers)

"""insert() – Insert an Element at a Specific Position"""

colors = ["red", "blue", "green"]
colors.insert(1, "yellow")  # Insert "yellow" at index 1

print(colors)

"""remove() – Remove a Specific Element"""

animals = ["cat", "dog", "rabbit"]
animals.remove("dog")

print(animals)

"""pop() – Remove and Return an Element (Default Last Element)"""

numbers = [10, 20, 30, 40]
removed_element = numbers.pop(2)  # Removes element at index 2

print(numbers)
print("Removed:", removed_element)

"""sort() – Sort Elements in Ascending Order"""

scores = [50, 30, 40, 10, 20]
scores.sort()

print(scores)

"""reverse() – Reverse the Order of Elements"""

nums = [1, 2, 3, 4, 5]
nums.reverse()

print(nums)

"""count() – Count Occurrences of an Element"""

numbers = [1, 2, 3, 1, 4, 1, 5]
print(numbers.count(1))

"""index() – Find the First Index of an Element"""
names = ["Alice", "Bob", "Charlie", "Alice"]
print(names.index("Alice"))

"""copy() – Copy a List (Shallow Copy)"""

original_list = [1, 2, 3]
copied_list = original_list.copy()

print(copied_list)


"""List Comprehension"""

"""List comprehension provides a concise way to create lists.
Example: Creating a List of Squares"""

squares = [x**2 for x in range(1, 6)]
print(squares)


"""Example: Filtering Even Numbers"""

numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]

print(evens)
