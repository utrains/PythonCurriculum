"Module 4: Control Flow Statements"

"""
1. Conditional Statements in Python
Conditional statements allow a program to execute different code blocks based on conditions.

1.1 The if Statement
The if statement executes a block of code only if the condition is True.

Syntax of if Statement

if condition:
    # Code to execute if condition is True

"""

#Example: Checking for a Positive Number

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")


"""

If num > 0 is True, it prints "The number is positive."
If num > 0 is False, nothing happens.

"""


"""
1.2 The if-else Statement
The if-else statement allows two possible execution paths:

If the condition is True, the if block executes.
Otherwise, the else block executes.

Syntax of if-else

if condition:
    # Code executes if condition is True
else:
    # Code executes if condition is False

"""

#Example: Checking Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

"""
If num is divisible by 2, it prints "Even number".
Otherwise, it prints "Odd number".
"""


"""
1.3 The if-elif-else Ladder
Sometimes, we need to check multiple conditions. Instead of multiple if-else statements, we use if-elif-else.

Syntax of if-elif-else Ladder

if condition1:
    # Executes if condition1 is True
elif condition2:
    # Executes if condition2 is True
else:
    # Executes if none of the conditions are True

"""


num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


"""
The if condition checks if num > 0.
The elif condition checks if num < 0.
The else block executes when both conditions are False (i.e., num == 0).
"""


"""
2. Looping Constructs (for, while)


Understanding the range() Function

Before diving into conditional statements and loops, let's understand the range() function, which is commonly used in loops.

The range() function generates a sequence of numbers that can be iterated over.

Syntax of range()

range(start, stop, step)
start: (Optional) The starting number (default is 0).
stop: The ending number (not included in the range).
step: (Optional) The increment between numbers (default is 1).

"""


"""
Loops allow repeated execution of code until a condition is met.

2.1 The for Loop
A for loop iterates over a sequence (list, tuple, string, range()).
"""

#Example: Printing Numbers from 1 to 5

for i in range(1, 6):
    print(i)


"""
2.2 The while Loop
A while loop runs as long as a condition is True.

"""

#Example: Printing Numbers from 1 to 5 Using while

i = 1
while i <= 5:
    print(i)
    i += 1  # Increment to avoid an infinite loop


"""
3. Break, Continue, and Pass Statements
These statements control the flow of loops.

3.1 The break Statement
The break statement exits the loop immediately.
"""

#Example: Stop Printing at 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

"""
3.2 The continue Statement
The continue statement skips the current iteration and moves to the next one.
"""

#Example: Skip 5 in a Loop
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


"""
3.3 The pass Statement
The pass statement does nothing and is a placeholder.
"""

#Example: Using pass

for i in range(5):
    pass  # Placeholder for future code

