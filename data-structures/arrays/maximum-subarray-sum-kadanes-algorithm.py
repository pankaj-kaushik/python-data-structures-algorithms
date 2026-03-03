# Problem: Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Approach: Use Kadane's algorithm, which runs in O(n) time. Iterate through the array, keeping track of the maximum sum of a subarray ending at the current position. Update the global maximum sum whenever the current maximum exceeds it. If the current maximum becomes negative, reset it to zero, as a negative sum would not contribute to a larger sum in the future.
# Time Complexity: O(n) - We traverse the array once.
# Space Complexity: O(1) - We are using a constant amount of space for the variables.

def get_max_sub_array_sum(arr: list[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    Args:
        arr: A list of integers containing at least one element
        
    Returns:
        The maximum sum of any contiguous subarray
        
    Example:
        >>> get_max_sub_array_sum([-2,1,-3,4,-1,2,1,-5,4])
        6
    """
    current_sum = arr[0]
    max_sum = arr[0]
    max_sub_array_start = 0
    max_sub_array_end = 0

    for i in range(1, len(arr)):
        if current_sum < 0:
            current_sum = arr[i]
            max_sub_array_start = i
        else:
            current_sum += arr[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_array_end = i
            
    return arr[max_sub_array_start:max_sub_array_end + 1]

# Example usage
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(get_max_sub_array_sum(arr))  # should return [4, -1, 2, 1]