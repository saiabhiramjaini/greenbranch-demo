from text_utils import is_palindrome, reverse, word_count


def test_reverse():
    assert reverse("abc") == "cba"


def test_word_count():
    assert word_count("the quick brown fox") == 4


def test_palindrome_simple():
    assert is_palindrome("racecar")


def test_palindrome_ignores_case_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_not_palindrome():
    assert not is_palindrome("greenbranch")
