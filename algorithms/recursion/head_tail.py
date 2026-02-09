def head(n):
    # Base case: when n is 0, we stop the recursion
    if n == 0:
        return
    head(n - 1)
    print(n)

def tail(n):
    # Base case: when n is 0, we stop the recursion
    if n == 0:
        return
    print(n)
    tail(n - 1)

# Example usage:
print("Head recursion:")
head(5)  # Output: 1 2 3 4 5

print("\nTail recursion:")
tail(5)  # Output: 5 4 3 2 1