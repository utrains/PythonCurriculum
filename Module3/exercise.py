"""
1. Swap Two Numbers Using Arithmetic Operations
Task: Swap two numbers without using a third variable.

"""

"""
2. Check If a Number Is Even or Odd
Task: Write a program to check whether a number is even or odd using the modulus operator.
"""

"""
3. What is the Difference Between == and is?
Answer:

== checks if values are the same.
is checks if objects are the same (memory location).

"""

"""
4. Explain Short-Circuit Evaluation in Python.
Answer:
Short-circuit evaluation means Python stops evaluating a logical expression as soon as the result is known.
"""

def func():
    print("Function called")
    return True

print(True or func())  # "True" (function is never called)
print(False and func())  # "False" (function is never called)
