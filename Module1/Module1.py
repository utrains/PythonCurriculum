"""Module 1: Introduction to Python"""

"""
Introduction to Python

1. What is Python?
Python is a high-level, interpreted programming language developed by Guido van Rossum in 1991. It is widely used for web development, data analysis, artificial intelligence, automation, and more.

Key characteristics of Python:
✔️ Readable and simple syntax
✔️ Interpreted (no need to compile before running)
✔️ Dynamically typed (no need to declare variable types)
✔️ Cross-platform (runs on Windows, macOS, Linux, etc.)
✔️ Large standard library for various tasks

"""

"""
2. Why Python? (Features and Applications)
Python is popular due to its:

✅ Ease of Learning: Simple syntax similar to English
✅ Portability: Runs on multiple platforms
✅ Interpreted Nature: Executes line by line, making debugging easier
✅ Extensive Libraries: Includes NumPy, Pandas, TensorFlow, etc.
✅ Object-Oriented: Supports classes and objects

Applications of Python:

Web Development (Django, Flask)
Data Science & Machine Learning (Pandas, TensorFlow)
Automation & Scripting (Automate repetitive tasks)
Game Development (Pygame)
Cybersecurity (Penetration testing)
"""

"""
3. Installing Python and Setting Up Environment
Windows:
Download Python from Python.org
Run the installer and select "Add Python to PATH"
Verify installation by running:

python --version

Mac/Linux:
Pre-installed on most Linux/macOS systems. To verify:

python3 --version
If not installed, use:

sudo apt install python3  # Ubuntu
brew install python       # macOS
"""

"""
4. Writing and Running Your First Python Script
Using Interactive Mode (REPL - Read, Evaluate, Print, Loop):
Open a terminal or command prompt
Type python or python3 and press Enter

"""

print("Hello, World!")

#2. Basic Arithmetic Operations

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


#3. Checking Python Version

import sys
print("Python Version:", sys.version)