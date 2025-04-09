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

🐧 Linux (Ubuntu) or 🖥️ macOS:

Check version:
python3 --version

If not installed:
# For Ubuntu/Debian
sudo apt install python3

# For macOS (using Homebrew)
brew install python

🔹 4. Writing and Running Your First Python Script

print("Hello, World!")

Save this code in a file called hello.py and run it using:

python hello.py

🔹 5. Basic Arithmetic Operations in Python

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


🔹 6. Introduction to print() and input() Functions
✅ print() – Display Output:

print("Welcome to Python!")
print("My name is John.")
print("The sum of 5 and 3 is:", 5 + 3)

✅ input() – Take User Input:

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")

🔹 7. Simple Interactive Program
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Converting input to integers
num1 = int(num1)
num2 = int(num2)

print("Sum:", num1 + num2)

💡 Why convert to int?
The input() function returns a string. Arithmetic operations require numeric types like int or float.

### 🟢 **Module 2: Variables, Data Types & Type Casting**

---

#### 🔹 1. Variables and Constants

A **variable** is a name that refers to a value stored in memory. In Python, variables are dynamically created when a value is assigned.

**🔧 Syntax:**
```python
variable_name = value


🧪 Example:
name = "Alice"         # String variable
age = 25               # Integer variable
height = 5.6           # Float variable
is_student = True      # Boolean variable

print(name, age, height, is_student)


🔹 Variable Naming Rules
✅ Must start with a letter (a-z, A-Z) or underscore _
✅ Can include letters, numbers (0-9), and underscores
✅ Case-sensitive (Name and name are different)
✅ Cannot use Python reserved keywords (if, while, import, etc.)

✅ Valid Examples:

my_variable = 10
_myVar = "Python"
age_2024 = 30

❌ Invalid Examples:

2name = "John"      # Cannot start with a number
my-variable = 50    # Hyphens are not allowed
if = 25             # 'if' is a reserved keyword

🔹 2. Data Types in Python
Python provides built-in types to store different kinds of values.

