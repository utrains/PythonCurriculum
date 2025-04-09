# 📘 Python Fundamentals Course

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