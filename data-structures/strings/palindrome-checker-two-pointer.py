# Problem: Check if a given string is a palindrome.
# Approach: Use two pointers, one starting at the beginning of the string and the other at the end. Move the pointers towards each other, comparing characters at each step. If any characters do not match, the string is not a palindrome. If the pointers meet or cross, the string is a palindrome.
# Time Complexity: O(n) - We need to check each character at most once.
# Space Complexity: O(1) - We are using a constant amount of space for the pointers and temporary variables.

def is_palindrome(s: str) -> bool:
    """
    Checks if the given string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.
    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """

    # declare two pointers
    start = 0
    end = len(s) - 1

    # edge cases
    if s is None:
        return False
    
    if end == 0 or end == 1:
        return True

    # happy path
    # loop until the pointers meet    
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False