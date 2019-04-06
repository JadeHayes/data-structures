import string


def is_palindrome(str) -> bool:
    """recursively checks to see if a string is a palindrome"""
    str_lower = str.lower()
    if len(str_lower) <= 1:
        return True
    elif str_lower[0] == str_lower[-1]:
        return is_palindrome(str_lower[1:-1])
    else:
        return False


