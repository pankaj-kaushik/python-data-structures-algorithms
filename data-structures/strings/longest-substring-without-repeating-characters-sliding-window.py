# Problem: Given a string, find the longest substring without repeating characters.
# Approach: Use a sliding window approach with a hash map to track the last seen index of each character. As we iterate through the string, if we encounter a character that has been seen before and its last seen index is within the current window, we move the start of the window to the right of the last seen index of that character. We also update the longest substring length and starting index as we go.
# Time Complexity: O(n) - We traverse the string once.
# Space Complexity: O(min(m, n)) - Where m is the size of the character set and n is the length of the string. In the worst case, we may need to store all characters in the string in the hash map.
# Note: This implementation assumes that the input string consists of ASCII characters. If the input string can contain Unicode characters, the space complexity may increase due to a larger character set.
          


def get_longest_substring_without_repeating_characters(s: str) -> str:

    # edge cases
    if s is None or len(s) == 0:
        return None
    
    # happy case
    char_index_map = {}
    longest_substring_start = 0
    longest_substring_length = 0

    # Initialize the start of the current substring
    start = 0

    for i, char in enumerate(s):
        # If the character is already in the map, move the start pointer
        if char in char_index_map:
            start = max(start, char_index_map[char] + 1)

        # Update the last seen index of the character
        char_index_map[char] = i

        # Update the longest substring length and start position
        if i - start + 1 > longest_substring_length:
            longest_substring_length = i - start + 1
            longest_substring_start = start

    # Return the longest substring without repeating characters
    return s[longest_substring_start:longest_substring_start + longest_substring_length]

# Example usage:
print(get_longest_substring_without_repeating_characters("abcabcbb"))  # should return "abc"
print(get_longest_substring_without_repeating_characters("bbbbb"))  # should return "b"
print(get_longest_substring_without_repeating_characters("pwkw"))  # should return "wkw"

