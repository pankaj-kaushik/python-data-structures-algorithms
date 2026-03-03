# Problem: Given an array of integers and a number k, find the maximum sum of a subarray of size k.
# Approach: Use a sliding window of size k to calculate the sum of the first k elements. Then, slide the window through the array by adding the next element and removing the first element of the previous window. Keep track of the maximum sum encountered during this process.
# Time Complexity: O(n) - We traverse the array once to calculate the sums.
# Space Complexity: O(1) - We are using a constant amount of space for the window sum and maximum sum.

def max_sum_subarray_k_sliding_window(arr, k):
    # edge case
    if arr is None or k <= 0 or k > len(arr):
        return None
    
    # happy path
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Example usage:
print(max_sum_subarray_k_sliding_window([1, 2, 3, 4, 5], 2))  # should return 9 (4 + 5)
print(max_sum_subarray_k_sliding_window([1, 2, 3, 4, 5], 3))  # should return 12 (3 + 4 + 5)
print(max_sum_subarray_k_sliding_window([1, 2, 3, 4, 5], 1))  # should return 5 (5)  