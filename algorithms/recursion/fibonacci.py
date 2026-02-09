def fib(n):
    # Base cases: fib(0) = 0, fib(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Example usage:
print(fib(10))  # Output: 55