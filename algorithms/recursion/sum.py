# Problem: Write a recursive function to calculate the sum of the first n natural numbers.
# Approach: The sum of the first n natural numbers can be defined recursively as follows:
# - get_sum(0) = 0 (base case)
# - get_sum(n) = n + get_sum(n - 1) for n >
# Time Complexity: O(n) - Each call to get_sum results in one additional call until we reach the base case.
# Space Complexity: O(n) - The maximum depth of the recursion is n, which means we can have at most n function calls on the call stack at any time.

def get_sum(n):
    # Base case: when n is 0, the sum is 0
    if n == 0:
        return 0
    else:
        return n + get_sum(n - 1)

# Example usage:
print(get_sum(5))  # Output: 15 (1 + 2 + 3 + 4 + 5)