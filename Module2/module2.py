"""
In this module, we will learn how to declare variables, understand different data types, perform type conversion, and check variable types in Python.

1. Variables and Constants
What is a Variable?
A variable is a name that refers to a value stored in memory. In Python, variables are created dynamically when a value is assigned to them.

Syntax:

variable_name = value
"""
name = "Alice"   # String variable
age = 25         # Integer variable
height = 5.6     # Float variable
is_student = True  # Boolean variable

print(name, age, height, is_student)

"""
Variable Naming Rules
✅ Must start with a letter (a-z, A-Z) or an underscore _
✅ Can contain letters, digits (0-9), and underscores
✅ Case-sensitive (name and Name are different)
✅ Should not be a Python keyword (e.g., if, while, import)
"""

my_variable = 10
_myVar = "Python"
age_2024 = 30


"""
2name = "John"  # Cannot start with a number
my-variable = 50  # Hyphens are not allowed
if = 25  # 'if' is a keyword

"""

"""
2. Data Types in Python
Python has five primary data types:

Data Type	                           Description	                                  Example
int (Integer)	                        Whole numbers	                            10, -5, 200
float (Floating Point)	                Decimal numbers	                            3.14, -0.5, 2.0
str (String)	                        Sequence of characters	                    "Hello", 'Python'
bool (Boolean)	                        True or False values	                     True, False
NoneType	                            Represents the absence of a value	            None
"""


age = 25  # Integer
price = 19.99  # Float
message = "Hello, World!"  # String
is_python_easy = True  # Boolean
nothing = None  # NoneType

print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(message))   # <class 'str'>
print(type(is_python_easy))  # <class 'bool'>
print(type(nothing))   # <class 'NoneType'>

"""
3. Type Casting (Type Conversion)
Python allows you to convert one data type into another using casting functions:

Function	Converts To
int(x)	Integer
float(x)	Float
str(x)	String
bool(x)	Boolean

"""

num = 10
print(type(num))  # <class 'int'>

num_str = str(num)
print(type(num_str))  # <class 'str'>

pi = "3.14"
pi_float = float(pi)
print(type(pi_float))  # <class 'float'>

"""
Note:
int(3.9) → 3 (Removes decimal)
float("10") → 10.0
bool(0) → False, bool(1) → True
"""

"""
4. Type Checking
Python provides the type() function to check the type of a variable.
"""

x = 42
y = "Python"
z = 3.14

print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>

"""
Additionally, isinstance() can be used to check whether a variable is of a specific type.
"""

print(isinstance(42, int))  # True
print(isinstance("Python", float))  # False
print(isinstance(3.14, (int, float)))  # True (because it's checking both)
