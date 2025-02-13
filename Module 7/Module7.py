#Introduction to Strings
#A string in Python is a sequence of characters enclosed within single ('), double ("), or triple (''' """) quotes.

"""Immutable: Strings cannot be modified once created.
Indexed: Characters can be accessed using indices.
Iterable: Strings can be looped through character by character.
"""

"""Creating Strings in Python
Example: Different Ways to Create a String"""

# Using single, double, and triple quotes
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline 
string using triple quotes.'''

print(str1, str2, str3)


"""String Indexing and Slicing
Strings are indexed, meaning each character has a position:"""

"""
H     e      l      l      o
0     1      2      3      4  → Forward Indexing
-5   -4     -3     -2     -1  → Reverse Indexing
"""
#Accessing Characters Using Indexing

word = "Python"
print(word[0])   # Output: P (First character)
print(word[-1])  # Output: n (Last character)

#String Slicing ([start:end:step])

word = "Programming"
print(word[0:5])   # Output: Progr (0 to 4)
print(word[:6])    # Output: Progra (0 to 5)
print(word[3:])    # Output: gramming (from index 3 to end)
print(word[::2])   # Output: Pormig (every 2nd character)
print(word[::-1])  # Output: gnimmargorP (Reversed string)


"Iterating Over a String"
#Example: Iterating Over Each Character

text = "Python"
for char in text:
    print(char, end=" ")
# Output: P y t h o n

"""String Methods and Functions
String Length (len())
"""
text = "Python"
print(len(text))  # Output: 6

"""Changing Case (upper(), lower(), title(), capitalize())"""
text = "hello world"
print(text.upper())       # Output: HELLO WORLD
print(text.lower())       # Output: hello world
print(text.title())       # Output: Hello World
print(text.capitalize())  # Output: Hello world

"""Checking String Content (isalpha(), isdigit(), isalnum(), isspace())"""
print("Python".isalpha())  # True (Only letters)
print("1234".isdigit())    # True (Only digits)
print("Hello123".isalnum()) # True (Letters and numbers)
print("   ".isspace())     # True (Only spaces)

"""Searching in Strings (find(), index(), count())"""
text = "Python programming"
print(text.find("prog"))  # Output: 7 (Returns index of first occurrence)
print(text.count("o"))    # Output: 2 (Counts occurrences of 'o')

"""Replacing and Splitting (replace(), split(), join())"""
text = "I love Python"
print(text.replace("love", "like"))  # Output: I like Python

words = text.split()  # Splits string into a list
print(words)  # Output: ['I', 'love', 'Python']

joined_text = "-".join(words)
print(joined_text)  # Output: I-love-Python

"""Checking Prefix and Suffix (startswith(), endswith())"""

text = "hello.py"
print(text.startswith("hello"))  # True
print(text.endswith(".py"))      # True


"""Stripping Whitespace (strip(), lstrip(), rstrip())"""

text = "  hello  "
print(text.strip())  # Output: "hello" (Removes spaces from both sides)
print(text.lstrip()) # Output: "hello  " (Removes left spaces)
print(text.rstrip()) # Output: "  hello" (Removes right spaces)


"String Formatting"
"Using format()"

name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 25 years old.

"Using f-strings (Python 3.6+)"
print(f"My name is {name} and I am {age} years old.")


"""
Escape Sequences
Escape sequences allow special formatting inside strings."""

"""Escape Sequence	         Meaning
      \n	                 Newline
      \t	                   Tab
      \\	                Backslash
"""
"Example: Using Escape Sequences"
print("Hello\nWorld")  # Output:
# Hello
# World



"""Raw Strings (r"string")"""
print(r"C:\newfolder\test")  # Output: C:\newfolder\test
