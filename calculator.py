# https://github.com/Dddd559/lab11-RCK-ZD
# Partner 1: Zixian Dong
# Partner 2: Rishil Kodela

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("The divisor a cannot be zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("The base must be positive and not 1; the argument must be positive.")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


