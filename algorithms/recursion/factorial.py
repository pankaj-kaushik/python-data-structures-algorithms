# Problem: Calculate the factorial of a given number using recursion.
# Approach: The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n. We can define the factorial function recursively as follows:
# - factorial(0) = 1 (base case)
# - factorial(n) = n * factorial(n - 1) for n > 0
# Time Complexity: O(n) - Each call to factorial results in one additional call until we reach the base case.
# Space Complexity: O(n) - The maximum depth of the recursion is n, which means we can have at most n function calls on the call stack at any time.

def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage:
print(factorial(5))  # Output: 120