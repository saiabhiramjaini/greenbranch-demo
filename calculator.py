def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    return sum(numbers) / len(numbers)

TARGET_FILE: text_utils.py
import re


def is_palindrome(s):
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]