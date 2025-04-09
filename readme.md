# 📘 Utrains :- Python Fundamentals Course

## 📌 Course Overview
This course covers the fundamentals of Python programming, starting from basic syntax to file handling. Each module includes conceptual understanding, examples, and exercises.

---

## 📚 Course Modules

### 🟢 **Module 1: Introduction to Python**

---

#### 🔹 1. What is Python?

Python is a high-level, interpreted programming language developed by **Guido van Rossum** in 1991. It is widely used in web development, data analysis, AI/ML, automation, and more.

**Key Characteristics:**
- ✔️ Simple and readable syntax
- ✔️ Interpreted language (no need to compile)
- ✔️ Dynamically typed
- ✔️ Cross-platform support
- ✔️ Rich standard libraries

---

#### 🔹 2. Why Python? (Features and Applications)

**Advantages:**
- ✅ Easy to learn
- ✅ Platform-independent
- ✅ Interactive and interpreted
- ✅ Extensive community support
- ✅ Huge collection of libraries and frameworks

**Popular Use Cases:**
- 🌐 Web Development – *Django, Flask*
- 📊 Data Science & ML – *Pandas, NumPy, TensorFlow*
- 🤖 Automation & Scripting
- 🎮 Game Development – *Pygame*
- 🔐 Cybersecurity & Ethical Hacking

---

#### 🔹 3. Installing Python and Setting Up Environment

