"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("The divisor cannot be zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("The logarithm base must be positive and cannot be 1.")
    if b <= 0:
        raise ValueError("The logarithm argument must be positive.")
    return math.log(b, a)

def exp(a, b): a ** b



