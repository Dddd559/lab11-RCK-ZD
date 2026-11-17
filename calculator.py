# https://github.com/Dddd559/lab11-RCK-ZD
# Partner 1: Zixian Dong
# Partner 2: Rishil Kodela

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("The divisor cannot be zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("The base must be positive and not 1; the argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a ** b