**🔧 Windows:**
- Download Python from [https://www.python.org](https://www.python.org)
- Run the installer and **check the box**: ✅ *Add Python to PATH*
- Open Command Prompt and verify installation:

```bash
python --version
```
🐧 Linux (Ubuntu) or 🖥️ macOS:

Check version:
```bash
python3 --version
```

If not installed:
# For Ubuntu/Debian
```bash
sudo apt install python3
```
# For macOS (using Homebrew)
```bash
brew install python
```

🔹 4. Writing and Running Your First Python Script
```python
print("Hello, World!")
```

Save this code in a file called hello.py and run it using:
```python
python hello.py
```

🔹 5. Basic Arithmetic Operations in Python

```python
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
```

🔹 6. Introduction to print() and input() Functions

✅ print() – Display Output:
```python
print("Welcome to Python!")
print("My name is John.")
print("The sum of 5 and 3 is:", 5 + 3)
```

✅ input() – Take User Input:
```python
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")
```
🔹 7. Simple Interactive Program
```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
```

# Converting input to integers
```python
num1 = int(num1)
num2 = int(num2)

print("Sum:", num1 + num2)
```

💡 Why convert to int?
The input() function returns a string. Arithmetic operations require numeric types like int or float.

### 🟢 **Module 2: Variables, Data Types & Type Casting**

---

#### 🔹 1. Variables and Constants

A **variable** is a name that refers to a value stored in memory. In Python, variables are dynamically created when a value is assigned.

**🔧 Syntax:**
```python
variable_name = value
```

🧪 Example:

```python
name = "Alice"         # String variable
age = 25               # Integer variable
height = 5.6           # Float variable
is_student = True      # Boolean variable

print(name, age, height, is_student)
```

🔹 Variable Naming Rules
✅ Must start with a letter (a-z, A-Z) or underscore _
✅ Can include letters, numbers (0-9), and underscores
✅ Case-sensitive (Name and name are different)
✅ Cannot use Python reserved keywords (if, while, import, etc.)

✅ Valid Examples:
```python
my_variable = 10
_myVar = "Python"
age_2024 = 30
```
❌ Invalid Examples:
```python
2name = "John"      # Cannot start with a number
my-variable = 50    # Hyphens are not allowed
if = 25             # 'if' is a reserved keyword
```

🔹 2. Data Types in Python
Python provides built-in types to store different kinds of values.

| Data Type   | Description                         | Example       |
|:------------|:------------------------------------|:--------------|
| `int`       | Whole numbers                       | `10`, `-5`    |
| `float`     | Decimal numbers                     | `3.14`, `2.0` |
| `str`       | Sequence of characters (strings)    | `"Hello"`     |
| `bool`      | Boolean values                      | `True`, `False` |
| `NoneType`  | Represents the absence of a value   | `None`        |

🧪 Examples:
```python
age = 25                 # int
price = 19.99            # float
message = "Hello"        # str
is_python_easy = True    # bool
nothing = None           # NoneType

print(type(age))
print(type(price))
print(type(message))
print(type(is_python_easy))
print(type(nothing))
```

### 🔄 3. Type Casting (Type Conversion)

Python allows converting between data types using casting functions.

| Function     | Description             | Example                  |
|--------------|-------------------------|--------------------------|
| `int(x)`     | Converts to Integer     | `int(3.9)` → `3`         |
| `float(x)`   | Converts to Float       | `float("10")` → `10.0`   |
| `str(x)`     | Converts to String      | `str(123)` → `"123"`     |
| `bool(x)`    | Converts to Boolean     | `bool(0)` → `False`      |


🧪 Example:
```python
num = 10
print(type(num))     # <class 'int'>

num_str = str(num)
print(type(num_str)) # <class 'str'>

pi = "3.14"
pi_float = float(pi)
print(type(pi_float)) # <class 'float'>
```
ℹ️ Notes:

int(3.9) → 3 (decimal removed)

float("10") → 10.0

bool(0) → False, bool(1) → True

🔹 Why Type Casting is Important with input()
The input() function always returns a string, even for numeric inputs. You need type casting to perform arithmetic.

🚫 Incorrect way (no casting):
```python
num1 = input("Enter first number: ")  # User enters 5
num2 = input("Enter second number: ") # User enters 3
print("Sum:", num1 + num2)  # Output: 53 (string concatenation)
```

✅ Correct way using int():
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)  # Output: 8
```

✅ For decimal inputs using float():
```python
num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))
print("Sum:", num1 + num2)
```

🔹 4. Type Checking
Python provides type() to check the variable's type and isinstance() to verify it against a specific type or tuple of types.

🧪 Example:
```python
x = 42
y = "Python"
z = 3.14
```
```python
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'float'>
```
```python
print(isinstance(42, int))             # True
print(isinstance("Python", float))     # False
print(isinstance(3.14, (int, float)))  # True
```


### 🟣 Module 3: Strings in Python

---

#### 1️⃣ Introduction to Strings

A **string** in Python is a sequence of characters enclosed within single (`'`), double (`"`), or triple (`'''` or `"""`) quotes.

**Key Properties of Strings**  
✅ Immutable: Strings cannot be modified once created  
✅ Indexed: Characters can be accessed using positive and negative indices  
✅ Iterable: Strings can be looped through character by character  

---

#### 2️⃣ Creating Strings in Python

Python allows multiple ways to create a string:

```python
# Using single, double, and triple quotes
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline 
string using triple quotes.'''

print(str1, str2, str3)
```

3️⃣ String Indexing and Slicing


### 🔹 String Indexing Table

| Characters         | P  | Y  | T  | H  | O  | N  |
|--------------------|----|----|----|----|----|----|
| Forward Indexing   | 0  | 1  | 2  | 3  | 4  | 5  |
| Reverse Indexing   | -6 | -5 | -4 | -3 | -2 | -1 |

String Indexing:
```python
word = "Python"
print(word[0])    # P (First character)
print(word[-1])   # n (Last character)
```

String Slicing:
```python
word = "Programming"
print(word[0:5])    # Output: Progr (0 to 4)
print(word[:6])     # Output: Progra (0 to 5)
print(word[3:])     # Output: gramming (from index 3 to end)
print(word[::2])    # Output: Pormig (every 2nd character)
print(word[::-1])   # Output: gnimmargorP (Reversed string)
```

4️⃣ Built-in String Methods (Raw Markdown Table)

| Method               | Description                                         |
|----------------------|-----------------------------------------------------|
| `capitalize()`       | Capitalizes first letter                            |
| `casefold()`         | Converts to lowercase (more aggressive)             |
| `center(width)`      | Centers string in a given width                     |
| `count(substring)`   | Counts occurrences of a substring                   |
| `encode()`           | Converts string to bytes                            |
| `endswith(suffix)`   | Checks if string ends with the given suffix         |
| `expandtabs(size)`   | Replaces tabs with spaces                           |
| `find(substring)`    | Returns the index of first occurrence               |
| `index(substring)`   | Same as find but raises error if not found          |
| `isalnum()`          | Checks if all characters are alphanumeric           |
| `isalpha()`          | Checks if all characters are letters                |
| `isdigit()`          | Checks if all characters are digits                 |
| `islower()`          | Checks if all characters are lowercase              |
| `isspace()`          | Checks if all characters are whitespace             |
| `istitle()`          | Checks if string is title-cased                     |
| `isupper()`          | Checks if all characters are uppercase              |
| `join(iterable)`     | Joins elements of an iterable with the string       |
| `ljust(width)`       | Left-aligns string within given width               |
| `lower()`            | Converts to lowercase                               |
| `lstrip()`           | Removes leading whitespace                          |
| `replace(old, new)`  | Replaces old substring with new                     |
| `rfind(substring)`   | Finds last occurrence of substring                  |
| `rindex(substring)`  | Like rfind, but raises error if not found           |
| `rjust(width)`       | Right-aligns string                                 |
| `rstrip()`           | Removes trailing whitespace                         |
| `split(sep)`         | Splits string into list                             |
| `splitlines()`       | Splits string at line breaks                        |
| `startswith(prefix)` | Checks if string starts with given prefix           |
| `strip()`            | Removes leading/trailing whitespace                 |
| `swapcase()`         | Swaps case of all characters                        |
| `title()`            | Converts to title case                              |
| `upper()`            | Converts to uppercase                               |
| `zfill(width)`       | Pads string with zeros                              |


5️⃣ String Methods and Functions
```python
# Finding String Length
text = "Python"
print(len(text))  # Output: 6

# Changing Case
text = "hello world"
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world
print(text.title())       # Hello World
print(text.capitalize())  # Hello world

# Checking String Content
print("Python".isalpha())    # True
print("1234".isdigit())      # True
print("Hello123".isalnum())  # True
print("   ".isspace())       # True

# Searching in Strings
text = "Python programming"
print(text.find("prog"))  # Output: 7
print(text.count("o"))    # Output: 2

# Replacing and Splitting
text = "I love Python"
print(text.replace("love", "like"))  # I like Python

words = text.split()
print(words)  # ['I', 'love', 'Python']

joined = "-".join(words)
print(joined)  # I-love-Python

# Checking Prefix and Suffix
text = "hello.py"
print(text.startswith("hello"))  # True
print(text.endswith(".py"))      # True

# Stripping Whitespace
text = "  hello  "
print(text.strip())   # 'hello'
print(text.lstrip())  # 'hello  '
print(text.rstrip())  # '  hello'
```

6️⃣ String Formatting

```python
# Using format()
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```
```python
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
```

7️⃣ Escape Sequences

| Escape Sequence | Meaning     |
|------------------|-------------|
| `\n`             | Newline     |
| `\t`             | Tab         |
| `\\`             | Backslash   |

```python
print("Hello\nWorld")  # Newline
print("Name:\tAlice")  # Tab
```

8️⃣ Raw Strings

```python
# Raw strings ignore escape sequences
print(r"C:\newfolder\test")  # Output: C:\newfolder\test
```




### 🟣 Module 4: Operators and Expressions

# 🎯 Module 4: Operators and Expressions

Operators are symbols that perform operations on variables and values.  
Expressions are combinations of values, variables, and operators that produce a result.

In this module, we will explore different types of operators in Python and how they work.

---

## ➕ 1. Arithmetic Operators

These operators perform mathematical operations like addition, subtraction, multiplication, and division.

```python
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

```

| Operator        | Symbol | Example   | Result                            |
|----------------|--------|-----------|-----------------------------------|
| Addition        | +      | 10 + 5    | 15                                |
| Subtraction     | -      | 10 - 5    | 5                                 |
| Multiplication  | *      | 10 * 5    | 50                                |
| Division        | /      | 10 / 3    | 3.3333                            |
| Floor Division  | //     | 10 // 3   | 3 (Removes decimal part)         |
| Modulus         | %      | 10 % 3    | 1 (Remainder)                    |
| Exponentiation  | **     | 2 ** 3    | 8 (2³)                            |


🧮 2. Comparison (Relational) Operators
These operators return True or False based on a condition.

```python
x = 10
y = 5

print(x > y)    # True
print(x < y)    # False
print(x == 10)  # True
print(y != 5)   # False
```

| Operator | Meaning                      | Example   | Result |
|----------|------------------------------|-----------|--------|
| ==       | Equal to                     | 5 == 5    | True   |
| !=       | Not equal to                 | 5 != 3    | True   |
| >        | Greater than                 | 10 > 5    | True   |
| <        | Less than                    | 2 < 5     | True   |
| >=       | Greater than or equal to     | 3 >= 3    | True   |
| <=       | Less than or equal to        | 4 <= 2    | False  |


⚙️ 3. Logical Operators
Used to combine multiple conditions.

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```


| Operator | Meaning                                     | Example                          | Result |
|----------|---------------------------------------------|----------------------------------|--------|
| and      | Returns True if both conditions are True    | (5 > 2) and (10 > 3)             | True   |
| or       | Returns True if at least one is True        | (5 > 2) or (10 < 3)              | True   |
| not      | Reverses the Boolean result                 | not (5 > 2)                      | False  |


📝 4. Assignment Operators
Used to assign or modify values of variables.

```python
x = 10
x += 5  # x = x + 5
print(x)  # 15

x *= 2  # x = x * 2
print(x)  # 30
```

| Operator | Meaning                    | Example   | Equivalent To   |
|----------|----------------------------|-----------|-----------------|
| =        | Assign value               | x = 10    | x = 10          |
| +=       | Add & assign               | x += 5    | x = x + 5       |
| -=       | Subtract & assign          | x -= 3    | x = x - 3       |
| *=       | Multiply & assign          | x *= 2    | x = x * 2       |
| /=       | Divide & assign            | x /= 2    | x = x / 2       |
| //=      | Floor divide & assign      | x //= 2   | x = x // 2      |
| %=       | Modulus & assign           | x %= 3    | x = x % 3       |
| **=      | Exponentiate & assign      | x **= 2   | x = x ** 2      |



🧭 5. Identity and Membership Operators
🧠 Identity Operators
Check if two variables reference the same object in memory.

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True
print(a is c)   # False
print(a == c)   # True
```

| Operator | Meaning                          | Example     |
|----------|----------------------------------|-------------|
| is       | True if objects are identical    | x is y      |
| is not   | True if objects are not same     | x is not y  |


📦 Membership Operators
Used to check if a value exists in a collection.

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)     # True
print("grape" not in fruits)  # True

```

| Operator | Meaning                                 | Example              |
|----------|-----------------------------------------|----------------------|
| in       | True if value exists in the sequence    | 'a' in 'apple'       |
| not in   | True if value does not exist            | 5 not in [1, 2, 3]   |



