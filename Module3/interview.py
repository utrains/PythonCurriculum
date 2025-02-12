"""
1. What is the Difference Between == and is?
Answer:

== checks if values are the same.
is checks if objects are the same (memory location).

"""

"""
2. Explain Short-Circuit Evaluation in Python.
Answer:
Short-circuit evaluation means Python stops evaluating a logical expression as soon as the result is known.
"""

def func():
    print("Function called")
    return True

print(True or func())  # "True" (function is never called)
print(False and func())  # "False" (function is never called)
