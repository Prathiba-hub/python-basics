# Day 15
# Problem: Fibonacci Series (Nth Term)
# Topic: Recursion
# Language: Python

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive call
        return fibonacci(n - 1) + fibonacci(n - 2)

# Read term position
num = int(input())

# Find nth Fibonacci term
f = fibonacci(num - 1)

# Display result
print(f"The term {num} in the Fibonacci series is {f}")
