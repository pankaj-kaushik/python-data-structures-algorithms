# Problem: Given a sorted array of integers and a target sum, find the indices of the two numbers that add up to the target.
# Approach: Use two pointers, one starting at the beginning of the array and the other at the end. Calculate the sum of the numbers at the two pointers. If the sum is equal to the target, return the indices. If the sum is less than the target, move the left pointer to the right to increase the sum. If the sum is greater than the target, move the right pointer to the left to decrease the sum. Continue this process until the pointers meet or cross.
# Time Complexity: O(n) - In the worst case, we may need to check each pair of numbers once.
# Space Complexity: O(1) - We are using a constant amount of space for the pointers and temporary variables.

def two_sum_sorted(arr: list[int], target: int) -> list[int]:
    """
    Finds two numbers in a sorted array that add up to a given target.
    Args:
        arr (list[int]): A sorted list of integers.
        target (int): The target sum.
    Returns:
        list[int]: A list containing the indices of the two numbers that add up to the target, or an empty list if no such pair exists.
    """

    # edge cases
    if arr is None or len(arr) < 2:
        return []
    
    # happy path
    # declare two pointers
    left = 0
    right = len(arr) - 1

    # loop until the pointers meet
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Example usage:
print(two_sum_sorted([1, 2, 3, 4, 5], 5))  # Output: [0, 3] (1 + 4 = 5)
print(two_sum_sorted([1, 2, 3, 4, 5], 10)) # Output: [] (no two numbers add up to 10)