"""Small string helpers."""


def reverse(text):
    return text[::-1]


def word_count(text):
    return len(text.split())


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and non-letters."""
    letters = [c.lower() for c in text if c.isalnum()]
    return letters == letters[::-1]
