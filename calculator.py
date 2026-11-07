"""Small arithmetic helpers."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("average of an empty list")
    return sum(numbers) / len(numbers)
