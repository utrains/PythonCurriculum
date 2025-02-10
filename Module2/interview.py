"""
1. What is Dynamic Typing in Python?
Answer:
Python uses dynamic typing, which means you don’t need to declare a variable’s data type explicitly. The type is assigned based on the value.
"""

x = 10  # x is an integer
x = "Python"  # Now x is a string (allowed in Python)


"""
2. How Do You Check the Data Type of a Variable?
Answer:
We use the type() function to check the data type of a variable.
"""

x = 100
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
