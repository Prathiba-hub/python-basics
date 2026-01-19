# Day 15
# Problem: Prime Number Check
# Topic: Recursion
# Language: Python

def is_prime(n, i=2):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # If divisor squared is greater than n, n is prime
    if i * i > n:
        return True
    # If divisible by i, not prime
    if n % i == 0:
        return False
    # Recursive call
    return is_prime(n, i + 1)

# Read input number
number = int(input())

# Check and display result
if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
